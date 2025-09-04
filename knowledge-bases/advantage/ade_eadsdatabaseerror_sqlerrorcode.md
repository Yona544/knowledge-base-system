EADSDatabaseError.SQLErrorCode




Advantage Database Server 12  

EADSDatabaseError.SQLErrorCode

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EADSDatabaseError.SQLErrorCode  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - EADSDatabaseError.SQLErrorCode Advantage TDataSet Descendant ade\_Eadsdatabaseerror\_sqlerrorcode Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| EADSDatabaseError.SQLErrorCode  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.htm)

Native SQL Error code returned inside of the 7200 class error string.

Syntax

property SQLErrorCode : UNSIGNED32;

Description

Use SQLErrorCode for easy access to the native sql error code that is often embedded inside of the error string returned by SQL operations. If the error object in question was not raised by an SQL operation, the SQLErrorCode property will be zero.