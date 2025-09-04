---
title: Master Ignore Rights
slug: master_ignore_rights
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_ignore_rights.htm
source: Advantage CHM
tags:
  - master
checksum: 8af91322617be996fd37a19a39500629b7bb880f
---

# Master Ignore Rights

Ignore Rights

Ignore Rights

Advantage Concepts

| Ignore Rights  Advantage Concepts |  |  |  |  |

Restricting a user's network access rights to the directory and/or files as described in the [Check Rights](master_check_rights.md) security method often does not provide enough database security for free connections. If a user has been given the necessary read, write, create, and/or delete rights necessary to read, write, create, and/or delete data via your database application, then that user can also read, write, create, and/or delete data without using your application. Users can maliciously or accidentally corrupt the database by writing to the database with uncontrolled database editors. Files in the database could also be purposely or accidentally deleted entirely. What mission critical database applications often need is an additional level of security that only allows users to access the database via your database application. That way the database application has full control over what users are reading, writing, creating, and/or deleting data in the database. Non-client/server applications have no way to enforce this additional security; the Advantage Database Server does.

The Advantage Database Server "Ignore Rights" security method for free connections allows you to "hide" files in the database from all users who are not accessing data through an Advantage application.

The first step necessary to provide the Advantage "Ignore Rights" method of security is to have the system administrator remove network access rights from all users who could potentially damage the database. Once network access rights have been revoked from users to the database directory and/or files, users cannot maliciously or accidentally corrupt the database by writing to the database, creating new files, or deleting existing files in the database because they no longer have access to those files.

The second step necessary to provide the Advantage "Ignore Rights" method of security is use the "Ignore Rights" method of Advantage rights checking in your application when opening and creating files for free connections. When a file is to be opened or created by the Advantage Database Server, and "Ignore Rights" security is being used, the Advantage Database Server will NOT verify that the user has sufficient network access to the directory and/or file and will open or create the file for the application regardless of the user's network access rights. The Advantage Database Server can do this because it is running on the server and is running at a "supervisor" level. Using Advantage's "ignore rights" security method allows your Advantage application to have full control over who can access the database and how the database can be modified. Only Advantage applications using the "ignore rights" security method may access the database. Non-Advantage applications will have no access to the database at all.

The first step described above, in which the system administrator should remove network access rights from all users who could potentially damage the database, is very flexible. You and/or the system administrator can decide if all users and/or groups will have their network access rights revoked or if just certain users and/or groups will have their rights revoked. You and/or the system administrator can also decide if all network rights will be revoked, or if just some rights (such as delete and write rights) will be revoked. For example, if a report writer is being used, but that report writer is not an Advantage application, that report writer will be unable to function if all rights have been removed from all users. If a network "REPORTS" group is created and that group is given read-only access to the database directory and/or files, then users who are members of the "REPORTS" group can run the report writer utility in read-only mode against the database.

Ignore Rights security is not available with the Advantage Local Server. Check Rights security is effectively used during any connection to the Advantage Local Server.

If you are using the Advantage Database Server for Windows, and your data files are located on a drive using NTFS, that PCs "system" group must have full access to the share that contains the data in order for the Advantage Database Server service to have access to that data. Note that it must be that PCs system group that has full access, not the domains system group.

Note: Beginning with version 10.0, the client no longer performs rights checking by default. The default behavior is to use Ignore Rights regardless of the setting provided by the application. The pre-version 10.0 behavior can be restored with a call to [AdsSetRightsChecking](ace_adssetrightschecking.md).

Configured Semaphore Connection File Directory Often Necessary with the Advantage Database Server

When an Advantage application either calls an Advantage "connect" API (if available) or opens the first table, it establishes a connection between the application and the Advantage Database Server. During the connect, a semaphore connection file is created by the Advantage Database Server if the Use Semaphore Files configuration setting is set to 1. The semaphore connection file is implicitly opened by the Advantage application using a generic file open call. That is, the file is not opened through the Advantage Database Server. The semaphore connection file is used to aid in determining the connection status between the workstation and the server. The default directory in which this semaphore connection file is opened is the server directory specified in the "connect" API or where the first table is to be opened. The directory in which semaphore connection files are opened is configurable via the Advantage configuration file, ADS.CFG. Since the semaphore connection file is actually opened from the workstation and not via the Advantage Database Server, the user must have network READ rights in the directory in which the semaphore connection file exists.

When using the Advantage "Ignore Rights" method of security, user access rights are usually revoked from the directory where the data exists and, thus, where the semaphore connection file is created and needs to be opened. Therefore, it usually makes sense to configure a specific semaphore connection file directory in the Advantage Configuration file where no important data exists, but where all users have been given at least network READ access.

The network administrator can take further advantage of this semaphore connection file creation if the Use Semaphore Files configuration setting is set to 1 to limit which users can connect to the Advantage Database Server and have access to the database. Each user's network rights to the configured semaphore connection file directory will determine if a user can connect to the Advantage Database Server. Those users having network READ rights in the semaphore connection file directory will be able to connect to the Advantage Database Server. Those users who do not have network READ rights will not be able to connect to the Advantage Database Server and thus, will not be able to open any data files.

Opening the semaphore connection file does not obey the Advantage "rights checking" setting. A user must have at least READ access rights to the directory where the semaphore connection files are created in order to connect to the Advantage Database Server no matter how the "rights checking" setting is set.

The information above is only pertinent if you are connecting to Advantage with 16-bit client applications, or if you explicitly set the Use\_Semaphore\_Files option on the server. See the configuration option [Use\_Semaphore\_Files](master_use_semaphore_files.md) for more information.

See Also

[Database Security](master_database_security.md)
