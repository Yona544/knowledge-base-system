7030 Missing Advantage configuration file, ADS.CFG or ADSLOCAL.CFG




Advantage Database Server 12  

7030 Missing Advantage configuration file ADSLOCAL.CFG

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7030 Missing Advantage configuration file ADSLOCAL.CFG  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7030 Missing Advantage configuration file ADSLOCAL.CFG Advantage Error Guide error\_7030\_missing\_advantage\_configuration\_file\_ads\_cfg\_or\_adslocal\_cfg Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7030 Missing Advantage configuration file ADSLOCAL.CFG  Advantage Error Guide |  |  |  |  |

Problem: This error is applicable to the Advantage Local Server only. The Advantage configuration file, ADSLOCAL.CFG, was not found when the Advantage Local Server DLL was loaded. The ADSLOCAL.CFG configuration file must be located in the current working directory, the Windows system directory, or the client's search path. If the ADSLOCAL.CFG file is not found when the Advantage Local Server DLL is loaded, the configuration defaults will get used and no error will be generated other than this 7030 warning in the error log file.

Solution: Put ADSLOCAL.CFG in the current working directory, the Windows system directory, or the client's search path.