AdsGetErrorString




Advantage Database Server 12  

AdsGetErrorString

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetErrorString  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetErrorString Advantage Client Engine ace\_Adsgeterrorstring Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetErrorString  Advantage Client Engine |  |  |  |  |

Retrieves the error string for the given error code

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetErrorString (UNSIGNED32 ulErrCode,  UNSIGNED8 \*pucBuf,  UNSIGNED16 \*pusBufLen); |

Parameters

|  |  |
| --- | --- |
| ulErrCode (I) | An Advantage error code. |
| pucBuf (O) | Return the generic error string for ulErrCode. |
| pusBufLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetErrorString is used to retrieve the error string for a specific error code. Errors that occur in the Advantage Client Engine are 5000 class errors. There are also relevant error messages built into the Advantage Client Engine for server and communications layer errors. By calling AdsGetErrorString, [AdsShowError](ace_adsshowerror.htm), or [AdsGetLastError](ace_adsgetlasterror.htm) an application can display immediate information on failures that have occured.

[AdsGetLastError](ace_adsgetlasterror.htm) can also be used to return information about any valid Advantage error code. When used immediately after an Advantage Client Engine error occurs, additional error information will be returned.

Example

[Click Here](ace_examples.htm#adsgeterrorstringexample)

See Also

[AdsGetLastError](ace_adsgetlasterror.htm)

[AdsShowError](ace_adsshowerror.htm)