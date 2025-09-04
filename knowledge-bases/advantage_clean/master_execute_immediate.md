---
title: Master Execute Immediate
slug: master_execute_immediate
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_execute_immediate.htm
source: Advantage CHM
tags:
  - master
checksum: ddb7719c1a0d636cf641e0065aa0589708592e3a
---

# Master Execute Immediate

EXECUTE IMMEDIATE

EXECUTE IMMEDIATE

Advantage SQL Engine

| EXECUTE IMMEDIATE  Advantage SQL Engine |  |  |  |  |

The EXECUTE IMMEDIATE statement is used to execute a dynamically constructed SQL statement or SQL script.

Syntax

EXECUTE IMMEDIATE char\_expr;

Description

The EXECUTE IMMEDIATE statement prepares the SQL statement or SQL script in the char\_expr and executes it immediately. The prepared statement or script is freed immediately after execution. The SQL statement or script is executed within its own scope and it has no access to variables declared in the outer script. However, runtime and custom exceptions raised while executing the SQL statements contained in the char\_expr may be caught and handled by the outer script.

Example 1.

// A sample stored procedure that adds a auto increment column to a

// table if one does not exist.

// Note that the table name and the column name in the dynamically constructed

// SQL statement are not delimited so this stored procedure only works if

// the tblName and colName do not contain space or other special characters.

 

CREATE PROCEDURE AddAutoInc( tblName cichar(20), colName cichar(20))

BEGIN

 DECLARE col cursor, \_\_input cursor as select \* FROM \_\_input;

 DECLARE stmt string;

 

 OPEN \_\_input;

 FETCH \_\_input;

 // Check to see if the column already exists

 OPEN col as SELECT \* FROM system.columns WHERE parent = \_\_input.tblName AND name = \_\_input.colName;

 IF FETCH col THEN

   // already exists

 ELSE

   // column does not exists, add it

   // Construct the ALTER TABLE statement

   stmt = 'ALTER TABLE ' + \_\_input.tblName + ' ADD ' + \_\_input.colName + ' autoinc ';

   EXECUTE IMMEDIATE stmt;

 END IF;

 

 CLOSE col;

 CLOSE \_\_input;    

END;
