7085 Invalid UNC server name




Advantage Database Server 12  

7085 Invalid UNC server name

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7085 Invalid UNC server name  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7085 Invalid UNC server name Advantage Error Guide error\_7085\_invalid\_unc\_server\_name Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7085 Invalid UNC server name  Advantage Error Guide |  |  |  |  |

Remote Server

Problem: A UNC path passed to the server does not match the servers computer name.

Solution: This indicates an internal error. Contact Advantage [Technical Support](master_technical_support_u_s__and_canada.htm).

Local Server

Problem: There was an error reading the UNC server name from the REPLACE\_UNC\_SERVER key in the ads.ini file. Either the ads.ini file could not be found or the server name specified was not found.

Solution: Verify the ads.ini file is in the search path and that an entry exists for the server used in the connection string.