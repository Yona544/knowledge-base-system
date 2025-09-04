Advantage Python Driver




Advantage Database Server 12  

Advantage Python Driver

Advantage Python Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Python Driver  Advantage Python Driver |  |  | Feedback on: Advantage Database Server 12 - Advantage Python Driver Advantage Python Driver web\_python\_driver Advantage Web Development > Python > Advantage Python Driver / Dear Support Staff, |  |
| Advantage Python Driver  Advantage Python Driver |  |  |  |  |

The Advantage Python Driver (adsdb) is a Python module designed to provide database access from the Python environment to Advantage Database Server.  The driver conforms to the database API 2.0 interface specification for Python (<http://www.python.org/dev/peps/pep-0249/>).

Download

The adsdb driver is available from the adsdb google code project here:

<http://code.google.com/p/adsdb/downloads/list>

There you can download the latest version of the driver package and source.

Requirements

Python 2.4 or greater (note that 3.x breaks some functionality and is not supported)

Python ctypes module if missing (the default Python installation will have this)

Advantage Database Server 10.1 or newer (Advantage Local Server works too)

Supported Platforms

Currently only platforms that support both the Advantage Client Engine (ACE) and Python are supported.  These include Windows and Linux.

Installation

Run the following command as an administrative user to install adsdb:

python setup.py install

Testing the adsdb module

To test that the Python interface to Advantage is working correctly run the test.py script in the scripts subdirectory.  If the path "C:\" is not valid on your system, change it to a valid path.  You should see this expected output:

adsdb successfully installed.

Questions or bug reports

Questions, bug reports, suggestions and other general communication about the driver should be posted in the Web\_Development forum located here:

<news://DevZone.AdvantageDatabase.com/advantage.web_development>

Example

An example Python program using adsdb can be found in the Scripts subdirectory of the adsdb installation.  Test.py shows a simple connection and SQL query execution.  Also in the Scripts subdirectory are two scripts that run the DB API 2.0 test suite.  Running test.py should be enough to verify adsdb and ACE are installed and working correctly, but you can also run runtests.py to test adsdb.  Note that you might need to change the connection path and test dictionary location of C:\test.add as necessary.