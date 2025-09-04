EADSDatabaseError.DatabasePath




Advantage Database Server 12  

EADSDatabaseError.DatabasePath

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EADSDatabaseError.DatabasePath  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - EADSDatabaseError.DatabasePath Advantage TDataSet Descendant ade\_Eadsdatabaseerror\_databasepath Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| EADSDatabaseError.DatabasePath  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.htm)

Path to the table/connection associated with the dataset that raised the exception.

Syntax

property DatabasePath : STRING;

Description

DatabasePath contains the path to the table/connection that raised the exception. If the datasets DatabaseName property is a path this property is equivalent to the EADSDatabaseError.DatabaseName property. If the datasets DatabaseName property is either an alias or a TAdsConnection object this property will be the path associated with the alias or TAdsConnection.

If the dataset was not available to the method raising the exception the DatabasePath property will contain an empty string.