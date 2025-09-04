EADSDatabaseError.DatabaseName




Advantage Database Server 12  

EADSDatabaseError.DatabaseName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EADSDatabaseError.DatabaseName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - EADSDatabaseError.DatabaseName Advantage TDataSet Descendant ade\_Eadsdatabaseerror\_databasename Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| EADSDatabaseError.DatabaseName  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.htm)

The DatabaseName property associated with the dataset that raised the exception.

Syntax

property DatabaseName : STRING;

Description

DatabaseName contains the DatabaseName property of the dataset that raised the exception (e.g., DBDEMO). This string is equivalent to the TAdsDataSet.DatabaseName property assigned to the dataset that raised the exception.

If the DatabaseName property of the dataset is an alias or TAdsConnection object and path information is desired utilize the [DatabasePath](ade_eadsdatabaseerror_databasepath.htm) property.

If the dataset was not available to the method raising the exception the DatabaseName property will contain an empty string.