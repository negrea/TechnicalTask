#! /usr/bin/python3
import re
import csv
import gzip
from urllib.request import urlopen, Request
from urllib.request import URLError
import argparse

regex = re.compile(r"""
        (GIR\s0AA) |
        (
            # A9 or A99 prefix
            ( ([A-PR-UWYZ][0-9][0-9]?) |
                # AA99 prefix with some excluded areas
                (([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9]) |
                    # AA9 prefix with some excluded areas
                    ([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9]) |
                    # WC1A prefix
                    (WC[0-9][A-Z]) |
                    (
                        # A9A prefix
                        ([A-PR-UWYZ][0-9][A-HJKPSTUW]) |
                        # AA9A prefix
                        ([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])
                    )
                )
            )
            # 9AA suffix
            \s[0-9][ABD-HJLNP-UW-Z]{2}
        )
    """, re.VERBOSE)


def bulk_import(fail_file, success_file,
                url='https://drive.google.com/uc?export=download&id=0BwxZ38NLOGvoTFE4X19VVGJ5NEk'):
    """Creates two files on disk : 'failed_validation.csv' and 'succeeded_validation.csv' based on validation results
       of data from the given file

    Args:
        fail_file (str): Name of file that contains the rows which failed validation
        success_file(str): Name of file that contains the rows which passed validation
        url (str): Name of the url/file
    """
    try:
        with open(fail_file, 'wt') as fail_out, open(success_file, 'wt') as success_out:
            fail_writer = csv.writer(fail_out)
            success_writer = csv.writer(success_out)
            # Write Headers
            headers = ['row_id', 'postcode']
            fail_writer.writerow(headers)
            success_writer.writerow(headers)

            success_rows, failed_rows = sort_csv(url)

            fail_writer.writerows(failed_rows)
            success_writer.writerows(success_rows)
    except OSError as e:
        print('An error occurred while trying to write to %s and %s!\nReason: %s' % (fail_file, success_file, e))


def sort_csv(filename):
    """Gets the lists of validated rows sorted in ascending numeric order by row_id from a file

    Args:
        filename (str): Name of the file/url

    Returns:
        tuple(list(str), list(str)): A tuple containing the lists of rows that pass and fail validation respectively
    """

    success_rows = []
    success_rows_append = success_rows.append
    fail_rows = []
    fail_rows_append = fail_rows.append
    for row in get_rows(filename) if args.file else stream_rows(filename):
        if validate_postcode(row[1]):
            success_rows_append(row)
        else:
            fail_rows_append(row)

    success_rows.sort(key=lambda row: int(row[0]))
    fail_rows.sort(key=lambda row: int(row[0]))

    return success_rows, fail_rows


def stream_rows(url):
    """ Generator for streaming a csv file from a URL

        Args:
            url (str): Name of the url

        Yields:
            str: A row from the file
        """
    try:
        with urlopen(Request(url, headers={'Accept-encoding': 'gzip'})) as response, \
                gzip.open(response, 'rt',  newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Skip Headers
            next(csv_reader)
            for row in csv_reader:
                yield row
    except URLError as e:
        if hasattr(e, 'reason'):
            print('Failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)


def get_rows(filename):
    """ Generator for reading a csv file from disk

    Args:
        filename (str): Name of the file

    Yields:
        str: A row from the file
    """
    try:
        with gzip.open(filename, 'rt', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Skip Headers
            next(csv_reader)
            for row in csv_reader:
                yield row
    except OSError as e:
        print('An error occurred while trying to read the file from disk!\nReason: ', e)


def validate_postcode(postcode):
    """ Checks if a string is a valid UK postcode

    Args:
        postcode (str): A string representing a UK postcode
1
    Returns:
        bool: MatchObject (True) if postcode is valid
    """

    return regex.match(postcode)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, help='Specify file to load from')
    args = parser.parse_args()
    if args.file:
        bulk_import('failed_validation.csv', 'succeeded_validation.csv', url=args.file)
    else:
        bulk_import('failed_validation.csv', 'succeeded_validation.csv')
