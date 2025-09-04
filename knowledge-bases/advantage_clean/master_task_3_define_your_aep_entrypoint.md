---
title: Master Task 3 Define Your Aep Entrypoint
slug: master_task_3_define_your_aep_entrypoint
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_task_3_define_your_aep_entrypoint.htm
source: Advantage CHM
tags:
  - master
checksum: aefd1cf318a519c4efe6a6994af55d05ef76338e
---

# Master Task 3 Define Your Aep Entrypoint

Task 3: Define Your AEP EntryPoint

Task 3: Define Your AEP EntryPoint

Advantage Concepts

| Task 3: Define Your AEP EntryPoint  Advantage Concepts |  |  |  |  |

Every AEP has a pre-defined function prototype:

function NameOfAEP( ulConnectionID: UNSIGNED32;

hConnection: ADSHANDLE;

pulNumRowsAffected: PUNSIGNED32 ): UNSIGNED32;

begin

 

end;

Each parameter is described in detail in the general [Advantage Extended Procedures](master_advantage_extended_procedures.md) documentation. We wont describe each parameter here; well address these parameters as they are used throughout the rest of the tutorial.

The AEP template that was created for you already contains one procedure entrypoint, MyProcedure. We will enhance this existing procedure in later sections.
