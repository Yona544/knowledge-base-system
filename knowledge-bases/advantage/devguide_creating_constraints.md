Creating Constraints




Advantage Database Server 12  

 

     Creating Constraints

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Creating Constraints Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_Constraints Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 5 - Constraints and RI > Creating Constraints / Dear Support Staff, |  |
| Creating Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Data dictionaries support three types of constraint definitions: field-level, record-level, and referential integrity. While there are some similarities between these various types of constraints, the steps you take to implement them are quite different. As a result, the creation of each constraint type is described in its own section.

Both field-level and record-level constraints are actually properties of dictionary-bound tables. There are other field and table-related properties as well. The need to discuss constraints provides us with a fine opportunity to consider these properties in general.