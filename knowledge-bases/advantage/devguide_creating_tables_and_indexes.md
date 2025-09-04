Creating Tables and Indexes




Advantage Database Server 12  

     Creating Tables and Indexes

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating Tables and Indexes  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating Tables and Indexes Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_Tables\_and\_Indexes Advantage Developer's Guide > Part II - Advantage SQL > Chapter 12 - SQL to Perform Common Tasks > Creating Tables and Indexes / Dear Support Staff, |  |
| Creating Tables and Indexes  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You use the CREATE statement to create data dictionaries, tables, indexes, views, stored procedures, triggers, and user defined functions. Creating tables and indexes is covered in the following sections.

Creating Tables

You create a table using the CREATE TABLE SQL statement. If you want to create a data dictionarybound table on a data dictionary connection, you must be connected using the data dictionary administrator's user name (ADSSYS) and password, or through a user name with create table permission (users without create table privileges on a data dictionary can still create a free table). If you are not connected to a data dictionary, CREATE TABLE always creates a free table.

When calling CREATE TABLE, you must supply a name for the table as well as the name and type of each field in the table, at a minimum. For example, the following statement creates a table named DEMO1 with four fields:

CREATE TABLE DEMO1 (  
  "Full Name" CHAR(30),  
  "Date of Birth" DATE,  
  "Credit Limit" MONEY,  
  Active LOGICAL)

The names that you use in SQL for the valid field types for ADT tables are shown in Table 12-1. For the valid field types for DBF tables, refer to the Advantage help.

 

|  |  |  |
| --- | --- | --- |
| AUTOINC | BINARY | CHAR |
| CICHAR | CURDOUBLE | DATE |
| DOUBLE | IMAGE | INTEGER |
| LOGICAL | MEMO | MODTIME |
| MONEY | NUMBER | NUMERIC |
| RAW | ROWVERSION | SHORT |
| TIME | TIMESTAMP |  |

Table 12-1: Valid Field Types for ADT Tables

Almost all tables will have at least one index, which is typically a unique primary index. There are two ways to define a primary index. If the index is based on a single field, you can include the keywords PRIMARY KEY following the field type.

Alternatively, you can follow the field list with the keywords PRIMARY KEY followed by a list of one or more fields that will constitute the index key expression. If you want the index to sort in descending order, include the DESC keyword after each descending field.

The following CREATE TABLE statement creates a table named DEMO2 that includes a primary index named PrimeIdx:

CREATE TABLE DEMO2 (  
  CustID INTEGER CONSTRAINT PrimeIdx PRIMARY KEY,  
  [Full Name] CICHAR(25),  
  Date DATE)

The following statement performs the exact same task:

CREATE TABLE DEMO2 (  
  CustID INTEGER,  
  [Full Name] CICHAR(25),  
  Date DATE,  
  CONSTRAINT PrimeIdx PRIMARY KEY (CustID))

In both of these statements, the CONSTRAINT PrimeIdx can be omitted, in which case ADS will assign the name PK\_INDEX to the primary key index.

   
NOTE: You cannot define a primary key index for DBF tables.  
 

You can also define field-level constraints when creating a table. This is demonstrated in the following CREATE TABLE statement:

CREATE TABLE DEMO3 (  
  "Customer ID" INTEGER PRIMARY KEY,  
  "Credit Limit" MONEY  
    DEFAULT '0'  
      CONSTRAINT MINIMUM '0'  
      CONSTRAINT MAXIMUM '100000'  
      CONSTRAINT NOT NULL  
      CONSTRAINT ERROR MESSAGE 'Invalid credit limit',  
  "Date Last Accessed" DATE)

   
NOTE: If you create a new table through the data dictionary administrator's account (or user account with create table privileges), and you have rights checking enabled for the data dictionary, you must specifically grant table access rights to the users and groups who need to work with it. Granting rights using SQL is discussed in Chapter 14.  
 

 

   
TIP: Rather than writing a CREATE TABLE statement, you can use the Advantage Data Architect to create a table, after which you can right-click the table's name in the TABLES node and select Generate SQL from the displayed context menu.  
 

Using the SELECT statement, you can both create a table and populate it with data from an existing table. To do this, follow the SELECT list with the name of the table into which you want to place the selected records. For example, the following statement will create a new table based on the EMPLOYEE table. The resulting table has two fields, First Name and Last Name. This statement creates a free table and its files are written to the same path as the data dictionary in which the EMPLOYEE table is bound:

SELECT "First Name", "Last Name" INTO DEMO4 FROM EMPLOYEE

While a table created using this syntax on a data dictionary connection is created in the same directory as the data dictionary, the table is created as a free table. If you want to make this table part of the data dictionary, follow this call with a call to the sp\_AddTableToDatabase system stored procedure.

