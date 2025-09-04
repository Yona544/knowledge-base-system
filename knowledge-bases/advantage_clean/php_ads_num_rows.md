---
title: Php Ads Num Rows
slug: php_ads_num_rows
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_num_rows.htm
source: Advantage CHM
tags:
  - php
checksum: b70f5cb06c498b6aa328d6af2f6d1aadbe185b6c
---

# Php Ads Num Rows

ads\_num\_rows

ads\_num\_rows

Advantage PHP Extension

| ads\_num\_rows  Advantage PHP Extension |  |  |  |  |

Returns the number of rows in a result set.

Syntax

int ads\_num\_rows( resource result\_id )

Parameters

| result\_id (I) | ID of a result set. |

Remarks

For SELECT statements or EXECUTE PROCEDURE statements with a result set, the number of rows will be 1 until the last row has been fetched. For INSERT, UPDATE, and DELETE statements, the number of rows affected by the statement is returned. In the event of an error, 1 will be returned.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Double all customer's credit limit.<br>\n";

$rResult = ads\_do( $rConn, "UPDATE customers SET credit\_limit = ( credit\_limit \* 2 )" );

 

$iCount = ads\_num\_rows( $rResult );

echo $iCount . " records updated.<br>\n";

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>
