---
title: Ace Ads Mgmt Table Info
slug: ace_ads_mgmt_table_info
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_ads_mgmt_table_info.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 06e71967b3b9b90649b747bdd01fb63af8d709f8
---

# Ace Ads Mgmt Table Info

ADS\_MGMT\_TABLE\_INFO

ADS\_MGMT\_TABLE\_INFO

Advantage Client Engine

| ADS\_MGMT\_TABLE\_INFO  Advantage Client Engine |  |  |  |  |

#define ADS\_MGMT\_MAX\_PATH 260

 

typedef struct

{

UNSIGNED8 aucTableName[ADS\_MGMT\_MAX\_PATH];/\* Fully qualified table name \*/

UNSIGNED16 usLockType; /\* Advantage locking mode \*/

} ADS\_MGMT\_TABLE\_INFO;
