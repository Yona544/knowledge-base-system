AdsGetIndexFilename




Advantage Database Server 12  

AdsGetIndexFilename

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetIndexFilename  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetIndexFilename Advantage Client Engine ace\_Adsgetindexfilename Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetIndexFilename  Advantage Client Engine |  |  |  |  |

Retrieves the full filename of this index order.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetIndexFilename (ADSHANDLE hIndex,  UNSIGNED16 usOption,  UNSIGNED8 \*pucName,  UNSIGNED16 \*pusLen); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order of interest (either of an index order from an NTX or IDX file or of a tag within a CDX or ADI). |
| usOption (I) | Specifies the portion of the filename desired. Valid option are ADS\_BASENAME (retrieve the name of the file without the extension), ADS\_BASENAMEANDEXT (retrieve the name of the file with the extension), ADS\_FULLPATHNAME (retrieve the fully qualified UNC filename). |
| pucName (O) | Return the name in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetIndexFilename returns the file name of the index file containing the indicated index order. If ADS\_FULLPATHNAME is given as the option, then the fully qualified UNC path name is returned regardless of how the file was opened. For example, even if the file was opened with a drive letter style path (e.g., f:\data\file.idx), a UNC filename will be returned by this routine (e.g., \\server\volume\data\file.idx). The UNC path can include connection path information such as the port number if it was included in the connection path.  Also note that if the connection path used a server-side alias, then that alias will be in the path as opposed to the actual folder on the server.

Example

[Click Here](ace_examples.htm#adsgetindexfilenameexample)

See Also

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsGetIndexName](ace_adsgetindexname.htm)

[AdsGetTableFilename](ace_adsgettablefilename.htm)