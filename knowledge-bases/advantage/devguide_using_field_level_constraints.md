Using Field-Level Constraints




Advantage Database Server 12  

     Using Field-Level Constraints

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Field-Level Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Using Field-Level Constraints Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Using\_Field\_Level\_Constraints Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 5 - Constraints and RI > Using Field-Level Constraints / Dear Support Staff, |  |
| Using Field-Level Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Field-level constraints permit you to improve the integrity of data in individual columns by defining meaningful limits to the range of values that a field can store. They are especially useful for fields designed to hold data that have a fixed range. For example, a field designed to hold the relative humidity of a meteorological measurement has a fixed range of between 0 and 100. Relative humidity cannot be lower than 0, nor can it be greater than 100 percent. Placing minimum and maximum values on a relative humidity field of 0 and 100, respectively, makes some sense.

But some domains do not have clear limits. For example, imagine that you have a date of birth (DOB) field in your employee table. Should you put a minimum date on the field? Probably not. In this case, the use of a minimum value on a date of birth field doesn't help your data much. On the one hand, if you set the minimum value on a date of birth field to 1/1/1920, you might actually prevent an employee's valid birthday from being entered. On the other, permitting DOB values as early as 1/1/1880 does little to prevent inaccurate data.

The issue here is fixed limits versus artificial ones. Percentages, such as relative humidity, have well-defined limits. When a field represents a domain that does not have physical limits, it is probably best to avoid using minimum and maximum limits. Instead, you may want to employ client-side code to ask the user to confirm data values that lie in extreme, yet potentially valid, ranges.

You should also be careful when setting the NULL Valid field to No, meaning that null values are not allowed for a particular field. In reality, most tables have only a few fields whose values absolutely must be entered before you can accept the record. Most of these are fields that uniquely identify a record, such as the fields associated with a table's primary key.

What you want to avoid doing is setting NULL Valid to No for fields that are not actually essential. For example, you may need the invoice date in your invoice table. But if the end user does not have the order date when they are entering the record, requiring them to supply a non-null value for this field either provokes them to enter fake data or prevents them from entering the record altogether.