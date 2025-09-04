AdsGetDefault




Advantage Database Server 12  

AdsGetDefault

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetDefault  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetDefault Advantage Client Engine ace\_Adsgetdefault Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetDefault  Advantage Client Engine |  |  |  |  |

Retrieves the current default path

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetDefault (UNSIGNED8 \*pucDefault,  UNSIGNED16 \*pusLen); |

Parameters

|  |  |
| --- | --- |
| pucDefault (O) | Return the current default path in this buffer. |
| pusLen (I/O) | Length of buffer on input, length of data stored on output. |

Remarks

AdsGetDefault will return the current default path that has been set by [AdsSetDefault](ace_adssetdefault.htm). If no default path has been set, a string of length zero is returned.

AdsGetDefault is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.htm#adsgetdefaultexample)

See Also

[AdsSetDefault](ace_adssetdefault.htm)

[AdsSetSearchPath](ace_adssetsearchpath.htm)

[AdsOpenTable](ace_adsopentable.htm)

[AdsCreateTable](ace_adscreatetable.htm)