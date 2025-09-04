EADSDatabaseError.Create




Advantage Database Server 12  

EADSDatabaseError.Create

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EADSDatabaseError.Create  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - EADSDatabaseError.Create Advantage TDataSet Descendant ade\_Eadsdatabaseerror\_create Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| EADSDatabaseError.Create  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.htm)

Creates an instance of an EADSDatabaseError exception.

Syntax

constructor Create( oDataSet : TAdsDataSet;

ulErrCode : UNSIGNED32;

const strMsg : STRING );

Description

Call Create to construct an exception with an error string and extended [EADSDatabaseError Properties](ade_eadsdatabaseerror_properties.htm).

oDataSet is a pointer to the dataset generating the exception. If the dataset is not available pass this parameter as nil and the extended [EADSDatabaseError Properties](ade_eadsdatabaseerror_properties.htm) will remain empty.

ulErrCode is the Advantage Client Engine (ACE) error code to be associated with this exception.

strMsg is the runtime error message to display, and is also used to fill the EADSDatabaseError.Message property.