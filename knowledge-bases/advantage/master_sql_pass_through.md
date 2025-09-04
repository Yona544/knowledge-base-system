SQL Pass Through




Advantage Database Server 12  

SQL Pass Through

Advantage and Visual FoxPro

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SQL Pass Through  Advantage and Visual FoxPro |  |  | Feedback on: Advantage Database Server 12 - SQL Pass Through Advantage and Visual FoxPro master\_Sql\_pass\_through Visual FoxPro > SQL Pass Through / Dear Support Staff, |  |
| SQL Pass Through  Advantage and Visual FoxPro |  |  |  |  |

Like [remote views](master_remote_views.htm), SQL Pass Through utilizes ODBC to perform data access in Visual FoxPro. It provides a more direct access to the ODBC interface. It gives excellent low level control with the ability to specify transactions, execute stored procedures, run specific updates, etc. However, it can involve writing more code especially if you want updates to be sent to Advantage automatically.

The following example code runs a simple SELECT statement to retrieve the contents of a table named test. It stores the results in a Visual FoxPro cursor named MyResult. It assumes that an ODBC data source named "ads" exists.

hConn = SQLCONNECT( "ads" )

IF hConn > 0

SQLEXEC( hConn, "select \* from test", "MyResult" )

BROWSE

USE

SQLDISCONNECT( hConn )

ELSE

? "Failed to connect to the data source"

ENDIF

In the above example, if you wanted to perform updates to the data, one possibility would be to execute SQL statements to do the updates. For example, SQLEXEC( hConn, "insert into test (empid) values (111);" ).

If you want updates to be automatically sent to Advantage, however, some additional code must be written. In particular, several cursor properties must be set in order for the update statements to be automatically generated. The following code is a short example that makes some of the fields in the view editable.

#include "foxpro.h"

hConn = SQLCONNECT( "ads" )

IF hConn > 0

\*\* retrieve the cursor

SQLEXEC( hConn, "select \* from test", "MyResult" )

 

\*\* Set the properties necessary for automatic updates

 

\*\* specify the table name

CURSORSETPROP("Tables", "test", "MyResult" )

\*\* indicate which field is the primary key

CURSORSETPROP("KeyFieldList", "empid", "MyResult" )

\*\* specify which fields can be updated

CURSORSETPROP("UpdatableFieldList", "deptnum, lastname", "MyResult" )

\*\* provide a mapping of view names to table names for the update

CURSORSETPROP("UpdateNameList", ;

 "deptnum  test.deptnum, ;

 empid  test.empid, ;

 lastname  test.lastname", "MyResult" )

\*\* indicate that the WHERE clause will use only the primary key

CURSORSETPROP("WhereType", DB\_KEY, "MyResult" )

\*\* Specify that updates should be sent to the backend

CURSORSETPROP("SendUpdates", .t., "MyResult")

 

BROWSE

USE

SQLDISCONNECT( hConn )

ELSE

? "Failed to connect to the data source"

ENDIF

See Also

[Getting Started with Visual FoxPro](master_getting_started_with_visual_foxpro.htm)

[Remote Views](master_remote_views.htm)

[Cursor Adapters](master_cursor_adapters.htm)