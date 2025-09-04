7165 FIPS Mode Failed




Advantage Database Server 12  

7165 FIPS Mode Failed

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7165 FIPS Mode Failed  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7165 FIPS Mode Failed Advantage Error Guide Error\_7165\_fips\_mode\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7165 FIPS Mode Failed  Advantage Error Guide |  |  |  |  |

Problem: Advantage Database Server was not able to enable [FIPS mode](master_fips.htm) when starting up.

Solution: If FIPS mode is not desired, verify that the [FIPS configuration parameter](master_fips_config.htm) is not specified with a value of 1. If FIPS mode is desired, check the error log for more detailed information on the exact nature of the error.

The OpenSSL libraries are required in order to use FIPS mode. If there was an error loading the libraries, the error log should have a [7160](error_7160_unable_to_load_ssl.htm), [7161](error_7161_unable_to_verify_si.htm), [7162](error_7162_unable_to_load_ssl_.htm) error that may indicate why they could not be loaded.

It is also possible for the internal FIPS mode verification performed at startup to fail. If this happened, the error log should contain additional information.