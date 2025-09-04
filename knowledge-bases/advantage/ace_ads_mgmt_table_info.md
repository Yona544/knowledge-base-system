ADS\_MGMT\_TABLE\_INFO




Advantage Database Server 12  

ADS\_MGMT\_TABLE\_INFO

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_TABLE\_INFO  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_TABLE\_INFO Advantage Client Engine ace\_Ads\_mgmt\_table\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_TABLE\_INFO  Advantage Client Engine |  |  |  |  |

#define ADS\_MGMT\_MAX\_PATH 260

 

typedef struct

{

UNSIGNED8 aucTableName[ADS\_MGMT\_MAX\_PATH];/\* Fully qualified table name \*/

UNSIGNED16 usLockType; /\* Advantage locking mode \*/

} ADS\_MGMT\_TABLE\_INFO;