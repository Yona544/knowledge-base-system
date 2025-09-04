AdsSetEmpty




Advantage Database Server 12  

AdsSetEmpty

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetEmpty  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetEmpty Advantage Client Engine ace\_Adssetempty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetEmpty  Advantage Client Engine |  |  |  |  |

Sets the given field to its NULL value when using ADTs or to its empty value when using DBFs (including VFP tables).

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetEmpty (ADSHANDLE hObj,  UNSIGNED8 \*pucFldName); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, or index order. |
| pucFldName (I) | Name of field to set to empty/null. |

Remarks

Null and empty values vary by field type. AdsSetEmpty ensures that the value set in the field is what Advantage expects as a NULL value for ADTs or an empty value for DBFs. To set a VFP field to NULL, use [AdsSetNull](ace_adssetnull.htm).

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to [AdsInitRawKey](ace_adsinitrawkey.htm) and [AdsBuildRawKey](ace_adsbuildrawkey.htm).

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.htm). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2. Note that when used with SQL statement handles, AdsSetEmpty is equivalent to AdsSetNull even when the table type is VFP; it will set the parameter value to NULL.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.htm#adssetemptyexample)

See Also

[AdsIsEmpty](ace_adsisempty.htm)

[AdsSetField](ace_adssetfield.htm)

[AdsInitRawKey](ace_adsinitrawkey.htm)

[AdsBuildRawKey](ace_adsbuildrawkey.htm)

[AdsSetNull](ace_adssetnull.htm)