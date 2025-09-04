Selecting Advantage Server Types via the TAdsSettings Component




Advantage Database Server 12  

Selecting Advantage Server Types via the TAdsSettings Component

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Selecting Advantage Server Types via the TAdsSettings Component  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Selecting Advantage Server Types via the TAdsSettings Component Advantage TDataSet Descendant ade\_Selecting\_advantage\_server\_types\_via\_the\_tadssettings\_component Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Selecting Advantage Server Types via the TAdsSettings Component  Advantage TDataSet Descendant |  |  |  |  |

The AdsServerTypes property in the TAdsSettings component allows you to specify which Advantage server type(s) to use when obtaining an Advantage server connection and not using a TAdsConnection component and specifying the server types in that TAdsConnection component. To add a TAdsSettings component to your form and select Advantage server types:

|  |  |
| --- | --- |
| 1. | Click on the Advantage tab in the Delphi Component Palette. |

|  |  |
| --- | --- |
| 2. | Select the TAdsSettings component. |

|  |  |
| --- | --- |
| 3. | Select the AdsServerTypes property. |

Multiple AdsServerTypes sub-properties exist. stADS\_REMOTE refers to the Advantage Database Server, stADS\_AIS refers to the Advantage Internet Server, and stADS\_LOCAL refers to the Advantage Local Server. The default AdsServerTypes setting is stADS\_REMOTE set to True, stADS\_AIS set to True, and stADS\_LOCAL set to False. If multiple AdsServerTypes sub-properties are set to True, the application will attempt to connect to Advantage servers in the following order: stADS\_REMOTE first (if set to True), stADS\_AIS next (if set to True), and stADS\_LOCAL last (if set to True). If either the stADS\_REMOTE connect or the stADS\_AIS connect is successful, the stADS\_LOCAL connect will never be attempted.

Note Changing the AdsServerTypes property will affect all subsequent Advantage server connection attempts that are not associated with a TAdsConnection component where the server types are specified in the TAdsConnection.AdsServerTypes property. Existing connections to Advantage servers will not be affected by a change to the AdsServerTypes properties.