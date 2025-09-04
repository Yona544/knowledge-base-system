---
title: Php Ads Longreadlen
slug: php_ads_longreadlen
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_longreadlen.htm
source: Advantage CHM
tags:
  - php
checksum: 35e60e30b9e2dbfd09af817fec974008c5849f80
---

# Php Ads Longreadlen

ads\_longreadlen

ads\_longreadlen

Advantage PHP Extension

| ads\_longreadlen  Advantage PHP Extension |  |  |  |  |

Limits the amount of data that is read from memo or BLOB fields.

Syntax

bool ads\_longreadlen( resource result\_id,

int length )

Parameters

| result\_id (I) | ID of a result set. |
| length (I) | Amount of data to read. |

Remarks

ads\_longreadlen sets the maximum amount of data that is read from memo and BLOB fields in a table. The default length read for memo and BLOB fields is 4096 bytes. True is returned if the value is successfully modified. False is returned in the event of an error.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Retrieve the customers.<br>\n";

$rResult = ads\_do( $rConn, "SELECT \* FROM customers" );

 

echo "Set the amount of data read from memo fields to 16k.<br>\n";

ads\_longreadlen( $rResult, 16384 );

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

See Also

[ads\_fetch\_array](php_ads_fetch_array.md)

[ads\_fetch\_into](php_ads_fetch_into.md)
