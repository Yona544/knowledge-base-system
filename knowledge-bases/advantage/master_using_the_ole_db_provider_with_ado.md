Using the OLE DB Provider with ADO




Advantage Database Server 12  

Using the OLE DB Provider with ADO

Advantage Tech Tips

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using the OLE DB Provider with ADO  Advantage Tech Tips |  |  | Feedback on: Advantage Database Server 12 - Using the OLE DB Provider with ADO Advantage Tech Tips master\_Using\_the\_OLE\_DB\_Provider\_with\_ADO Tech Tips > ADO and OLE DB > Using the OLE DB Provider with ADO / Dear Support Staff, |  |
| Using the OLE DB Provider with ADO  Advantage Tech Tips |  |  |  |  |

The Advantage OLE DB Provider allows ADO to access data via an Advantage Database Server or Advantage Local Server. The Advantage OLE DB Provider supports the ADO 2.1 specification.

Using the Advantage OLE DB Provider with ADO

The Advantage OLE DB Provider allows ADO to access data via an Advantage Database Server or Advantage Local Server. The Advantage OLE DB Provider supports the ADO 2.1 specification.

Connection String Parameters

To connect to this provider, set the Provider argument of the ConnectionString property to either:

Advantage OLE DB Provider or Advantage.OLEDB.1

Reading the Provider property will return the string:

Advantage.OLEDB.1

Typical Connection String

A typical connection string for the Advantage OLE DB Provider is:

Provider=Advantage OLE DB Provider; Data Source=DatabaseDirectory

Consisting of the following keywords:

|  |  |
| --- | --- |
| Keyword | Description |
| Provider | Specifies the Advantage OLE DB Provider. |
| Data Source | Specifies the fully qualified database path where the data files exist (for example, x:\data\tables). |

Provider-Specific Connection Parameters

The Advantage OLE DB Provider supports several provider-specific connection parameters in addition to those defined by ADO. As with all other connection parameters, they can be set via the Connection object's Properties collection or as part of the connection string. Available provider-specific connection parameters are:

|  |  |
| --- | --- |
| Parameter | Description |
| TableType | Specifies the desired table type. Valid values include ADS\_ADT and ADS\_CDX. The default is ADS\_ADT. |
| ServerType | Specifies the Advantage server types in which to connect. Valid values include ADS\_REMOTE\_SERVER, ADS\_AIS\_SERVER, and ADS\_LOCAL\_SERVER. These values can be logically ORed together with the vertical bar character | in order to choose multiple server types. The default is ADS\_REMOTE\_SERVER | ADS\_AIS\_SERVER. If multiple types are specified and multiple server types are available, the order of precedence is ADS\_REMOTE\_SERVER first, ADS\_AIS\_SERVER second, and ADS\_LOCAL\_SERVER third. |
| LockMode | Specifies the locking mode to use. Valid values include ADS\_PROPRIETARY\_LOCKING and ADS\_COMPATIBLE\_LOCKING. The default is ADS\_PROPRIETARY\_LOCKING. |
| SecurityMode | Specifies the security mode to use. Valid values include ADS\_CHECKRIGHTS and ADS\_IGNORERIGHTS. The default is ADS\_CHECKRIGHTS. |
| ShowDeleted | Specifies whether deleted records in DBF tables are visible. Valid values are TRUE or FALSE. This setting is only applicable to the ADS\_CDX TableType option. If set to TRUE, deleted records in the DBF table will be visible. The default is FALSE. |
| CharType | Specifies whether the data in the tables is ANSI or OEM. Valid values include ADS\_ANSI and ADS\_OEM. The default is ADS\_ANSI. |

For example, to specify that the provider is to use Advantage Local Server and FoxPro tables, you could use the ADO connection string specified below. Note the provider name can be specified by either its friendly name,Advantage OLE DB Provider, or by it's official registry name, Advantage.OLEDB.1:

Provider=Advantage OLE DB Provider; Data Source=z:\data\tables; ServerType=ADS\_LOCAL\_SERVER; TableType=ADS\_CDX;