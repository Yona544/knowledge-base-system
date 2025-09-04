---
title: Php Ads Field Scale
slug: php_ads_field_scale
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_field_scale.htm
source: Advantage CHM
tags:
  - php
checksum: 06578bc51f5e910ff16da114acff31c63253ea53
---

# Php Ads Field Scale

ads\_field\_scale

ads\_field\_scale

Advantage PHP Extension

| ads\_field\_scale  Advantage PHP Extension |  |  |  |  |

Retrieves the scale of a field in a result set.

Syntax

int ads\_field\_scale( resource result\_id,

int field\_number )

Parameters

| result\_id (I) | ID of a result set. |
| field\_number (I) | Number of the field in the result set. |

Remarks

ads\_field\_scale returns the number of digits of decimal precision for a field in a result set or returns False in the event of an error. For the field\_number parameter, the index of the first field of a result set is 1.

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

[ads\_field\_len](php_ads_field_len.md)
