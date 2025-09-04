---
title: Master Sp Ignoretransactions
slug: master_sp_ignoretransactions
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_ignoretransactions.htm
source: Advantage CHM
tags:
  - master
checksum: ae1ff15ff2686f90ca0e61b95ec6abca38a1bdfd
---

# Master Sp Ignoretransactions

sp\_IgnoreTransactions

sp\_IgnoreTableTransactions

Advantage SQL Engine

| sp\_IgnoreTableTransactions  Advantage SQL Engine |  |  |  |  |

Sets the tables transaction-free table state.

Syntax

sp\_IgnoreTableTransactions( TableName, CHARACTER, 515, [ IgnoreTransactions, LOGICAL] )

Parameters

| TableName (I) | The name of the table to configure.  For free tables, this must be a relative path to the table on the server or a fully qualified UNC path.  For database tables, this should be the name of the table in the database. |
| IgnoreTransactions (I) | Optional parameter indicating the desired transaction-free table state.  If not specified, the table is converted into a transaction-free table. |

Output

None

Remarks

The sp\_IgnoreTableTransactions system procedure is used to configure a table as a transaction-free table (when IgnoreTransactions is true, or omitted) or restore the table to its default state (when IgnoreTransations is False).

This system procedure requires exclusive access to the table.

See Also

[system.tables](master_system_tables.md)

[AdsSetTableTransactionFree](ace_adssettabletransactionfree.md)

[Transaction-Free Tables](master_transaction_free_tables.md)

[sp\_ModifyTableProperty](master_sp_modifytableproperty.md)

Examples

 

EXECUTE PROCEDURE sp\_IgnoreTableTransactions( 'customers' );

 

EXECUTE PROCEDURE sp\_IgnoreTableTransactions( '\\server\share\log\_table', false );
