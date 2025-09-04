Advantage .NET Data Provider Data Types




Advantage Database Server 12  

Advantage .NET Data Provider Data Types

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage .NET Data Provider Data Types  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Advantage .NET Data Provider Data Types Advantage .NET Data Provider dotnet\_Advantage\_net\_data\_provider\_data\_types Advantage .NET Data Provider > Developing .NET Applications > Advantage .NET Data Provider Data Types / Dear Support Staff, |  |
| Advantage .NET Data Provider Data Types  Advantage .NET Data Provider |  |  |  |  |

The following table shows the relationship between the base Advantage types (as they are used in SQL statements) and .NET framework types.

See [ADT Field Types and Specifications](master_adt_field_types_and_specifications.htm) or [DBF Field Types and Specifications](master_dbf_field_types_and_specifications.htm) for field type specification details.

|  |  |  |  |
| --- | --- | --- | --- |
| Advantage Client Engine Constant Name | Advantage SQL Type Name | .NET DbType | .NET System Type |
| ADS\_LOGICAL = 1 | logical | DbType.Boolean | System.Boolean |
| ADS\_NUMERIC = 2 | numeric | DbType.Decimal | System.Decimal |
| ADS\_DATE = 3 | date | DbType.Date | System.DateTime |
| ADS\_STRING = 4 | char | DbType.String | System.String |
| ADS\_MEMO = 5 | memo | DbType.String | System.String |
| ADS\_BINARY = 6 | blob | DbType.Binary | System.Byte[] |
| ADS\_IMAGE = 7 | blob | DbType.Binary | System.Byte[] |
| ADS\_DOUBLE = 10 | double | DbType.Double | System.Double |
| ADS\_INTEGER = 11 | integer | DbType.Int32 | System.Int32 |
| ADS\_SHORTINT = 12 | short | DbType.Int16 | System.Int16 |
| ADS\_TIME = 13 | time | DbType.Time | System.TimeSpan |
| ADS\_TIMESTAMP = 14 | timestamp | DbType.DateTime | System.DateTime |
| ADS\_AUTOINC = 15\* | autoinc | DbType.Int32 | System.Int32 |
| ADS\_RAW = 16 | raw | DbType.Binary | System.Byte[] |
| ADS\_CURDOUBLE = 17 | curdouble | DbType.Double | System.Double |
| ADS\_MONEY = 18 | money | DbType.Currency | System.Decimal |
| ADS\_LONGINT = 19 | LongInt | DbType.Int64 | System.Int64 |
| ADS\_CISTRING = 20 | cichar | DbType.String | System.String |
| ADS\_ROWVERSION = 21 | rowversion | DbType.Int64 | System.Int64 |
| ADS\_MODTIME = 22 | modtime | DbType.DateTime | System.DateTime |
| ADS\_VARCHAR\_FOX = 23 | varchar | DbType.String | System.String |
| ADS\_VARBINARY\_FOX = 24 | varbinary | DbType.Binary | System.Byte[] |
| ADS\_NCHAR = 26 | nchar | DbType.String | System.String |
| ADS\_NVARCHAR = 27 | nvarchar | DbType.String | System.String |
| ADS\_NMEMO = 28 | nmemo | DbType.String | System.String |
| ADS\_GUID = 29 | GUID | DbType.GUID |  |

\* Advantage stores auto-increment values as unsigned 32-bit integers. However, for .NET Common Language Specification (CLS) compliance, the Advantage .NET Data Provider does not expose unsigned integers. As a result, it reports auto-increment values as signed 32-bit integers. If you have auto-increment values in your tables that exceed 2,147,483,647, you will need to cast the value as an unsigned 32-bit integer or retrieve them as 64-bit integers (e.g., [AdsDataReader.GetInt64](dotnet_adsdatareader_getint64.htm)).