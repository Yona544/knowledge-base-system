Getting Tables from Result Sets Using PHP




Advantage Database Server 12  

     Getting Tables from Result Sets Using PHP

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Getting Tables from Result Sets Using PHP  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Getting Tables from Result Sets Using PHP Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Getting\_Tables\_from\_Result\_Sets\_Using\_PHP Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 19 - ODBC, PHP, DBI/Perl > Getting Tables from Result Sets Using PHP / Dear Support Staff, |  |
| Getting Tables from Result Sets Using PHP  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

After executing a query, you can easily display the entire result set by calling ads\_result\_all. This function takes the handle returned from a call to ads\_execute in its first parameter, and an optional string containing HTML table element attributes in the second, and returns a string containing a complete HTML <TABLE> definition that includes one row for each record in the result set. This function is only used when you execute a query that returns one or more records.

The use of ads\_result\_all is demonstrated in the showtables.php script. The PHP statements from this file are shown in the following listing:

<?  
$rConn = ads\_connect( "DataDirectory=\\\\server\\share\\".  
  "adsbook\\DemoDictionary.add;ServerTypes=2;",   
  "adsuser", "password" );  
$rStmt = ads\_prepare( $rConn, "SELECT Name FROM ".   
  "system.tables" );  
$rResult = ads\_execute( $rStmt );  
ads\_result\_all( $rStmt );  
ads\_close( $rConn );  
?>

When this script is rendered, it produces the Web page shown in Figure 19-5.

Figure 19-5: The Web page returned by showtables.php

As mentioned earlier, the ads\_result\_all function can accept a second, optional parameter. You use this parameter to pass a string that will be incorporated into the <TABLE> element. Normally you use this parameter to pass one or more table attributes that will be used to control the table's format and behavior, such as bgcolor, border, onclick, style, id, and width, to name a few.