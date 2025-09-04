---
title: Master Ads Ini File Support
slug: master_ads_ini_file_support
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_ads_ini_file_support.htm
source: Advantage CHM
tags:
  - master
checksum: 8e4b1ca8e5bed6898f96936c5992ec1289b9d1d8
---

# Master Ads Ini File Support

ADS.INI File Support

ads.ini File Support

Advantage Concepts

| ads.ini File Support  Advantage Concepts |  |  |  |  |

All Advantage clients based on the Advantage Client Engine can use an initialization file, ads.ini, to override specific default settings such as the Advantage server type. The Advantage JDBC Driver and the Advantage CA-Clipper RDDs do not use the ads.ini file.

The Advantage TDataSet Descendant supports database aliases that are defined in the ads.ini files. See the topic, Database Aliases and the ads.ini File in the Advantage TDataSet Descendant Help documentation (ADE.HLP or ade.htm) for more information. (Note that each of the Advantage products and their corresponding Help files are installed separately.)

Windows

In order for the ads.ini file to be used, it must be located in the application directory, the Windows directory, the Windows System directory, or the client's search path.

In addition, if an environment variable exists with the name adsini\_path, that path will be used to locate the ads.ini file. This can be helpful when you do not want to modify the applications search path, but still need the ads.ini file to exist in a directory multiple users have rights to (for example on Windows Vista installations). An application can often set the environment variable at run-time before calling any Advantage functions, which avoids the need to set a per-workstation environment variable.

Linux

In order for the ads.ini file to be used, it must be located in the application directory, a directory specified in an environment variable named ADSPATH, in the users home directory, or in the /etc directory. If located in the users home directory the ads.ini file should be named .ads.ini (note the initial "dot").

The following entries can be added to the ads.ini file.

ADS\_SERVER\_TYPE

This setting changes the default Advantage server type(s) to which an Advantage Windows client will connect if the server type is not specified in the Advantage application. The ADS\_SERVER\_TYPE setting must exist within a section titled "[SETTINGS]".

The ways to specify the Advantage server type in an application include:

- Using the AdsSetServerType function with the Advantage Client Engine API or the Advantage CA-Visual Objects RDDs.

- Using the TAdsSettings.AdsServerTypes or TAdsConnection.AdsServerTypes properties with the Advantage TDataSet Descendant.

- Using the ServerTypes property in the ADO connection string, the OLE DB Provider String, or the ADSPROP\_INIT\_SERVER\_TYPE property.

The available Advantage Server types are ADS\_REMOTE\_SERVER (which is the Advantage Database Server), ADS\_AIS\_SERVER (which is the Advantage Internet Server), and ADS\_LOCAL\_SERVER (which is the Advantage Local Server). These Advantage Server type constants are defined in the ACE.H and ACE.PAS files. ADS\_REMOTE\_SERVER has the value 2, ADS\_AIS\_SERVER has the value 4, and ADS\_LOCAL\_SERVER has the value 1. The default Advantage Server types in which to connect are ADS\_REMOTE\_SERVER and ADS\_AIS\_SERVER. Therefore, the default value for the ads.ini ADS\_SERVER\_TYPE setting is 6 (2 + 4 = 6). For example, if you wanted your Advantage application to attempt to connect to all Advantage server types, if necessary, you need to set the value for the ADS\_SERVER\_TYPE key to 7 (1 + 2 + 4 = 7). It would look like this:

[SETTINGS]

ADS\_SERVER\_TYPE = 7

Note The ADS\_SERVER\_TYPE entry will only change the default Advantage Server type setting. If your application programmatically changes the Advantage Server type setting, it will override this setting in the ads.ini file.

If the Advantage server types in which to connect are specified as either the Advantage Database Server or the Advantage Local Server, the Advantage application will first attempt to connect to the Advantage Database Server and then to the Advantage Local Server if the Advantage Database Server is not available. The very first connect attempt to the Advantage Database Server may take up to two seconds to time out if the Advantage Database Server is not available before automatically attempting to connect to the Advantage Local Server. The two-second timeout will only occur if the Advantage Database Server is not present on the specified server and if the Advantage remote communication DLL (AXCWS32.DLL) exists. If the Advantage remote communication DLL is NOT located in the application directory, the Windows directory, the Windows System directory, or the client PC's search path, the connection timeout to the Advantage Database Server will be immediate.

ADS\_FORCE\_CLIPPER\_MEMOS

