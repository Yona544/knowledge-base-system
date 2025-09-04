AdsShowError




Advantage Database Server 12  

AdsShowError

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsShowError  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsShowError Advantage Client Engine ace\_Adsshowerror Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsShowError  Advantage Client Engine |  |  |  |  |

Displays a message box for the last error (if there was one)

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsShowError (UNSIGNED8 \*pucTitle); |

Parameters

|  |  |
| --- | --- |
| pucTitle (I) | The title for the message box. Can be NULL. |

Remarks

AdsShowError will display a message box containing the last error message. The message displayed is identical to the error message available from [AdsGetErrorString](ace_adsgeterrorstring.htm). This function is useful during development or debugging to view error messages immediately after the error occurred.

Example

[Click Here](ace_examples.htm#adsshowerrorexample)

See Also

[AdsGetLastError](ace_adsgetlasterror.htm)

[AdsGetErrorString](ace_adsgeterrorstring.htm)