EADSDatabaseError.TableName




Advantage Database Server 12  

EADSDatabaseError.TableName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EADSDatabaseError.TableName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - EADSDatabaseError.TableName Advantage TDataSet Descendant ade\_Eadsdatabaseerror\_tablename Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| EADSDatabaseError.TableName  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.htm)

The TableName property associated with the dataset that raised the exception.

Syntax

property TableName : STRING;

Description

TableName contains the TableName property of the dataset that raised the exception (e.g., demotable.adt). This string is equivalent to the TAdsDataSet.TableName property assigned to the dataset that raised the exception.

If the dataset was not available to the method raising the exception the TableName property will contain an empty string.

Note When using TAdsQuery this property will always contain an empty string.