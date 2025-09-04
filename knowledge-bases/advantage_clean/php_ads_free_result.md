---
title: Php Ads Free Result
slug: php_ads_free_result
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_free_result.htm
source: Advantage CHM
tags:
  - php
checksum: 95afd18ed35a710969f0b5083ed175135d0c4f32
---

# Php Ads Free Result

ads\_free\_result

ads\_free\_result

Advantage PHP Extension

| ads\_free\_result  Advantage PHP Extension |  |  |  |  |

Frees the resources associated with a result set.

Syntax

bool ads\_free\_result( resource result\_id )

Parameters

| result\_id (I) | ID of a result set. |

Remarks

ads\_free\_result can be used to free the resources associated with a result set before a script is finished executing. All memory for result sets is automatically freed when a script is finished. If a result set is successfully freed, True is returned. In the event of an error, False is returned.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Executing a statement<br>\n";

$rResult = ads\_do( $rConn, "SELECT SUM( amount ) as Total FROM orders" );

echo "Statment executed<br>\n";

 

echo "Free the result<br>\n";

$sName = ads\_free\_result( $rResult );

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

See Also

[ads\_execute](php_ads_execute.md)

[ads\_exec](php_ads_exec.md)

[ads\_do](php_ads_do.md)
