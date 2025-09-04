---
title: Ade Ads Mgmt Index Info
slug: ade_ads_mgmt_index_info
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_ads_mgmt_index_info.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 453f4dd14d2910f15bd067366bc8dfe47eb951f8
---

# Ade Ads Mgmt Index Info

ADS\_MGMT\_INDEX\_INFO

ADS\_MGMT\_INDEX\_INFO

Advantage TDataSet Descendant

| ADS\_MGMT\_INDEX\_INFO  Advantage TDataSet Descendant |  |  |  |  |

ADS\_MGMT\_MAX\_PATH = 260;  
   
ADS\_MGMT\_INDEX\_INFO = record  
  aucIndexName: array[0..ADS\_MGMT\_MAX\_PATH - 1] of char; { Fully qualified index name }   
end;
