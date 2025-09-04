---
title: Ace Ads Mgmt Thread Activity
slug: ace_ads_mgmt_thread_activity
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_ads_mgmt_thread_activity.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: f4b8b9bfb27bbbc2adc999e75f7c6691138a8408
---

# Ace Ads Mgmt Thread Activity

ADS\_MGMT\_THREAD\_ACTIVITY

ADS\_MGMT\_THREAD\_ACTIVITY

Advantage Client Engine

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
