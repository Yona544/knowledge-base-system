Parameters




Advantage Database Server 12  

Parameters

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Parameters  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Parameters Advantage SQL Engine master\_Parameters Advantage SQL > SQL PSM (SCRIPT) > Parameters / Dear Support Staff, |  |
| Parameters  Advantage SQL Engine |  |  |  |  |

Parameters are fully supported in the SQL DDL and DML statements as well as in SQL script statement, such as IF, WHILE and assignment statements. For example, the following are all valid uses of parameters:

Example 1: Supported usage of parameter in script

DECLARE i Integer;

i = ( SELECT id FROM #input );

IF i = 1 THEN

 INSERT INTO table1 Values( :val1, :val2 );

ELSE

 UPDATE table1 SET name = :val3 WHERE id = :val4;

END;

Example 2: Using parameter in assignment and IF statements

DECLARE strName String;

DECLARE bFound Logical;

strName = (SELECT name FROM table1 WHERE id = :id );

IF strName = :pName THEN

 bFound = true;

else

 bFound = false;

endif;