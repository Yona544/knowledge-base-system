EADSDatabaseError.DataSetInstanceOwner




Advantage Database Server 12  

EADSDatabaseError.DataSetInstanceOwner

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EADSDatabaseError.DataSetInstanceOwner  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - EADSDatabaseError.DataSetInstanceOwner Advantage TDataSet Descendant ade\_Eadsdatabaseerror\_datasetinstanceowner Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| EADSDatabaseError.DataSetInstanceOwner  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.htm)

String representation of the object owning the dataset that raised the exception.

Syntax

property DataSetInstanceOwner : STRING;

Description

DataSetInstanceOwner contains a string representation of the name of the owner of the dataset that raised the exception (e.g., Form1). This property can be utilized while debugging or in other instances where the name of the owning object could be helpful in determining which form or object owns the table raising the exception.

If the name of the datasets owner was not available to the method raising the exception the DataSetInstanceOwner property will contain an empty string.