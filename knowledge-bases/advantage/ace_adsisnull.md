AdsIsNull




Advantage Database Server 12  

AdsIsNull

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsNull  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsNull Advantage Client Engine ace\_Adsisnull Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsNull  Advantage Client Engine |  |  |  |  |

Determines if a given field is NULL.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsNull (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pbNull); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to query. |
| pbNull (O) | Will be True on return if the specified field is NULL. |

Remarks

For table types ADS\_ADT, ADS\_NTX, and ADS\_CDX, this API behaves identically to [AdsIsEmpty](ace_adsisempty.htm). Use AdsIsNull to determine if the indicated field is NULL for ADT and VFP tables or empty for non-VFP DBFs.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

See Also

[AdsSetNull](ace_adssetnull.htm)

[AdsIsEmpty](ace_adsisempty.htm)