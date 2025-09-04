---
title: Php Ads Field Len
slug: php_ads_field_len
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_field_len.htm
source: Advantage CHM
tags:
  - php
checksum: bd0ec5637a9df2f272fb86266c3bfba98eca5d4b
---

# Php Ads Field Len

ads\_field\_len

ads\_field\_len

Advantage PHP Extension

| ads\_field\_len  Advantage PHP Extension |  |  |  |  |

Retrieves the length of a field in a result set.

Syntax

int ads\_field\_len( resource result\_id,

int field\_number )

Parameters

| result\_id (I) | ID of a result set. |
| field\_number (I) | Number of the field in the result set. |

Remarks

ads\_field\_len returns the length of a field in a result, with the index of the first field being 1. In the event of an error, False is returned.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Selecting the customers table.<br>\n";

$rResult = ads\_do( $rConn, "SELECT \* FROM customers" );

 

echo "Describing the customers table.<br>\n";

 

$iNumFields =ads\_num\_fields( $rResult );

echo "The number of fields is: " . $iNumFields . "<br>\n";

 

for ( $iField = 1; $iField < $iNumFields; $iField++ )

{

echo "Field Number: " . $iField . "<br>\n";

 

$strField = ads\_field\_name( $rResult, $iField );

echo " Name: " . $strField . "<br>\n";

 

$strField = ads\_field\_type( $rResult, $iField );

echo " Type: " . $strField . "<br>\n";

 

$iFieldLen = ads\_field\_len( $rResult, $iField );

echo " Length: " . $iFieldLen . "<br>\n";

 

$iFieldLen = ads\_field\_precision( $rResult, $iField );

echo " Precision: " . $iFieldLen . "<br>\n";

 

$iFieldLen = ads\_field\_scale( $rResult, $iField );

echo " Scale: " . $iFieldLen. "<br>\n";

}

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

See Also

[ads\_execute](php_ads_execute.md)

[ads\_exec](php_ads_exec.md)

[ads\_do](php_ads_do.md)

[ads\_field\_scale](php_ads_field_scale.md)
