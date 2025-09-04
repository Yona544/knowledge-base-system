---
title: Php Ads Cursor
slug: php_ads_cursor
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_cursor.htm
source: Advantage CHM
tags:
  - php
checksum: d0c53202a65812893f7c237424296cb3e3ae3951
---

# Php Ads Cursor

ads\_cursor

ads\_cursor

Advantage PHP Extension

| ads\_cursor  Advantage PHP Extension |  |  |  |  |

Returns the cursor name of a given result set.

Syntax

string ads\_cursor( int result\_id )

Parameters

| result\_id (I) | ID of a result set. |

Remarks

Returns the cursor name for the given result\_id.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Executing a statement<br>\n";

$rResult = ads\_do( $rConn, "SELECT SUM( amount ) as Total FROM orders" );

echo "Statement executed<br>\n";

 

echo "Getting the cursor name<br>\n";

$sName = ads\_cursor( $rResult );

echo "The cursor is named: " . $sName . "<br>\n";

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>