This setting will force the CA-Clipper style carriage return linefeed character pairs (0x8D 0x0A) to be stripped from any memo fields that are read. The ADS\_FORCE\_CLIPPER\_MEMOS setting must exist within a section titled "[SETTINGS]". If this ADS\_FORCE\_CLIPPER\_MEMOS entry is specified and set to zero, the character pairs will not be stripped from memos in tables opened directly by the Advantage Client Engine (that is, not those opened by an SQL statement). If this ADS\_FORCE\_CLIPPER\_MEMOS entry is specified and set to a non-zero value, all character pairs will be stripped from memos in tables opened directly by the Advantage Client Engine (that is, not those opened by an SQL statement). For example, to force all future table opens to strip the carriage return line feed pairs from memos, you need to create an ads.ini file that contains the entry:

[SETTINGS]

ADS\_FORCE\_CLIPPER\_MEMOS = 1

DEFAULT\_PROTOCOL

This setting changes the default network protocol to use for communication between the Advantage client and the Advantage Database Server. The DEFAULT\_PROTOCOL setting must exist within a section titled "[SETTINGS]". Advantage auto-senses what communication protocols (IP or IPX) are available on the client and the server that can be used for communication between the client and server. If only IP is available on both ends, Advantage will use IP. If only IPX is available on both ends, Advantage will use IPX. If both protocols are available on both ends, it depends upon how the DEFAULT\_PROTOCOL is set. If it's not specified at all in ads.ini, Advantage will use IP. If it's specified and set to 1 in ads.ini, Advantage will use IPX. If it's specified and set to any other value (other than 1) in ads.ini Advantage will use IP.

In order for an Advantage application to use IPX as the default protocol, you need to create an ads.ini file that contains the entry:

[SETTINGS]

DEFAULT\_PROTOCOL = 1

RETRY\_ADS\_CONNECTS

This setting controls the functionality associated with the Advantage Database Server connection errors being cached. The RETRY\_ADS\_CONNECTS setting must exist within a section titled "[SETTINGS]". By default, the Advantage Client Engine caches certain errors that are generated during attempts to connect to the Advantage Database Server. This allows future connection attempts to avoid some of the timeout periods associated with the Advantage Database Server discovery process. For example, if a connection to the Advantage Database Server fails, all future connection attempts to that server from a particular client will immediately return the same error code.

It can take several seconds for the client to determine that the Advantage Database Server is not available on a specified server. By saving the server name and error code related with a failed connection attempt to an Advantage Database Server, the application only has to attempt to connect one time. All future "ADS\_REMOTE" connection attempts will fail immediately rather than possibly waiting several seconds each. This is particularly useful if you distribute an application that scales to the Advantage Local Server if the Advantage Database Server is not available.

By setting the value to 1, every "ADS\_REMOTE" connection attempt to a server will look for the Advantage Database Server regardless of the success of past connection attempts. If you want your application to check for the Advantage Database Server each time it attempts an "ADS\_REMOTE" connection, you need to create an ads.ini file with the following entry:

[SETTINGS]

RETRY\_ADS\_CONNECTS = 1

The default for this setting is 0.

Note RETRY\_ADS\_CONNECTS was designed such that modifying the ads.ini file programmatically will change the connection behavior for the next connection made.

MAX\_CONNECTIONS

This setting changes the default maximum number of Advantage Database Server connections. The MAX\_CONNECTIONS setting must exist within a section titled "[SETTINGS]". By default, an application can get a maximum of 50 connections to one or more Advantage Database Servers. If an application attempts to get more than 50 connections, a 6303 error will result. To change the maximum value, modify or add the MAX\_CONNECTIONS parameter under the SETTINGS section in the ads.ini file. An example ads.ini file with the maximum connections set to 100 looks like:

[SETTINGS]

MAX\_CONNECTIONS =100

MAX\_TIMEOUTS

The Max Timeouts setting specifies the maximum number of times the client will attempt to communicate with the Advantage Database Server. The MAX\_TIMEOUTS setting must exist within a section titled "[SETTINGS]". This setting should only need to be increased when a slow network is causing a 6610 error, which indicates the Advantage Database Server did not respond to a client request in a timely manner. In this case, this setting should probably be used in conjunction with the server setting of Partial Connection Timeout.

The actual duration of the timeout period can very depending on network speeds. On a faster network, the total timeout period may be shorter. In general, the default value of 30 will result in a timeout period of approximately 15 seconds.

[SETTINGS]

// A Default value of 30 is used if this is 0 or not specified

