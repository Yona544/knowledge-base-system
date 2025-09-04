AdsIsIndexCompound




Advantage Database Server 12  

AdsIsIndexCompound

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsIndexCompound  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsIndexCompound Advantage Client Engine ace\_Adsisindexcompound Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsIndexCompound  Advantage Client Engine |  |  |  |  |

Determines if the given index order is from a compound index file.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsIndexCompound (ADSHANDLE hIndex,  UNSIGNED16 \*pbCompound); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order of interest. |
| pbCompound (O) | Returns True if index order is from a compound index file. |

Remarks

AdsIsIndexCompound will return True only if the index order specified is in a compound index file (a Foxpro-compatible CDX file or Advantage proprietary ADI file). Indexes built with NTX and FoxPro-compatible IDX files are not compound indexes.

Example

[Click Here](ace_examples.htm#adsisindexcompoundexample)

See Also

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsCreateIndex](ace_adscreateindex.htm)