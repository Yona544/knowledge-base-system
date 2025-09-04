---
title: Master Relations Master Detail Relationships
slug: master_relations__master_detail_relationships_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_relations__master_detail_relationships_.htm
source: Advantage CHM
tags:
  - master
checksum: e63d81bf8a813f76ad6258c84a99adefd4934402
---

# Master Relations Master Detail Relationships

Relations (Master/Detail Relationships)

Relations (Master/Detail Relationships)

Advantage Concepts

| Relations (Master/Detail Relationships)  Advantage Concepts |  |  |  |  |

The Advantage TDataSet Descendant equivalent of the generic Advantage "Relation" concept is a called a "Master-Detail" relationship. The "parent" table is equivalent to the "master" table, and the "child" table is equivalent to the "detail" table.

Relations provide for a simple foreign key)primary key type relationship in ISAM file structures. Relations associate a "child" ("detail") table to a "parent" ("master") table through the child's index. When an application performs a record movement in the parent table, the child's current record is logically positioned. The actual movement in the child table is performed on demand for efficiency purposes rather than with each parent movement. The child record position is determined by seeking for a key resulting from evaluating the expression against the parent table's current record. The child is repositioned after the parent moves, but it is valid to navigate anywhere in the child table between movements in the parent.
