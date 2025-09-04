AdsGetTableLockType




Advantage Database Server 12  

AdsGetTableLockType

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetTableLockType  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetTableLockType Advantage Client Engine ace\_Adsgettablelocktype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetTableLockType  Advantage Client Engine |  |  |  |  |

Retrieves the type of locking used with the table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetTableLockType (ADSHANDLE hTable,  UNSIGNED16 \*pusLockType); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pusLockType (O) | Type of locking used for table (ADS\_PROPRIETARY\_LOCKING, ADS\_COMPATIBLE\_LOCKING). |

Remarks

AdsGetTableLockType will retrieve the setting of the type of locking specified during the table open/create. See [Advantage Locking Modes](master_advantage_locking_modes.htm) for more information on Advantage locking options. Note that if the usTableType parameter used in the open/create was ADS\_ADT, ADS\_PROPRIETARY\_LOCKING will always be returned when using the Advantage Database Server, and ADS\_COMPATIBLE\_LOCKING will always be returned when using the Advantage Local Server.

Example

[Click Here](ace_examples.htm#adsgettablelocktypeexample)

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsCreateTable](ace_adscreatetable.htm)