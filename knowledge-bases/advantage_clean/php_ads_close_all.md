---
title: Php Ads Close All
slug: php_ads_close_all
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_close_all.htm
source: Advantage CHM
tags:
  - php
checksum: 62e7083ff82b49a708e45b3389459a3485575979
---

# Php Ads Close All

ads\_close\_all

ads\_close\_all

Advantage PHP Extension

| ads\_close\_all  Advantage PHP Extension |  |  |  |  |

Closes all connections to the Advantage Database Server.

Syntax

void ads\_close\_all( void )

Parameters

None.

Remarks

ads\_close\_all is used to close all connections to the server. All active transactions will be rolled back before all connections are closed

Example

<?php

echo "Basic Connect<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connect<br>\n";

ads\_close\_all();

echo "Closed All Transactions<br>\n";

?>

See Also

[ads\_close](php_ads_close.md)

[ads\_connect](php_ads_connect.md)
