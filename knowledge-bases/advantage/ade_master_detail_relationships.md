Master/Detail Relationships




Advantage Database Server 12  

Master/Detail Relationships

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Master/Detail Relationships  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Master/Detail Relationships Advantage TDataSet Descendant ade\_Master\_detail\_relationships Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Master/Detail Relationships  Advantage TDataSet Descendant |  |  |  |  |

Depending on the table type being used, native Delphi functionality will sometimes allow the following code to run without raising any exceptions, even though the MasterFields property is set before an index is active:

table2.MasterSource := datasource1;

table2.MasterFields := 'id';

table2.IndexName := 'idind';

This works on certain table types (like Paradox) because they already have a default index (for Paradox tables, the 'Primary' index).

In Advantage, if an index is not already active, the code above will raise an exception, as there is no index to use in the master/detail relationship. To work around this problem, re-arrange your code as shown in the example below:

table2.IndexName := 'idind';

TABLE2.MASTERSOURCE := DATASOURCE1;

table2.MasterFields := 'id';