---
title: Master Open Close Fetch
slug: master_open_close_fetch
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_open_close_fetch.htm
source: Advantage CHM
tags:
  - master
checksum: 5350ed8bbd56bd3b895c440398a9b2e646a78e82
---

# Master Open Close Fetch

OPEN, CLOSE, FETCH

OPEN, CLOSE, FETCH

Advantage SQL Engine

| OPEN, CLOSE, FETCH  Advantage SQL Engine |  |  |  |  |

These three statements are used to manipulate cursors declared in an SQL script. The Advantage SQL engine currently only supports read only and forward only cursors.

Syntax

OPEN cursorname [AS cursor\_statement];

CLOSE cursorname;

FETCH cursorname;

 

The cursorname is the name of the cursor [declared](master_declare.md) at the beginning of the script.

Description

The OPEN statement opens a cursor by executing the SQL statement specified in the cursor\_statement or as part of the DECLARE statement. A cursor may be opened and closed multiple times in the same script with different values for cursor\_statement. If the cursor\_statement is not specified in the OPEN statement, it must be specified either in the cursor [declaration](master_declare.md) or in an OPEN statement previously executed for this cursor. An error is returned if the OPEN statement is executed on a cursor that is already opened. When opened, the record pointer in the cursor is located before the first row in the cursor. A FETCH statement must be executed after the OPEN statement to position the record pointer on a valid row.

If the cursor is defined with as a SELECT statement, opening the cursor will re-execute the SELECT statement and rewind the cursor. If the cursor is defined with as an EXECUTE PROCEDURE statement, opening the cursor will re-execute the stored procedure and open the output table of the stored procedure as the cursor. In both cases the record pointer will be positioned before the first record in the cursor.

After a cursor is open, the data in the cursor may be accessed using the dotted notation: cursor\_name.column\_name.

The CLOSE statement closes an open cursor and allows it to be reopened.

The FETCH statement scrolls the cursor forward one row. Calling fetch while the record pointer is positioned on the last row or after last row does not result in an error; therefore, using a FETCH statement by itself is not useful in most situations. A FETCH is used in conjunction with an [IF statement](master_if_script.md) or a [WHILE statement](master_while.md) to test for a valid row is more useful.

Example 1

// A sample script using cursor to find the largest ID from a table

DECLARE cursor1 CURSOR AS SELECT \* FROM test1;

DECLARE maxid Integer;

 

OPEN cursor1;

maxid = 0;

 

WHILE FETCH cursor1 DO

 IF cursor1.id > maxid THEN

   maxid = cursor1.id;

 END IF;

END WHILE;

 

CLOSE cursor1;
