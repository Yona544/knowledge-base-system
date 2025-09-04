AdsSetNull




Advantage Database Server 12  

AdsSetNull

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetNull  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetNull Advantage Client Engine ace\_Adssetnull Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetNull  Advantage Client Engine |  |  |  |  |

Sets the given field to its NULL value when using ADT or VFP tables or to its empty value when using non-VFP DBFs.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetNull (ADSHANDLE hObj,  UNSIGNED8 \*pucFldName); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, or index order. |
| pucFldName (I) | Name of field to set to empty/null. |

Remarks

For table types ADS\_ADT, ADS\_NTX, and ADS\_CDX, this API behaves identically to [AdsSetEmpty](ace_adssetempty.htm). With ADS\_VFP tables, empty and NULL values are not the same, and the AdsSetNull API will set VFP fields to their NULL value if the field can be null. If the field cannot be NULL, then it will return error AE\_NOT\_VFP\_NULLABLE\_FIELD (5205).

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to [AdsInitRawKey](ace_adsinitrawkey.htm) and [AdsBuildRawKey](ace_adsbuildrawkey.htm).

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.htm). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2. Note that when used with SQL statement handles, AdsSetNull is equivalent to AdsSetEmpty even when the table type is VFP; it will set the parameter value to NULL.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

See Also

[AdsIsNull](ace_adsisnull.htm)

[AdsSetField](ace_adssetfield.htm)

[AdsInitRawKey](ace_adsinitrawkey.htm)

[AdsBuildRawKey](ace_adsbuildrawkey.htm)

[AdsSetEmpty](ace_adssetempty.htm)