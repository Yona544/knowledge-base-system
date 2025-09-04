AdsGetSearchPath




Advantage Database Server 12  

AdsGetSearchPath

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetSearchPath  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetSearchPath Advantage Client Engine ace\_Adsgetsearchpath Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetSearchPath  Advantage Client Engine |  |  |  |  |

Retrieves the current search path

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetSearchPath (UNSIGNED8 \*pucPath,  UNSIGNED16 \*pusLen); |

Parameters

|  |  |
| --- | --- |
| pucPath (O) | Return the search path in this buffer. |
| pusLen (I/O) | Length of buffer on input, length of search path on output. |

Remarks

AdsGetSearchPath retrieves the current search path in the supplied buffer. If the search path has not been set, a string of length zero is returned.

AdsGetSearchPath is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.htm#adsgetsearchpathexample)

See Also

[AdsSetSearchPath](ace_adssetsearchpath.htm)

[AdsSetDefault](ace_adssetdefault.htm)

[AdsOpenTable](ace_adsopentable.htm)

[AdsCreateTable](ace_adscreatetable.htm)

[AdsGetTableHandle](ace_adsgettablehandle.htm)