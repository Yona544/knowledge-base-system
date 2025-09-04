---
title: Ade Ads Mgmt Activity Info
slug: ade_ads_mgmt_activity_info
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_ads_mgmt_activity_info.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: e2f1667d3e22228b90d2b21182e9004ca3ed4bd1
---

# Ade Ads Mgmt Activity Info

ADS\_MGMT\_ACTIVITY\_INFO

ADS\_MGMT\_ACTIVITY\_INFO

Advantage TDataSet Descendant

| ADS\_MGMT\_ACTIVITY\_INFO  Advantage TDataSet Descendant |  |  |  |  |

ADS\_MGMT\_USAGE\_INFO = record  
  ulInUse: UNSIGNED32; { Number of items in use }   
  ulMaxUsed: UNSIGNED32; { Max number of items ever used }   
  ulRejected: UNSIGNED32; { Number of items rejected }   
end;  
   
ADS\_MGMT\_UPTIME\_INFO = record  
  usDays: UNSIGNED16; { Number of days server has been up }   
  usHours: UNSIGNED16; { Number of hours server has been up }   
  usMinutes: UNSIGNED16; { Number on minutes server has been up }   
  usSeconds: UNSIGNED16; { Number of seconds server has been up }   
end;  
   
ADS\_MGMT\_ACTIVITY\_INFO = record  
  ulOperations: UNSIGNED32; { Number operations since started }   
  ulLoggedErrors: UNSIGNED32; { Number logged errors }   
  stUpTime: ADS\_MGMT\_UPTIME\_INFO; { Length of time ADS has been up }   
  stUsers: ADS\_MGMT\_USAGE\_INFO; { Users in use, max, rejected }   
  stConnections: ADS\_MGMT\_USAGE\_INFO; { Connections in use, max, rejected }   
  stWorkAreas: ADS\_MGMT\_USAGE\_INFO; { Work areas in use, max, rejected }   
  stTables: ADS\_MGMT\_USAGE\_INFO; { Tables in use, max, rejected }   
  stIndexes: ADS\_MGMT\_USAGE\_INFO; { Indexes in use, max, rejected }   
  stLocks: ADS\_MGMT\_USAGE\_INFO; { Locks in use, max, rejected }   
  stTpsHeaderElems: ADS\_MGMT\_USAGE\_INFO; { TPS header elems in use, max }   
  stTpsVisElems: ADS\_MGMT\_USAGE\_INFO; { TPS visibility elems in use, max }   
  stTpsMemoElems: ADS\_MGMT\_USAGE\_INFO; { TPS memo elems in use, max }   
  stWorkerThreads: ADS\_MGMT\_USAGE\_INFO; { Worker Threads in use, max }

 stQueries:   ADS\_MGMT\_USAGE\_INFO;   { Queries in use, max, rejected }

 stStatefulUsers:   ADS\_MGMT\_USAGE\_INFO;   { Stateful users in use }

 stStatelessUsers:   ADS\_MGMT\_USAGE\_INFO;   { Stateless (web platform) users in use }  
end;
