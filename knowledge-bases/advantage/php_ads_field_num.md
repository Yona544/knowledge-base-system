ads\_field\_num




Advantage Database Server 12  

ads\_field\_num

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_field\_num  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - ads\_field\_num Advantage PHP Extension php\_Ads\_field\_num Advantage PHP Extension > Extension Functions > ads\_field\_num / Dear Support Staff, |  |
| ads\_field\_num  Advantage PHP Extension |  |  |  |  |

Retrieves the position of a field in a result set given a field name.

Syntax

int ads\_field\_num( resource result\_id,

string field\_name )

Parameters

|  |  |
| --- | --- |
| result\_id (I) | ID of a result set. |
| field\_name (I) | Name of a field in a result set. |

Remarks

ads\_field\_num returns the position of a field in a result set given a field name or returns False in the event of an error. The index of the first field of a result set is 1.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Retrieve the customers.<br>\n";

$rResult = ads\_do( $rConn, "SELECT \* FROM customers" );

 

echo "Retrieve the field number of the CREDIT\_LIMIT field.<br>\n";

$iField = ads\_field\_num( $rResult, "CREDIT\_LIMIT" );

 

echo "CREDIT\_LIMIT is field number: " . $iField . "<br>\n";

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

See Also

[ads\_execute](php_ads_execute.htm)

[ads\_exec](php_ads_exec.htm)

[ads\_do](php_ads_do.htm)