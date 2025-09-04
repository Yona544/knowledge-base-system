---
title: Vo Advantage Functions
slug: vo_advantage_functions
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_advantage_functions.htm
source: Advantage CHM
tags:
  - vo
checksum: 33d098ae5eb28bfe4bc3fdb8825804f331ffdd38
---

# Vo Advantage Functions

Advantage Functions

Advantage Functions

Advantage Visual Objects and Vulcan.NET RDD

| Advantage Functions  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Advantage provides advanced features to Visual Objects and Vulcan.NET through additional functions. These functions are more specific to Advantage and client/server features and thus, require the Advantage RDD be available within the application.

To use Advantage advanced functions, an additional Advantage library is needed. For Visual Objects an Application Export File (.AEF) is provided that contains a library file, DBFAXS. The AEF must be imported into the Visual Objects repository in order for the library to be accessible. The application then must reference the library. In order for the changes to take effect, the application must be recompiled.  For Vulcan.NET additional source files DBFAXS.prg and DBFAXS.vh are provided that contain the DBFAXS library of functions.  These files must be added to you Vulcan.NET project.

The SetSelectiveRelation method in the CAVO DBServer does not provide accurate relations. This problem has been fixed in Visual Objects version 2.0b-1. For earlier versions, the file, ADSDBSER.AEF, containing the AdsDBServer is provided to fix this problem. All data servers that will use the SetSelectiveRelation method must inherit from AdsDBServer instead of DBServer.

The object-oriented examples used in the following function descriptions are based on a class named AxDBServer. See [CLASS AxDBServer](vo_class_axdbserver.md) for a code sample.

[AX\_AXSLocking()](vo_ax_axslocking.md)

[AX\_BLOB2File()](vo_ax_blob2file.md)

[AX\_File2BLOB()](vo_ax_file2blob.md)

[AX\_GetAceIndexHandle()](vo_ax_getaceindexhandle.md)

[AX\_GetAceTableHandle()](vo_ax_getacetablehandle.md)

[AX\_IsServerLoaded()](vo_ax_isserverloaded.md)

[AX\_PercentIndexed()](vo_ax_percentindexed.md)

[AX\_RightsCheck()](vo_ax_rightscheck.md)

[AX\_SetConnectionHandle()](vo_ax_setconnectionhandle.md)

[AX\_SetPassword()](vo_ax_setpassword.md)

[AX\_SetServerType()](vo_ax_setservertype.md)

[AX\_Transaction()](vo_ax_transaction.md)

[AX\_UsingClientServer()](vo_ax_usingclientserver.md)
