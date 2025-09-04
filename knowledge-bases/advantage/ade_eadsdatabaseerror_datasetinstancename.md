EADSDatabaseError.DataSetInstanceName




Advantage Database Server 12  

EADSDatabaseError.DataSetInstanceName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EADSDatabaseError.DataSetInstanceName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - EADSDatabaseError.DataSetInstanceName Advantage TDataSet Descendant ade\_Eadsdatabaseerror\_datasetinstancename Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| EADSDatabaseError.DataSetInstanceName  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.htm)

The name of the dataset that raised the exception.

Syntax

property DataSetInstanceName : STRING;

Description

DataSetInstanceName contains a string representation of the name of the dataset that raised the exception (e.g., AdsTable1). This string is equivalent to the TAdsDataSet.Name property assigned to the dataset that raised the exception.

If the name of the dataset was not available to the method raising the exception the DataSetInstanceName property will contain an empty string.