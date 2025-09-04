AdsGetTableType




Advantage Database Server 12  

AdsGetTableType

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetTableType  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetTableType Advantage Client Engine ace\_Adsgettabletype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetTableType  Advantage Client Engine |  |  |  |  |

Returns the table type with which the table was opened

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetTableType (ADSHANDLE hTable,  UNSIGNED16 \*pusType); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pusType (O) | Return type of table (ADS\_ADT, ADS\_VFP, ADS\_NTX or ADS\_CDX). |

Remarks

Tables opened with ADS\_ADT can open only ADI indexes. Tables opened with ADS\_CDX ands ADS\_VFP can only open IDX or CDX FoxPro-compatible indexes. Tables opened with ADS\_NTX will only open NTX indexes. Attempting to open a table with a memo file containing the incorrect table type (ADM for ADS\_ADT, DBT for ADS\_NTX or FPT for ADS\_CDX and ADS\_VFP) will result in a failed open with the error code AE\_CORRUPT\_TABLE.

Example

[Click Here](ace_examples.htm#adsgettabletypeexample)

See Also

[AdsCreateTable](ace_adscreatetable.htm)

[AdsOpenTable](ace_adsopentable.htm)