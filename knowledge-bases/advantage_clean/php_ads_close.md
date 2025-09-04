---
title: Php Ads Close
slug: php_ads_close
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_close.htm
source: Advantage CHM
tags:
  - php
checksum: 494652a097fa1d3f0656b45ca7596af3ca777f64
---

# Php Ads Close

ads\_close

ads\_close

Advantage PHP Extension

| ads\_close  Advantage PHP Extension |  |  |  |  |

Closes a connection to the Advantage Database Server.

Syntax

void ads\_close( int connection\_id )

Parameters

| connection\_id (I) | ID of a connection to the Advantage Database Server. |

Remarks

ads\_close is used to close a connection to the specified server. If ads\_close is called on a connection with a transaction active, the transaction will be rolled back and then the connection closed.

Example

<?php

echo "Basic Connect<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connect<br>\n";

ads\_close( $rConn );

echo "Closed<br>\n";

?>

See Also

[ads\_close\_all](php_ads_close_all.md)

[ads\_connect](php_ads_connect.md)
