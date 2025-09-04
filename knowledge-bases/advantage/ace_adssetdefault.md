AdsSetDefault




Advantage Database Server 12  

AdsSetDefault

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetDefault  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetDefault Advantage Client Engine ace\_Adssetdefault Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetDefault  Advantage Client Engine |  |  |  |  |

Sets the default search directory for opening and creating tables

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetDefault (UNSIGNED8 \*pucDefault); |

Parameters

|  |  |
| --- | --- |
| pucDefault (I) | Default directory. Can be in the form of drive letter and path (f:\path) or UNC (\\server\vol\path). If an empty or NULL string is given, then the default path is cleared. |

Remarks

If a path is given, then subsequent AdsCreateTable or AdsOpenTable calls will look first in the given path (if no path is provided with the table name). This setting affects open/creation of indexes in the same manner. AdsSetDefault does not result in a connection to the server, nor does this routine verify the existence of the server on the given path.

The default path is used for path resolution when opening and creating tables. If an application creates or opens a table (AdsOpenTable), and it does not supply a path with the table name, then the default path is used as the path for opening the table. If the table name has no path, no default path, or no search path (see [AdsSetSearchPath](ace_adssetsearchpath.htm)), then the current working directory of the application is used. Only a single path can be used.

AdsSetDefault is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.htm#adssetdefaultexample)

See Also

[AdsGetDefault](ace_adsgetdefault.htm)

[AdsSetSearchPath](ace_adssetsearchpath.htm)

[AdsOpenTable](ace_adsopentable.htm)

[AdsCreateTable](ace_adscreatetable.htm)

[AdsGetTableHandle](ace_adsgettablehandle.htm)