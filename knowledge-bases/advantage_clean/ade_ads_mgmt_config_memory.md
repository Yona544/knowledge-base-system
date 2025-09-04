---
title: Ade Ads Mgmt Config Memory
slug: ade_ads_mgmt_config_memory
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_ads_mgmt_config_memory.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ae8cf4b99fdc23fe5d1a14addddb78cea1217e9c
---

# Ade Ads Mgmt Config Memory

ADS\_MGMT\_CONFIG\_MEMORY

ADS\_MGMT\_CONFIG\_MEMORY

Advantage TDataSet Descendant

| ADS\_MGMT\_CONFIG\_MEMORY  Advantage TDataSet Descendant |  |  |  |  |

ADS\_MGMT\_CONFIG\_MEMORY = record  
  ulTotalConfigMem: UNSIGNED32; { total mem used by cfg params }   
  ulConnectionMem: UNSIGNED32; { memory taken by connections }   
  ulWorkAreaMem: UNSIGNED32; { memory taken by work areas }   
  ulTableMem: UNSIGNED32; { memory taken by tables }   
  ulIndexMem: UNSIGNED32; { memory taken by indexes }   
  ulLockMem: UNSIGNED32; { memory taken by locks }   
  ulUserBufferMem: UNSIGNED32; { memory taken by user buffer }   
  ulTPSHeaderElemMem: UNSIGNED32; { memory taken by TPS hdr elems }   
  ulTPSVisibilityElemMem:UNSIGNED32; { memory taken by TPS vis elems }   
  ulTPSMemoTransElemMem: UNSIGNED32; { mem taken by TPS memo elems }   
  ulRcvEcbMem: UNSIGNED32; { mem taken by rcv ECBs (NLM) }   
  ulSendEcbMem: UNSIGNED32; { mem taken by send ECBs (NLM) }   
  ulWorkerThreadMem: UNSIGNED32; { mem taken by worker threads }   
end;