// The following example setting specifies that the client will retry communicating with the

// server 40 times before returning a timeout error.

MAX\_TIMEOUTS=40

PACKET\_SIZE

The PACKET\_SIZE setting must exist within a section titled "[SETTINGS]". The default protocol packet size is determined by which protocol is being used by the Advantage communication layer. For IPX packets, the default packet size is 576 bytes. For IP, the default and maximum packet size is 1450 bytes. This setting may be used to further restrict the size of the network packet that is used while communicating with the Advantage Database Server. For example, if a router is fragmenting packets artificially, this setting can eliminate that problem by reducing the packet size. It is recommended to not use this setting unless needed.

[SETTINGS]

; This will change the packet size to 512 bytes. Adjusting this size is not recommended unless you are sure it will help performance.

PACKET\_SIZE=512

RECORD\_CACHE\_SIZE

This ads.ini setting is applicable to the Advantage OLE DB Provider only. The RECORD\_CACHE\_SIZE setting must exist within a section titled "[SETTINGS]". By default, the Advantage OLE DB Provider performs some caching of records as it reads them to reduce network traffic. By default, the cache size for each rowset is 1 Megabyte. You can change the cache size through this RECORD\_CACHE\_SIZE entry. It specifies the cache size in bytes. For example, the following would set the cache size to 2 Megabytes:

[SETTINGS]

RECORD\_CACHE\_SIZE=2097152

The amount of cache required for each record is the record length plus 4. If you do not want a cache to be maintained, you can set the value to 0 to turn it off. Note that the cache is allocated as needed up to the specified limit. Thus, if you set a cache size of 4 Megabytes, for example, it will only allocate that much memory if enough records are read to fill the cache. In addition, if the cache is ever exceeded for a given rowset, the cache is eliminated for that rowset instance to avoid the cost of maintaining the cache with little chance of benefiting from future cache hits.

The record cache is primarily intended to speed up performance of applications that are oriented mainly toward user interaction. For example, data bound grids can be highly network intensive because of the number of record requests they make. If the record cache is available, it can reduce the number of network requests and improve grid response time. Note that this record caching is unrelated to the client-side caching performed by ADO when client-side cursors (adUseClient) are used. With ADO's client-side cursors, the entire rowset is read from the server as soon as the rowset as opened. After it has opened the rowset and read the data, ADO does not make further requests to read data from the provider. Once the data has been read, the client-side cursor is very fast. The drawback is the initial time to read the rowset. The record caching provided by the Advantage OLE DB Provider, on the other hand, caches the records on demand, so there is no initial penalty although it can ultimately result in more network traffic in the long run depending on the type of data bound controls used and operations performed.

If an application uses client-side cursors entirely, then it may make sense to turn off the Advantage OLE DB record caching for a slight performance gain. In addition, an application that is highly geared toward batch processing may not benefit from the record caching.

[DRIVES]

If you wish to connect to the Advantage Database Server via the Advantage Internet Server, and your application uses drive letters, you will need a [DRIVES] section to contain the information needed for an Internet connection to Advantage. The [DRIVES] section should contain a list of all drive letters used by the application and the server name and share (or volume) in which the drive letter should map on the server in which the Advantage Database Server is running. The server name and share (or volume) should be UNC (\\SERVERNAME\SHARE).

In rare cases, it might also be desirable to use the [DRIVES] section when making a standard LAN connection (as opposed to an Advantage Internet Server connection). In these situations it is possible to use the [DRIVES] section to define virtual drive letters.

Following is an example of an application that uses the drive letters Q and R:

[DRIVES]

Q:=\\Server1\datashare

R:=\\Server2\volume1

INTERNET\_IP/INTERNET\_PORT

The INTERNET\_IP/INTERNET\_PORT settings specify the server IP address or DNS name and port information needed for Internet connections if you wish to connect to the Advantage Database Server via the Advantage Internet Server. The INTERNET\_IP and INTERNET\_PORT settings must exist within a section titled "[<SERVER\_NAME>]", where <SERVER\_NAME> is the name of the server upon which the Advantage Database Server is running. The INTERNET\_IP setting should contain the IP address or DNS name and the INTERNET\_PORT setting the IP port number. Below are two examples of the IP address and port information for a server named SERVER1 upon which the Advantage Database Server is running:

A static IP example would be:

[SERVER1]

INTERNET\_IP=144.233.44.91

INTERNET\_PORT=2001

A DNS example would be:

[SERVER1]

