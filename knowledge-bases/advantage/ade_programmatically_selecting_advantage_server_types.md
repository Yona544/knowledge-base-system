Programmatically Selecting Advantage Server Types




Advantage Database Server 12  

Programmatically Selecting Advantage Server Types

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Programmatically Selecting Advantage Server Types  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Programmatically Selecting Advantage Server Types Advantage TDataSet Descendant ade\_Programmatically\_selecting\_advantage\_server\_types Advantage TDataSet Descendant > Developing and Distributing Applications > Programmatically Selecting Advantage Server Types / Dear Support Staff, |  |
| Programmatically Selecting Advantage Server Types  Advantage TDataSet Descendant |  |  |  |  |

Advantage server types can be selected programmatically using one of three methods:

|  |  |
| --- | --- |
| · | Setting the TAdsConnection component's AdsServerTypes property: |

[Selecting Advantage Server Types via the TAdsConnection Component](ade_selecting_advantage_server_types_via_the_tadsconnection_component.htm)

|  |  |
| --- | --- |
| · | Setting the TAdsSettings component's [AdsServerTypes](ade_adsservertypes_adssettings.htm) property: |

[Selecting Advantage Server Types via the TAdsSettings Component](ade_selecting_advantage_server_types_via_the_tadssettings_component.htm)

|  |  |
| --- | --- |
| · | Setting the value for the ADS\_SERVER\_TYPE key in the ads.ini file: |

[Selecting Advantage Server Types via the ADS.INI File](master_selecting_advantage_server_types_via_the_ads_ini_file.htm)

The ADS\_SERVER\_TYPE setting in the ads.ini will only be used if a TAdsConnection or TAdsSettings component is not used in the application.