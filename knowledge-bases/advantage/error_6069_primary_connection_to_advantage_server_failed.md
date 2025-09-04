6069 Primary connection to Advantage server failed




Advantage Database Server 12  

6069 Primary connection to Advantage server failed

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6069 Primary connection to Advantage server failed  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6069 Primary connection to Advantage server failed Advantage Error Guide error\_6069\_primary\_connection\_to\_advantage\_server\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6069 Primary connection to Advantage server failed  Advantage Error Guide |  |  |  |  |

Problem: The primary connection attempt to the Advantage server failed. If you are running a CA-Clipper application that is using the IP communication library, and you incorrectly linked in the Advantage IP comm layer library using "LIB" instead of "SEARCH" or "MODULE"in your link script, this error will occur.

Solution: If you are running a CA-Clipper application that is using the IP communication library, change your link script to use "SEARCH" or "MODULE" to link in the Advantage IP comm library. Refer to the ADS DOS IP documentation, readme.txt file, or sample link scripts for more information on how to correctly link in the Advantage IP comm library. If you are NOT running a CA-Clipper application that is using the IP communication library, then retry the operation or try reloading your network shell.