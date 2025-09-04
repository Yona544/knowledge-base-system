---
title: Vo Ax Getacestmthandle
slug: vo_ax_getacestmthandle
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_getacestmthandle.htm
source: Advantage CHM
tags:
  - vo
checksum: 07695a0efc02c8a59975ee1cd5748e4e08e0fcf4
---

# Vo Ax Getacestmthandle

AX\_GetAceStmtHandle

AX\_GetAceStmtHandle()

Advantage Visual Objects and Vulcan.NET RDD

| AX\_GetAceStmtHandle()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Returns the Advantage Client Engine SQL statement handle that corresponds with the SQL cursor opened in the current work area. The handle can be used to call any Advantage Client Engine API directly. This function only applies to the AXSQL RDDs. For all other RDDs, it will always return zero.

Syntax

AX\_GetAceStmtHandle() -> DWORD

Returns

An Advantage Client Engine SQL statement handle

Description

Returns the statement handle associated with the current work area. The handle can be used to call any Advantage Client Engine API directly. The APIs can be imported into Visual Objects from the ACE.AEF file.

The AX\_GetAceStmtHandle function gets the statement handle from the current work area. If you are unsure which work area is current, use select() to set it. For example:

select( sqlServer:workarea )

or

select( sqlServer:alias )

To avoid all ambiguity you could also retrieve the statement handle directly from the AdsSQLServer or DBServer object using the Info method. For example:

sqlServer:Info( DBI\_GET\_ACE\_STMT\_HANDLE )

DBI\_GET\_ACE\_STMT\_HANDLE is defined in the dbfaxs.aef library.
