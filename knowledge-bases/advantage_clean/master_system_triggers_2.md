---
title: Master System Triggers 2
slug: master_system_triggers_2
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_triggers_2.htm
source: Advantage CHM
tags:
  - master
checksum: 1e22d3e125dfbfc7ba688f78fdc2d1972e00a821
---

# Master System Triggers 2

system.ansi\_triggers

system.ansi\_triggers

Advantage SQL Engine

| system.ansi\_triggers  Advantage SQL Engine |  |  |  |  |

Contains one row for each trigger in the database.

| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Trigger name. |
| Trig\_TableName | Character | 200 | The table the trigger is assigned to. For [database triggers](master_database_triggers.md), this is null. |
| Trig\_Event\_Type | Integer | 4 | The type of event that causes a trigger to fire. |
| Trig\_Trigger\_Type | Integer | 4 | The kind of event the trigger should fire on. |
| Trig\_Container\_Type | Integer | 4 | The type of container holding the trigger. |
| Trig\_Container | NMemo | variable | The name of the trigger container. This value varies depending on the container type. |
| Trig\_Function\_Name | Character | 260 | The name of the function called when the trigger is executed. |
| Trig\_Priority | Integer | 4 | Determines when the trigger is fired in relation to other triggers. |
| Trig\_Options | Integer | 4 | Options for the trigger in numeric format. |
| Comment | Memo | variable | The description of the trigger. |
