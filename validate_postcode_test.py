#! /usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase
from validate_postcodes import validate_postcode


class ValidatePostcodeTests(TestCase):
    def test_validate_success(self):
        valid_postcodes = ['EC1A 1BB', 'W1A 0AX', 'M1 1AE', 'B33 8TH', 'CR2 6XH', 'DN55 1PT', 'GIR 0AA', 'SO10 9AA',
                           'FY9 9AA', 'WC1A 9AA', 'OX9 1PS']
        for postcode in valid_postcodes:
            print('Validating postcode: {0}'.format(postcode))
            self.assertTrue(validate_postcode(postcode), '{0} should be a valid postcode'.format(postcode))

    def test_validate_failure(self):
        invalid_postcodes = ['$%± ()()', 'XX XXX', 'A1 9A', 'LS44PL', 'Q1A 9AA', 'X1A 9BB', 'LI10 3QP', 'LJ10 3QP',
                             'LZ10 3QP', 'A9Q 9AA', 'AA9C 9AA', 'FY10 4PL', 'SO1 4QQ']
        for postcode in invalid_postcodes:
            print('Validating postcode: {0}'.format(postcode))
            self.assertFalse(validate_postcode(postcode), '{0} should be an invalid postcode'.format(postcode))

if __name__ == '__main__':
    unittest.main()