INTERNET\_IP=server1.mycompany.com

INTERNET\_PORT=2001

Make sure the INTERNET\_IP address is a static IP address or a resolvable domain name of the server in which the Advantage Database Server is running. Make sure the INTERNET\_PORT number is the same number used on the server. See [IP Port](master_ip_port.md).

LAN\_IP/LAN\_PORT

The IP address and port of the server on which the Advantage Database Server is running can be specified in the ads.ini file. The LAN\_IP and LAN\_PORT settings must exist within a section titled "[<SERVER\_NAME>]", where <SERVER\_NAME> is the name of the server upon which the Advantage Database Server is running. Each server that the Advantage client wishes to connect to can have a section specifying the IP address and port. When an IP address and port of the server on which the Advantage Database Server is running is specified, the Advantage client will use these settings and will not try any other methods to "discover" the Advantage Database Server. If the Advantage Database Server is not found at the specified IP address and port, a 6097 error (Bad IP address specified in connection path or in ads.ini file) will occur.

In order to use this setting, the IP port that the Advantage Database Server uses must be specified within the Advantage Database Server configuration information. See the IP Port topic in the Advantage Database Server Help (ADS.HLP) for more information. (Note that each of the Advantage products and their corresponding Help files are installed separately.)

The LAN\_IP setting should contain the IP address and the LAN\_PORT setting the IP port number. Below is an example of the IP address and port information for a server named MYSERVER upon which the Advantage Database Server is running:

[MYSERVER]

LAN\_IP=155.690.41.69

LAN\_PORT=2069

Note These settings should only be used over a LAN/WAN. The settings should not be used over the Internet since no security checks (authentication, encryption, etc.) are performed. See [Advantage Internet Server](master_advantage_internet_server.md) for information about connecting to the Advantage Database Server over the Internet.

 

Note As an alternative to using these settings, it is possible to specify the server name and port number or IP address and port number directly in the connection string (e.g., \\myserver:2000\path, or \\1.2.3.4:2000\path). If the server name and port are given in the connection string, a DNS lookup is used to find the IP address.

REPLACE\_UNC\_SERVER

This setting is used by the Advantage Local Server for Linux to resolve UNC server names into direct paths. For example, if you have a remote Linux machine mounted at "/mnt/MyOtherServer", you could put the following entry into the ads.ini file:

[REPLACE\_UNC\_SERVER]

scooby=/mnt/MyOtherServer

Connect and open data on scooby using the connection string "\\scooby\path". Advantage will automatically convert the connection string "\\scooby\path" into "/mnt/MyOtherServer/path" before attempting to open any files.

COMPRESSION

This setting controls communications compression between the client and Advantage Database Server. The setting specified here will be used only if the connect request from the client did not specify one of the options. The client-specified connection parameters override this setting if they are given. The valid values for this setting are "Internet", "Always", and "Never". The default is "Internet". If "Internet" is specified, then connections of type ADS\_AIS\_SERVER will use compression unless Advantage Database Server is configured to not use compression (link to the above ADS compression setting). If "Always" is specified, then all connections will use compression unless it is turned off at the server. If "Never" is specified, then no connections from this workstation will use compression. The following is an example ADS.INI entry to show how to change the default compression setting from "Internet" to "Always".

[SETTINGS]

; Turn compression on for all connections from this workstation.

COMPRESSION=Always

USE\_TCP\_IP

This setting controls the communication protocol between the client and Advantage Database Server. The setting specified here will be used only if the connect request from the client did not specify a communication type. The client-specified connection parameter overrides this setting if they are given. Setting this value to 1 will force the client to use the TCP/IP protocol when communicating with the server.

USE\_TLS

This setting controls the communication protocol between the client and Advantage Database Server. The client-specified connection parameter overrides this setting if they are given. Setting this value to 1 will force the client to use [Transport Layer Security (TLS)](master_communications_encryption.md) when communicating with the server.

USE\_IPX

This setting controls the communication protocol between the client and Advantage Database Server. The setting specified here will be used only if the connect request from the client did not specify a communication type. The client-specified connection parameter overrides this setting if they are given. Setting this value to 1 will force the client to use the IPX protocol when communicating with the server.

USE\_UDP\_IP

This setting controls the communication protocol between the client and Advantage Database Server. The setting specified here will be used only if the connect request from the client did not specify a communication type. The client-specified connection parameter overrides this setting if they are given. Setting this value to 1 will force the client to use the UDP/IP protocol when communicating with the server.
