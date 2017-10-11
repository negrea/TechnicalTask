# Instructions

## Linux

### Install Python 3.5

Ubuntu 16.04 ships with both Python 3 and Python 2 pre-installed.

To see which version of Python3 you have installed, open a command prompt and run:

	$ python3 -V

### Install Python manually

#### Install the required packages

Run the following command from a terminal window (Ctrl - Alt + T) to install prerequisites.

	$ sudo apt-get install build-essential checkinstall
	$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

#### Download Python 3.5.2

	$ cd /usr/src
	$ wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz

Extract the downloaded package.

	$ sudo tar xzf Python-3.5.2.tgz

#### Compile Python Source

	$ cd Python-3.5.2
	$ sudo ./configure
	$ sudo make altinstall

Make altinstall is used to prevent replacing the default python binary file /usr/bin/python

### Running the solution

Download both: 'validate_postcode.py' and 'validate_postcode_test.py' files into a directory  of your choice. 

Open a 'Terminal window'. (Ctrl - Alt + T)

Change your working directory to the one containing the downloaded files.
	
	$ cd <Path to your directory>

To run the solution type:

	$ ./validate_postcodes.py

To run the solution by specifying the name of the import file from disk type:

	$ ./validate_postcodes.py -f <Name of file>

This will produce two files: 'succeeded_validation.csv' and 'failed_validation.csv' containing the valid and invalid postcodes from 'import_data.csv.gz' respectively.

### Running the unit tests

To run the unit tests type:

	$ ./validate_postcode_test.py

## Windows 10

### Install Python 3.5.2

Download [Python](https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe) from the official Website.

To install it manually, just double-click the file and follow the onscreen instructions.

By default this will install python in C:\Python352

#### Set the system’s PATH variable to include Python

Open the Control Panel (easy way: right click the Start Menu icon and select Control Panel).

In the Control Panel, search for Environment; click Edit the System Environment Variables. Then click the Environment Variables button.

In the System Variables section, we will need to either edit an existing PATH variable or create one. If you are creating one, make 'Path' the variable name and add the following directories to the variable values section, separated by a semicolon. If you’re editing an existing PATH, the values are presented on separate lines in the edit dialog. Click New and add one directory per line.

C:\Python35-32;C:\Python35-32\Lib\site-packages\;C:\Python35-32\Scripts\

### Running the solution

Download both: 'validate_postcode.py' and 'validate_postcode_test.py' files into a directory  of your choice. 

Press Windows+R to open “Run” box.

Type 'cmd' and then press Ctrl+Shift+Enter to open an administrator Command Prompt.

Change your working directory to the one containing the downloaded files.

	> cd <Path to your directory>

To run the solution type:

	> validate_postcodes.py

To run the solution by specifying the name of the import file from disk type:

	$ ./validate_postcodes.py -f <Name of file>

### Running the unit tests

To run the unit tests type:

	> validate_postcode_test.py


	
	



	






