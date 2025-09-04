---
title: Master Movement Operations
slug: master_movement_operations
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_movement_operations.htm
source: Advantage CHM
tags:
  - master
checksum: a3aaed4577983a297d65da674543394d6ebece01
---

# Master Movement Operations

Movement Operations

Movement Operations

Advantage Concepts

| Movement Operations  Advantage Concepts |  |  |  |  |

There are several basic movement operations available for use on Advantage ISAM files. For the Advantage TDataSet Descendant, the following table shows the TDataSet specific method names for movement operations and the equivalent generic Advantage operations.

| TDataSet Specific Methods | Advantage Generic Operation |
| First | [Go Top](master_go_top_movement.md) |
| Last | [Go Bottom](master_go_bottom_movement.md) |
| FindKey, FindNearest, GotoKey, GotoNearest | [Seek](master_seek_movement.md) |
| Next, Prior, MoveBy | [Skip](master_skip_movement.md) |
| GotoBookmark | [Go To](master_go_to_movement.md) |
| Locate | \* |

\* Advantage does not have a direct equivalent to the Delphi/C++Builder specific Locate method. Advantage implements a Locate in the Advantage TDataSet Descendant by doing either a Seek or an [Advantage Optimized Filter](master_advantage_optimized_filters.md).

ADO Specific Methods/Properties

For the ActiveX Data Objects (ADO), the following table shows the ADO specific method names for movement operations and the equivalent generic Advantage operations.

| ADO Specific Methods/Properties | Advantage Generic Operation |
| MoveFirst | [Go Top](master_go_top_movement.md) |
| MoveLast | [Go Bottom](master_go_bottom_movement.md) |
| Seek | [Seek](master_seek_movement.md) |
| MoveNext, MovePrevious | [Skip](master_skip_movement.md) |
| \*\*Bookmark | [Go To](master_go_to_movement.md) |
| Find | [Locate](master_locate_movement.md) |

\*\* Setting the ADO Bookmark property to a valid record number is the same as doing an ISAM Go To when using ADO with the Advantage OLE DB Provider.
