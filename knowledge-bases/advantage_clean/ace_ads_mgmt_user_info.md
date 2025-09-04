---
title: Ace Ads Mgmt User Info
slug: ace_ads_mgmt_user_info
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_ads_mgmt_user_info.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 09adf21af8b9521ea6d8b554be7906391bc9d20b
---

# Ace Ads Mgmt User Info

ADS\_MGMT\_USER\_INFO

ADS\_MGMT\_USER\_INFO

Advantage Client Engine

| ADS\_MGMT\_USER\_INFO  Advantage Client Engine |  |  |  |  |

#define ADS\_MAX\_USER\_NAME 50

#define ADS\_MAX\_ADDRESS\_SIZE 30

 

| typedef struct |  |
| { |  |
| UNSIGNED8 aucUserName[ADS\_MAX\_USER\_NAME]; | // The user's computer name |

| UNSIGNED16 usConnNumber; | // NetWare connection number  // (Deprecated)) |

| UNSIGNED8 aucAuthUserName[ADS\_MAX\_USER\_NAME]; | // Name of user that has authenticated  // to an Advantage Data Dictionary |

| UNSIGNED8 aucAddress[ADS\_MAX\_ADDRESS\_SIZE]; | // IP or IPX address of  // connected user |

| UNSIGNED8 aucOSUserLoginName[ADS\_MAX\_USER\_NAME]; | // OS user login name |

| UNSIGNED8 aucTSAddress[ADS\_MAX\_ADDRESS\_SIZE]; | // IP Address of Terminal Services  // client if connection is made from a  // Terminal Server. |
| UNSIGNED8 aucApplicationID[ADS\_MAX\_MGMT\_APPID\_SIZE]; | // ApplicationID, see sp\_SetApplicationID |
| UNSIGNED32 ulAveRequestCost; | // estimated average cost of  // each server request |

| } ADS\_MGMT\_USER\_INFO; |  |
