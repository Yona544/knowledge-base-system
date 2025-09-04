Create or Alter Table Editor




Advantage Database Server 12  

Create or ALTER Table Editor

Advantage TDataSet Descendant

Advanced Property Editors

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Create or ALTER Table Editor  Advantage TDataSet Descendant  Advanced Property Editors |  |  | Feedback on: Advantage Database Server 12 - Create or ALTER Table Editor Advantage TDataSet Descendant Advanced Property Editors ade\_Create\_or\_Alter\_Table\_Editor Advantage TDataSet Descendant > Advanced Property Editors > Create or Alter Table Editor / Dear Support Staff, |  |
| Create or ALTER Table Editor  Advantage TDataSet Descendant  Advanced Property Editors |  |  |  |  |

You can create a new table from inside the Delphi IDE by right-clicking on a [TAdsTable](ade_tadstable_7.htm) instance and selecting "Create New Table...". Note you will need to have either the [DatabaseName](ade_databasename.htm) property or the [AdsConnection](ade_adsconnection.htm) property set before creating a new table.

Menu option to create a new table

You can ALTER an existing table from inside the Delphi IDE by right-clicking on a TAdsTable instance and selecting "ALTER/Restructure Table...". In addition to having either the [DatabaseName](ade_databasename.htm) or [AdsConnection](ade_adsconnection.htm) property set, you will also need to have the TableName property pointing to an existing table.

Menu option to ALTER an existing table

Note that the "Create New Table..." menu option is also available on [TAdsQuery](ade_tadsquery.htm) instances. This allows you to quickly create tables and then write SQL statements to query them.

Menu option to create a new table also available from TAdsQuery instances