---
title: Ace Ads Mgmt Config Memory
slug: ace_ads_mgmt_config_memory
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_ads_mgmt_config_memory.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 71c0686ba18e6411f6a023e72b08ad69ebfcaf95
---

# Ace Ads Mgmt Config Memory

ADS\_MGMT\_CONFIG\_MEMORY

ADS\_MGMT\_CONFIG\_MEMORY

Advantage Client Engine

| ADS\_MGMT\_CONFIG\_MEMORY  Advantage Client Engine |  |  |  |  |

typedef struct

{

UNSIGNED32 ulTotalConfigMem; /\* Total mem taken by cfg params \*/

UNSIGNED32 ulConnectionMem; /\* memory taken by connections \*/

UNSIGNED32 ulWorkAreaMem; /\* memory taken by work areas \*/

UNSIGNED32 ulTableMem; /\* memory taken by tables \*/

UNSIGNED32 ulIndexMem; /\* memory taken by indexes \*/

UNSIGNED32 ulLockMem; /\* memory taken by locks \*/

UNSIGNED32 ulUserBufferMem; /\* memory taken by user buffer \*/

UNSIGNED32 ulTPSHeaderElemMem; /\* memory taken by TPS hdr elems \*/

UNSIGNED32 ulTPSVisibilityElemMem; /\* memory taken by TPS vis elems \*/

UNSIGNED32 ulTPSMemoTransElemMem; /\* mem taken by TPS memo elems \*/

UNSIGNED32 ulReceiveEcbMem; /\* mem taken by rcv ECBs (NLM) \*/

UNSIGNED32 ulSendEcbMem; /\* mem taken by send ECBs (NLM) \*/

UNSIGNED32 ulWorkerThreadMem; /\* mem taken by worker threads \*/

UNSIGNED32 ulQueryMem; /\* mem taken by queries \*/

} ADS\_MGMT\_CONFIG\_MEMORY;
