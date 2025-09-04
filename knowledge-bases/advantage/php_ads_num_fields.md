ads\_num\_fields




Advantage Database Server 12  

ads\_num\_fields

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_num\_fields  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - ads\_num\_fields Advantage PHP Extension php\_Ads\_num\_fields Advantage PHP Extension > Extension Functions > ads\_num\_fields / Dear Support Staff, |  |
| ads\_num\_fields  Advantage PHP Extension |  |  |  |  |

Returns the number of fields in a result set.

Syntax

int ads\_num\_fields( resource result\_id )

Parameters

|  |  |
| --- | --- |
| result\_id (I) | ID of a result set. |

Remarks

Returns the number of fields in a result set or returns 1 in the event of an error.

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