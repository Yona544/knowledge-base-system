---
title: Master Triggers On Static Views
slug: master_triggers_on_static_views
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_triggers_on_static_views.htm
source: Advantage CHM
tags:
  - master
checksum: dcd9a69c10d1f031ced8f9ccec3e039b0e79f038
---

# Master Triggers On Static Views

Triggers on Static Views

Triggers on Static Views

Advantage Concepts

| Triggers on Static Views  Advantage Concepts |  |  |  |  |

Triggers can be defined on views for the purpose of manually updating tables used by static views. Normally, static views are not updatable, but by defining a trigger on a static view, the trigger can then perform updates to the underlying tables of the view. As a convenience, the static cursor (temporary table) of a view will be updated in addition to firing the trigger. The theory here is that the trigger would update the underlying tables of the view, therefore, modifying the contents of the view.

Notes

Result sets populated by SELECT statements on static views are not updatable. Use UPDATE/INSERT/DELETE SQL statements or open the view directly (using AdsOpenTable for example) instead.
