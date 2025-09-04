---
title: Php Ads Error
slug: php_ads_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_error.htm
source: Advantage CHM
tags:
  - php
checksum: 2fa40bc937dfd8ca07ee11e01d1c412d402a8b34
---

# Php Ads Error

ads\_error

ads\_error

Advantage PHP Extension

| ads\_error  Advantage PHP Extension |  |  |  |  |

Returns the last Advantage error code.

Syntax

string ads\_error( [int connection\_id] )

Parameters

| connection\_id (I) | Optional ID of a connection to the Advantage Database Server. |

Remarks

ads\_error returns an error code if an error occurred or an empty string if no error occurred in last Advantage API that was performed. If a connection ID is not specified, the last error of any connection is returned.

Example

<?

echo "Connecting to a Server that does not exist.<br>\n";

echo "This connect should FAIL!<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\NOServer\\NonExistantShare\\;ServerTypes=2", "", "" );

 

if ( $rConn == False )

{

$strErrCode = ads\_error( );

$strErrString = ads\_errormsg( );

echo "Connection failed: " . $strErrCode . " " . $strErrString . "<br>\n";

}

else

{

echo "Connection successful!<br>\n";

ads\_close( $rConn );

echo "Connection closed<br>\n";

}

?>

See Also

[ads\_connect](php_ads_connect.md)

[ads\_errormsg](php_ads_errormsg.md)
