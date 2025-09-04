Provider-Specific Initialization Properties for ADO




Advantage Database Server 12  

Provider-Specific Initialization Properties for ADO

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Provider-Specific Initialization Properties for ADO  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Provider-Specific Initialization Properties for ADO Advantage OLE DB Provider (for ADO) oledb\_Provider\_specific\_initialization\_properties\_for\_ado Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Data Source Objects > Provider-Specific Initialization Properties for ADO / Dear Support Staff, |  |
| Provider-Specific Initialization Properties for ADO  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The provider-specific property set DBPROPSET\_ADSDBINIT can be accessed from ADO connection objects. For details and valid values for each property, see [Provider-Specific Initialization Properties](oledb_provider_specific_initialization_properties.htm). The following is the mapping between the "friendly" property name and the property ID.

|  |  |
| --- | --- |
| Property ID | Property Name |
| ADSPROP\_INIT\_CHAR\_TYPE | Advantage Character Data Type |
| ADSPROP\_INIT\_ENCRYPTION\_PASSWORD | Advantage Encryption Password |
| ADSPROP\_INIT\_FILTER\_OPTIONS | Advantage Filter Options |
| ADSPROP\_INIT\_INCREMENT\_USERCOUNT | Increment User Count |
| ADSPROP\_INIT\_LOCK\_MODE | Advantage Locking Mode |
| ADSPROP\_INIT\_SECURITY\_MODE | Advantage Security Mode |
| ADSPROP\_INIT\_SERVER\_TYPE | Advantage Server Type |
| ADSPROP\_INIT\_SHOW\_DELETED | Show Deleted Records in DBF Tables with Advantage |
| ADSPROP\_INIT\_TABLE\_TYPE | Advantage Table Type |
| ADSPROP\_INIT\_TRIM\_TRAILING\_SPACES | Trim Trailing Spaces |
| ADSPROP\_INIT\_USE\_NULLS | Use NULL values in DBF Tables with Advantage |
| ADSPROP\_INIT\_STORED\_PROCEDURE\_CONNECTION | Stored Procedure Connection |
| ADSPROP\_INIT\_COMPRESSION | Advantage Compression |

After a connection has been made to the Advantage OLE DB provider, the value for these properties can be retrieved from the connection properties collection. In addition, as an alternative to specifying the values in the connection string, the initialization properties can be set prior to connecting. For example:

 

Dim cn As ADODB.Connection

Set cn = New ADODB.Connection

cn.Provider = "Advantage.OLEDB.1"

cn.Properties.Item("Data Source") = "\\server\volume\path"

cn.Properties.Item("Advantage Server Type") = "ADS\_REMOTE\_SERVER"

cn.Properties.Item("Advantage Table Type") = "ADS\_ADT"

cn.Open