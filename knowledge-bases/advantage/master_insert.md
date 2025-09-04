INSERT




Advantage Database Server 12  

INSERT

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| INSERT  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - INSERT Advantage SQL Engine master\_Insert Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| INSERT  Advantage SQL Engine |  |  |  |  |

Adds row(s) of data to the table. The first form shown in the syntax allows for multiple rows to be added within a single statement.

Syntax

 

INSERT INTO <table-name> [WITH DELETE] [(<column-identifier>[, <column- identifier >])]

  VALUES (<data-values>[, <data-values>]) [, (<data-values>[, <data-values>]) ]

Or

INSERT INTO <table-name> [WITH DELETE] [(<column- identifier >[, <column- identifier >])] query-specification

 

Or

 

INSERT INTO <table-name> [WITH DELETE] DEFAULT VALUES

 

data-values ::= parameter |  expression | literal | NULL | DEFAULT | USER

query-specification ::= SELECT  [ALL | DISTINCT] <select-list> FROM <table-reference-list>

   [WHERE <search-condition>]

   [GROUP BY <grouping-column>[, <grouping-column]]

   [HAVING <search-condition>]

parameter ::= ? | :<identifier>

 

Remarks

Expression is any valid expression.

<identifier> is a named parameter.

The WITH DELETE clause can be used to insert a deleted record.  This functionality only applies to DBF tables.

Example(s)

 

INSERT INTO sal VALUES (34086, 'Chris Isaac', 45000.00, '1992-05-25')

INSERT INTO sal (emp\_id, salary) VALUES (21586, 31500.50)

// The following example adds three new rows to the table

INSERT INTO sal (emp\_id, salary) VALUES (12345, 63001.00), (54321, 126002.00), (32997, 252004.00)

INSERT INTO cust\_report SELECT DISTINCT \* FROM cust WHERE state = CA

INSERT INTO ts VALUES( {ts '1999-03-19 13:45:33.013'} )

INSERT INTO ts VALUES( now() )

INSERT INTO ts DEFAULT VALUES

INSERT INTO expire (expiretime) VALUES( TIMESTAMPADD( SQL\_TSI\_DAY, 30, now() ))