ads\_fetch\_into




Advantage Database Server 12  

ads\_fetch\_into

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_fetch\_into  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - ads\_fetch\_into Advantage PHP Extension php\_Ads\_fetch\_into Advantage PHP Extension > Extension Functions > ads\_fetch\_into / Dear Support Staff, |  |
| ads\_fetch\_into  Advantage PHP Extension |  |  |  |  |

Fetches a single row of a result set into an array.

Syntax

resource ads\_fetch\_into( resource result\_id

[, int row\_number],

array result\_array )

Parameters

|  |  |
| --- | --- |
| result\_id (I) | ID of a result set. |
| row\_number (I) | Optional row number of the result set to fetch. |
| result\_array (I/O) | Reference to the array in which to fetch values. |

Remarks

ads\_fetch\_into returns the number of fields in the result or returns False in the event of an error. Data from binary fields is not read into the array; instead the field is left empty. The maximum amount of data read from memo fields is controlled by the length value specified in a call to [ads\_longreadlen](php_ads_longreadlen.htm).

If the optional row number is not specified, the next row in the result set will be returned. To read the values from a result set again, call ads\_fetch\_into with a value of 1. This moves the current position to the top of the result set. Subsequent calls to ads\_fetch\_into without a row\_number will fetch the next row in the result set.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Retrieve the customers.<br>\n";

$rResult = ads\_do( $rConn, "SELECT \* FROM customers" );

 

echo "Retrieve the sixth row into the array.<br>\n";

ads\_fetch\_into( $rResult, $aArray );

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

See Also

[ads\_execute](php_ads_execute.htm)

[ads\_exec](php_ads_exec.htm)

[ads\_do](php_ads_do.htm)

[ads\_fetch\_row](php_ads_fetch_row.htm)

[ads\_fetch\_array](php_ads_fetch_array.htm)

[ads\_longreadlen](php_ads_longreadlen.htm)