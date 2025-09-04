---
title: Ade Ads Mgmt Install Info
slug: ade_ads_mgmt_install_info
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_ads_mgmt_install_info.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 7eb51facdb9cfc6e2eedc340e145cfaef92e1780
---

# Ade Ads Mgmt Install Info

ADS\_MGMT\_INSTALL\_INFO

ADS\_MGMT\_INSTALL\_INFO

Advantage TDataSet Descendant

| ADS\_MGMT\_INSTALL\_INFO  Advantage TDataSet Descendant |  |  |  |  |

ADS\_REG\_OWNER\_LEN = 36;  
ADS\_REVISION\_LEN = 16;  
ADS\_INST\_DATE\_LEN = 16;  
ADS\_OEM\_CHAR\_NAME\_LEN = 16;  
ADS\_ANSI\_CHAR\_NAME\_LEN = 16;  
ADS\_SERIAL\_NUM\_LEN = 16;  
   
ADS\_MGMT\_INSTALL\_INFO = record  
  ulUserOption : UNSIGNED32; { For ADS, user option purchased. For ALS, }  
                             { max users that can have any given table open }  
  aucRegisteredOwner: array[0..ADS\_REG\_OWNER\_LEN - 1] of char;   
  aucVersionStr: array[0..ADS\_REVISION\_LEN - 1] of char;   
  aucInstallDate: array[0..ADS\_INST\_DATE\_LEN - 1] of char;   
  aucOemCharName: array[0..ADS\_OEM\_CHAR\_NAME\_LEN - 1] of char;   
  aucAnsiCharName: array[0..ADS\_ANSI\_CHAR\_NAME\_LEN - 1] of char;   
  aucEvalExpireDate: array[0..ADS\_INST\_DATE\_LEN - 1] of char;   
  aucSerialNumber: array[0..ADS\_SERIAL\_NUM\_LEN - 1] of char;

 ulMaxStatefulUsers: UNSIGNED32; { How many stateful connections allowed }

 ulMaxStatelessUsers: UNSIGNED32; { How many stateless (web platform) connections allowed }  
end;
