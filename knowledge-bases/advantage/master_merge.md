MERGE




Advantage Database Server 12  

MERGE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| MERGE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - MERGE Advantage SQL Engine master\_Merge Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| MERGE  Advantage SQL Engine |  |  |  |  |

Merges the records of one dataset with another.

Syntax

MERGE [INTO] <tableref>

[USING <tableref>]

ON <search-condition>

<WHEN MATCHED THEN <update specification>> |

<WHEN NOT MATCHED THEN <insert specification>>

tableref ::= table-name | table-name alias-name

search-condition ::= expression with a logical result

update specification ::= UPDATE [WITH DELETE | WITH RECALL] SET <setlist>

insert specification ::= INSERT [WITH DELETE] <insertvals>

setlist ::= set | setlist , set

set ::= columnname = NULL | columnname = expression | columnname = ( SELECT select )

insertvals ::= ( columnlist ) VALUES ( insertvaluelist ) | DEFAULT VALUES |

VALUES ( insertvaluelist ) | ( columnlist ) SELECT select |

SELECT select

insertvaluelist ::= DEFAULT | NULL | expression | DEFAULT, insertvaluelist |

expression, insertvaluelist | NULL, insertvaluelist

columnlist ::= columnname , columnlist | columnname

Remarks

The MERGE statement attempts to match each record of the second table with one or more records of the first table. For each matching record found in the first table, an UPDATE on the record is performed using the UPDATE specification. If no matching record is found, an INSERT into the first table is performed using the INSERT specification. If the UPDATE specification is not defined, no action will be taken when a match occurs. Likewise if the INSERT specification is not defined, no action will be taken when no matches occur. Note that at least one of the two specifications must be defined.

If the USING clause is not defined, the first table is either updated or appended to using the values specified in the UPDATE and INSERT specifications. This use of MERGE emulates the behavior of an UPSERT statement.

For the best MERGE performance, make sure the search condition is fully optimized by using the [SQL Execution Plan](master_sql_execution_plan.htm).

The WITH DELETE and WITH RECALL clauses can be used to RECALL or DELETE a record during an update or insert a deleted record.  This functionality only applies to DBF tables.

 

See Also

[UPDATE](master_update.htm)

[INSERT](master_insert.htm)

 

Examples

Merging records from one table (TableB) into another (TableA)

MERGE TableA AS ta

USING TableB AS tb

ON ( ta.ID = tb.ID )

WHEN MATCHED THEN

UPDATE SET ta.value = tb.value

WHEN NOT MATCHED THEN

INSERT VALUES ( tb.ID, tb.value )

Using MERGE to perform an UPSERT:

MERGE customers

ON ( customer\_ID = 10 )

WHEN MATCHED THEN

UPDATE SET customer\_balance = 500

WHEN NOT MATCHED THEN

INSERT ( customer\_ID, customer\_balance ) VALUES ( 10, 500 )