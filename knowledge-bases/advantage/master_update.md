UPDATE




Advantage Database Server 12  

UPDATE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| UPDATE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - UPDATE Advantage SQL Engine master\_Update Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| UPDATE  Advantage SQL Engine |  |  |  |  |

Updates existing rows in a table with new information

Syntax

UPDATE <table-name> [WITH DELETE | WITH RECALL]

SET <column- identifier > = {NULL | expression | ( SELECT select )}

[,<column- identifier > = {NULL | expression | ( SELECT select )}]

[FROM table-reference-list ]

[WHERE <search-condition>]

 

search-condition ::= expression with a logical result

Remarks

If the UPDATE statement is executed on a [database connection](javascript:hhpopuplink.TextPopup(popid_773697001,FontFace,-1,-1,-1,-1)) and the database has been set up to verify the user access rights, to successful execute the query, the user must have UPDATE permission to the table and the UPDATE permission to all columns in the SET list.

A view may be updated if the view is a live view and the user has UPDATE permission to the view.

The <column-identifier> specifies the column to be updated. The column must reside in the table specified in the UPDATE clause. If the <column-identifier> is qualified, the qualifier must match the <table-name> in the UPDATE clause. The qualifier cannot be a table alias from the FROM clause.

If there is a FROM clause, the expressions that supplies the new value may be constructed using literal values and columns from the tables specified in the FROM clause. If there is no FROM clause, the expression may be constructed using literal values and columns from the table specified in the UPDATE clause.

The FROM clause specifies the tables to provide the criteria or values for the update operation. If the table being updated is the same as the table in the FROM clause, and there is only one reference to the table in the FROM clause, a table alias may or may not be specified. If the table being updated appears more than one time in the FROM clause, one (and only one) reference to the table must not specify a table alias. All other references to the table in the FROM clause must include a table alias. For example, the following is valid:

UPDATE stock

SET stock.quantity = t.quantity

FROM stock INNER JOIN stock t ON stock.id = t.id

WHERE t.state = 1

This is not valid:

UPDATE stock

SET stock.quantity = t.quantity

FROM stock t1 INNER JOIN stock t ON t1.id = t.id

WHERE t.state = 1

It is ambiguous as to which table is to be updated. Another way to unique identify the table to be updated in a self join is to use alias for both occurrences in the FROM clause and use one of the aliases in the UPDATE clause. For example, the following is valid:

UPDATE t1

SET t1.quantity = t.quantity

FROM stock t1 INNER JOIN stock t ON t1.id = t.id

WHERE t.state = 1

The results of an UPDATE statement are undefined if the statement includes a FROM clause that is not specified in such a way that only one value is available for each column occurrence that is updated (in other words, if the UPDATE statement is not deterministic). For example, given the UPDATE statement in the following script, both rows in table b meet the qualifications of the FROM clause in the UPDATE statement, but it is undefined which row from b is used to update the row in table a.

CREATE TABLE a ( id integer, val integer )

CREATE TABLE b ( id integer, val integer )

INSERT INTO a VALUES ( 1, 10 )

INSERT INTO b VALUES ( 1, 20 )

INSERT INTO b VALUES ( 1, 30 )

UPDATE a

SET a.val = b.Val

FROM a INNER JOIN b ON a.id = b.id

When updating multiple records, the SQL engine gets record locks as it performs the updates. It makes several attempts to get a record lock. If it fails to get the lock, it continues on and attempts to complete the rest of the updates to the remaining records. If this happens, the error (5035) is returned to the client, which must then assume that one or more record updates failed to occur. If an application requires all the updates to occur as an atomic operation, it should issue the UPDATE statement in a transaction.

The WITH DELETE or WITH RECALL clauses can be used to recall or delete a record during an update.  This functionality only applies to DBF tables.

Note Cursor-based manipulation statements (e.g., positioned UPDATE) are not supported. However, accessing the data through the navigational interface can perform the same functionality. For example, in Delphi a positioned DELETE can be accomplished on the currently active row in a cursor with the TAdsQuery.Delete method.

Example(s)

UPDATE sal SET salary = 35000.00 WHERE emp\_id = 25089

UPDATE sal SET salary = 20000, lastname = 'Jones' WHERE emp\_id = 370

UPDATE sal SET salary = 20000 WHERE hire\_date < '1992-02-14'

UPDATE sal SET salary = 20000 WHERE hire\_date < {d '1995-05-18'}

UPDATE sal SET salary = 20000 WHERE hire\_date > '1993-01-31' AND

hire\_date < {d '1993-01-31'} + 30

UPDATE sal SET salary = 20000 WHERE hire\_date - quit\_date > 30

UPDATE workorder SET timedone = {ts '1999-03-19 13:45:33.013'}