AdsGetFieldOffset




Advantage Database Server 12  

AdsGetFieldOffset

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetFieldOffset  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetFieldOffset Advantage Client Engine ace\_Adsgetfieldoffset Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetFieldOffset  Advantage Client Engine |  |  |  |  |

Retrieves the offset of a field in a table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetFieldOffset (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED32 \*pulOffset); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field. |
| pulOffset (O) | Return field offset. This is the offset within the record. |

Remarks

Returns the offset of the field in the tables record image in the table.

Example

[Click Here](ace_examples.htm#adsgetfieldoffsetexample)

See Also

[AdsGetFieldLength](ace_adsgetfieldlength.htm)

[AdsGetFieldName](ace_adsgetfieldname.htm)

[AdsGetFieldNum](ace_adsgetfieldnum.htm)

[AdsGetNumFields](ace_adsgetnumfields.htm)

[AdsGetRecord](ace_adsgetrecord.htm)