---
title: Ade Ads Mgmt Table Info
slug: ade_ads_mgmt_table_info
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_ads_mgmt_table_info.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a9d42ed8e518fd20fc8e3ba7c9fbc9dfcc709b2c
---

# Ade Ads Mgmt Table Info

ADS\_MGMT\_TABLE\_INFO

ADS\_MGMT\_TABLE\_INFO

Advantage TDataSet Descendant

| ADS\_MGMT\_TABLE\_INFO  Advantage TDataSet Descendant |  |  |  |  |

ADS\_MGMT\_MAX\_PATH = 260;  
   
ADS\_MGMT\_TABLE\_INFO = record  
  aucTableName: array[0..ADS\_MGMT\_MAX\_PATH - 1] of char; { Fully qualified table name }   
  usLockType: UNSIGNED16; { Advantage locking mode }   
end;
