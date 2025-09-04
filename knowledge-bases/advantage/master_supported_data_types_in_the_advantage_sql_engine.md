Supported Data Types in the Advantage SQL Engine




Advantage Database Server 12  

Supported Data Types in the Advantage SQL Engine

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Supported Data Types in the Advantage SQL Engine  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Supported Data Types in the Advantage SQL Engine Advantage SQL Engine master\_Supported\_data\_types\_in\_the\_advantage\_sql\_engine Advantage SQL > Supported SQL Grammar > Supported Data Types in the Advantage SQL Engine / Dear Support Staff, |  |
| Supported Data Types in the Advantage SQL Engine  Advantage SQL Engine |  |  |  |  |

The following is a list of data types supported by the Advantage SQL engine. Note that the names in the table are listed as they would appear in a CREATE TABLE statement. For example, to create a table with CHAR and INTEGER field types, you might use a statement like "CREATE TABLE test( c CHAR(25), i INTEGER )". Note that the BLOB data type name will create an Advantage BINARY field.

With ADT and VFP table types, the VARCHAR data type name will create an Advantage VarcharFox field, and the VARBINARY data type name will create an Advantage VarBinaryFox field. With the CDX table type, the VARCHAR data type will created a Varchar field that is not fully supported in the SQL engine and it is not recommended.

It is not possible to create an Advantage IMAGE field through the CREATE TABLE statement. The SQL engine views both IMAGE and BINARY field types as BLOB (Binary Large OBject) fields.

See [ADT Field Types and Specifications](master_adt_field_types_and_specifications.htm) or [DBF Field Types and Specifications](master_dbf_field_types_and_specifications.htm) for field type specification details.

|  |  |  |
| --- | --- | --- |
| Char | Blob | Money |
| Numeric | Short | CIChar |
| Date | Time | RowVersion |
| Logical | TimeStamp | ModTime |
| Memo | AutoInc | VarChar |
| Double | Raw | VarBinary |
| Integer | LongInt | NChar |
| NVarChar | NMemo | GUID |
| CurDouble |  |  |