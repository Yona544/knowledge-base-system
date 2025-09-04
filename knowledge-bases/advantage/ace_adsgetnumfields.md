AdsGetNumFields




Advantage Database Server 12  

AdsGetNumFields

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetNumFields  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetNumFields Advantage Client Engine ace\_Adsgetnumfields Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetNumFields  Advantage Client Engine |  |  |  |  |

Retrieves the number of fields in the given table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetNumFields (ADSHANDLE hTable,  UNSIGNED16 \*pusCount); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pusCount (O) | Return field count for given table. |

Remarks

The returned field count does not include the deleted byte in DBF tables.

When using SQL statements the table handle parameter can be replaced with a cursor handle. In this situation AdsGetNumFields will return the number of columns in the rowset.

Example

[Click Here](ace_examples.htm#adsgetnumfieldsexample)

See Also

[AdsCreateTable](ace_adscreatetable.htm)

[AdsGetFieldName](ace_adsgetfieldname.htm)