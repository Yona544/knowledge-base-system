---
title: Ace Adsverifysql
slug: ace_adsverifysql
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsverifysql.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 554e9d9d18ee2c302d9741ab48ac087c825c9679
---

# Ace Adsverifysql

AdsVerifySQL

AdsVerifySQL / AdsVerifySQLW

Advantage Client Engine

| AdsVerifySQL / AdsVerifySQLW  Advantage Client Engine |  |  |  |  |

Verifies the validity of an SQL statement without executing it

Syntax

| UNSIGNED32 | AdsVerifySQL( ADSHANDLE hStatement,               UNSIGNED8 \*pucSQL ) |
| UNSIGNED32 | AdsVerifySQLW( ADSHANDLE hStatement,                WCHAR     \*pwcSQL ) |

Parameters

| hStatement (I) | Handle of an SQL statement created by a call to AdsCreateSQLStatement. |
| pucSQL (I) | The SQL statement given as an ANSI encoded null terminated string. |
| pwcSQL (I) | The SQL statement given as a UTF-16 encoded null terminated Unicode string. UTF-16LE encoding is assumed unless the first two characters are the BOM indicating the encoding is UTF-16BE. |

Remarks

AdsVerifySQL and AdsVerifySQLW are useful to call prior to executing a time consuming SQL statement or to test a dynamically created SQL statement. The only difference between the two functions is the encoding of the SQL statement.

Example

ulRetVal = AdsVerifySQL( hStatement, "SELECT \* FROM demo10");

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "Invalid SQL statement" );

return ulRetVal;

}

ulRetVal = AdsExecute( hSQL, &hCursor );

 

See Also

[AdsPrepareSQL](ace_adspreparesql.md)

[AdsPrepareSQLW](ace_adspreparesql.md)

[AdsExecuteSQL](ace_adsexecutesql.md)

[AdsExecuteSQLDirect](ace_adsexecutesqldirect.md)
