ADS\_MGMT\_THREAD\_ACTIVITY




Advantage Database Server 12  

ADS\_MGMT\_THREAD\_ACTIVITY

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_THREAD\_ACTIVITY  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_THREAD\_ACTIVITY Advantage Client Engine ace\_Ads\_mgmt\_thread\_activity Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_THREAD\_ACTIVITY  Advantage Client Engine |  |  |  |  |

#define ADS\_MAX\_USER\_NAME 50

 

typedef struct

{

UNSIGNED32 ulThreadNumber; /\* Thread Number \*/

UNSIGNED16 usOpCode; /\* Operation in progress \*/

UNSIGNED8 aucUserName[ADS\_MAX\_USER\_NAME];/\* Name of user \*/

UNSIGNED16 usConnNumber; /\* NetWare conn num (Deprecated) \*/

UNSIGNED16 usReserved1; /\* Reserved \*/

UNSIGNED8 aucOSUserLoginName[ADS\_MAX\_USER\_NAME]; /\* OS user login name \*/

} ADS\_MGMT\_THREAD\_ACTIVITY;