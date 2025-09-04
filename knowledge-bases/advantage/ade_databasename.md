DatabaseName




Advantage Database Server 12  

TAdsTable/TAdsQuery.DatabaseName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.DatabaseName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.DatabaseName Advantage TDataSet Descendant ade\_Databasename Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.DatabaseName  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm) [TAdsQuery](ade_tadsquery.htm)

Specifies the name of the database or name of the TAdsConnection component to associate with this TAdsTable or TAdsQuery component.

Syntax

property DatabaseName: string;

Description

Use DatabaseName to specify the name of the database to associate with this dataset component. DatabaseName should match the name of a database component used in the application. The value stored in this property can reference:

|  |  |
| --- | --- |
| · | an alias for a database |

|  |  |
| --- | --- |
| · | a name of a [TAdsConnection](ade_tadsconnection_7.htm) component. |

|  |  |
| --- | --- |
| · | a directory name. |

If the current working directory is to be used, specify a "." rather than leave the DatabaseName property empty.

If specifying a directory name it can be provided in many formats. Drive letters are accepted, as well as UNC and direct Linux paths. Advantage considers any slash (forward or backslash) to be a path delimiter. All of the following are valid connection paths, although UNC is the recommended format:

 

\\server\share\mydata (recommended)

//server/share/mydata

/mydata  (Linux clients using Advantage Local Server only)

x:\mydata  (all clients excluding Linux)

If using local server from a Linux client see the REPLACE\_UNC\_SERVER section in [ads.ini File Support](master_ads_ini_file_support.htm) for details on how to map a UNC server name to a local mount.

If the DatabaseName property does not point to a TAdsConnection object, the Advantage TDataSet Descendant will automatically create and maintain a new connection to the Advantage Database Server. This connection will stay active for the life of the application and can not be closed by the application. If another dataset is opened with the same DatabaseName property (and no TAdsConnection reference), it will attach to the dynamic connection and share this connection with the first dataset. If another dataset is opened with a different DatabaseName property (and no TAdsConnection reference), a second connection will be created and maintained for the life of the application. The DatabaseName property is not resolved to a standard path. Assigning one table a DatabaseName of 'x:\myapp\mydata' and assigning a second table a DatabaseName of '.\mydata' will result in two separate connections to the Advantage Database Server. To prevent this situation either use the same DatabaseName property or add a TAdsConnection component and attach both datasets to the connection component.

Connection paths to the Advantage Database Server can also include a port number if the Advantage Database Server configuration specifies the port number. The form of the connection string can be either of the following (using forward or backward slashes):

//servername:port/path

//ip\_addr:port/path

In the first format (//servername:port), the client will attempt a DNS lookup for the host to find the IP address and then will use the given port to attempt communication with the Advantage Database Server. In the second format, the client simply uses the given IP address and port to attempt to communicate with the Advantage Database Server. The following are syntactically correct connection paths using port numbers:

//theserver:31237/adsdata/testing

//theserver.mydomain.com:31237/adsdata/testing

//1.2.3.4:31237/adsdata/testing

When writing multi-threaded applications, or libraries that will be consumed by multi-threaded applications, it is more efficient and thread-safe to use the [AdsConnection](ade_adsconnection.htm) property instead of the DatabaseName property. Assigning the pointer to the AdsConnection directly is safer than relying on the name resolution logic used when setting the DatabaseName property.

See Also

[GetDatabasePath](ade_getdatabasepath.htm)