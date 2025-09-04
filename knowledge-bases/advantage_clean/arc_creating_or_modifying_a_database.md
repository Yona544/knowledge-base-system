---
title: Arc Creating Or Modifying A Database
slug: arc_creating_or_modifying_a_database
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_creating_or_modifying_a_database.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 75a39499819bda6b96af6c88134ad3c7c128c579
---

# Arc Creating Or Modifying A Database

Creating or Modifying a Database

Creating or Modifying a Database

Advantage Data Architect

| Creating or Modifying a Database  Advantage Data Architect |  |  |  |  |

To create a new Database and Data Dictionary, select File | Create New Data Dictionary from the main menu.

To modify an existing Database and Data Dictionary properties, right-click on a connected database in the Connection Repository and select Properties from the quick menu. See [Opening a Database](arc_opening_a_database2.md) for details. You must login to the database as a user with ALTER DATABASE permissions in order to modify a database.

Database Property Field Descriptions

General Tab

Name (required)

Enter a name for the new database. For an existing database, the name will be displayed and cannot be modified. An extension is not required. The file name is the name by which the Data Dictionary files for this database will be created. For example, if you enter the name BankDatabase, Advantage will create the data dictionary files BankDatabase.ADD, BankDatabase.AI, and BankDatabase.AM. The file name (minus extension) will be how your database is identified in the Connection Repository and in the alias in the ads.ini file.

Server Type (required)

Select the type of Advantage connection you want to use to create this database. Your choices are Local Server, Remote Server, and Internet Server.

The Advantage Local Server is a non-client/server solution for accessing data located on local drives as well as computers on the network that are not running the the Advantage Database Server.

Advantage Remote Server is a scalable, high-performance database management solution that brings client/server benefits to critical database applications.

Advantage Internet Server is a special WAN connection to a remote server running Advantage Database Server

AdsSys Password (optional)

Use this field to specify the administrator password for the new database.

Paths

The browse button to the right of these fields allows a point and click selection of the path. For an existing database, it will be displayed and cannot be modified.

Database (required)

For a new database, enter the path to where the new data dictionary files should be stored.

Default (optional)

The default table path is the path where all new database tables) will be created. If this property is not set, it will default to the database file path. This can only be entered for an existing database.

Temp (optional)

The temporary table path is the path where all temporary database tables will be created. These temporary tables are the ones that can get created during SQL queries. If this property is not set, it will default to the Default table path. This can only be entered for an existing database.

Version

Major Version (optional)

The user defined major version number of the data dictionary. This property is read, set, and interpreted only by the application and Advantage Data Architect. The Advantage Database Server does not currently use it internally. This value can be used by the application developer to determine when the Advantage "database upgrade" functionality needs to be used. This allows developers to ship version "1.0" of a database defined in a data dictionary, then later ship version "1.1" of the data dictionary. The "database upgrade" functionality will be available for applications developers to create and execute the code necessary to upgrade the files and/or definitions in the version "1.0" database to the version "1.1" database. The default value for this property, if it has never been set, is 0.

Minor Version (optional)

The user defined minor version number of the data dictionary. This property is read, set, and interpreted only by the application and Advantage Data Architect. The Advantage Database Server does not currently use it internally. This value can be used by the application developer to determine when the Advantage "database upgrade" functionality needs to be used. This allows developers to ship version "1.0" of a database defined in a data dictionary, then later ship version "1.1" of the data dictionary. The "database upgrade" functionality will be available for applications developers to create and execute the code necessary to upgrade the files and/or definitions in the version "1.0" database to the version "1.1" database. The default value for this property, if it has never been set, is 0.

Security Tab

User Access

Logins Required (optional)

Specifies whether an anonymous user connection to the database is allowed. If this check box is set, a user name and password is required to make a database connection to the data database. Otherwise, anonymous connections to the database with no user name and no password are allowed. The setting applies to Advantage Database Server, Advantage Local Server, and Advantage Internet Server connections. When an Advantage Internet Server connection is used, the more restrictive authentication requirement between this setting and the [Internet Security Level](master_internet_security_levels.md) is used. For example, if Logins Required is selected and the Internet Security Level is level 0, a login (authentication) is required. The contrary is also true. If Logins Required is not selected and the Internet Security Level is 1 or 2, a login (authentication) is required.

