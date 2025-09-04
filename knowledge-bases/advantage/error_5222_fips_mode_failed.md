5222 FIPS Mode Failed




Advantage Database Server 12  

5222 FIPS Mode Failed

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5222 FIPS Mode Failed  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5222 FIPS Mode Failed Advantage Error Guide Error\_5222\_fips\_mode\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5222 FIPS Mode Failed  Advantage Error Guide |  |  |  |  |

Problem: The Advantage client was not able to enable [FIPS mode](master_fips.htm) when starting up.

Solution: If FIPS mode is not desired, verify that the [FIPS connection option](ace_adsconnect101.htm) is not specified. If FIPS mode is desired, the error text associated with this error should contain addition information on identifying the problem. The internal FIPS mode verification performed at startup may have failed.