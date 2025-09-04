6314 Error opening connection semaphore file




Advantage Database Server 12  

6314 Error opening connection semaphore file

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6314 Error opening connection semaphore file  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6314 Error opening connection semaphore file Advantage Error Guide error\_6314\_error\_opening\_connection\_semaphore\_file Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6314 Error opening connection semaphore file  Advantage Error Guide |  |  |  |  |

Problem: An error occurred when opening the Advantage connection semaphore file. When an Advantage application first connects to the Advantage Database Server, it attempts to open a semaphore connection file. This open failed.

Solution: By default, the semaphore connection file exists in the same directory as the first table opened. If the user does not have network READ privileges in this directory, the semaphore file cannot be opened and the user cannot connect to the Advantage server. The application must either open its first table in a directory where the user has network READ privileges or a non-default semaphore file path must be setup. See the Semaphore File Path description in the Configuration chapter in your Advantage Database Server Guide for information on setting up a semaphore connection file path. It is also possible for the semaphore file open failure to occur in 16-bit Windows applications due to a file open limit. By default, some applications limit the total number of open files to 20. If this is the case with your application, increase the maximum number of open files.

Note If using a 16-bit client application to connect to a Linux server the following semaphore file restrictions apply:

\* Must be running Samba to share the file system on the Linux server

\* Samba share name must be less than or equal to 8 characters

\* Must turn off Samba optimistic locks (oplocks) in smb.conf file