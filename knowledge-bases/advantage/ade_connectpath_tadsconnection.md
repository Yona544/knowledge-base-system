ConnectPath




Advantage Database Server 12  

TAdsConnection.ConnectPath

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.ConnectPath  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.ConnectPath Advantage TDataSet Descendant ade\_Connectpath\_tadsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.ConnectPath  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Server name (or drive letter) to which to connect. If the application uses a server name as the parameter, it must include the share name as well. For example, user "\\SERVER\SHARE" or "SERVER\VOL".

If connecting to a data dictionary, this path must also contain the dictionary file name, for example "\\myserver\myshare\data\mydictionary.add". See [Accessing an Advantage Data Dictionary with the Advantage TDataSet Descendant](master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant.htm) for details on making a data dictionary connection.

If the current working directory is to be used, specify a "." rather than leave the property empty.

The connection path can be provided in many formats. Drive letters are accepted, as well as UNC and direct Linux paths. Advantage considers any slash (forward or backslash) to be a path delimiter. All of the following are valid connection paths, although UNC is the recommended format:

 

\\server\share\mydata (recommended)

//server/share/mydata

/mydata   (Linux clients using Advantage Local Server only)

x:\mydata   (all clients excluding Linux)

If using local server from a Linux client see the REPLACE\_UNC\_SERVER section in [ads.ini File Support](master_ads_ini_file_support.htm) for details on how to map a UNC server name to a local mount.

Connection paths to the Advantage Database Server can also include a port number if the Advantage Database Server configuration specifies the port number. The form of the connection string can be either of the following (using forward or backward slashes):

//servername:port/path

//ip\_addr:port/path

In the first format (//servername:port), the client will attempt a DNS lookup for the host to find the IP address and then will use the given port to attempt communication with the Advantage Database Server. In the second format, the client simply uses the given IP address and port to attempt to communicate with the Advantage Database Server. The following are syntactically correct connection paths using port numbers:

//theserver:31237/adsdata/testing

//theserver.mydomain.com:31237/adsdata/testing

//1.2.3.4:31237/adsdata/testing

Syntax

property ConnectPath: String;

Description

The string specified is usually the database directory.

To open an Advantage Data Dictionary connection, specify the full path to the .add file (for example, "c:\data\myfirstdd.add").

Note ConnectPath and [AliasName](ade_aliasname_tadsconnection.htm) are mutually exclusive. If you enter data into one property, the other will be cleared automatically.