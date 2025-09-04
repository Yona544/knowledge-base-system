---
title: Master Create Trigger
slug: master_create_trigger
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_create_trigger.htm
source: Advantage CHM
tags:
  - master
checksum: 8a475cdcfcebce13683417e3235a8078e3863d6e
---

# Master Create Trigger

CREATE TRIGGER

[ALTER | CREATE] TRIGGER

Advantage SQL Engine

| [ALTER | CREATE] TRIGGER  Advantage SQL Engine |  |  |  |  |

Adds or modifies a trigger definition in the [Advantage Data Dictionary](master_advantage_data_dictionary.md)

Syntax

[ALTER | CREATE] TRIGGER <trigger-name>

 ON [<table-name> | DATABASE] <trigger-type> [<trigger-event> | <database-event>]

 <trigger-container>

 [trigger-options]

 

| trigger-type ::= | BEFORE | INSTEAD OF | AFTER | CONFLICT [ON] |
| trigger-event ::= | INSERT | UPDATE | DELETE |
| database-event ::= | OPEN\_TABLE | CLOSE\_TABLE | CONNECT | DISCONNECT |
| trigger-container ::= | <library-container> | <script-container> |
| library-container ::= | FUNCTION <function-name> IN <library-type> <library-name> |
| function-name ::= | A user-defined function name. Name of the function in the library that holds the trigger code. |
| library-type ::= | LIBRARY | ASSEMBLY |
| library-name ::= | A user-defined library name. If library-type is LIBRARY, this is the name of the Windows DLL or Linux shared object that contains the trigger function. If library-type is ASSEMBLY, this is the name of the COM ProgID or the .NET assembly that contains the trigger function. If the file name has any special characters, the name should be enclosed in double quotes or square brackets. |
| script-container ::= | BEGIN <statement> ; [, <statement> ; ] END |
| statement ::= | any valid SQL statement |
| trigger-options ::= | NO VALUES | NO MEMOS | NO TRANSACTION | PRIORITY <trigger-priority> |
| trigger-priority ::= | A user-defined integer values, specifying the triggers firing priority. |

Remarks

For table triggers, CREATE TRIGGER and ALTER TRIGGER can only be called by a user with ALTER permissions on the associated table. The CREATE TRIGGER statement creates a new trigger for the table. The ALTER TRIGGER statement modifies the definition of an existing trigger. For database triggers, ALTER permissions on the database are required.

Trigger creation or modification does not verify library or .NET assembly existence. If a trigger is defined on a library or assembly that does not exist, a run-time error will occur when the trigger is executed.

Statements inside script triggers are validated for syntactical correctness only. If any semantic errors exist, a run-time error will occur when the trigger is executed. For SQL script based trigger, the \_\_new and \_\_old tables are automatically opened as cursors when executing the trigger script. The values in the cursors may be references as \_\_new.col1, \_\_old.col1, etc. Note that the \_\_new and \_\_old cursor are automatically opened and positioned on the valid row so there is no need to FETCH from the cursor. Attempts to OPEN, FETCH or CLOSE the \_\_new or \_\_old cursor will result in exception being raised.

If a trigger container is in use, and modifications are made to a trigger definition (including trigger addition or deletion), the changes will not take effect until all users who have used a trigger in that container disconnect from the database.

Currently trigger creation and deletion will not affect tables already opened by the server. For example, if table1 is opened by active clients, and the administrator adds a new trigger to table1, the trigger will not activate until all active users have closed table1 and it has been re-opened.

See [What is a Trigger?](master_what_is_a_trigger_.md) for detailed information.

Examples

CREATE TRIGGER mytrigger ON orders AFTER DELETE

BEGIN

INSERT INTO backup\_orders SELECT \* FROM \_\_old;

END

 

-- Trigger using the \_\_old and \_\_new cursor

CREATE TRIGGER mytrigger ON orders AFTER UPDATE

BEGIN

  If \_\_old.quantity <> \_\_new.quantity Then

     INSERT INTO ChangeLog ( ChangeDate, ColumnName ) VALUES ( now(), 'Quantity' );

  End;

