Advantages of Constraints




Advantage Database Server 12  

     Advantages of Constraints

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantages of Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Advantages of Constraints Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Advantages\_of\_Constraints Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 5 - Constraints and RI > Advantages of Constraints / Dear Support Staff, |  |
| Advantages of Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Constraints have two primary advantages. First, they are declarative in nature. With the exception of the Boolean expressions that you use to specify record-level constraints, they require no programming. Compared to client-side validation and triggers, constraints are simple to create and document.

The second major advantage of constraints is that they reside in the data dictionary. As a result, Advantage enforces the constraints regardless of how the data is accessed. No matter how many client applications you have that use the database, the constraints within the data dictionary are enforced. (Here again we are talking about ADT tables. Constraints on DBF tables are not enforced if those tables are accessed without the data dictionary.)

That constraints reside in the data dictionary has another benefit. Specifically, if you need to change one or more constraints after deployment, you only need to update the data dictionary. No changes to client applications are necessary.