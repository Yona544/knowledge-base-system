AdsGetTableCharType




Advantage Database Server 12  

AdsGetTableCharType

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetTableCharType  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetTableCharType Advantage Client Engine ace\_Adsgettablechartype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetTableCharType  Advantage Client Engine |  |  |  |  |

Retrieves the setting of the character data type with which the table was opened/created

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetTableCharType (ADSHANDLE hTable,  UNSIGNED16 \*pusCharType); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pusCharType (O) | Type of character data in table (ADS\_OEM, ADS\_ANSI). |

Remarks

AdsGetTableCharType will retrieve the setting of the character data type specified during the table open/create. Note that ADS\_ANSI will always be returned if the usTableType parameter used in the open/create was ADS\_ADT.

If one of the [dynamic collations](master_collation_support.htm) was specified when creating or opening the table, the value returned will still be ADS\_ANSI or ADS\_OEM depending on the collation selected.

Example

[Click Here](ace_examples.htm#adsgettablechartypeexample)

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsCreateTable](ace_adscreatetable.htm)

[AdsGetTableCollation](ace_adsgettablecollation.htm)