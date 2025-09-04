Communications Compression




Advantage Database Server 12  

Communications Compression

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Communications Compression  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Communications Compression Advantage Concepts master\_Communications\_compression Advantage Concepts > Advantage Functionality > Communications Compression / Dear Support Staff, |  |
| Communications Compression  Advantage Concepts |  |  |  |  |

Overview

Advantage supports compression of communications between the client and the server when using the Advantage Database Server. Compression provides reduced network traffic at the expense of additional processing at the client and server. It can provide improved performance in low bandwidth situations and when the network is saturated.

By default, compression is turned on only for [Internet](master_advantage_internet_server_overview.htm) connections. Compression can significantly improve performance when using the Internet as the communications medium especially over connections involving low speed modems. Many modems have compression built into them, but it is not very effective when using Advantage communications [encryption](master_communications_encryption.htm). Data that has been encrypted has the "appearance" of random data with high entropy as far as compression algorithms are concerned, and thus does not compress well. When Advantage uses compression, it compresses the data prior to encryption when using the Advantage Internet Server.

The developer should probably test with and without compression turned on to determine if there is any performance improvement when using compression. When using slow PCs over a relatively fast network, compression can actually reduce performance. For example, in a specific test run using a slow client and server (e.g., 180 MHz) over a 10 Mbit network, compression reduced performance by about 5%. When testing faster PCs (e.g., 500 MHz) on a 10 Mbit network, compression improved performance by about 10%. In another test over a 28K modem, using compression improved performance by about 55%.

Compression Ratios

The compression factor is highly dependent on the type of data. For example, records from tables with large character fields may compress very well when sending them between the client and server. BLOB fields, however, that contain information such as JPEGs that have already been compressed will likely not compress any further. Typical compression ratios can range from 2:1 to 5:1.

Compression Settings

The settings to control the communications compression in Advantage exist at both the client and the server. Each of them has three settings: Internet, Always, and Never. The default setting is "Internet", which means that only ADS\_AIS\_SERVER (Advantage Internet Server) connections will use compression. The various settings provide the capability to turn compression on or off for specific connections, for specific workstations, or for all connections to a server. The sections following describe the how the various settings work together.

Server Settings

The server configuration setting is named COMPRESSION. See [Advantage Database Server Configuration](master_advantage_database_server_configuration_overview.htm) for information on how to configure Advantage Database Server for each operating system. For Windows, use the [Advantage Configuration Utility](master_advantage_configuration_utility_for_windows_nt_2000_2003.htm). For Linux, edit the ads.conf file.

Client Settings

The settings at the client have the same values as the server (Internet, Always, and Never). It is possible to specify the compression option in the ads.ini configuration file in order to control all connections from that workstation to any Advantage Database Server. See [ADS.INI File Support](master_ads_ini_file_support.htm) for information about the client-side configuration file. The option is named COMPRESSION and must be placed in the [SETTINGS] section of the file.

In addition, it is possible to specify the compression option for specific connections in the application itself. If the compression option is provided specifically for the connection, it overrides the setting in the ADS.INI file. The following is a summary of the methods to set the compression option for each client type.

|  |  |
| --- | --- |
| · | For Delphi applications, set the Compression property in the TAdsConnection component. |

|  |  |
| --- | --- |
| · | For applications using the Advantage Client Engine API, specify the option in the call to AdsConnect60 through the ulOptions parameter. |

|  |  |
| --- | --- |
| · | For OLE DB, specify the option in the connection string. For example, "COMPRESSION=Always". |

|  |  |
| --- | --- |
| · | For ODBC, use the ODBC Administrator to configure the Advantage data source and specify the Packet Compression option. |

|  |  |
| --- | --- |
| · | For DOS CA-Clipper applications using the Advantage RDDs, linking a compression-specific communications library into your application will turn on compression. Note that DOS CA-Clipper applications will not read the ADS.INI file. To use compression, use axscomc.lib instead of axscomm.lib, axsbcomc.lib instead of axsbcomm.lib, or axsxcomc.lib instead of axsxcomm.lib. |

|  |  |
| --- | --- |
| · | For DOS CA-Clipper applications using IP communications through ADSDOSIP, compression is performed by the 32-bit Windows communication DLL and is controlled by the ADS.INI COMPRESSION setting. |

|  |  |
| --- | --- |
| · | For FiveWin and Clip-4-Win applications, the 16-bit Windows DLL communications libraries adsip16.dll and adsipx16.dll perform the compression and are controlled by the ADS.INI COMPRESSION setting. |

Compression Combinations

The variety of methods of setting the compression option provides for several scenarios. It is possible, for example, to turn on compression for all applications running on a single workstation by setting the COMPRESSION=Always option in the [ADS.INI file](master_ads_ini_file_support.htm). Alternatively, an application can specifically turn compression on or off for individual connections via the client-specific connection option. In addition, it is possible to turn on compression at the server (for all connections) for cases where Advantage Database Server might be handling connections over a particularly congested network.

The following table indicates whether compression is on or off for each setting combination. Note that Advantage Local Server connections are not included. Compression is not applicable with local server. Also note that this does not apply to older clients (prior to version 7.0) that do not support compression.

Server Compression Setting

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | Internet | Always | Never |
| Client Compression Setting | Internet | ON for AIS  OFF for REMOTE | ON for all connections | OFF for all connections |
| Always | ON for all connections | ON for all connections | OFF for all connections |
| Never | OFF for all connections | OFF for all connections | OFF for all connections |
|  |  |  |  |  |

ON = Compression Enabled

OFF = Compression Disabled