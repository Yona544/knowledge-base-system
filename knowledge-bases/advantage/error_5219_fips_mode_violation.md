5219 FIPS Mode Violation




Advantage Database Server 12  

5219 FIPS Mode Violation

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5219 FIPS Mode Violation  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5219 FIPS Mode Violation Advantage Error Guide Error\_5219\_fips\_mode\_violation Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5219 FIPS Mode Violation  Advantage Error Guide |  |  |  |  |

Problem: The current request could not be completed because Advantage is running in [FIPS mode](master_fips.htm) and the request required use of cryptography that is not approved for FIPS usage.

Solution: If you are trying to open a dictionary or a table that is not using AES encryption while the server is in FIPS mode, the operation cannot be completed. The system procedure [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.htm) can be used to change a dictionary to use AES encryption. Tables can be converted to AES encryption with the system procedure [sp\_EncryptTable](master_sp_encrypttable.htm). In order to perform the conversion, it is necessary to use clients and servers that are not running in FIPS mode.