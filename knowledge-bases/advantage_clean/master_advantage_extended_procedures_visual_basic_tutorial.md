---
title: Master Advantage Extended Procedures Visual Basic Tutorial
slug: master_advantage_extended_procedures_visual_basic_tutorial
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_extended_procedures_visual_basic_tutorial.htm
source: Advantage CHM
tags:
  - master
checksum: f149a11cf4d532b05099f8549fb3b31c764128a3
---

# Master Advantage Extended Procedures Visual Basic Tutorial

Advantage Extended Procedures - Visual Basic Tutorial

Advantage Extended Procedures - Visual Basic Tutorial

Advantage Concepts

| Advantage Extended Procedures - Visual Basic Tutorial  Advantage Concepts |  |  |  |  |

This tutorial will guide you, step-by-step, through the process of creating and debugging an [Advantage Extended Procedure](master_advantage_extended_procedures.md) using Visual Basic .NET.

Visual Basic 6 users

In Visual Basic 6 (as opposed to VB .NET) all ActiveX DLLs run in a single-threaded apartment. This means all global variables are safe because only one Advantage thread can be calling a stored procedure at any instance. While this makes writing an AEP simple (no need to protect global variables from other threads), it can cause major performance problems in a multi-user environment. It is recommended you use VB .NET to write all Advantage Extended Procedures. While the code examples in this tutorial are written for VB .NET users, VB6 users will still find the tutorial itself informational.

Important All of the tasks in this tutorial must be completed or the tutorial application will not work correctly.

[Task 1: Copy Test Data and Application](master_task_1_copy_test_data_and_application_vb.md)

[Task 2: Create Your AEP Project](master_task_2_create_your_aep_project_vb.md)

[Task 3: Define Your AEP Function](master_task_3_define_your_aep_function_vb.md)

[Task 4: Add Startup and Shutdown Functions](master_task_4_add_startup_and_shutdown_functions_vb.md)

[Task 5: Implement Your Procedure Logic](master_task_5_implement_your_procedure_logic_vb.md)

[Task 6: Build and Register Your Procedure for COM Usage](master_task_6_build_and_register_your_procedure_for_com_usage_vb.md)

[Task 7: Register Your Procedure in the Data Dictionary](master_task_7_register_your_procedure_in_the_data_dictionary_vb.md)

[Task 8: Test Your Procedure](master_task_8_test_your_procedure_vb.md)
