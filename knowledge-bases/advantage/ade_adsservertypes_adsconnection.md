AdsServerTypes




Advantage Database Server 12  

TAdsConnection.AdsServerTypes

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.AdsServerTypes  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.AdsServerTypes Advantage TDataSet Descendant ade\_Adsservertypes\_adsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.AdsServerTypes  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Defines the Advantage server types to which this connection may attempt to connect.

Syntax

property AdsServerTypes : TAdsServerTypes;

 

TAdsServerTypes = set of TAdsServerType

TAdsServerType = ( stADS\_REMOTE, stADS\_LOCAL, stADS\_AIS )

Description

This property overrides the TAdsSettings.AdsServerTypes value if the application has a TAdsSettings component. The Advantage server connection for this TAdsConnection component will only attempt to use the server types indicated in the set. If this set is empty, the default, then the TAdsSettings.AdsServerTypes property set will be used.

See [TAdsSettings.AdsServerTypes](ade_adsservertypes_adssettings.htm) for a full explanation.