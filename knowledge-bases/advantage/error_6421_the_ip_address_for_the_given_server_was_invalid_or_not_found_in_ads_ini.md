6421 The IP address for the given server was invalid or not found in ADS.INI




Advantage Database Server 12  

6421 The IP address for the given server was invalid or not found in ADS.INI

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6421 The IP address for the given server was invalid or not found in ADS.INI  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6421 The IP address for the given server was invalid or not found in ADS.INI Advantage Error Guide error\_6421\_the\_ip\_address\_for\_the\_given\_server\_was\_invalid\_or\_not\_found\_in\_ads\_ini Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6421 The IP address for the given server was invalid or not found in ADS.INI  Advantage Error Guide |  |  |  |  |

Problem: A 6421 error occurs when connecting to the Advantage Internet Server.

Solution: Verify that the Internet address in the ads.ini file is correct. The Internet section in the ads.ini file should have the following format.

[pbr]

INTERNET\_IP=144.233.44.91

INTERNET\_PORT=2001

For more information, see [ads.ini file support](master_ads_ini_file_support.htm)