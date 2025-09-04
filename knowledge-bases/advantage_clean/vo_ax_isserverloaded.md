---
title: Vo Ax Isserverloaded
slug: vo_ax_isserverloaded
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_isserverloaded.htm
source: Advantage CHM
tags:
  - vo
checksum: 413bbde7818ef5f66e028546185ec55b02c6d334
---

# Vo Ax Isserverloaded

AX\_IsServerLoaded()

AX\_IsServerLoaded()

Advantage Visual Objects and Vulcan.NET RDD

| AX\_IsServerLoaded()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Verifies the Advantage Database Server is loaded

Syntax

AX\_IsServerLoaded( <strPathName> ) -> logical

| <strPathName> | The path where database server availability is to be checked. This path may include a file name. |

Returns

Returns a logical value. This function returns a .T. if a file opened in specified directory will be opened using the Advantage Database Server or .F. if the Database Server is not available.

Description

This function is identical to the Advantage for Clipper AX\_Loaded() function. In order to make this function available to your application, you must open the DBFAXS library in your VO repository. Find and open the entry labeled "TEXTBLOCK DBFAXS:AX\_IsServerLoaded\_\_README". Uncomment the DLL FUNCTION definition that matches your version of Visual Objects.

Example

if AX\_IsServerLoaded()

oDB1 := AxDBServer{ "TEST1", .F., .F., "AXDBFNTX" }

Else

oDB1 := DBServer{ "TEST1", .F., .F., "DBFNTX" }

Endif
