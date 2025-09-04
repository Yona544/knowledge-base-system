AdsClearProgressCallback




Advantage Database Server 12  

AdsClearProgressCallback

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsClearProgressCallback  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsClearProgressCallback Advantage Client Engine ace\_Adsclearprogresscallback Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsClearProgressCallback  Advantage Client Engine |  |  |  |  |

Clears the progress callback registered using AdsRegisterProgressCallback.

Note This API still functions as before, but is now obsolete. It is suggested you use [AdsRegisterCallbackFunction](ace_adsregistercallbackfunction.htm) and [AdsClearCallbackFunction](ace_adsclearcallbackfunction.htm) instead, as they work better with threads and have more complete functionality.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsClearProgressCallback (); |

Parameters

None.

Remarks

AdsClearProgressCallback will make the Advantage Client Engine stop calling the registered callback function. The progress callback is used to indicate progress while an Advantage server is building an index.

Example

[Click Here](ace_examples.htm#adsclearprogresscallbackexample)

See Also

[AdsRegisterCallbackFunction](ace_adsregistercallbackfunction.htm)

[AdsClearCallbackFunction](ace_adsclearcallbackfunction.htm)

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsReindex](ace_adsreindex.htm)