END

 

 

-- This is similar to the previous example but gives a slightly more

-- extensive example of how one might log changes for auditing purposes.

CREATE TRIGGER ProductsUpdateAudit

  ON products

  AFTER

  UPDATE

BEGIN

 DECLARE @auditID string;

 DECLARE @changeDate timestamp;

 

 // Use a single guid to track the fields modified in this one update

 @auditID = newidstring(d);

 @changeDate = now();

 

 // Log changes to the desired fields

 If \_\_old.Name <> \_\_new.Name Then

   INSERT INTO AuditLog( AuditID, ChangeDate, UserName, TableName, ColumnName, OldValue, NewValue )

          VALUES( @auditID, @changeDate, user(), 'Products', 'Name', \_\_old.Name, \_\_new.Name );

 End;

 

 If \_\_old.Price <> \_\_new.Price Then

   INSERT INTO AuditLog( AuditID, ChangeDate, UserName, TableName, ColumnName, OldValue, NewValue )

          VALUES( @auditID, @changeDate, user(), 'Products', 'Price',

                  CAST( \_\_old.Price AS SQL\_CHAR ), CAST( \_\_new.Price AS SQL\_CHAR ));

 End;

 

 If \_\_old.Description <> \_\_new.Description Then

   INSERT INTO AuditLog( AuditID, ChangeDate, UserName, TableName, ColumnName, OldValue, NewValue )

          VALUES( @auditID, @changeDate, user(), 'Products', 'Description',

                  // This shows how you might limit the size of the data if logging memo data.

                  // Alternatively, you could include a memo field in the audit table.

                  CAST( \_\_old.Description AS SQL\_CHAR(100)), CAST( \_\_new.Description AS SQL\_CHAR(100)));

 End;

END

 

 

 

-- Example of a trigger contained in an assembly

CREATE TRIGGER mytrigger ON orders INSTEAD OF UPDATE

FUNCTION MyFunction IN ASSEMBLY [MyAssembly.MyClass] PRIORITY 68

 

 

-- Example of a trigger contained in a DLL

CREATE TRIGGER mytrigger ON orders AFTER INSERT

FUNCTION MyFunction IN LIBRARY [mytriggers.dll]

 

 

CREATE TRIGGER mytrigger ON orders BEFORE INSERT

FUNCTION MyFunction IN ASSEMBLY [MyAssembly.MyClass]

NO VALUES PRIORITY 23

 

 

-- Simple trigger that adds all fields except memos

-- to a backup table when a record is deleted.

CREATE TRIGGER mytrigger ON orders AFTER DELETE

BEGIN

INSERT INTO backup\_orders SELECT \* FROM \_\_old;

END

NO MEMOS PRIORITY 1

-- Example trigger that logs a deleted record with memo data

-- to a table for auditing purposes.

ALTER TRIGGER mytrigger ON orders AFTER DELETE

BEGIN

INSERT INTO log\_orders\_delete SELECT \* FROM \_\_old;

END

PRIORITY 2

 

-- The following example creates a database trigger that fires after opening

-- a table.  It inserts the contents of the \_\_info table into a logging table.

CREATE TRIGGER LogOpenTable ON DATABASE AFTER OPEN\_TABLE

BEGIN

  if \_\_info.tablename <> 'LogTable' then

     insert into LogTable select now(), i.\* from \_\_info i;

  end if;

END;

 

-- The following example creates a database trigger that fires prior to opening

-- a table and selectively produces an exception that will prevent the table from

-- being opened.

CREATE TRIGGER PreventOpenTable ON DATABASE BEFORE OPEN\_TABLE

BEGINa

  if \_\_info.tablename = 'SomeTable' and \_\_info.username = 'SomeUser' then

     insert into \_\_error values (1234, 'This table cannot be opened.');

  end if;

END;

 

-- The following example creates a database trigger that fires after a successful

-- connection and logs the connection information.

CREATE TRIGGER LogConnection ON DATABASE AFTER CONNECT

BEGIN

  insert into ConnLog select now(), i.\* from \_\_info i;

END;
