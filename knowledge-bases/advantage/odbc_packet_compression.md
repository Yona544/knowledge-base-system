Packet Compression




Advantage Database Server 12  

Packet Compression

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Packet Compression |  |  | Feedback on: Advantage Database Server 12 - Packet Compression odbc\_Packet\_compression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Packet Compression |  |  |  |  |

This setting controls the option for communications compression (see Advantage.hlp for more information.) If INTERNET is specified, then all data communications for ADS\_AIS\_SERVER connections will be compressed unless compression is specifically turned off at the server. If ALWAYS is specified, then all data communications between the client and server will be compressed unless compression is specifically turned off at the server. If NEVER is specified, then compression will not be used for communications between the client and server. If this entry is not specified or is left empty, then the COMPRESSION setting in the ADS.INI file will be used if available. This entry is ignored for ADS\_LOCAL\_SERVER connections.