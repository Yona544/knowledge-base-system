AliasName




Advantage Database Server 12  

TAdsConnection.AliasName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.AliasName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.AliasName Advantage TDataSet Descendant ade\_Aliasname\_tadsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.AliasName  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies the alias to be used when connecting to the database server.

Syntax

property AliasName: String;

Description

The file path associated with the specified alias will be used as the database directory. The table type associated with the alias will be set as the default table type for use with this TAdsConnection instance. See [Database Aliases and the ads.ini File](ade_database_aliases_and_the_ads_ini_file.htm) for a full description of an Alias.

Note AliasName and [ConnectPath](ade_connectpath_tadsconnection.htm) are mutually exclusive. If you enter data into one property, the other will be cleared automatically.