---
title: Php Ads Rollback
slug: php_ads_rollback
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_rollback.htm
source: Advantage CHM
tags:
  - php
checksum: fadb1ca7d36415c83cb9d3a4c0c8768891a07d7e
---

# Php Ads Rollback

ads\_rollback

ads\_rollback

Advantage PHP Extension

| ads\_rollback  Advantage PHP Extension |  |  |  |  |

Rolls back the active transaction for the given connection.

Syntax

boolean ads\_rollback( resource connection\_id )

Parameters

| connection\_id (I) | ID of a connection to the Advantage Database Server. |

Remarks

Calling ads\_rollback when the Advantage PHP Extension is not in auto-commit mode rolls back the active transaction on the given connection and begins a new transaction. If the Advantage PHP Extension is in auto-commit mode, calling ads\_rollback has no effect and True is returned. If the active transaction is successfully rolled back, True is returned. False is returned in the event of an error.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Turning off auto-commit. Starts a transactions.<br>\n";

ads\_autocommit( $rConn, False );

 

echo "Updating the customers credit limit.<br>\n";

$rResult = ads\_do( $rConn, "UPDATE customers SET credit\_limit = ( credit\_limit \* 2 )" );

 

echo "Rolling back the changes.<br>\n";

ads\_rollback( $rConn );

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

See Also

[ads\_autocommit](php_ads_autocommit.md)

[ads\_commit](php_ads_commit.md)

[ads\_connect](php_ads_connect.md)
