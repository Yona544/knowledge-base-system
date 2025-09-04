Selecting Advantage Server Types via the TAdsConnection Component




Advantage Database Server 12  

Selecting Advantage Server types via the TAdsConnection Component

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Selecting Advantage Server types via the TAdsConnection Component  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Selecting Advantage Server types via the TAdsConnection Component Advantage TDataSet Descendant ade\_Selecting\_advantage\_server\_types\_via\_the\_tadsconnection\_component Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Selecting Advantage Server types via the TAdsConnection Component  Advantage TDataSet Descendant |  |  |  |  |

The AdsServerTypes property in the TAdsConnection component allows you to specify which Advantage server type(s) to use when activating that TAdsConnection component. To add a TAdsConnection component to your form and select Advantage server types:

|  |  |
| --- | --- |
| 1. | Click on the Advantage tab in the Delphi Component Palette. |

|  |  |
| --- | --- |
| 2. | Select the TAdsConnection component. |

|  |  |
| --- | --- |
| 3. | Select the AdsServerTypes property. |

Multiple AdsServerTypes sub-properties exist. stADS\_REMOTE refers to the Advantage Database Server, stADS\_AIS refers to the Advantage Internet Server, and stADS\_LOCAL refers to the Advantage Local Server. The default AdsServerTypes setting is stADS\_REMOTE set to True, stADS\_AIS set to True, and stADS\_LOCAL set to False. If multiple AdsServerTypes sub-properties are set to True, the application will attempt to connect to Advantage servers in the following order: stADS\_REMOTE first (if set to True), stADS\_AIS next (if set to True), and stADS\_LOCAL last (if set to True). If either the stADS\_REMOTE connect or the stADS\_AIS connect is successful, the stADS\_LOCAL connect will never be attempted.

Note This property overrides the TAdsSettings.AdsServerTypes value if the application has a TAdsSettings component. The Advantage server connection for this TAdsConnection component will only attempt to use the server types indicated in the set. If this set is empty, which is the default, the TAdsSettings.AdsServerTypes property set will be used.