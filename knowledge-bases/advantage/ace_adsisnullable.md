AdsIsNullable




Advantage Database Server 12  

AdsIsNullable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsNullable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsNullable Advantage Client Engine Ace\_Adsisnullable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsNullable  Advantage Client Engine |  |  |  |  |

Determines if a given field can be set to NULL.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsNullable (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pbNullable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to examine. |
| pbNull (O) | Will be True on return if the specified field can store NULL. |

Remarks

This API is primarily intended for the VFP table type to be able to determine if a specific column was created with a NULL or NOT NULL option.  See [DBF Field Types and Specifications](master_dbf_field_types_and_specifications.htm). It can, however, be used with other table types and will return the appropriate value.  For example, it will return FALSE for an AUTOINC field and TRUE for an INTEGER field an an ADT table.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

See Also

[AdsSetNull](ace_adssetnull.htm)

[AdsIsNull](ace_adsisnull.htm)