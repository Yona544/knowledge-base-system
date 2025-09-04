---
title: Ace Adsstmtdisableencryption
slug: ace_adsstmtdisableencryption
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsstmtdisableencryption.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 263a4e32115944bb828480e8eb9ff0f8c48d9553
---

# Ace Adsstmtdisableencryption

AdsStmtDisableEncryption

AdsStmtDisableEncryption

Advantage Client Engine

| AdsStmtDisableEncryption  Advantage Client Engine |  |  |  |  |

Does not encrypt the cursor generated after executing the SQL statement.

Syntax

| UNSIGNED32 | AdsStmtDisableEncryption( ADSHANDLE hStatement ); |

Parameter

| hStatement(I) | Handle of an SQL statement created by a call to AdsCreateSQLStatement. |

Remarks

This function reverses the effect of [AdsStmtEnableEncryption](ace_adsstmtenableencryption.md).

Example

[Click Here](ace_more_examples.md#adsstmtdisableencryption_example)

See Also

[AdsStmtEnableEncryption](ace_adsstmtenableencryption.md)
