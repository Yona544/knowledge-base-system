Accessing Data Using the Advantage DBI Driver (for Perl)




Advantage Database Server 12  

     Accessing Data Using the Advantage DBI Driver (for Perl)

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Accessing Data Using the Advantage DBI Driver (for Perl)  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Accessing Data Using the Advantage DBI Driver (for Perl) Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Accessing\_Data\_Using\_the\_Advantage\_DBI\_Driver\_for\_Perl\_ Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 19 - ODBC, PHP, DBI/Perl > Accessing Data Using the Advantage DBI Driver (for Perl) / Dear Support Staff, |  |
| Accessing Data Using the Advantage DBI Driver (for Perl)  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Accessing data using the Advantage DBI Driver (for Perl) is very similar to that for PHP, since both drivers rely on the Advantage ODBC Driver, but there are important differences. Besides the language difference, there are four primary differences between the Advantage PHP Extension and the Advantage DBI Driver.

The first is associated with the connection string that the DBI driver will send to the ODBC API. This connection string always begins with the dbi:Advantage: string. Everything that follows this string is identical to the parameters listed in Table 19-1 that you use for both the Advantage ODBC Driver and the Advantage PHP Extension.

The following is an example of a connection string that makes a connection similar to that shown in the PHP examples:

use DBI;  
$dbh = DBI->connect( 'dbi:Advantage:DataDirectory=\\server\share' .  
  '\adsbook\DemoDictionary.add;ServerTypes=2;',   
  'adsuser', 'password' );

The second difference, which you may have already noticed if you examined the preceding example, is that the extended functions for the DBI are similar in name (but not identical) to those used by the PHP Extension. Specifically, while the number and type of parameters are the same, the functions do not use the "ads\_" prefix. For example, in PHP you connect to Advantage by calling the ads\_connect function, but in Perl you call the connect method of the DBI object.

The third difference is that data access in Perl uses a different paradigm from PHP. This approach to data access should be familiar to any seasoned Perl developer.

And, finally, the fourth difference is that the Advantage DBI Driver can only produce a forward-scrolling cursor. In most Web applications, this is inconsequential since most CGI applications don't need to perform any navigation other than forward navigation.

For more information about the Advantage DBI Driver, see the Advantage help.