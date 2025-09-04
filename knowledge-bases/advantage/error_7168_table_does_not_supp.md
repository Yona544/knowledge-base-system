7168 Table does not Support Strong Encryption




Advantage Database Server 12  

7168 Table does not Support Strong Encryption

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7168 Table does not Support Strong Encryption  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7168 Table does not Support Strong Encryption Advantage Error Guide Error\_7168\_table\_does\_not\_supp Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7168 Table does not Support Strong Encryption  Advantage Error Guide |  |  |  |  |

Problem: An attempt was made to enable encryption on a table using [AES encryption](master_encryption.htm), but the table format does not support it.

Solution: Only ADT and VFP table types support AES encryption; verify that the table type is correct. In addition, the table may need to be updated with additional information to support the encryption type. The system procedure [sp\_EncryptTable](master_sp_encrypttable.htm) can be used to convert the table format.