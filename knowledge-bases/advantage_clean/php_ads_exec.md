---
title: Php Ads Exec
slug: php_ads_exec
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_exec.htm
source: Advantage CHM
tags:
  - php
checksum: ffd6084e27ffc4004c3fabcf10cc149065677af2
---

# Php Ads Exec

ads\_exec

ads\_exec

Advantage PHP Extension

| ads\_exec  Advantage PHP Extension |  |  |  |  |

Prepares and executes an SQL statement.

Syntax

resource ads\_exec( int connection\_id, string query )

Parameters

| connection\_id (I) | ID of a connection to the Advantage Database Server. |
| query (I) | The SQL statement to be executed. |

Remarks

ads\_exec is a combination of ads\_prepare and ads\_execute. The SQL statement executed via ads\_exec cannot have parameters. If parameters are required, use ads\_prepare and ads\_execute.

When executing a successful SELECT statement or EXECUTE statement with a result set, a result set identifier will be returned. This result set identifier can be used to retrieve values from the result set.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Executing a statement<br>\n";

$rResult = ads\_exec( $rConn, "SELECT SUM( amount ) as Total FROM orders" );

echo "Statement executed<br>\n";

 

echo "Getting the cursor name<br>\n";

$sName = ads\_cursor( $rResult );

echo "The cursor is named: " . $sName . "<br>\n";

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

See Also

[ads\_connect](php_ads_connect.md)

[ads\_prepare](php_ads_prepare.md)

[ads\_execute](php_ads_execute.md)

[ads\_do](php_ads_do.md)
