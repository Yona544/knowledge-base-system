---
title: Vo Updating The Advantage Rdd For Vulcan Net
slug: vo_updating_the_advantage_rdd_for_vulcan_net
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_updating_the_advantage_rdd_for_vulcan_net.htm
source: Advantage CHM
tags:
  - vo
checksum: 2d20fd2c1240f02f7d618847159a1c141cf5875d
---

# Vo Updating The Advantage Rdd For Vulcan Net

Updating the Advantage RDD for Vulcan.NET (AdvantageRDD.dll)

Updating the Advantage RDD for Vulcan.NET (AdvantageRDD.dll)

Advantage Visual Objects and Vulcan.NET RDD

| Updating the Advantage RDD for Vulcan.NET (AdvantageRDD.dll)  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

The Advantage Vulcan.NET RDD (AdvantageRDD.dll) is built for a specific version of Vulcan.NET.  When a new version of Vulcan.NET is released, a new version of the AdvantageRDD.dll is required to work with it.  This page describes the steps necessary to update an existing Advantage Vulcan.NET RDD installation with a new version of the AdvantageRDD.dll assembly.

Typically the AdvantageRDD.dll assembly is released as a single file as opposed to including it in an installation program.  The manual process of updating it in this situation is described below.  If the AdvantageRDD.dll is released with an installation program, all you need to do is run the installation to update the AdvantageRDD.dll assembly.  To get the latest version of AdvantageRDD.dll visit the Advantage.Visual\_Objects newsgroup on the server devzone.advantagedatabase.com.

Manually Updating AdvantageRDD.dll

The AdvantageRDD.dll file is a .NET assembly file.  To use it with your application, you can simply place it in the same folder as the application (or in the path of the application) and use it like a normal DLL.  Alternatively you can add it to the GAC (global assembly cache) and your application will find it no matter where it is located.  If you are just using AdvantageRDD.dll like a DLL then you can simply replace the existing version of AdvantageRDD.dll that your application uses with the new one.  Note that you will also need to update the reference to AdvantageRDD.dll in your application's project and recompile it.  Otherwise your application will expect to find the old version of AdvantageRDD.dll and fail to work properly.

To update the AdvantageRDD.dll in the GAC you need to use the GAC utility gacutil.exe found in the Microsoft Visual Studio or .NET framework installation folder (e.g. C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\Bin or C:\WINDOWS\Microsoft.NET\Framework\v1.1.4322).  gacutil.exe can be used to install or uninstall .NET assemblies from the GAC.  To install or update the AdvantageRDD in the GAC, use the following command:

gacutil.exe /i AdvantageRDD.dll

To see if the AdvantageRDD assembly is installed:

gacutil.exe /l AdvantageRDD

To remove the AdvantageRDD assembly from the GAC:

gacutil.exe /u AdvantageRDD
