Navigational Actions with ADS and Java




Advantage Database Server 12  

     Navigational Actions with ADS and Java

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Navigational Actions with ADS and Java  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Navigational Actions with ADS and Java Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Navigational\_Actions\_with\_ADS\_and\_Java Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 16 - Advantage and Java > Navigational Actions with ADS and Java / Dear Support Staff, |  |
| Navigational Actions with ADS and Java  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Unlike Delphi and ADO-based Advantage applications, which support a wide range of navigational operations, JDBC supports only simple navigation. Specifically, the ResultSet class permits you to navigate forward through the records of the result set, and if the cursor is bidirectional, you can move forward and backward using methods with names such as first, next, last, and previous. The use of simple forward navigation is demonstrated in the following section.

   
NOTE: Some classes in Borland's DataExpress in JBuilder support additional navigational capabilities, such as filtering. These classes are not, however, native to JDBC.