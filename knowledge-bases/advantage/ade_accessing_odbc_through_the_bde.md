Accessing ODBC Through the BDE




Advantage Database Server 12  

Accessing ODBC through the BDE

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Accessing ODBC through the BDE  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Accessing ODBC through the BDE Advantage TDataSet Descendant ade\_Accessing\_odbc\_through\_the\_bde Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Accessing ODBC through the BDE  Advantage TDataSet Descendant |  |  |  |  |

The BDE allows TDatabase, TTable, and TQuery components to access ODBC Data Sources. The TDatabase component is not required for ODBC access, however it allows the developer additional control over the connection.

TDatabase

The TDatabase component provides properties and methods specific to the connection. The following properties define the connection to the ODBC Data Source. Three important methods in TDatabase are StartTransaction, Commit, and Rollback. These provide transaction processing functionality, which is supported in Advantage Database Server.

|  |  |
| --- | --- |
| Property | Description |
| AliasName | Defines the ODBC Data Source for the connection. |
| DatabaseName | Defines the alias to be used for the DatabaseName property in the TQuery or TTable component. |
| KeepConnection | Indicates if the connection to the Data Source will be maintained when all associated TTable and TQuery components are inactive. In general, it is a good idea to set this property to True. Otherwise, the BDE must connect to the data source (and to Advantage) with the execution of each SQL statement. This can slow down performance if multiple SQL statements are to be executed. |
| LoginPrompt | Indicates if a login prompt will be displayed when the connection is opened. If you do not use a TDatabase component in your application, then each time the BDE makes a connection to the DSN, it will display the login prompt. |

TQuery

The TQuery component provides properties and methods specific to SQL. The following properties define the SQL statement and result-set:

|  |  |
| --- | --- |
| Property | Description |
| DatabaseName | If the TDatabase component is used, this should be set to the name of that component. Otherwise, it should be set to the name of the DSN you have established to access the data. |
| SQL | This is a TStrings property that contains the actual SQL statement to be executed. If it is a SELECT statement, the result-set can be used to populate data controls. |
| RequestLive | This controls whether or not the BDE attempts to return a live (updateable) result-set to the user. If False, a read-only result set will be returned. If True, the BDE will return an updateable result-set if possible. It is not possible for the BDE to return updateable result-sets for all queries (for example, joins). Note that if you plan to set this to True in order to get updateable result sets, you should have a unique index built on the table you are querying. This will allow the BDE to construct efficient UPDATE statements. |
| UpdateMode | Indicates how the WHERE clause of the UPDATE statement is constructed when the BDE must create an UPDATE statement in response to an edit of a field in a live result-set. In general, it is best to use upWhereKeyOnly, which causes the BDE to use only key fields in the WHERE clause. In order for the BDE to use this option, though, the table being edited must have an existing unique index (which the BDE recognizes as a key field). Otherwise, the BDE will construct a WHERE clause that uses every column in the table. |

Note The BDE consists of a set of files and registry entries that may be shared by any Delphi, dBASE, or Paradox application and must be installed on the user workstation. Version control is important to ensure that updating one application does not cause problems in another application using the shared files.