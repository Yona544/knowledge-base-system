ADS\_MGMT\_ACTIVITY\_INFO




Advantage Database Server 12  

ADS\_MGMT\_ACTIVITY\_INFO

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_ACTIVITY\_INFO  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_ACTIVITY\_INFO Advantage Client Engine ace\_Ads\_mgmt\_activity\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_ACTIVITY\_INFO  Advantage Client Engine |  |  |  |  |

typedef struct

{

UNSIGNED16 usDays; /\* Number of days server has been up \*/

UNSIGNED16 usHours; /\* Number of hours server has been up \*/

UNSIGNED16 usMinutes; /\* Number of minutes server has been up \*/

UNSIGNED16 usSeconds; /\* Number of seconds server has been up \*/

} ADS\_MGMT\_UPTIME\_INFO;

 

typedef struct

{

UNSIGNED32 ulInUse; /\* Number of items in use \*/

UNSIGNED32 ulMaxUsed; /\* Max number of items ever used \*/

UNSIGNED32 ulRejected; /\* Number of items rejected \*/

} ADS\_MGMT\_USAGE\_INFO;

 

typedef struct

{

UNSIGNED32 ulOperations; /\* Number operations since started \*/

UNSIGNED32 ulLoggedErrors; /\* Number logged errors \*/

ADS\_MGMT\_UPTIME\_INFO stUpTime; /\* Length of time ADS has been up \*/

ADS\_MGMT\_USAGE\_INFO stUsers; /\* Users in use, max, rejected \*/

ADS\_MGMT\_USAGE\_INFO stConnections; /\* Conns in use, max, rejected \*/

ADS\_MGMT\_USAGE\_INFO stWorkAreas; /\* WAs in use, max, rejected \*/

ADS\_MGMT\_USAGE\_INFO stTables; /\* Tables in use, max, rejected \*/

ADS\_MGMT\_USAGE\_INFO stIndexes; /\* Indexes in use, max, rejected \*/

ADS\_MGMT\_USAGE\_INFO stLocks; /\* Locks in use, max, rejected \*/

ADS\_MGMT\_USAGE\_INFO stTpsHeaderElems;/\* TPS header elems in use, max \*/

ADS\_MGMT\_USAGE\_INFO stTpsVisElems; /\* TPS vis elems in use, max \*/

ADS\_MGMT\_USAGE\_INFO stTpsMemoElems; /\* TPS memo elems in use, max \*/

ADS\_MGMT\_USAGE\_INFO stWorkerThreads; /\* Worker threads in use, max \*/

ADS\_MGMT\_USAGE\_INFO stQueries; /\* Queries in use, max, rejected \*/

ADS\_MGMT\_USAGE\_INFO  stStatefulUsers;  /\* Stateful (fully connected) users in use \*/

ADS\_MGMT\_USAGE\_INFO  stStatelessUsers; /\* Stateless (web platform) users in use \*/

} ADS\_MGMT\_ACTIVITY\_INFO;