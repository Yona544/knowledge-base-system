AdsGetFieldNum




Advantage Database Server 12  

AdsGetFieldNum

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetFieldNum  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetFieldNum Advantage Client Engine ace\_Adsgetfieldnum Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetFieldNum  Advantage Client Engine |  |  |  |  |

Retrieves the number of a field in a table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetFieldNum (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pusNum); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field. |
| pusNum (O) | Return field number corresponding to given name. |

Remarks

The field number is an index in the table of fields from first to last, with the index of the first field being 1.

When using SQL statements the table handle parameter can be replaced with a cursor handle. In this situation AdsGetFieldNumber will return the column number in the rowset.

Example

[Click Here](ace_examples.htm#adsgetfieldnumexample)

See Also

[AdsGetFieldName](ace_adsgetfieldname.htm)

[AdsGetNumFields](ace_adsgetnumfields.htm)