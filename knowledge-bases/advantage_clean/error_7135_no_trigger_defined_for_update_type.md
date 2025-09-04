---
title: Error 7135 No Trigger Defined For Update Type
slug: error_7135_no_trigger_defined_for_update_type
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7135_no_trigger_defined_for_update_type.htm
source: Advantage CHM
tags:
  - error
checksum: 81b018027ad4787227743adb51e085bc82306dd0
---

# Error 7135 No Trigger Defined For Update Type

7135 No trigger defined for update type

7135 No trigger defined for update type

Advantage Error Guide

| 7135 No trigger defined for update type  Advantage Error Guide |  |  |  |  |

Problem: Triggers exist for the view, but not for the update type (INSERT, UPDATE, DELETE).

Solution: In order to update a static view, at least one trigger must exist for that update type. Create a trigger for that update type or do not perform that update to the static view.
