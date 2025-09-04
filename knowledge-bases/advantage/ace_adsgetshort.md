AdsGetShort




Advantage Database Server 12  

AdsGetShort

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetShort  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetShort Advantage Client Engine ace\_Adsgetshort Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetShort  Advantage Client Engine |  |  |  |  |

Retrieves the short (two byte) integer value from the given field

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetShort (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  SIGNED16 \*psValue); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| psValue (O) | Return the value. |

Remarks

AdsGetShort returns the signed short (two byte) value stored in the numeric, long integer, integer, short integer, double, CurDouble, Money, RowVersion, or auto-increment field. It is possible to either overflow the value or lose decimal precision by using this function. If more precision is desired, use [AdsGetDouble](ace_adsgetdouble.htm). If AdsGetShort is used to retrieve a Money field, the four decimal digits will be rounded to the nearest whole number.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_more_examples.htm#adsgetshortexample)

See Also

[AdsGetField](ace_adsgetfield.htm)

[AdsSetShort](ace_adssetshort.htm)