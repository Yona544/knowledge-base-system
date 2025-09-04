AdsGetTableAlias




Advantage Database Server 12  

AdsGetTableAlias

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetTableAlias  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetTableAlias Advantage Client Engine ace\_Adsgettablealias Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetTableAlias  Advantage Client Engine |  |  |  |  |

Retrieves the alias associated with the given table handle

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetTableAlias (ADSHANDLE hTable,  UNSIGNED8 \*pucAlias,  UNSIGNED16 \*pusLen); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucAlias (O) | Return the alias in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetTableAlias retrieves the alias associated with the table during the open or create. If no alias was specified when the table was opened, the Advantage Client Engine generates the alias from the base filename of the table.

If the table in question is in an Advantage Data Dictionary, AdsGetTableAlias will return the name of the table object in the dictionary.

Example

[Click Here](ace_examples.htm#adsgettablealiasexample)

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsCreateTable](ace_adscreatetable.htm)

[AdsGetTableFilename](ace_adsgettablefilename.htm)

[AdsGetTableHandle](ace_adsgettablehandle.htm)