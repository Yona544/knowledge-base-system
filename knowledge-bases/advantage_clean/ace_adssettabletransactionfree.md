---
title: Ace Adssettabletransactionfree
slug: ace_adssettabletransactionfree
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssettabletransactionfree.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 417c59637064aa1c364aad9a00b3af3f57ce616c
---

# Ace Adssettabletransactionfree

AdsSetTableTransactionFree

AdsSetTableTransactionFree

Advantage Client Engine

| AdsSetTableTransactionFree  Advantage Client Engine |  |  |  |  |

Sets the tables transaction-free state.

Syntax

| UNSIGNED32 | AdsSetTableTransactionFree( ADSHANDLE hTable,                             UNSIGNED16 usTransFree ); |

Parameters

| hTable (I) | Handle of table |
| usTransFree (I) | Desired transaction-free state of the table.  A non-zero value configures the table as a transaction-free table.  The default value is false. |

Remarks

The tables transaction-free state controls how the table responds to updates performed on the table while a transaction is active.  When the tables usTransFree state is set to true, the table is recognized as a transaction-free table.  Updates to transaction-free tables and their associated indexes performed outside of the scope of all transactions:  The updates are immediate, visible to other clients, and are persisted to the table regardless of whether the transaction is committed, or rolled-back.

Changing a table to a transaction-free table should be done with care, and only after considering all uses of the given table.  For most applications, a great majority of tables should not be defined as transaction-free tables.  There are, however, some situations which may warrant the use of transaction-free tables.  One such situation is the use of audit tables:  When triggers are defined that populate one or more audit tables when sensitive data is updated, it is possible that database administrators will want to capture an attempt to update data, even if that attempt was part of a transaction that was rolled-back.  (When usTransFree is set to False, the rollback of the transaction will also rollback the entries in the audit table.)

Using AdsSetTableTransactionFree to modify the tables transaction-free table state requires that the table be opened exclusively.

While this API can be used with Advantage Local Server, it makes little sense to do so, as Advantage Local Server does not support transactions.  When using Advantage Local Server, all tables respond to updates the same, regardless of whether or not they are defined as transaction-free tables.

See Also

[AdsBeginTransaction](ace_adsbegintransaction.md)

[AdsCommitTransaction](ace_adscommittransaction.md)

[AdsIsTableTransactionFree](ace_adsistabletransactionfree.md)

[AdsRollbackTransaction](ace_adsrollbacktransaction.md)

[Transaction-Free Tables](master_transaction_free_tables.md)

[sp\_ModifyTableProperty](master_sp_modifytableproperty.md)
