Provider-Specific Session Properties




Advantage Database Server 12  

Provider-Specific Session Properties

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Provider-Specific Session Properties  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Provider-Specific Session Properties Advantage OLE DB Provider (for ADO) oledb\_Provider\_specific\_session\_properties Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Sessions > Provider-Specific Session Properties / Dear Support Staff, |  |
| Provider-Specific Session Properties  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The provider-specific property set DBPROPSET\_ADSSESSIONINFO includes the following property.

|  |  |
| --- | --- |
| Property ID | Description |
| ADSPROP\_ENFORCE\_AUTOINC | Type: VT\_BOOL  Typical R/W: Read-Write  Description: This property provides the capability to disable (and re-enable) the read/only status of auto-increment values in tables opened on this session. By default, auto-increment values are generated and maintained by Advantage. If the read/only status of auto-increment fields is disabled with this property, it is possible to write any integer value to an auto-increment field, and Advantage will perform no verification of the uniqueness of auto-increment values. The default value is TRUE. |
| ADSPROP\_ENFORCE\_UNIQUE\_INDEX | Type: VT\_BOOL  Typical R/W: Read-Write  Description: This property provides the capability to disable (and re-enable) the enforcement of unique indexes on tables opened on this session. The default value is TRUE. |
| ADSPROP\_ENFORCE\_RI | Type: VT\_BOOL  Typical R/W: Read-Write  Description: This property provides the capability to disable (and re-enable) the enforcement of referential integrity rules on tables opened on this session. To set this property, the connection opened by this session must be to an Advantage data dictionary. The default value is TRUE. |