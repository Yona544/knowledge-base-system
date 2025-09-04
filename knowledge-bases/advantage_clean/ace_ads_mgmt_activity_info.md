---
title: Ace Ads Mgmt Activity Info
slug: ace_ads_mgmt_activity_info
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_ads_mgmt_activity_info.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 36cf77a3cbd921e928447dfa8ca62db889326269
---

# Ace Ads Mgmt Activity Info

ADS\_MGMT\_ACTIVITY\_INFO

ADS\_MGMT\_ACTIVITY\_INFO

Advantage Client Engine

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
