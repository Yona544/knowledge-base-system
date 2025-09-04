Row Level Trigger Support




Advantage Database Server 12  

Row Level Trigger Support

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Row Level Trigger Support  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Row Level Trigger Support Advantage Concepts master\_Row\_level\_trigger\_support Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Row Level Trigger Support  Advantage Concepts |  |  |  |  |

Advantage supports row-level triggers. Row-level triggers are fired once for each row that an update operation affects. For example, if a table contains multiple records with the deptnum field equal to 5, and the following SQL statement is executed:

DELETE FROM mytable WHERE deptnum = 5

a trigger will fire once for each row that is affected by the DELETE operation (each row in which deptnum is equal to 5).