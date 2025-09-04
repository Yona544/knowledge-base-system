---
title: Master Selecting Advantage Server Types Via The Ads Ini File
slug: master_selecting_advantage_server_types_via_the_ads_ini_file
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_selecting_advantage_server_types_via_the_ads_ini_file.htm
source: Advantage CHM
tags:
  - master
checksum: 4fc11789b1104608ae13c7bb6ff02e6397fcbbe6
---

# Master Selecting Advantage Server Types Via The Ads Ini File

Selecting Advantage Server Types via the ADS.INI File

Selecting Advantage Server Types via the ADS.INI File

Advantage Concepts

| Selecting Advantage Server Types via the ADS.INI File  Advantage Concepts |  |  |  |  |

The ADS\_SERVER\_TYPE key in the ADS.INI file can be used to select the Advantage server type(s) to use when obtaining an Advantage server connection if the server type is not specified programmatically within the Advantage application. The available Advantage Server types are ADS\_REMOTE\_SERVER (Advantage Database Server), ADS\_AIS\_SERVER (Advantage Internet Server), and ADS\_LOCAL\_SERVER (Advantage Local Server). ADS\_REMOTE\_SERVER has the value 2, ADS\_AIS\_SERVER has the value 4, and ADS\_LOCAL\_SERVER has the value 1. For example, if you wanted your Advantage application to attempt to connect to all Advantage server types, if necessary, you need to set the value for the ADS\_SERVER\_TYPE key to 7 (1 + 2 + 4 = 7). The default ADS\_SERVER\_TYPE value is to use ADS\_REMOTE\_SERVER and ADS\_AIS\_SERVER, which are 6 (2 + 4 = 6). See [ads.ini File Support](master_ads_ini_file_support.md) for more information.

For more information on programmatically selecting the Advantage server type, that is, not using the ADS.INI setting, see the appropriate Help documentation for the following products:

Note Each Advantage product and their corresponding help files are installed separately. You need to only reference the Help file associated with the product that you have installed.

- Advantage TDataSet Descendant (ADE.HLP or ade.htm): See the topic Programmatically Selecting Advantage Server Types.

- Advantage OLE DB Provider (ADSOLEDB.HLP or adsoledb.htm): See the topic Programmatically Selecting Advantage Server Types.

- Advantage Client Engine (ACE.HLP or ace.htm): See the topic AdsSetServerType.

- Advantage CA-Visual Objects RDD (ADSVO.HLP): See the topic AX\_SetServerType.

- Advantage .NET Data Provider (ADS\_DOTNET.hlp): See the topic AdsConnection.ConnectionSting

Note The ADS\_SERVER\_TYPE value will only change the default Advantage server type setting. If your application programmatically changes the Advantage server type setting, it will override the ADS\_SERVER\_TYPE value in the ADS.INI file.

If the Advantage server types in which to connect are specified as either the Advantage Database Server or the Advantage Local Server, the Advantage application will first attempt to connect to the Advantage Database Server and then to the Advantage Local Server if the Advantage Database Server is not available. The very first connect attempt to the Advantage Database Server may take up to two seconds to time out if the Advantage Database Server is not available before automatically attempting to connect to the Advantage Local Server. The two second timeout will only occur if the Advantage Database Server is not present on the specified server and if the Advantage remote communication DLL (AXCWS32.DLL) is located in the client PC's search path. If the Advantage remote communication DLL is NOT located in the client PC's search path, the connection timeout to the Advantage Database Server will be immediate.
