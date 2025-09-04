Advantage Extended Procedures - Visual Basic Tutorial




Advantage Database Server 12  

Advantage Extended Procedures - Visual Basic Tutorial

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Extended Procedures - Visual Basic Tutorial  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Advantage Extended Procedures - Visual Basic Tutorial Advantage Concepts master\_Advantage\_extended\_procedures\_visual\_basic\_tutorial Advantage Concepts > Advantage Functionality > Advantage Extended Procedures > Visual Basic Tutorial > Advantage Extended Procedures - Visual Basic Tutorial / Dear Support Staff, |  |
| Advantage Extended Procedures - Visual Basic Tutorial  Advantage Concepts |  |  |  |  |

This tutorial will guide you, step-by-step, through the process of creating and debugging an [Advantage Extended Procedure](master_advantage_extended_procedures.htm) using Visual Basic .NET.

Visual Basic 6 users

In Visual Basic 6 (as opposed to VB .NET) all ActiveX DLLs run in a single-threaded apartment. This means all global variables are safe because only one Advantage thread can be calling a stored procedure at any instance. While this makes writing an AEP simple (no need to protect global variables from other threads), it can cause major performance problems in a multi-user environment. It is recommended you use VB .NET to write all Advantage Extended Procedures. While the code examples in this tutorial are written for VB .NET users, VB6 users will still find the tutorial itself informational.

Important All of the tasks in this tutorial must be completed or the tutorial application will not work correctly.

[Task 1: Copy Test Data and Application](master_task_1_copy_test_data_and_application_vb.htm)

[Task 2: Create Your AEP Project](master_task_2_create_your_aep_project_vb.htm)

[Task 3: Define Your AEP Function](master_task_3_define_your_aep_function_vb.htm)

[Task 4: Add Startup and Shutdown Functions](master_task_4_add_startup_and_shutdown_functions_vb.htm)

[Task 5: Implement Your Procedure Logic](master_task_5_implement_your_procedure_logic_vb.htm)

[Task 6: Build and Register Your Procedure for COM Usage](master_task_6_build_and_register_your_procedure_for_com_usage_vb.htm)

[Task 7: Register Your Procedure in the Data Dictionary](master_task_7_register_your_procedure_in_the_data_dictionary_vb.htm)

[Task 8: Test Your Procedure](master_task_8_test_your_procedure_vb.htm)