AdsNullTerminateStrings




Advantage Database Server 12  

AdsNullTerminateStrings

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsNullTerminateStrings  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsNullTerminateStrings Advantage Client Engine ace\_Adsnullterminatestrings Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsNullTerminateStrings  Advantage Client Engine |  |  |  |  |

This API is no longer supported.  It returns error code 5120 (AE\_OBSOLETE\_FUNCTION) and does nothing else.

The original purpose of this function was to allow an application to change the behavior of the Advantage Client Engine API with respect to string values returned. If called with a parameter of FALSE, it would cause APIs that returned string data (e.g., AdsGetString) to not null terminate the output string. This option is no longer available. The behavior now is to always null terminate those types of strings (which was the original default behavior).