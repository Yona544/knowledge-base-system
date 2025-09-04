AdsLockType




Advantage Database Server 12  

AdsTableOptions.AdsLockType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsLockType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsLockType Advantage TDataSet Descendant ade\_Adslocktype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsLockType  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

Indicates which type of table locking to perform.

Syntax

type TAdsLockTypes = ( Proprietary, Compatible );

 

property AdsTableOptions.AdsLockType;

Description

Type of locking to use. Options are Proprietary locking and Compatible locking. If the application needs to share data in a writable mode with non-Advantage applications, then Compatible locking should be used. If the table will be used only by Advantage applications or by non-Advantage applications in a read-only mode, then Proprietary locking should be used. See [Advantage Locking Modes](master_advantage_locking_modes.htm) for more information.

For Advantage proprietary ADT tables, this setting is ignored. When an ADT table is opened with Advantage Database Server (i.e., remote server), proprietary locking is always used. When an ADT table is opened with Advantage Local Server, compatible locking is used to allow other Advantage applications using the Advantage Local Server to open the same table.