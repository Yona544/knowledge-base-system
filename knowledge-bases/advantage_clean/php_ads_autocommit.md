---
title: Php Ads Autocommit
slug: php_ads_autocommit
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_autocommit.htm
source: Advantage CHM
tags:
  - php
checksum: bf35e57d5074b906f8798f62d1f8614257bd2d16
---

# Php Ads Autocommit

ads\_autocommit

ads\_autocommit

Advantage PHP Extension

| ads\_autocommit  Advantage PHP Extension |  |  |  |  |

Toggles the auto-commit mode or retrieves the current setting.

Syntax

boolean ads\_autocommit( int connection\_id [, boolean OnOff] )

Parameters

| connection\_id (I) | ID of a connection to the Advantage Database Server. |
| OnOff (I) | Optional parameter that specifies whether to use auto-commit or manual commit mode. |

Remarks

Without the optional OnOff parameter, ads\_autocommit returns whether the Advantage PHP Extension is in auto-commit mode. A value of True means auto-commit mode is on, and False means auto-commit mode is off. By default, the Advantage PHP Extension is in auto-commit mode.

When in auto-commit mode, all changes made via data manipulation statements are automatically committed to the database. Turning off auto-commit mode starts a transaction. A transaction allows for a series of data manipulation statements to be either rolled back or committed to a database. When a transaction is rolled back, all changes to the database are undone and the database is the same as before the transaction. When the transaction is committed, all changes are saved to the database. See [Advantage Transaction Processing System (TPS)](master_advantage_transaction_processing_system_overview.md) for more details.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Turning off auto-commit. Starts a transaction.<br>\n";

ads\_autocommit( $rConn, False );

 

echo "Updating the customers credit limit.<br>\n";

$rResult = ads\_do( $rConn, "UPDATE customers SET credit\_limit = ( credit\_limit \* 2 )" );

 

echo "Committing the changes.<br>\n";

ads\_commit( $rConn );

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

See Also

[ads\_commit](php_ads_commit.md)

[ads\_rollback](php_ads_rollback.md)

[ads\_connect](php_ads_connect.md)
