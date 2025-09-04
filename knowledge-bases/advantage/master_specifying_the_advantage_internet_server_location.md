Specifying the Advantage Internet Server Location




Advantage Database Server 12  

Specifying the Advantage Internet Server Location

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Specifying the Advantage Internet Server Location  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Specifying the Advantage Internet Server Location Advantage Database Server master\_Specifying\_the\_advantage\_internet\_server\_location Advantage Database Server > Advantage Internet Server > Client-Side Settings > Specifying the Advantage Internet Server Location / Dear Support Staff, |  |
| Specifying the Advantage Internet Server Location  Advantage Database Server |  |  |  |  |

The location of the Internet-enabled Advantage Database Server must be specified. In addition, you must also configure your application to use the Advantage Internet Server server type. See [Connecting Clients through the Internet to Advantage](master_connecting_clients_through_the_internet_to_advantage.htm) for details. Below are the three ways to specify the location of the Internet-enabled Advantage Database Server:

|  |  |
| --- | --- |
| 1. | Use the server's IP address and Internet port number in the connection path string. The path can be specified as \\<ip address>:<ip port>\share\Dir\DataDictionary.add, where the <ip address> is the IP address where the Advantage Database Server is located, and the <ip port> is the Internet Port that the Advantage Database Server is listening. |

Example of using the servers IP address and Internet port number with the Advantage Client Engine API:

ulRetVal = AdsConnect60("\\\\193.69.232.1:6262\\share1\\test.add",

ADS\_AIS\_SERVER,

"User1",

"foobar",

ADS\_DEFAULT,

&hConnect );

Similar functionality for specifying the IP address and port in the connection string/path is available in other Advantage clients. The details related to making a connection through the Internet to the Advantage Database Server from other clients can be found in the respective Advantage client Help documentation.

|  |  |
| --- | --- |
| 2. | Specify the server name in the connection string. The path can be specified as \\<server name>\share\Dir\DataDictionary.add, where the <server name> is the name of a server specified in the ADS.INI file. The ADS.INI file specifies the actual IP address where the Advantage Database Server is located, and IP port that the Advantage Database Server is listening, that correspond to the specified server name. See [Setting Up Your Clients Using ADS.INI](master_setting_up_your_clients_using_ads_ini.htm) for more specifics on information in the ADS.INI file. |

Example of using a server name with the Advantage Client Engine API:

ulRetVal = AdsConnect60( "\\\\server1\\share1\\test.add",

ADS\_AIS\_SERVER,

"User1",

"foobar",

ADS\_DEFAULT,

&hConnect );

|  |  |
| --- | --- |
| 3. | Specify a drive letter in the connection string. The drive letter can be specified as <x:>\Dir\DataDictionary.add, where the <x:> is the name of a drive letter specified in the ADS.INI file. The ADS.INI file directly or indirectly specifies the actual IP address where the Advantage Database Server is located, as well as the IP port that the Advantage Database Server is listening, that correspond to the specified drive letter. See [Setting Up Your Clients Using ADS.INI](master_setting_up_your_clients_using_ads_ini.htm) for more specifics on information in the ADS.INI file. |

Example of using a drive letter with the Advantage Client Engine API:

ulRetVal = AdsConnect60( "x:\\test.add",

ADS\_AIS\_SERVER,

"User1",

"foobar",

ADS\_DEFAULT,

&hConnect );