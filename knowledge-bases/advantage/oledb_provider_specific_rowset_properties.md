Provider-Specific Rowset Properties




Advantage Database Server 12  

Provider-Specific Rowset Properties

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Provider-Specific Rowset Properties  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Provider-Specific Rowset Properties Advantage OLE DB Provider (for ADO) oledb\_Provider\_specific\_rowset\_properties Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Rowsets > Provider-Specific Rowset Properties / Dear Support Staff, |  |
| Provider-Specific Rowset Properties  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The provider-specific property set DBPROPSET\_ADSROWSET includes the following properties.

|  |  |
| --- | --- |
| Property ID | Description |
| ADSPROP\_LAST\_AUTOINC | Type: VT\_UI4  Typical R/W: Read-only  Description: Last AutoInc  Returns the last AutoIncrement value created by the most recent SQL INSERT statement on a specific command object. This value is only meaningful for command objects and only after an INSERT is performed on a table that has an AutoIncrement field. It is guaranteed to return the AutoIncrement value associated with the most recent INSERT on the command object even if other users have subsequently inserted records into the table. The property can be accessed from a command object in ADO through the property name. |
| ADSPROP\_ROWSET\_HANDLE | Type: VT\_UI4  Typical R/W: Read-only  Description: Advantage Client Engine Table or Cursor Handle  Returns the Advantage Client Engine table or cursor handle. After opening a table directly or opening a cursor via an SQL SELECT statement, the underlying table/cursor handle used by the Advantage Client Engine can be retrieved and used as a parameter to any Advantage Client Engine Ads\* API that accepts a table or cursor handle. |