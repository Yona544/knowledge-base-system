New Field Types




Advantage Database Server 12  

     New Field Types

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| New Field Types  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      New Field Types Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_New\_Field\_Types Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > New Field Types / Dear Support Staff, |  |
| New Field Types  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage 8.1 includes three new field types: RowVersion, ModTime, and Numeric.

When you include a RowVersion field in a table, that field can hold an unsigned 64-bit integer that is automatically assigned each time a record is inserted or changed. This is an auto-incrementing value, with the last record inserted or modified containing the highest value. RowVersion is particularly useful for detecting record changes when applying changes from a cached dataset, such as a .NET DataTable or a Delphi ClientDataSet.

ModTime is a timestamp field that is automatically assigned a value each time a record is inserted or changed. ModTime eliminates the need to write an insert and update trigger to record the time of the most recent change to a record.

Numeric fields are similar to Money fields, in that they both can hold numbers whose values remain accurate to a specified number of decimal places. This accuracy is maintained during arithmetic operations. Numeric values are not assumed to contain monetary values, whereas Money fields are.

The Numeric fields have a maximum length of 32 characters. When creating a numeric field, you need to specify both its overall length and its decimal precision. Accounting for the decimal and a sign, this allows for up to 29 characters of precision. Numeric fields were added to Advantage 8.1.