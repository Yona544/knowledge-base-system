---
title: Master Task 6 Build And Register Your Procedure For Com Usage Vb
slug: master_task_6_build_and_register_your_procedure_for_com_usage_vb
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_task_6_build_and_register_your_procedure_for_com_usage_vb.htm
source: Advantage CHM
tags:
  - master
checksum: d0eaee92596a12973c7de1afb804810339265f66
---

# Master Task 6 Build And Register Your Procedure For Com Usage Vb

Task 6: Build and Register Your Procedure for COM Usage VB

Task 6: Build and Register Your Procedure for COM Usage VB

Advantage Concepts

| Task 6: Build and Register Your Procedure for COM Usage VB  Advantage Concepts |  |  |  |  |

Build Your Procedure

| 1. | Select Build AdvantageAEP1 from the Build menu. |

| 2. | You should now have a file called AdvantageAEP1.dll in your c:\data\AdvantageAEP1\bin directory. |

Register Your Assembly

If you are using local server (as we are in this tutorial) you will need to register the AEP assembly on the client machine. If you are using remote server you will need to register the AEP assembly on the server machine. Use the regasm.exe utility (included in your Visual Studio .NET installation) to register your assembly. Note the path to regasm.exe may vary depending on your Visual Studio installation and the version of the .NET framework you are using.

c:

cd \data\AdvantageAEP1\bin

C:\windows\Microsoft.NET\Framework\v2.0.50727\regasm.exe /codebase AdvantageAEP1.dll

 

Note Regasm.exe will warn you about registering an unsigned assembly. For the purpose of this tutorial a signed assembly is not required. Before deploying an assembly, however, you should read the .NET documentation and learn how to create signed assemblies.
