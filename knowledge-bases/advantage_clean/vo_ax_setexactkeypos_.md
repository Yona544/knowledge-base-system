---
title: Vo Ax Setexactkeypos
slug: vo_ax_setexactkeypos_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_setexactkeypos_.htm
source: Advantage CHM
tags:
  - vo
checksum: 7ee8cd39f70ea0fabb986d90eca5e80842348ee6
---

# Vo Ax Setexactkeypos

AX\_SetExactKeyPos()

AX\_SetExactKeyPos()

Advantage Visual Objects and Vulcan.NET RDD

| AX\_SetExactKeyPos()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Returns and sets the Exact Key Position Flag.

Syntax

AX\_SetExactKeyPos( [.T. | .F.] ) -> logical

[.T.|.F.] A logical value used to set the Exact Key Position TRUE (.T.) or FALSE (.F.).

Returns

If no parameter is passed to AX\_SetExactKeyPos(), then it returns the current Exact Key Position setting. If a parameter is passed to AX\_SetExactKeyPos(), then it returns previous Exact Key Position setting.

Description

The Exact Key Position setting is used internally by the Advantage RDD in calls to OrderKeyNo(). By setting Exact Key Position to false, Advantage will return an estimation of the key number. This provides a faster, but less accurate, method of obtaining the current key number. This is useful for applications that utilize the key number intensively (for example bBrowser). The default Exact Key Position setting is TRUE.

Example

oDB := AxDBServer{ "TEST", .F., .F., "AXDBFCDX" }

 

// With the default Exact Key Position setting, Advantage will compute the exact key number that can be expensive

lKeyNo := oDB:OrderKeyNo()

 

AX\_SetExactKeyPos( .F. )

// With Exact Key Position set to false, Advantage will return an estimate of the key number which should be much faster

lKeyNo := oDB:OrderKeyNo()
