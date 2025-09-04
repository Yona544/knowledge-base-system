---
title: Ace Adsgetsqlstatement
slug: ace_adsgetsqlstatement
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetsqlstatement.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 8e3f48d09839c24347369730a5206a600d91f987
---

# Ace Adsgetsqlstatement

AdsGetSQLStatement

AdsGetSQLStatement

Advantage Client Engine

| AdsGetSQLStatement  Advantage Client Engine |  |  |  |  |

Returns the SQL statement text associated with the statement handle passed in.

Syntax

UNSIGNED32 AdsGetSQLStatement( ADSHANDLE hStmt,

UNSIGNED8 \*pucSQL,

UNSIGNED16 \*pusLen );

Parameters

| hStmt (I) | Statement handle to retrieve the SQL statement text from. |
| pucSQL (O) | Buffer to return the statement in. |
| pusLen (I/O) | Length of pucSQL buffer on input, number of bytes returned on output. |

Remarks

Use AdsGetSQLStatement to retrive the SQL statement text last executed on hStmt
