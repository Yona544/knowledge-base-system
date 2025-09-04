---
title: Ade Ads Mgmt Thread Activity
slug: ade_ads_mgmt_thread_activity
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_ads_mgmt_thread_activity.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 02ac35af69916610824c0b034268ccafb4de8d06
---

# Ade Ads Mgmt Thread Activity

ADS\_MGMT\_THREAD\_ACTIVITY

ADS\_MGMT\_THREAD\_ACTIVITY

Advantage TDataSet Descendant

| ADS\_MGMT\_THREAD\_ACTIVITY  Advantage TDataSet Descendant |  |  |  |  |

ADS\_MAX\_USER\_NAME = 50;  
   
ADS\_MGMT\_THREAD\_ACTIVITY = record  
  ulThreadNumber: UNSIGNED32; { Thread Number }   
  usOpCode: UNSIGNED16; { Operation in progress }   
  aucUserName: array[0..ADS\_MAX\_USER\_NAME - 1] of char; { Name of user }   
  usConnNumber: UNSIGNED16; { NetWare conn num (Deprecated) }   
  usReserved1: UNSIGNED16; { Reserved }   
  aucOSUserLoginName: array[0..ADS\_MAX\_USER\_NAME - 1] of char; { OS User Login Name }   
end;
