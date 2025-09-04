Connecting to Advantage Using PHP




Advantage Database Server 12  

     Connecting to Advantage Using PHP

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Connecting to Advantage Using PHP  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Connecting to Advantage Using PHP Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Connecting\_to\_Advantage\_Using\_PHP Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 19 - ODBC, PHP, DBI/Perl > Connecting to Advantage Using PHP / Dear Support Staff, |  |
| Connecting to Advantage Using PHP  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You connect to Advantage from PHP by calling the function ads\_connect. This function takes either three or four arguments and returns a connection resource. The first argument is an ODBC connection string. The PHP driver connects through the ODBC API by invoking SQLDriverConnect, to which it passes this connection string. See Table 19-1 for the required and valid connection string parameters.

The second and third parameters are the user name and password to use for the connection, and the optional fourth parameter is used to define what type of cursor you want returned. The valid values for this fourth parameter are:

•        0 (SQL\_CURSOR\_FORWARD\_ONLY)

|  |  |
| --- | --- |
| • | 1 (SQL\_CURSOR\_DYNAMIC) |

|  |  |
| --- | --- |
| • | 2 (SQL\_CURSOR\_KEYSET\_DRIVEN) |

If you omit this parameter, a live (dynamic) cursor is returned.

The following is an example of a call to ads\_connect:

$rConn = ads\_connect("DataDirectory=\\\\server\\share\\".  
  "adsbook\\DemoDictionary.add;ServerTypes=2;",   
  "adsuser", "password");

The connection string in this command attempts to connect to the DemoDictionary data dictionary located on a share named share on a server named server. In addition, this connection string specifies that it wants to connect to ADS (the license for ALS does not permit you to connect to ALS from a Web server). As is the case with ODBC connections, all parameters not included in the connection string will be expanded using the default parameter values.

Once you are through with the connection, you must close it. You do this by invoking ads\_close, passing the connection resource obtained from the call to ads\_connect. The following is a simple example of this function call:

ads\_close( $rConn );