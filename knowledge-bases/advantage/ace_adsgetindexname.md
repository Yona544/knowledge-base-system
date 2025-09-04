AdsGetIndexName




Advantage Database Server 12  

AdsGetIndexName

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetIndexName  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetIndexName Advantage Client Engine ace\_Adsgetindexname Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetIndexName  Advantage Client Engine |  |  |  |  |

Retrieves the name of the index order.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetIndexName (ADSHANDLE hIndex,  UNSIGNED8 \*pucName,  UNSIGNED16 \*pusLen); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order of interest. |
| pucName (O) | Return the name in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. If it is the handle of a tag from a compound index file, the tag name is returned. Otherwise the base filename of the NTX or IDX is returned. |

Remarks

For NTX and IDX files, this function will return the base of the filename (up to 8 characters). For CDX indexes, this function will return the tag name (up to 10 characters). For ADI indexes, this function will return the tag name (up to 128 characters).

Example

[Click Here](ace_examples.htm#adsgetindexnameexample)

See Also

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsGetIndexHandle](ace_adsgetindexhandle.htm)

[AdsGetIndexFilename](ace_adsgetindexfilename.htm)