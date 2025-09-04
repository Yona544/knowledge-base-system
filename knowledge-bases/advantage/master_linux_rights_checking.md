Linux Rights Checking




Advantage Database Server 12  

Linux Rights Checking

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Linux Rights Checking  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Linux Rights Checking Advantage Concepts master\_Linux\_rights\_checking Advantage Concepts > Advantage Linux Development Notes > Linux Rights Checking / Dear Support Staff, |  |
| Linux Rights Checking  Advantage Concepts |  |  |  |  |

Rights checking functionality can only work if the client machine is logged in to the server in a manor that allows the client direct access to server files. If using Samba or NFS to access files on a remote machine then rights checking will behave as expected. If simply accessing files on a local machine using a native path (/mydata/tables, for example) rights checking will behave as expected.

There are a few situations, however, in which rights checking must be disabled. An example is a Windows client connecting to an ADS for Linux server that is not running Samba. In this situation the client machine is not logged in to the Linux server, and hence, can not perform any rights checking. If you attempt to open a table with the Advantage Rights Checking option turned on you will receive an AE\_FILE\_NOT\_FOUND (5004) error.