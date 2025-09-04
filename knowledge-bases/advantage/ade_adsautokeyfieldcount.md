AdsAutoKeyFieldCount




Advantage Database Server 12  

AdsTableOptions.AdsAutoKeyFieldCount

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsAutoKeyFieldCount  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsAutoKeyFieldCount Advantage TDataSet Descendant ade\_Adsautokeyfieldcount Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsAutoKeyFieldCount  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

When using ApplyRange or SetKey on a multi-field index, this property can be used to specify how the Advantage TDataSet Descendant determines which index segments to use.

Syntax

property AdsTableOptions.AdsAutoFieldCount

Description

In versions prior to 6.2, if a key segment was not specified, it simply was not used in the search. For example, if an index had a key expression of "lastname;firstname", and only the lastname was specified ("Smith", for example) for the search, then a partial key search would be done using only the lastname. This behavior has been changed to be the same as some TDataSet descendants, such as Paradox. Now the unspecified segment value will be set to NULL, so the search will now look for the key Smith;NULL.

The TDataSet property KeyFieldCount can be used to specify how many segments of a multi-segment key you want to be used in a seek/scope. See the Delphi documentation for KeyFieldCount information.

As an alternative, if you have an existing application and need it to work as older (pre 6.2) versions did, set the AdsAutoKeyFieldCount property to true. The default value for the AdsAutoKeyFieldCount property is false.