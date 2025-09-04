---
title: Master System Relations
slug: master_system_relations
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_relations.htm
source: Advantage CHM
tags:
  - master
checksum: d2f88056616cc8791689f98ec6a79e452526b67a
---

# Master System Relations

system.relations

system.relations

Advantage SQL Engine

| system.relations  Advantage SQL Engine |  |  |  |  |

Contains one row for each referential integrity constraint in the database.

| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Referential integrity constraint name. |
| RI\_Primary\_Table | Character | 200 | The name of the primary table. |
| RI\_Primary\_Index | Character | 200 | The name of the primary key used in the referential integrity constraint. |
| RI\_Foreign\_Table | Character | 200 | The name of the foreign table. |
| RI\_Foreign\_Index | Character | 200 | The name of the foreign key used in the referential integrity constraint. |
| RI\_UpdateRule | ShortInt | 2 | The numeric representation of the update rule used by the referential integrity constraint. |
| RI\_DeleteRule | ShortInt | 2 | The numeric representation of the deletion rule used by the referential integrity constraint. |
| RI\_No\_Pkey\_Error | Memo | variable | The custom error message returned when a new foreign key value does not exist in the primary key. |
| RI\_Cascade\_Error | Memo | variable | The custom error message returned when a cascading update or delete fails. |
