---
title: Ace Adsstmtcleartablepasswords
slug: ace_adsstmtcleartablepasswords
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsstmtcleartablepasswords.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: dfa654bcf9b83f5ab4ff59ce8a7e1e5441345114
---

# Ace Adsstmtcleartablepasswords

AdsStmtClearTablePasswords

AdsStmtClearTablePasswords

Advantage Client Engine

| AdsStmtClearTablePasswords  Advantage Client Engine |  |  |  |  |

Clears all table encryption passwords associated with the statement handle.

Syntax

| UNSIGNED32 | AdsStmtClearTablePasswords( ADSHANDLE hStatement ); |

Parameters

| hStatement(I) | Handle of an SQL statement created by a call to AdsCreateSQLStatement. |

Remarks

This function removes all table encryption passwords set using [AdsStmtSetTablePassword](ace_adsstmtsettablepassword.md).

Example

[Click Here](ace_more_examples.md#adsstmtcleartablepasswords_example)

See Also

[AdsStmtEnableEncryption](ace_adsstmtenableencryption.md)

[AdsStmtDisableEncryption](ace_adsstmtdisableencryption.md)

[AdsStmtSetTablePassword](ace_adsstmtsettablepassword.md)
