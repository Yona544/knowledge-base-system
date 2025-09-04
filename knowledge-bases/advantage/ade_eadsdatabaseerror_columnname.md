EADSDatabaseError.ColumnName




Advantage Database Server 12  

EADSDatabaseError.ColumnName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EADSDatabaseError.ColumnName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - EADSDatabaseError.ColumnName Advantage TDataSet Descendant ade\_Eadsdatabaseerror\_columnname Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| EADSDatabaseError.ColumnName  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.htm)

The column name associated with a constraint error.

Syntax

property ColumnName : STRING;

Description

ColumnName contains the name of the offending field when the error raised is a constraint error.

Note If a custom validation message has been assigned, this property will be populated only if the column name appears as the first quoted string after the word column. For example, 'this is a custom message for column "lastname"' would correctly populate this property with the value "lastname".