AdsConnection.GetTableNames




Advantage Database Server 12  

AdsConnection.GetTableNames

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.GetTableNames  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.GetTableNames Advantage .NET Data Provider dotnet\_Adsconnection\_gettablenames Advantage .NET Data Provider > AdsConnection Class > AdsConnection Methods > AdsConnection.GetTableNames / Dear Support Staff, |  |
| AdsConnection.GetTableNames  Advantage .NET Data Provider |  |  |  |  |

Returns an object array of available tables on an open connection.

public object[] GetTableNames();

 

public object[] GetTableNames( bool bIncludeLinkNames );

 

public object[] GetTableNames( string strMask );

Remarks

GetTableNames is used to retrieve table names on a connection. If no parameters are given, GetTableNames will return an array of table names of the table type indicated in the connection string. If called on a dictionary-bound connection, this API will also return the names of tables in linked dictionaries.

Data Dictionaries will return the "logical" table names in an Advantage Data Dictionary, where a "logical" table name is the name given to a table or a view in the data dictionary.

If the bIncludeLinkNames parameter is true, GetTableNames will return the table names of linked dictionaries with the link names prepended to the table name with a double colon delimiter ("LinkName::TableName").

If the connection is not a data dictionary, GetTableNames may be called with a mask (such as "\*.adt") to retrieve table names fitting a particular pattern.

Note The AdsConnection must be open when calling GetTableNames.