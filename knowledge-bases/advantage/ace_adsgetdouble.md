AdsGetDouble




Advantage Database Server 12  

AdsGetDouble

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetDouble  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetDouble Advantage Client Engine ace\_Adsgetdouble Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetDouble  Advantage Client Engine |  |  |  |  |

Retrieves an 8-byte double value from the given field.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetDouble (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  double64 \*pdValue); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| pdValue (O) | Return the value. |

Remarks

AdsGetDouble returns the IEEE 64-bit double representation of the value in a numeric, long integer, integer, short integer, double, CurDouble, Money, RowVersion, or autoincrement field. This function provides the largest range available in the Advantage Client Engine for retrieving numeric values. However, since the IEEE 64-bit double value has roughly 15 digits of precision, loss of precision is possible when retrieving values from long integer, Money or numeric field types.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.htm#adsgetdoubleexample)

See Also

[AdsSetDouble](ace_adssetdouble.htm)

[AdsGetField](ace_adsgetfield.htm)

[AdsGetLong](ace_adsgetlong.htm)

[AdsGetLongLong](ace_adsgetlonglong.htm)