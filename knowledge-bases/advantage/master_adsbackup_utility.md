adsbackup Utility




Advantage Database Server 12  

The adsbackup Utility

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| The adsbackup Utility  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - The adsbackup Utility Advantage Concepts master\_Adsbackup\_utility Advantage Concepts > Advantage Functionality > Backup > The adsbackup Utility / Dear Support Staff, |  |
| The adsbackup Utility  Advantage Concepts |  |  |  |  |

The adsbackup utility is a command-line utility that wraps the calls to the backup and restore canned procedures. This utility can easily be added to an operating system scheduler to create scheduled backups.

The adsbackup utility is installed to the same directory as the Advantage Database Server executable. A java utility (adsbackup.jar) is also available upon request.

Note that the newer and more generic [SQL command line utility](master_sql_command_line_utility_overview.htm) can be used in place of the adsbackup utility. The adsbackup utility is simply a wrapper for calling the [online backup system procedures](master_backup_and_restore_canned_procedures.htm). With the SQL command line utility, you can call those system procedures directly. In some situations, this might be a simpler and more flexible solution.

Example Usage

For this example, lets assume we are using a Microsoft Windows server, and our data resides in a data dictionary called "motors.add" in the c:\data\motors directory. The motors.add dictionary has an ADSSYS user password of "secret".

Before running a test of adsbackup, we will create two new subdirectories called "backup" and "restore" in the c:\data\motors directory. We will send our backup image to the "backup" directory, and we will restore into the "restore" directory (as opposed to restoring over the original database, which is possible, but not the safest approach).

Next, we will run the following test command to test our backup:

adsbackup -psecret c:\data\motors\motors.add c:\data\motors\backup

 

Then, we will add this new command to the Windows Scheduler to backup our database every night:

|  |  |
| --- | --- |
| 1. | Open the Control Panel |

|  |  |
| --- | --- |
| 2. | Open Scheduled Tasks |

|  |  |
| --- | --- |
| 3. | Click "Add Scheduled Task" |

|  |  |
| --- | --- |
| 4. | Follow the wizard prompts to add adsbackup.exe as a scheduled task |

Each time adsbackup is called, it will create a new backup log table of the form BACKUP\_CCYYMMDDHHMMSS, where CCYYMMDDHHMMSS is a timestamp based on the date and time the backup command was started. Command line options exist to alter the location and name of this file if you would like to customize the logging functionality of the utility.

If at some point you need to restore from this backup image, you would execute the following command to restore into the "restore" directory:

adsbackup r psecret c:\data\motors\backup\motors.add c:\data\motors\restore\motors.add

 

Or, you could execute this command to restore over the existing or damaged data (only recommended after making a copy of the data you are about to overwrite):

adsbackup r psecret c:\data\motors\backup\motors.add c:\data\motors\motors.add

 

Note that in both of the commands above, the destination path includes the .add filename. This is different than when performing a backup. While not common, if you want to rename the dictionary file when restoring with this command, you can do so by specifying a different dictionary name in the destination path.

Whenever you set up a new backup, it is a good idea to test a restore operation and run your application against the restored data to verify the backup and restore were successful.

Command Line Usage

To backup a directory of free tables:

adsbackup [options] <src path> [file mask] <dest path>

src path

The path to the free tables you want to back up. This path can be UNC ( \\myserver\myshare\mydir ) or a drive letter ( c:\mydir ) if connecting to a Microsoft Windows server. If using drive letters, keep in mind the drive letter must be recognized by the server machine, any drives mapped on the client executing the backup command are irrelevant. If using a drive letter for the source path, the drive must be a "local" drive; it cannot be a mapped drive. If connecting to a Linux server, UNC paths are recommended.

file mask

A file mask similar to "\*.adt" or "\*.dbf" which will be used to determine what tables should be included in the backup image. The file mask is only allowed when performing a backup of free tables. Multiple masks can be used in a single backup/restore by separating them with a semicolon. For example, "\*.adt;\*.dbf".

dest path

Path to place the backup image in. This path can be UNC ( \\myserver\myshare\mydir ) or a drive letter ( c:\mydir ) if connecting to a Microsoft Windows server. If using drive letters, keep in mind the drive letter must be recognized by the server machine, any drives mapped on the client executing the backup command are irrelevant. Unlike the source path, the destination path can use any drive letter, even one that references a mapped drive. If connecting to a Linux server UNC, paths are recommended.

To backup a data dictionary and the associated tables:

adsbackup [options] <src database> <dest path>

src database

The path to the data dictionary you want to back up. This path can be UNC ( \\myserver\myshare\mydir\mydd.add ) or a drive letter ( c:\mydir\mydd.add ) if connecting to a Microsoft Windows server. If using drive letters, keep in mind the drive letter must be recognized by the server machine, any drives mapped on the client executing the backup command are irrelevant. If using a drive letter for the source path, the drive must be a "local" drive, it cannot be a mapped drive. If connecting to a Linux server UNC, paths are recommended.

dest path

Path to place the backup image in. This path can be UNC ( \\myserver\myshare\mydir ) or a drive letter ( c:\mydir ) if connecting to a Microsoft Windows server. If using drive letters, keep in mind the drive letter must be recognized by the server machine, any drives mapped on the client executing the backup command are irrelevant. Unlike the source path, the destination path can use any drive letter, even one that references a mapped drive. If connecting to a Linux server UNC, paths are recommended.

Java Command Line Usage

The following are a few examples using the java adsbackup utility. The paths will vary depending on your installation.

To backup a directory of free tables:

java -cp main:ads\adsbackup.jar;main:ads\adsjdbc.jar AdsBackup \\server\share \*.adt \\server\share\backup

To restore a directory of free tables:

