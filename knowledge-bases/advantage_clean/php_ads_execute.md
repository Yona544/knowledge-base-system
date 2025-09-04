---
title: Php Ads Execute
slug: php_ads_execute
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_execute.htm
source: Advantage CHM
tags:
  - php
checksum: 14238023c8679177779dd1d996c6538fde1321d2
---

# Php Ads Execute

ads\_execute

ads\_execute

Advantage PHP Extension

| ads\_execute  Advantage PHP Extension |  |  |  |  |

Executes a prepared SQL statement.

Syntax

resource ads\_execute( resource result\_id

[, array parameters\_array]

[,array parameter\_types\_array] )

Parameters

| result\_id (I) | ID of a result set. |
| parameters\_array (I) | Optional array of values to be bound to the parameters of an SQL statement. |
| parameters\_type\_array (I) | Optional array of types associated with the values to be bound to the parameters. Available options are: SQL\_BINARY, SQL\_CHAR, and SQL\_WCHAR. |

Remarks

ads\_execute executes a statement that has been prepared by a previous call to ads\_prepare. Use of this function is required when executing an SQL statement that contains parameters. Parameters in the parameters\_array are substituted for placeholders in the order they appear in the SQL statement.

The values in the parameter\_types\_array are used to correctly pass the parameter data to the Advantage Database Server when working with binary or Unicode data. Set the type to SQL\_BINARY for data that is binary, SQL\_WCHAR for Unicode fields, and all other fields should use SQL\_CHAR.

When executing a successful SELECT statement or EXECUTE statement with a result set, a result set identifier will be returned. This result set identifier can be used to retrieve values from the result set.

Examples

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Preparing a statement with a parameter<br>\n";

$rStmt = ads\_prepare( $rConn, "SELECT \* FROM customers WHERE company LIKE ?" );

echo "Statement prepared<br>\n";

 

echo "Executing the statement. Notice the array of parameters<br>\n";

$aParams = array( 1 => 'A%' );

$rResult = ads\_execute( $rStmt, $aParams );

echo "Execution was successful<br>\n";

 

echo "Retrieve the Company Name and Credit Limit<br>\n";

while ( ads\_fetch\_row( $rStmt ) )

{

$strCompanyName = ads\_result( $rStmt, "COMPANY" );

$strCreditLimit = ads\_result( $rStmt, "CREDIT\_LIMIT" );

echo $strCompanyName . " can spend up to $" . $strCreditLimit . "<br>\n";

}

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

An example of inserting binary data using parameters:

 

<?php

 

$rConn = ads\_connect("DataDirectory=//server1/share1/data/;ServerTypes=2","", "");

echo "Connected<br>\n";

 

echo "Reading file into buffer<br>\n";

$infile = fopen ( "c:\data\picture.bmp", "rb");

if ($infile) //does the comp file exist?

{

$buf = "";

while (!feof($infile))

$buf .= fread ($infile, 1024);

$doc\_data = $buf;

fclose ($infile);

}

 

 

echo "Performing the insert<br>\n";

echo "Preparing an insert statement with a blob and binary parameter<br>\n";

$rStmt = ads\_prepare( $rConn, "INSERT INTO Employee ( EmpID, MugShot ) VALUES ( ?, ? )" );

echo "Statement prepared<br>\n";

 

$insertarray = array(1 => $doc\_data);

 

$insertarray = array(1 => 69,

2 => $doc\_data);

 

$typesarray = array( 1 => SQL\_CHAR,

2 => SQL\_BINARY );

 

echo "Executing the statement<br>\n";

$insertresult = ads\_execute( $rStmt, $insertarray, $typesarray );

echo "The statement has been executed. <br>\n";

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

 

 

?>

 

See Also

[ads\_connect](php_ads_connect.md)

[ads\_prepare](php_ads_prepare.md)

[ads\_do](php_ads_do.md)

[ads\_exec](php_ads_exec.md)
