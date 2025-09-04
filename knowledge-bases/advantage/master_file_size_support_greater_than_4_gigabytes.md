File Size Support Greater Than 4 Gigabytes




Advantage Database Server 12  

File Size Support Greater Than 4 Gigabytes

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| File Size Support Greater Than 4 Gigabytes  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - File Size Support Greater Than 4 Gigabytes Advantage Concepts master\_File\_size\_support\_greater\_than\_4\_gigabytes Advantage Concepts > Advantage File Formats > Advantage Proprietary File Format > File Size Support Greater Than 4 Gigabytes / Dear Support Staff, |  |
| File Size Support Greater Than 4 Gigabytes  Advantage Concepts |  |  |  |  |

The Advantage proprietary file format (ADT/ADM/ADI) can support files sizes greater than 4 GB when used on NTFS or Linux file systems.

Beginning with v8.0, Advantage Database Server can utilize DBF tables and their associated memo files (FPT and DBT) with file sizes greater than 4 GB. Index files associated with DBF tables (CDX, IDX, NTX) cannot exceed the 4 GB limit due to file format limitations, but this problem can be avoided by using multiple index files. When using DBF tables over 4 GB in size, you must use Advantage Proprietary Locking. Also, note that CA-Clipper applications must turn off rights checking (AX\_RightsCheck( .F. )) when opening tables that exceed 4 GB in size.