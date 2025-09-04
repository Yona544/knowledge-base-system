AdsGetTableOpenOptions




Advantage Database Server 12  

AdsGetTableOpenOptions

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetTableOpenOptions  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetTableOpenOptions Advantage Client Engine ace\_Adsgettableopenoptions Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetTableOpenOptions  Advantage Client Engine |  |  |  |  |

Retrieves the options used to open the table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetTableOpenOptions (ADSHANDLE hTable,  UNSIGNED32 \*pulOptions); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pulOptions (O) | A bit field of options with which the table was opened. |

Remarks

AdsGetTableOpenOptions will retrieve the option setting specified during the table open. Specific options can be determined by performing a bitwise "and" operation with a possible value to determine if the appropriate bit is set. For example, if ADS\_EXCLUSIVE was specified on an [AdsOpenTable](ace_adsopentable.htm) call, in the C programming language, ulOptions & ADS\_EXCLUSIVE will evaluate a non-zero value. In Visual Basic, ulOptions AND ADS\_EXCLUSIVE would be non-zero.

Example

[Click Here](ace_examples.htm#adsgettableopenoptionsexample)

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsCreateTable](ace_adscreatetable.htm)