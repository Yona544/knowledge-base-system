AdsServerTypes




Advantage Database Server 12  

TAdsDictionary.AdsServerTypes

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.AdsServerTypes  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.AdsServerTypes Advantage TDataSet Descendant ade\_Adsservertypes\_tadsdictionary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.AdsServerTypes  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Defines the Advantage server types to which this connection may attempt to connect.

Syntax

property AdsServerTypes : TAdsServerTypes;

 

TAdsServerTypes = set of TAdsServerType

TAdsServerType = ( stADS\_REMOTE, stADS\_LOCAL, stADS\_AIS )

Description

The Advantage server connection for this TAdsDictionary component will only attempt to use the server types indicated in the set.