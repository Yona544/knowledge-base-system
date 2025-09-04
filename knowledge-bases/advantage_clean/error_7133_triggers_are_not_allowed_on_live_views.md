---
title: Error 7133 Triggers Are Not Allowed On Live Views
slug: error_7133_triggers_are_not_allowed_on_live_views
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7133_triggers_are_not_allowed_on_live_views.htm
source: Advantage CHM
tags:
  - error
checksum: 8c18784cc989fd12fa378b466086cc4e924bd3e2
---

# Error 7133 Triggers Are Not Allowed On Live Views

7133 Triggers are not allowed on live views

7133 Triggers are not allowed on live views

Advantage Error Guide

| 7133 Triggers are not allowed on live views  Advantage Error Guide |  |  |  |  |

Problem: A trigger was created on a live view. Triggers are only allowed on static views.

Solution: Create the trigger on the view's table or re-write the view such that it produces a static cursor.
