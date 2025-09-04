Comments About Constraints and Referential Integrity




Advantage Database Server 12  

 

     Comments About Constraints and Referential Integrity

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Comments About Constraints and Referential Integrity  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Comments About Constraints and Referential Integrity Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Comments\_About\_Constraints\_and\_Referential\_Integrity Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 5 - Constraints and RI > Comments About Constraints and Referential Integrity / Dear Support Staff, |  |
| Comments About Constraints and Referential Integrity  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As pointed out at the beginning of this chapter, there are a number of benefits to constraints and referential integrity. They are easy to configure, all client applications must abide by them, and they can improve the overall integrity of your data.

But the ease with which constraints can be added to a data dictionary can lead to their overuse. When overused, they can prevent valid data from being entered into your database. And in the case of referential integrity constraints, they can produce an unexpected increase in resource use on the server.

The following sections take a final look at each of the types of constraints provided by a data dictionary. In each case, the limits of each approach are discussed.