6097 Bad IP address specified in connection path or in ADS.INI file




Advantage Database Server 12  

6097 Bad IP address and/or bad port specified in connection path or in ADS.INI file

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6097 Bad IP address and/or bad port specified in connection path or in ADS.INI file  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6097 Bad IP address and/or bad port specified in connection path or in ADS.INI file Advantage Error Guide error\_6097\_bad\_ip\_address\_specified\_in\_connection\_path\_or\_in\_ads\_ini\_file Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6097 Bad IP address and/or bad port specified in connection path or in ADS.INI file  Advantage Error Guide |  |  |  |  |

Problem: The Advantage Database Server was not found at the IP address and port specified in the connection path or in the ads.ini file.

Solution: Verify the following:

|  |  |
| --- | --- |
| · | The IP address and port are correct for the Advantage Database Server you are trying to connect to. If you are specifying the address and port in the connection path (e.g., //server:port/path or //ip:port/path), verify that both are valid values. |

|  |  |
| --- | --- |
| · | The Advantage Database Server is currently running. |

|  |  |
| --- | --- |
| · | You can ping the IP address from the client machine to the server machine. |

|  |  |
| --- | --- |
| · | UDP packets are not filtered between the client and server machine. |