Creating Indexes

You create an index for a table using the CREATE INDEX SQL statement. If you are creating an index for a table in a data dictionary, you must be connected to the data dictionary using the administrative account or a user account with the alter table permission on the table (otherwise, the index will be temporary).

The following SQL script creates a new table, and then uses two CREATE INDEX statements to create indexes for it:

CREATE TABLE DEMO5 (  
  CustID INTEGER,  
  "Full Name" CICHAR(30),  
  Address CICHAR(100),  
  City CICHAR(25),  
  Phone CHAR(14),  
  Notes MEMO);  
CREATE UNIQUE INDEX UniqueIdx ON DEMO5 (CustID);  
CREATE INDEX AddrIdx ON DEMO5 (Address, City);

Neither of these CREATE INDEX statements specifies an index file name. As a result, these index orders are created in the structural index file. If you want, you can create a new index file, in which case you can specify the filename and page size. This is shown in the following example:

CREATE INDEX NewIdx ON DEMO5 ("Full Name")  
  IN FILE "newfile" PAGESIZE 1024

   
NOTE: Page size can only be defined when creating the first index order in a given index file, and only applies to an ADI index file.  
 

You can also create FTS (full text search) indexes with CREATE INDEX. When creating an FTS index, you use the CONTENT keyword followed by one or more of the following keywords to define how the index is created and maintained: CASESENSITIVE, CONDITIONALS, DELIMITERS, DROPCHARS, KEEPSCORE, MAX WORD, MIN WORD, NOISE, NOTMAINTAINED, and PROTECTNUMBERS. The CONDITIONALS, DELIMITERS, DROPCHARS, and NOISE keywords can be preceded by the keyword NEW to define new values. When you omit the word NEW, the values are added to the default values for those parameters. (See Chapter 3 for a complete discussion of FTS indexes and their parameters.)

The following is an example of an FTS index on the Notes field of the DEMO5 table:

CREATE INDEX NotesIdx ON DEMO5 (Notes)  
  CONTENT  
  MIN WORD 3  
  MAX WORD 15  
  DELIMITERS ';:'  
  KEEPSCORE  
  CASESENSITIVE

   
NOTE: If you need to create an index with a complex index expression, you can use the sp\_CreateIndex system stored procedure.  
 

Altering Tables

You use the ALTER TABLE statement to change an existing table's definition. It permits you to add and remove fields from the table's structure, add or remove a primary index, and change field names and data types, as well as add, change, or drop field-level constraints.

If your table is bound to a data dictionary, you can only alter a table if you are connected using the data dictionary administrator's user name or through a user who specifically has alter privileges for that table. In any case, you must also be able to obtain an exclusive lock on the table in order to alter it. The following is an example of an ALTER TABLE statement:

ALTER TABLE DEMO5   
  ADD COLUMN State CICHAR(40)  
  ADD COLUMN Country CICHAR(35)  
  ALTER COLUMN Address Address CICHAR(80)  
  DROP COLUMN Phone  
  ALTER COLUMN "Full Name" "Full Name" CICHAR(30)  
    CONSTRAINT NOT NULL

Advantage SQL does not support ALTER statements for databases, indexes, views, stored procedures, or triggers. If you want to change one of these objects, you can either use DROP to delete the object and then call CREATE to create a new version or you can use one of the available modify system stored procedures to perform the change (such as sp\_ModifyIndexProperty). (If you DROP and CREATE, you may also have to specifically grant privileges over again. If you use a modify system stored procedures, existing privileges remain intact.) The modify system stored procedures are discussed in Chapter 14.

Dropping Objects

You use SQL DROP statements to destroy tables and objects within your data dictionary. DROP can be used with the following keywords: FUNCTION, PACKAGE, INDEX, PROCEDURE, TABLE, TRIGGER, and VIEW. For user defined functions, stored procedures, triggers, and views, as well as tables and index orders associated with a data dictionary, you must execute DROP using the data dictionary administrative connection or from a user connection for which drop privileges have specifically been granted for that particular object. To drop an index or a trigger, the user must have ALTER permission to the table object that owns the index or trigger.

To drop an index order or a trigger, use dot notation to specify the table name. For example, the following statement deletes the index named AddrIdx from the DEMO5 table:

DROP INDEX DEMO5.AddrIdx

The following example demonstrates how to delete the DEMO5 table:

DROP TABLE DEMO5

DROP TABLE removes the specified table from the data dictionary (if it was bound to one) and deletes the files associated with the table. Dropping user defined functions, packages, stored procedures, triggers, and views uses the same syntax as dropping a table. Simply provide the name of the object that you are dropping.