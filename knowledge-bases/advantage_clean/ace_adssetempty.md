---
title: Ace Adssetempty
slug: ace_adssetempty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetempty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 7d4e0eb0b9832ff5a4fece1c9b15566db3dac8d3
---

# Ace Adssetempty

AdsSetEmpty

AdsSetEmpty

Advantage Client Engine

| AdsSetEmpty  Advantage Client Engine |  |  |  |  |

Sets the given field to its NULL value when using ADTs or to its empty value when using DBFs (including VFP tables).

Syntax

| UNSIGNED32 | AdsSetEmpty (ADSHANDLE hObj,  UNSIGNED8 \*pucFldName); |

Parameters

| hObj (I) | Handle of table, cursor, or index order. |
| pucFldName (I) | Name of field to set to empty/null. |

Remarks

Null and empty values vary by field type. AdsSetEmpty ensures that the value set in the field is what Advantage expects as a NULL value for ADTs or an empty value for DBFs. To set a VFP field to NULL, use [AdsSetNull](ace_adssetnull.md).

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to [AdsInitRawKey](ace_adsinitrawkey.md) and [AdsBuildRawKey](ace_adsbuildrawkey.md).

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.md). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2. Note that when used with SQL statement handles, AdsSetEmpty is equivalent to AdsSetNull even when the table type is VFP; it will set the parameter value to NULL.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.md#adssetemptyexample)

See Also

[AdsIsEmpty](ace_adsisempty.md)

[AdsSetField](ace_adssetfield.md)

[AdsInitRawKey](ace_adsinitrawkey.md)

[AdsBuildRawKey](ace_adsbuildrawkey.md)

[AdsSetNull](ace_adssetnull.md)
