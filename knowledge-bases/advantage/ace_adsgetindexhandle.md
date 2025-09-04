AdsGetIndexHandle




Advantage Database Server 12  

AdsGetIndexHandle

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetIndexHandle  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetIndexHandle Advantage Client Engine ace\_Adsgetindexhandle Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetIndexHandle  Advantage Client Engine |  |  |  |  |

Retrieves the handle of an index order given the index order name.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetIndexHandle (ADSHANDLE hTable,  UNSIGNED8 \*pucIndexOrder,  ADSHANDLE \*phIndex); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucIndexOrder (I) | Name of index order for which to search. |
| phIndex (O) | Return index order handle corresponding to given name. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_INDEX\_ORDER\_NAME | The index order name given is invalid. |

Remarks

For non-compound indexes, the index order name is the base of the filename (up to 8 characters). For compound indexes, the index order name is the tag name (up to 10 characters).

If there is more than one index order open with the same name, the Advantage Client Engine will return the first one it finds.

Example

[Click Here](ace_examples.htm#adsgetindexhandleexample)

See Also

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsGetIndexName](ace_adsgetindexname.htm)