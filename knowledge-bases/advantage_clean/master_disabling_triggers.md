---
title: Master Disabling Triggers
slug: master_disabling_triggers
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_disabling_triggers.htm
source: Advantage CHM
tags:
  - master
checksum: 0d49863b439bdf7ed5eef136d4dcc5840625d8d4
---

# Master Disabling Triggers

Disabling Triggers

Disabling Triggers

Advantage Concepts

| Disabling Triggers  Advantage Concepts |  |  |  |  |

Triggers can be disabled and enabled using the system procedures sp\_DisableTriggers and sp\_EnableTriggers. Changes to the disabled state of triggers take place immediately. Triggers can be disabled or enabled for the current user (connection), all database users, a single table, or a single trigger.

Current User

All triggers are disabled/enabled on the connection which made the request. This setting will not affect other connections made by the same database user. This setting is not persisted after the user disconnects. Note that [DB:Admin](master_database_base_roles.md) membership is required to use this functionality.

All Database Users

All triggers for all users of the current database are disabled/enabled. This setting is persisted.

Single Table

All triggers associated with a single table are disabled/enabled. This setting affects all database users and is persisted.

Single Trigger

A single trigger of a single table is disabled/enabled. This setting affects all database users and is persisted.
