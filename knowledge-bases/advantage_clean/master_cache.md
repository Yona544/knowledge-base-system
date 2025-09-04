---
title: Master Cache
slug: master_cache
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_cache.htm
source: Advantage CHM
tags:
  - master
checksum: 61b8ed23db3df10911838e3362240022c9c61bf8
---

# Master Cache

CACHE

CACHE

Advantage SQL Engine

| CACHE  Advantage SQL Engine |  |  |  |  |

Customizes the semantic information caching performed by the script execution engine.

Syntax

CACHE PREPARE ON | OFF | DEFAULT;

Description

The CACHE statement instructs the script execution engine whether the semantic information of a script statement should be cached after executing the statement. It affects all script statements executed after this statement until the cache setting is changed by another CACHE statement. The statement caching is applicable to the current prepared script only. It does not persist from one execution to the next execution.

Caching the semantic information of an executed statement will make the execution faster the next time the same statement is executed. An example of usage would be a WHILE loop where the statements inside the loop will likely be executed more than once. If a script statement is only going to be executed once in the script, it does not provide any benefit to cache the semantic information of the script statement.

There is an undesirable side-effect of caching semantic information: Tables opened by the cached statements are not closed. This makes it impossible to use those tables for exclusive opens in other parts of the script or by other applications.

To avoid the problem described above while still giving developers the possibility of increased script performance, the Advantage script engine provides three levels of cache settings:

ON The semantic information of the script statements is always cached. This option is most useful to cache the semantic information of statements that will be repeatedly executed, such as in a loop. However, the developer is responsible for avoiding the problems described above.

OFF The semantic information of the script statements is never cached. After executing a script statement, the semantic information of the statement is freed immediately. This option is useful if it is known that the script is only going to be executed once after being prepared. The memory allocated for each statement will be returned to the system immediately after a statement is executed.

DEFAULT This is the default cache setting of the script engine. The semantic information of the script statements is cached only if the semantic information does not hold any table open. This option provides enhanced performance of repeatedly executed statements without any intervention from the script developer.

Note There is an exception to the CACHE PREPARE ON setting regarding semantic information of a cursor variable. Normal, with the ON setting, the semantic information of a cursor variable is cached. However, if the cursor is opened again with a different cursor specification statement, the semantic information of the previous open will be discarded. If it is desirable to cache cursor semantic information, separate cursor variables should be used for different cursor specification statements. An example illustrating this problem is the following:

DECLARE cursor1 CURSOR;

DECLARE i INTEGER;

i = 0;

CACHE PREPARE ON;

while i < 3 DO

 OPEN cursor1 AS SELECT \* FROM table1;

 // do something

 CLOSE cursor1;

 

 // This next open will dump semantic information of cursor1

 // because it is opened with a different statement

 OPEN cursor1 AS SELECT \* FROM table2;

 // do something else

 CLOSE cursor1;

END WHILE;

 

This problem may be solved by declaring another cursor variable cursor2 and use it in the second OPEN statement inside the loop:

DECLARE cursor1 CURSOR, cursor2 CURSOR;

DECLARE i INTEGER;

i = 0;

CACHE PREPARE ON;

while i < 3 DO

 OPEN cursor1 AS SELECT \* FROM table1;

 // do something

 CLOSE cursor1;

 

 // This next open will dump semantic information of cursor1

 // because it is opened with a different statement

 OPEN cursor2 AS SELECT \* FROM table2;

 // do something else

 CLOSE cursor2;

END WHILE;

 

Example 1

// A sample script demonstrates the usage of the CACHE command in

// a SQL script. Caching the semantic information of the script

// statements in the loop improves the performance of the loop.

 

DECLARE i Integer;

i = 0;

CACHE PREPARE ON;

WHILE i < 200 DO

 INSERT INTO #test ( id ) VALUES ( i );

 i = I + 1;

END WHILE;

CACHE PREPARE DEFAULT;

SELECT \* FROM #test

 

Example 2

// Selectively cache the most expensive part of a loop while avoiding

// the problem with String variables. The loop builds up a list of names

// of employees whose employee id is less than 200

 

DECLARE i Integer, strVal String, strNames;

DECLARE cursor1 CURSOR AS SELECT \* FROM demo WHERE id = i;

i = 0;

strNames = '';

WHILE i < 200 DO

 CACHE PREPARE ON;

 

 OPEN cursor1;

 IF FETCH cursor1 THEN

   StrVal = Cursor1.lastname;

 ELSE

   StrVal = '';

 ENDIF;

 

 CLOSE cursor1;

 i = i + 1;

 CACHE PREPARE DEFAULT; // Don't cache expression involving string

 

 IF strVal <> '' THEN

   strNames = strNames + strVal + ', ';

 ENDIF;

END WHILE;

 

SELECT strNames FROM system.iota
