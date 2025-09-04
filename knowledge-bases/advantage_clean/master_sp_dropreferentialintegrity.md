---
title: Master Sp Dropreferentialintegrity
slug: master_sp_dropreferentialintegrity
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_dropreferentialintegrity.htm
source: Advantage CHM
tags:
  - master
checksum: d9f61e67762db6471f8bc32fe98d7db30d51082c
---

# Master Sp Dropreferentialintegrity

sp\_DropReferentialIntegrity

sp\_DropReferentialIntegrity

Advantage SQL Engine

| sp\_DropReferentialIntegrity  Advantage SQL Engine |  |  |  |  |

Removes a referential integrity (RI) constraint from the data dictionary.

Syntax

sp\_DropReferentialIntegrity( Name,CHARACTER,200 )

Parameters

| Name (I) | Name of the RI constraint in the data dictionary to be removed. |

Remarks

sp\_DropReferentialIntegrity will remove a RI constraint from the data dictionary.

The parent and child table must not be opened, so that the Advantage Database Server can temporarily open the parent and the child tables exclusively. This function will temporarily open all tables exclusively that are in the data dictionary and that interlink with these tables through other RI constraints

Example

EXECUTE PROCEDURE sp\_DropReferentialIntegrity( salesreps\_has\_office );

See Also

[system.relations](master_system_relations.md)

[sp\_CreateReferentialIntegrity](master_sp_createreferentialintegrity.md)
