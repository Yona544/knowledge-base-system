---
title: Ace Adssetlogical
slug: ace_adssetlogical
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetlogical.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d577ae9726fe3beedcd681c2412665dd87c5ec5d
---

# Ace Adssetlogical

AdsSetLogical

AdsSetLogical

Advantage Client Engine

| AdsSetLogical  Advantage Client Engine |  |  |  |  |

Stores the given logical value in the given field.

Syntax

| UNSIGNED32 | AdsSetLogical (ADSHANDLE hObj,  UNSIGNED8 \*pucFldName,  UNSIGNED16 bValue); |

Parameters

| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFldName (I) | Name of field to set. |
| bValue (I) | Store this value in the field. Zero means False, non-zero means True. |

Remarks

AdsSetLogical can set the value of the logical field to True or False. To set a logical field to NULL, use [AdsSetEmpty](ace_adssetempty.md).

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to AdsInitRawKey and AdsBuildRawKey.

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.md). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example 1

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE married = :MarriedParam" );

AdsSetLogical( hStatement, "MarriedParam", TRUE );

AdsExecuteSQL( hStatement, &hCursor);

 

When using unnamed parameters these parameters MUST be referenced using their parameter number.

Example 2

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE married = :MarriedParam" );

AdsSetLogical( hStatement, ADSFIELD(1), TRUE );

AdsExecuteSQL( hStatement, &hCursor);

Example 3

[Additional Example](ace_examples.md#adssetlogicalexample)

See Also

[AdsGetLogical](ace_adsgetlogical.md)

[AdsSetField](ace_adssetfield.md)

[AdsInitRawKey](ace_adsinitrawkey.md)

[AdsBuildRawKey](ace_adsbuildrawkey.md)

[AdsPrepareSQL](ace_adspreparesql.md)
