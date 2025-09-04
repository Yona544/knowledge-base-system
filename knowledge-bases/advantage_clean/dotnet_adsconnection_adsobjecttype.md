---
title: Dotnet Adsconnection Adsobjecttype
slug: dotnet_adsconnection_adsobjecttype
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_adsobjecttype.htm
source: Advantage CHM
tags:
  - dotnet
checksum: aad0541a0dc7ea0ee2c582847b7f54f274455300
---

# Dotnet Adsconnection Adsobjecttype

AdsConnection.AdsObjectType

AdsConnection.AdsObjectType

Advantage .NET Data Provider

| AdsConnection.AdsObjectType  Advantage .NET Data Provider |  |  |  |  |

public enum AdsObjectType

AdsObjectType values are used to indicate the object type to retrieve in calls to GetDDObjects.

| Member Name | Description |
| TableObject | Retrieves the names of table objects. |
| ViewObject | Retrieves the names of view objects. |
| RelationObject | Retrieves the names of referential integrity definitions. |
| IndexFileObject | Retrieves the names of index file objects that are associated with the parent string parameter of GetDDObjects. |
| IndexObject | Retrieves the names of index orders that have been defined in any index file associated with the parent string parameter of GetDDObjects. |
| FieldObject | Retrieves the names of fields in the table specified by the parent string parameter of GetDDObjects. The object array of field names returned is in the same order that the fields appear in the table. |
| UserObject | Retrieves the names of user objects. If the parent string parameter of GetDDObjects is null or empty, the returned array will include the names of all users in the database. If the parent string parameter is not empty, it must specify a user group name, and the returned array will include all users who are members of that user group. |
| ProcedureObject | Retrieves the names of stored procedures. |
| LinkObject | Retrieves the names of a link object. |

See Also

[GetDDObjects](dotnet_adsconnection_getddobjects.md)
