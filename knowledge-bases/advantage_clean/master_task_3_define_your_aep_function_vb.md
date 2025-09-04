---
title: Master Task 3 Define Your Aep Function Vb
slug: master_task_3_define_your_aep_function_vb
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_task_3_define_your_aep_function_vb.htm
source: Advantage CHM
tags:
  - master
checksum: 9ce8c494df51163fd381d926b560debf07cc62ca
---

# Master Task 3 Define Your Aep Function Vb

Task 3: Define Your AEP Function

Task 3: Define Your AEP Function

Advantage Concepts

| Task 3: Define Your AEP Function  Advantage Concepts |  |  |  |  |

Every AEP has a pre-defined function prototype:

Public Function MyProcedure(ByVal ulConnectionID As Int32, \_

ByVal hConnection As Int32, \_

ByRef ulNumRowsAffected As Int32) As Int32

 

Each parameter is described in detail in the general [Advantage Extended Procedures](master_advantage_extended_procedures.md) documentation. We wont describe each parameter here; well address these parameters as they are used throughout the rest of the tutorial.

The AEP template that was created for you already contains one procedure entrypoint, MyProcedure. We will enhance this existing procedure in later sections.
