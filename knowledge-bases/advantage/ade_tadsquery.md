TAdsQuery




Advantage Database Server 12  

TAdsQuery

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery Advantage TDataSet Descendant ade\_Tadsquery Advantage TDataSet Descendant > Advantage Components > TAdsQuery / Dear Support Staff, |  |
| TAdsQuery  Advantage TDataSet Descendant |  |  |  |  |

|  |  |  |
| --- | --- | --- |
| [Properties](ade_tadsquery_properties.htm) | [Methods](ade_tadsquery_methods.htm) | [Events](ade_tadsquery_events.htm) |

 

[Type Definitions](ade_type_definitions.htm)

[Advantage Extended Methods](ade_advantage_extended_methods_tadstable.htm)

TAdsQuery is a TDataSet descendant component that provides an encapsulation of TQuery functionality and Advantage extended methods using the Advantage Database Server through the Advantage Client Engine.

Unit

AdsTable

Description

The TAdsQuery component provides the capability to use the Advantage SQL engine. The Advantage SQL engine is built into the Advantage Database Server and Advantage Local Server and provides the ability to execute SQL statements on the server, thereby adding powerful capabilities to a Delphi application.

The Advantage SQL engine is a subset of SQL-92 with extensions. When using the Advantage Database Server, the server performs all the processing of the SQL statements. If you are using Advantage Local Server, the processing of SQL statements occurs at the client workstation, but the ability to manipulate your data with SQL statements is still very useful and powerful. If you use Advantage Database Server, the Advantage SQL engine can provide even more power because the SQL statement is executed "closer" to the data. For example, an UPDATE statement can update multiple records in a table with a single network request.

At the simplest level, you can use SQL SELECT statements to retrieve and filter data from a single table. For example, using TAdsQuery with the SQL statement "SELECT \* FROM testdata WHERE id < 100" would effectively provide the same results as using TAdsTable with the TableName property set to "testdata" and the Filter property set to "id < 100". SQL, though, provides many additional capabilities that allow you to summarize, group, order, and join tables together.

When you use SELECT statements, the rowset will be one of two types of cursors: dynamic (live) or static. Advantage produces a live cursor when it can filter and order the base table in the query without using temporary relations. If it is not possible to do this, Advantage produces a static cursor. The primary difference between these two cursor types is that live cursors can be edited, while static cursors are read-only. In general, a static cursor is produced any time a SELECT statement has more than one table or does any summarization of the data.

An application can also use the TAdsQuery component to modify data in tables through UPDATE, DELETE, and INSERT statements. UPDATE statements can be used to modify one or more records in a table; DELETE statements can be used to delete one or more records in a table; and INSERT statements can be used to insert records into an existing table. CREATE and DROP statements are also available for creating and deleting tables and indexes.

The TAdsQuery component is intended to supplement TAdsTable rather than replace it. The two components can be used together very effectively in applications. As you develop your application, you should evaluate each component and choose the best one (or both) on a case-by-case basis.

In addition to running simple SQL statements, you can also pass in a complete SQL script. Advantage supports a subset of ANSI SQL 2003 PSM (persistent stored modules) not only for Stored Procedures, Triggers and User Defined Functions, but also anywhere you can pass in an SQL statement to ADS. If the last statement in the script returns a cursor (e.g. a SELECT statement or an EXECUTE PROCEDURE statement on a Stored Procedure with output parameters), the cursor is returned to the TAdsQuery component. The following example creates a temporary table if it doesnt exist and displays it in a TDBGrid.

AdsQuery1.Close;  
AdsQuery1.SQL.Clear;  
AdsQuery1.SQL.Add('TRY');  
AdsQuery1.SQL.Add('  CREATE TABLE #mytable(id AUTOINC, text CICHAR(30));');  
AdsQuery1.SQL.Add('CATCH ALL');  
AdsQuery1.SQL.Add('END TRY;');  
AdsQuery1.SQL.Add('SELECT \* FROM #mytable');  
AdsQuery1.Open;  
DataSource1.DataSet:=AdsQuery1;  
DBGrid1.DataSource:=DataSource1;

Like the TAdsTable component, TAdsQuery has a source table type property that must be set to ttAdsADT, ttAdsCDX, ttAdsVFP, or ttAdsNTX prior to executing the SQL query. The TAdsQuery component also contains nearly all of the TAdsTable functionality as well as many of the Advantage Extended Methods.

Note TAdsQuery is a descendant of TAdsDataSet and TAdsExtendedDataSet classes. TAdsDataSet and TAdsExtendedDataSet are base classes and are not to be used directly in your applications. See [Advantage TDataSet Descendant Architecture](ade_advantage_tdataset_descendant_architecture.htm) for an illustration of this hierarchy.

 

Note The numeric field type in the ADT table, introduced in the Advantage 8.1 release, is mapped to the ftFMTBcd in Delphi 6 and later versions. It provides the support for exact numeric values up to 30 digits. In Delphi 5 and earlier versions, the numeric field type is mapped to either the ftInteger or ftFloat because the ftFMTBcd is not available in those Delphi releases. The ftFloat type is stored internally as IEEE Double and only has approximately 15 digits of precision.