Check User Rights (optional)

This property determines whether Advantage will enforce the user's access rights when opening a database table) or view, or executing a stored procedure. By default, the box is not checked when the data database is created. If this box is not checked, Advantage does not verify the users access rights when opening a database table or view, or when executing a stored procedure. The implication is that all users have full rights to all objects in the database. If this box is checked, the users access rights are verified.

Note An anonymous user does not have any rights to objects in the database. If the database is set up to verify user access rights, an anonymous user can make a connection to the database but they cannot open any table or view, or execute any stored procedure.

Encryption

Encryption Type (optional)

Pick the type of encryption to use with data dictionaries.  RC4 is the default version of encryption supported in all versions of Advantage.  AES 128 and AES 256 strong encryption requires the FIPS Encryption Security Option Add-on.

Encrypt Data Dictionary Files (optional)

Check this box to encrypt the Advantage Data Dictionary files themselves. These are the .ADD, .AI, and .AM files. If left unchecked, the data dictionary files will not be encrypted. This can only be set when creating a database.

Encrypt Communication (optional)

Check this box to encrypt communications to the Advantage Database Server. For more information, see [communications encryption](master_communications_encryption.md).

Encrypt New Tables (optional)

Check this box to encrypt all new tables added to the dictionary automatically.

Encrypt Indexes (optional)

Check this box to encrypt all new index files automatically.

Change Table Encryption Password (optional)

Changes the current password for the Advantage Data Dictionary files. This can only be performed on an existing database. This property is only used for the default encryption. When using [AES encryption](master_encryption.md), key data from the dictionary password is used for table encryption.

Internet Access

Enabled (optional)

Allows the database to be accessed across the Internet using Advantage Internet Server. This can only be set on an existing database.

Security Level (optional)

The level of security specifies whether authentication and encryption are used for Advantage Internet Server connections. See [Internet Security Levels](master_internet_security_levels.md) for more information.

Max Login Attempts (optional)

The number of unsuccessful connection attempts for Advantage Internet Server connections before Internet access is disabled for a user. See [Maximum Failed Login Attempts](master_maximum_failed_login_attempts.md) for more information. This can only be set on an existing database.

Advanced Tab

FTS Defaults

Provides access to the Full Text Search (FTS) default parse values. This can only be performed on an existing database. This button displays a dialog box showing the default FTS values for the data dictionary including delimiters, drop characters, conditional drop characters, and noise words. For more information about these values, please see [Full Text Search Index Options](master_full_text_search_index_options_fts.md). When creating an FTS index, it is possible to provide the specific parse values for each index. Using the default values when building an FTS index causes Advantage to use the values stored in the data dictionary if they are provided, otherwise Advantage will use the system defaults. This provides a simpler way to manage, for example, noise word lists for individual languages.

Specifying the FTS defaults in the data dictionary provides an additional piece of functionality as well. When the Full Text Search CONTAINS() function is executed on a field without an FTS index, Advantage will evaluate the CONTAINS clause using the default delimiters, drop characters, and conditional drop characters. If these defaults are not specified in the dictionary, Advantage will use the system defaults.

On the FTS Defaults dialog, the "Include White Space" checkbox associated with the delimiters, drop characters, and conditional drop characters provides a mechanism to include all white space control characters (space, tab, line feed, etc.) in the group. By default, this is turned on only for the delimiter characters.

Disable Triggers

Use this option to disable triggers on all tables in the dictionary.

Description Tab

Database Description (optional)

Enter a description for a new or existing database.

OK

When creating a database, the OK option creates the database. When a database is created, there is no password set for ADSSYS. This will allow anyone access to the database and its properties. It is recommended that the ADSSYS password be set when you create the database, but it can also be set at a later time. For an existing database, saves the updated settings.

Cancel

Cancels any data entered or changed and exits the window.
