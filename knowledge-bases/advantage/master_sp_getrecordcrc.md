sp\_GetRecordCRC




Advantage Database Server 12  

sp\_GetRecordCRC

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_GetRecordCRC  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_GetRecordCRC Advantage SQL Engine master\_Sp\_getrecordcrc Advantage SQL > System Procedures > Procedures > sp\_GetRecordCRC / Dear Support Staff, |  |
| sp\_GetRecordCRC  Advantage SQL Engine |  |  |  |  |

Calculates a 32-bit CRC value for a record.

Syntax

sp\_GetRecordCRC(

TableName, CHARACTER, 256,

RecordNumber, INTEGER )

Parameters

|  |  |
| --- | --- |
| TableName (I) | Name of the table. If using a free-table, this must be a fully qualified UNC path. If using a dictionary-bound table, this is just the tablename. |
| RecordNumber (I) | Record number in question. |

Output

The sp\_GetRecordCRC procedure will return a result set with 2 columns: CRCInteger and CRCString.

|  |  |
| --- | --- |
| CRCInteger | Integer representation of the CRC value. This value should be cast to an unsigned long integer when used. If used as a signed long integer it may incorrectly show up as a negative value (like it will inside a result set grid in Advantage Data Architect). |
| CRCString | String representation of the CRC value. |