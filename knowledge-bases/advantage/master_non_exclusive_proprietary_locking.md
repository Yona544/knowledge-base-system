Non-Exclusive Proprietary Locking




Advantage Database Server 12  

Non-Exclusive Proprietary Locking

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Non-Exclusive Proprietary Locking  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Non-Exclusive Proprietary Locking Advantage Database Server master\_Non\_exclusive\_proprietary\_locking Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Non-Exclusive Proprietary Locking  Advantage Database Server |  |  |  |  |

In older versions of Advantage, proprietary locking did not open files using an exclusive mode, instead it used a "deny write" open mode. While this would allow applications that do not use Advantage Database Server to have access to the data files, it could also lead to index corruption. These other applications could still lock bytes in the files causing Advantage read and write operations to fail. For this reason the default proprietary open mode was changed. If, however, you require applications that do not use Advantage Database Server (such as backup software, or reporting software, or applications using Advantage Local Server) to open files in a shared, read-only mode, this server option is available to revert to the older behavior.

For more details on proprietary locking, see [Advantage Proprietary Locking](master_advantage_proprietary_locking.htm).

To turn off the exclusive proprietary locking file open mode, perform one of the following:

For Linux:

Add the following line in the Advantage Database Server configuration file (ads.conf).

NONEXCLUSIVE\_PROPRIETARY\_LOCKING=1

For Windows:

Add the following DWORD using the Registry Editor (REGEDIT.EXE) into the registry, and set its value to 1.

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\NONEXCLUSIVE\_PROPRIETARY\_LOCKING