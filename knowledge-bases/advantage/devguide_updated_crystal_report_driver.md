Updated Crystal Report Driver




Advantage Database Server 12  

     Updated Crystal Report Driver

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Updated Crystal Report Driver  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Updated Crystal Report Driver Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Updated\_Crystal\_Report\_Driver Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > Updated Crystal Report Driver / Dear Support Staff, |  |
| Updated Crystal Report Driver  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage 8's Crystal Report driver can now accept a handle to the client application's connection, permitting it to use the client's connection to the server. Previously, the Crystal Report driver established its own connection to the server, incurring the overhead of connecting and disconnecting. The enhancement not only improves performance, but also permits you to generate reports based on temporary tables available on the client connection.