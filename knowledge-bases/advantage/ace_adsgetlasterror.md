AdsGetLastError




Advantage Database Server 12  

AdsGetLastError

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetLastError  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetLastError Advantage Client Engine ace\_Adsgetlasterror Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetLastError  Advantage Client Engine |  |  |  |  |

Retrieves the result of the last Advantage Client Engine function call

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetLastError (UNSIGNED32 \*pulErrCode,  UNSIGNED8 \*pucBuf,  UNSIGNED16 \*pusBufLen); |

Parameters

|  |  |
| --- | --- |
| pulErrCode (O) | Returns the error code of the last error. |
| pucBuf (O) | Returns the error string corresponding to pulErrCode. It will be similar to the string return by AdsGetErrorString but may have information specific to the error instance, such as table names. |
| pusBufLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

The error code returned by this function will be the same as the one returned by the last Advantage Client Engine function call. The first action of each Advantage Client Engine function is to clear the previous error if there is one. Thus, a call to AdsGetLastError is valid only for the most recent function call as opposed to the most recently occurring error. If no error occured on the last Advantage Client Engine function call, AE\_SUCCESS is returned in pulErrCode.

Example

[Click Here](ace_examples.htm#adsgetlasterrorexample)

See Also

[AdsGetErrorString](ace_adsgeterrorstring.htm)

[AdsShowError](ace_adsshowerror.htm)