ads\_result\_all




Advantage Database Server 12  

ads\_result\_all

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_result\_all  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - ads\_result\_all Advantage PHP Extension php\_Ads\_result\_all Advantage PHP Extension > Extension Functions > ads\_result\_all / Dear Support Staff, |  |
| ads\_result\_all  Advantage PHP Extension |  |  |  |  |

Prints the entire result set as an HTML table.

Syntax

int ads\_result\_all( resource result\_id

[, string format] )

Parameters

|  |  |
| --- | --- |
| result\_id (I) | ID of a result set. |
| format (I) | Optional parameter used for table formatting. |

Remarks

ads\_result\_all returns the number of rows in the result set or returns False in the event of an error. The result is printed in HTML table format. Additional formatting information can be provided via the optional format parameter.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Retrieving the list of customers<br>\n";

$rResult = ads\_do( $rConn, "SELECT \* FROM customers" );

 

echo "Creating HTML table of results<br>\n";

$iCount = ads\_result\_all( $rResult );

echo $iCount . " records printed to the table.<br>\n";

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

See Also

[ads\_execute](php_ads_execute.htm)

[ads\_exec](php_ads_exec.htm)

[ads\_do](php_ads_do.htm)

[ads\_field\_len](php_ads_field_len.htm)