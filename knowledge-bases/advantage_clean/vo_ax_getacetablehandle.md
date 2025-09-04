---
title: Vo Ax Getacetablehandle
slug: vo_ax_getacetablehandle
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_getacetablehandle.htm
source: Advantage CHM
tags:
  - vo
checksum: 4d8dfd9fbfdf88c526fe29bd6a6858fe45e56597
---

# Vo Ax Getacetablehandle

AX\_GetAceTableHandle()

AX\_GetAceTableHandle()

Advantage Visual Objects and Vulcan.NET RDD

| AX\_GetAceTableHandle()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Returns the Advantage Client Engine table handle that corresponds with the DBF (or table) opened in the current work area. The handle can be used to call any Advantage Client Engine API directly.

Syntax

AX\_GetAceTableHandle() -> DWORD

Returns

An Advantage Client Engine table handle.

Description

Returns the table (or DBF) handle associated with the current work area. The handle can be used to call any Advantage Client Engine API directly. The APIs can be imported into Visual Objects from the ACE.AEF file.

The AX\_GetAceTableHandle function gets the table handle from the current work area. If you are unsure which work area is current, use select() to set it. For example:

select( dbServer:workarea )

or

select( dbServer:alias )

To avoid all ambiguity you could also retrieve the table handle directly from the DBServer object using the Info method. For example:

dbServer:Info( DBI\_GET\_ACE\_TABLE\_HANDLE )

DBI\_GET\_ACE\_TABLE\_HANDLE is defined in the dbfaxs.aef library.