java -cp main:ads\adsbackup.jar;main:ads\adsjdbc.jar AdsBackup -r \\server\share\data\backup \\server\share\data

 

To backup a data dictionary:

java -cp main:ads\adsbackup.jar;main:ads\adsjdbc.jar AdsBackup -pPassword \\server\share\data\datadictionary.add \\server\share\data\backup

 

To restore a data dictionary:

java -cp main:ads\adsbackup.jar;main:ads\adsjdbc.jar AdsBackup -r -pPassword \\server\share\data\backup\datadictionary.add \\server\share\data\datadictionary.add

 

Command Line Parameters

The following command line parameters can be passed to the adsbackup utility as options:

-a Prepare a database for a differential backup

This option will create a new backup image and also initialize the source data so it can be used in a subsequent [differential backup](master_differential_backups.htm).

-c [ANSI|OEM|<dynamic collation>] Character type (default ANSI)

This option sets the character type of the SQL statement or connection used by the backup utility. This is the character type used to open each table and transfer its data. If you are using one of the Visual FoxPro compatible collations (also known as dynamic collations), you can specify the name of the collation with this parameter (e.g., GENERAL\_VFP\_CI\_AS\_1252).

-d Don't overwrite existing backup tables

The default behavior is to overwrite all tables when doing a backup or restore operation. Use this option to cause a warning to be logged instead of overwriting existing tables.

-f Differential backup

This option will perform a [differential backup](master_differential_backups.htm), where only tables and records that have been modified since the last backup will be processed. Only use this option on databases that you have previously called adsbackup on using the a option to initialize the differential backup.

-h [ON|OFF] Rights checking (default ON)

This options sets the rights checking mode of the SQL statement or connection used by the backup utility. This is the rights checking mode used to open each table and transfer its data.

-i <file1, .. ,filen> Include file list

-e <file1, .. ,filen> Exclusion file list

These options can be used to provide a list of tables to include or exclude from the backup or restore command. When using a data dictionary specify the table name in the dictionary. When using free tables, specify the base table name including the file extension. For example, "table1.adt".

-m Backup metadata only

This option will make a backup or restore only copy of the data dictionary. None of the tables will be copied.

-n <path> Path to store the backup output table

This option can be used to specify the location you would like the backup log table to go to. The path specified must be in UNC form.

-o <filepath> Path and filename to the backup output table

This option cannot only be used to specify a specific path for the backup log, but can also specify a file name. The path specified must be in UNC form.

-p Password(s)

Database password for the ADSSYS user or a user in the DB:Backup group if source path is a database.

List of free table passwords if source path is a directory. Free table usage can pass a single password for all encrypted tables, or a name/value pair for each table, for example, "password\_for\_all" or "table1=pass1;table2=pass2".

-q [PROP|COMPAT] Locking mode, proprietary or compatible (default PROP)

This option sets the locking mode of the SQL statement or connection used by the backup utility. This is the locking mode used to open each table and transfer its data.

-r Restore database or free table files

Use this option to perform a restore instead of a backup (which is the default behavior).

-s <server path> Connection path of ADS server or full connection string to perform backup or restore

In most situations, the adsbackup utility can determine the connection path to use by examining the source path. If you are having connection problems, however, or want to use a specific connection path when performing the backup or restore, you can use this option.

 

In addition when using the Windows and Linux versions of the utility, this option can be used to provide a full connection string ([see AdsConnect101](ace_adsconnect101.htm) for a description of all parameter names and values). This option is not supported with the Java version. This can be used to provide additional connection information. For example, to make a Transport Layer Security (TLS) connection to the server and use FIPS mode, you can use this option.  If any spaces are in the provided connection string, it must be enclosed in quotes.  For example: -s "Data Source=\\server\share\path\my.add; DDPassword=mypassword; CommType=TLS; TLSCertificate=c:\certs\clientcert.pem; TLSCommonName=www.myserver.com;"

-t <server port> Connection port of Advantage Database Server to perform the backup or restore (default 6262)

This option defines the server port the adsbackup utiltity connects to when using the Advantage JDBC Driver. This option is only valid with the java adsbackup utility.

-u [ADT|CDX|VFP|NTX] Table type (default ADT)

This options sets the table type of the SQL statement or connection used by the backup utility. This is the table type used to open each table and transfer its data. Note this also determines the table type of the log file produced by the backup or restore procedure.

-v [1-10] Lowest level of error severity to return (default 1)

Use this option to configure adsbackups tolerance of warnings or low severity errors.

-w <table type maps> Map table extensions to a table type setting

Use this option to specify what table type should be used for a specific table extension. Only necessary for free table backup/restore operations. This option can be used to backup and/or restore a directory of free tables that consists of both ADT and DBF tables. The option should include a three byte extension, followed by an equal sign, followed by the Advantage table type constant. Each mapping is separated by a comma. For example, -wadt=ADS\_ADT,dbf=ADS\_CDX could be used to specify files with the extension "adt" should be opened using the ADS\_ADT table type, and files with the extension "dbf" should be opened with the ADS\_CDX table type. This mapping allows the caller to specify the table type at a more granular level (as opposed to a single table type global setting).

-x Dont create the output table if no errors are logged

Use this option if you do not want the empty log table created if the backup or restore operation completes with zero errors.

-y <user name> User name for the connection to the server for the backup

Use this option if you want to connect as a user other than ADSSYS.  Any non-ADSSYS user must be a member of the DB:Backup group to perform backups.  Use the -p option to specify the password.  This option should only be used with database backup and restore operations.

-z <options> Additional options

Any additional [backup and restore options](master_backup_and_restore_options.htm) can be specified with this parameter. For example, you can specify the name of an archive file, -z "ArchiveFile=mybackup.tar;".