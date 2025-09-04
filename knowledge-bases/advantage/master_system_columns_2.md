system.ansi\_columns




Advantage Database Server 12  

system.ansi\_columns

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| system.ansi\_columns  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - system.ansi\_columns Advantage SQL Engine master\_System\_columns\_2 Advantage SQL > System Views > Views > system.ansi\_columns / Dear Support Staff, |  |
| system.ansi\_columns  Advantage SQL Engine |  |  |  |  |

Contains one row for each field of a table in the database.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Field name. |
| Parent | Character | 200 | Table name the field belongs to. |
| Field\_Num | Integer | 4 | Position of the field in the table. |
| Field\_Type | ShortInt | 2 | Numeric representation of the field type. |
| Field\_Length | Integer | 4 | Size of the field in bytes. |
| Field\_Decimal | ShortInt | 2 | Precision of the field. |
| Field\_Min\_Value | Memo | variable | The minimum value for the field. |
| Field\_Max\_Value | Memo | variable | The maximum value for the field. |
| Field\_Can\_Be\_Null | Logical | 1 | Determines if a value must be specified for the field. |
| Field\_Default\_Value | Memo | variable | The expression used to generate a default value for the field. |
| Field\_Validation\_Msg | Memo | variable | Custom error message displayed when the field does not pass the assigned constraints. |
| Comment | Memo | variable | Description of the field. |
| User\_Defined\_Prop | Binary | variable | The user defined property. |
| Field\_Options | Integer | 4 | A bitmask of field options. Possible values include ADS\_DD\_FIELD\_OPT\_VFP\_BINARY (indicates it is a VFP field created with the NOCPTRANS option), and ADS\_DD\_FIELD\_OPT\_VFP\_NULLABLE (indicates it is a nullable VFP field). |

The following table lists values and their meanings for the Field\_Type column of system.columns.

|  |  |  |
| --- | --- | --- |
| Value | Field | Notes |
| 1 | Logical |  |
| 2 | Numeric |  |
| 3 | Date |  |
| 4 | String |  |
| 5 | Memo |  |
| 6 | Binary |  |
| 7 | Image |  |
| 8 | Varchar | Deprecated |
| 9 | Compactdate | Available only in DBF tables. |
| 10 | Double |  |
| 11 | Integer |  |
| 12 | ShortInt | Available only in ADT tables. |
| 13 | Time | Available only in ADT tables. |
| 14 | TimeStamp | Available only in ADT tables. |
| 15 | AutoInc | Available only in ADT tables. |
| 16 | Raw | Available only in ADT tables. |
| 17 | CurDouble | Available only in ADT tables. |
| 18 | Money | Available only in ADT tables. |
| 19 | LongInt | Available only in ADT tables. |
| 20 | CIString | Available only in ADT tables. |
| 21 | RowVersion | Available only in ADT tables. |
| 22 | ModTime | Available only in ADT tables. |

For more information about field types see [ADT Field Types and Specifications](master_adt_field_types_and_specifications.htm) or [DBF Field Types and Specifications](master_dbf_field_types_and_specifications.htm).