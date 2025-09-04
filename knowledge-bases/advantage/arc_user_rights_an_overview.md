User Rights - An Overview




Advantage Database Server 12  

User Rights - An Overview

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| User Rights - An Overview  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - User Rights - An Overview Advantage Data Architect arc\_User\_rights\_an\_overview Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| User Rights - An Overview  Advantage Data Architect |  |  |  |  |

Read Rights

The read rights apply to table or view objects. With read rights, the user can open a table or view for read purpose. The user can also issue SQL "SELECT " statements against the table or view, but the user is not allowed to issue SQL DML statements, such as "UPDATE " or "DELETE ", against the table or view. If the user has read rights but not write rights to a table or view, the user can open the table or view directly with the read-only option.

Write Rights

The write rights apply to table or view objects. With write rights, the user can modify the content of the table or view. Note that if the user has only write rights but not read rights to the table, the effects are; 1) the user can issue SQL DML statements, such as "UPDATE" or "DELETE", against the table or view but the user is not allowed to issue SQL "SELECT " statement against the table or view, and 2) the user cannot open the table or view directly because tables or views opened directly are always readable.

Execution Rights

The execution rights apply to the stored procedure objects. With execution rights, the user can execute a stored procedure. Without execution rights, the user is not allowed to execute the stored procedure.

Inherited Rights

The inherited rights can be granted to the database users only. With inherited rights, a users effective rights to a database object is the sum of all rights to the object that the user and the user groups, for which the user is a member of, have. Note that unless specifically excluded, the user has inherited rights to any database objects by default. For example, if "Group1" has read rights to "table1" and read/write rights to "table2", and "Group2" has write rights to "table1", after making "user1" a member of both "Group1" and "Group2", the effective rights of the user are read/write to both "table1" and "table2". To make "user1" have only read rights to "table1", the administrator can grant the user the read rights without the inherited rights to the table.