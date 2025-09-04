Advantage Django Backend




Advantage Database Server 12  

Advantage Django Backend

Advantage Django Backend

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Django Backend  Advantage Django Backend |  |  | Feedback on: Advantage Database Server 12 - Advantage Django Backend Advantage Django Backend web\_django\_backend Advantage Web Development > Django > Advantage Django Backend / Dear Support Staff, |  |
| Advantage Django Backend  Advantage Django Backend |  |  |  |  |

The Advantage Django Backend (adsdb-django) is a Python module designed to provide database access from the Django environment to Advantage Database Server.  The backend is distributed as a stand-alone python module.

Requirements

Python 2.4 or greater (note that 3.x breaks some functionality and is not supported)

Python ctypes module if missing (the default Python installation will have this)

Advantage Database Server 10.1 or newer

Advantage Python Interface (adsdb)

Django 1.2

Supported Platforms

Currently only platforms that support both the Advantage Client Engine (ACE) and Python are supported.  These include Windows and Linux.

 

Getting Started

Follow these steps to install the required software and configure a Django project to work with Advantage.

 

1. Install the required software

a) Advantage Database Server 10.1

Web based Advantage applications must use remote server connections (as oppposed to local server connections) to the Advantage Database Server.  Using local server in a web environment violates the local server license.  However, local server may be used during development on a local PC if desired.  Both local and remote server versions can be downloaded here:

<http://devzone.advantagedatabase.com/dz/content.aspx?key=20>

NOTE: You should also download and install Advantage Data Architect (ARC) to create the initial database and manage it in the future.

b) Python (2.4 or greater)

Install Python if you don't already have it installed. We recommend Python 2.7 but any version greater than 2.4 is supported. Note however that Python 3 introduced backwards incompatible features and many projects including Django do not currently have support for Python 3. You can download python from:

<http://www.python.org/download/>

If you are running on Linux you will most likely also be able to find python through your distribution's package management system.

c) Python setuptools

The setuptools project for python acts as a package manager for Python code. Using setuptools will make it trivial to install the correct version of Django to use with Advantage. You can get setuptools for python from:

<http://pypi.python.org/pypi/setuptools/>

Again, if you are running on Linux you most likely be able to find setuptools through your distribution's package management system. This package is called "python-setuptools" on Ubuntu and "python-setuptools-devel" on Fedora.

d) Django 1.2

Once you have install setuptools installing Django is a snap, simply run easy\_install from the Python Scripts directory:

$ easy\_install Django==1.2

On Windows with Python 2.7:

C:\Python27\Scripts\easy\_install.exe Django==1.2

e) Python Advantage Database Interface

The Advantage Database Interface for Python provides a Database API v2 compliant driver (see Python PEP 249) for accessing Advantage databases from Python. The Advantage backend for Django is built on top of this interface so installing it is required.

You can obtain the Python Advantage Database Interface from:

<http://code.google.com/p/adsdb/downloads/list>

Install the driver by extracting the archive and running the following command in the resulting directory:

$ python setup.py install

f) Advantage Django Backend

You can obtain the Advantage Database backend for Django from:

<http://code.google.com/p/adsdb-django/downloads/list>

Install the backend by extracting the archive and running the following command in the resulting directory:

$ python setup.py install

2. Create a database

Now you need to create a new database to use with Django.  Use Advantage Data Architect (or any other Advantage client application) to connect to the Advantage server (remote or local) and create a new database with CTRL-W in ARC or use the CREATE DATABASE SQL statement.  For example:

CREATE DATABASE [c:\test\django.add];

If all goes well Advantage will have created a new database file named 'django.add' in c:\test, or whichever directory you specified. Feel free to move the database files to any location you want. You can even copy it to a machine running a different operating system if you wish.

3. Configure Django

Creating a new Django site and configuring it to use Advantage is very easy. First create the site in the normal fashion:

$ django-admin.py startproject mysite

Then edit the file mysite/settings.py and change the DATABASES setting to match what is given below:

DATABASES = {

   'default' : {

             'ENGINE': 'adsdb\_django',

       'NAME': 'c:/test/django.add',  # insert the database path

       'USER': 'ADSSYS',

       'PASSWORD': ''  # insert ADSSYS password if necessary

         }

}

Note: Additional connection options can be set with the OPTIONS parameter. For example:

DATABASES = {

   'default' : {

             'ENGINE': 'adsdb\_django',

       'NAME': 'c:/test/django.add',  # insert the database path

       'USER': 'ADSSYS',

       'PASSWORD': ''  # insert ADSSYS password if necessary

                 'OPTIONS': { 'TrimTrailingSpaces' : 'True', 'ServerType' : 'Local' },

         }

}

4. Test to make sure everything is working

The Advantage database backend for Django makes use of the Python Advantage Database interface. We first want to test that this interface is working correctly before testing Django connectivity itself. Create a file named test\_adsdb.py with the following contents:

import adsdb

conn = adsdb.connect(DataSource='C:/test/django.add',UserID='ADSSYS')

curs = conn.cursor()

curs.execute("select 'Hello, world!' FROM system.iota")

print "Advantage says: %s" % curs.fetchone()

Run the test script and ensure that you get the expected output:

$ python test\_adsdb.py

Advantage says: Hello, world!

To test that Django can make use of the Advantage Database backend simply change to the "mysite" directory created in step 3 and ask Django to create the tables for the default applications.

$ python manage.py syncdb

If you don't receive any errors at this point then congratulations. Django is now correctly configured to use Advantage as a backend.

5. What to do if you have problems?

If you run into problems, don't worry. First try re-reading the instructions above and make sure you haven't missed a step. If you are still having issues here are a few resources to help you figure out what went wrong. You can consult the documentation, or post to a forum where many of the Advantage engineers hang out.

Advantage Online Documentation:

<http://devzone.advantagedatabase.com/dz/content.aspx?key=32>

Advantage developer forums:

<http://devzone.advantagedatabase.com/dz/content.aspx?key=7>

6. Where to go from here?

Advantage should now be successfully configured as a backend for your Django site. To learn more about creating web applications with Django try the excellent series of tutorials provided by the Django project:

<http://docs.djangoproject.com/en/dev/intro/tutorial01/#intro-tutorial01>