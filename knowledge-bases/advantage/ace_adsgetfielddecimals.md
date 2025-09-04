AdsGetFieldDecimals




Advantage Database Server 12  

AdsGetFieldDecimals

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetFieldDecimals  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetFieldDecimals Advantage Client Engine ace\_Adsgetfielddecimals Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetFieldDecimals  Advantage Client Engine |  |  |  |  |

Retrieves decimals (for numerics) of a field in a table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetFieldDecimals (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pusDecimals); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field. |
| pusDecimals (O) | Return field decimals. |

Remarks

AdsGetFieldDecimals returns the number of digits of decimal precision in the field to the right of the decimal point in a numeric field.

Example

[Click Here](ace_examples.htm#adsgetfielddecimalsexample)

See Also

[AdsGetFieldLength](ace_adsgetfieldlength.htm)

[AdsGetFieldName](ace_adsgetfieldname.htm)

[AdsGetFieldNum](ace_adsgetfieldnum.htm)

[AdsGetFieldType](ace_adsgetfieldtype.htm)

[AdsGetNumFields](ace_adsgetnumfields.htm)