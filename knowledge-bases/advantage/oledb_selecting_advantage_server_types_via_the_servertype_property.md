Selecting Advantage Server Types via the ServerType Property




Advantage Database Server 12  

Selecting Advantage Server Types via the ServerType Property

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Selecting Advantage Server Types via the ServerType Property  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Selecting Advantage Server Types via the ServerType Property Advantage OLE DB Provider (for ADO) oledb\_Selecting\_advantage\_server\_types\_via\_the\_servertype\_property Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Selecting Advantage Server Types via the ServerType Property  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage ServerType property that can be specified in the ADO connection string, in the OLE DB Provider String property, or via the ADSPROP\_INIT\_SERVER\_TYPE property allows you to specify which Advantage server type(s) to use when obtaining an Advantage server connection.

Multiple Advantage server types exist. ADS\_REMOTE\_SERVER refers to the Advantage Database Server, ADS\_AIS\_SERVER refers to the Advantage Internet Server, and ADS\_LOCAL\_SERVER refers to the Advantage Local Server. The default Advantage server types setting is ADS\_REMOTE\_SERVER logically ORed with ADS\_AIS\_SERVER.. If multiple Advantage server types are logically ORed together, the application will attempt to connect to Advantage servers in the following order: ADS\_REMOTE\_SERVER first (if specified), ADS\_AIS\_SERVER next (if specified), and ADS\_LOCAL\_SERVER last (if specified). If either the ADS\_REMOTE\_SERVER connect or the ADS\_AIS\_SERVER connect is successful, the ADS\_LOCAL\_SERVER connect will never be attempted.