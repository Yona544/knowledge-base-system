AdsGetKeyCount




Advantage Database Server 12  

AdsGetKeyCount

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetKeyCount  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetKeyCount Advantage Client Engine ace\_Adsgetkeycount Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetKeyCount  Advantage Client Engine |  |  |  |  |

Retrieves the number of keys in the given index.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetKeyCount (ADSHANDLE hIndex,  UNSIGNED16 usFilterOption,  UNSIGNED32 \*pulCount); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order. |
| usFilterOption (I) | Indicates if filters and/or scopes are to be respected if they are set. Options are ADS\_RESPECTFILTERS, ADS\_IGNOREFILTERS, and ADS\_RESPECTSCOPES. Using ADS\_RESPECTFILTERS respects filters and scopes. Using ADS\_RESPECTSCOPES respects scopes only. Using ADS\_IGNOREFILTERS will ignore filters and scopes. |
| pulCount (O) | Return number of keys in the index. |

Remarks

There may not be the same number of records referenced in an index as in the associated table if the index order is a conditional index or a custom index.

If usFilterOption contains ADS\_IGNOREFILTERS or ADS\_RESPECTSCOPES, this function should return fairly quickly and provide good performance if the index is not large. If the index is large, this function could take some time to complete because the index keys are literally counted.

If usFilterOption contains ADS\_RESPECTFILTERS, the Advantage Client Engine must skip through all records referenced by keys in the index that pass the filter and scope and count them. Thus, with large indexes where many records pass the filter and/or keys pass the scope, this function can be very slow.

Note This function works identically to [AdsGetRecordCount](ace_adsgetrecordcount.htm) when an index handle is passed to AdsGetRecordCount.

Example

[Click Here](ace_examples.htm#adsgetkeycountexample)

See Also

[AdsGetRecordCount](ace_adsgetrecordcount.htm)