---
title: Ade Ads Mgmt User Info
slug: ade_ads_mgmt_user_info
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_ads_mgmt_user_info.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a582a0175fcc65af564b5dce54c2a56e289a9972
---

# Ade Ads Mgmt User Info

ADS\_MGMT\_USER\_INFO

ADS\_MGMT\_USER\_INFO

Advantage TDataSet Descendant

| ADS\_MGMT\_USER\_INFO  Advantage TDataSet Descendant |  |  |  |  |

ADS\_MAX\_USER\_NAME = 50;  
ADS\_MAX\_ADDRESS\_SIZE = 30;  
ADS\_MAX\_MGMT\_APPID\_SIZE = 70;  
   
ADS\_MGMT\_USER\_INFO = record  
  aucUserName: array[0..ADS\_MAX\_USER\_NAME - 1] of char; { Computer name }   
  usConnNumber: UNSIGNED16; { NetWare connection number (Deprecated) }   
  aucDictionaryName: array[0..ADS\_MAX\_USER\_NAME-1] of char; { Name of user that has authenticated to an Advantage Data Dictionary }   
  aucAddress: array[0..ADS\_MAX\_ADDRESS\_SIZE - 1] of char; { IP or IPX address of connected user }   
  aucOSUserLoginName: array[0..ADS\_MAX\_USER\_NAME - 1] of char; { OS User Login Name }   
  aucApplicationID: array[0..ADS\_MAX\_MGMT\_APPID\_SIZE - 1] of char; { Application ID }  
  ulAveRequestCost: UNSIGNED32; { estimated average cost of each server request }  
end;
