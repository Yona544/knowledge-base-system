---
title: Master Nested And Recursive Triggers
slug: master_nested_and_recursive_triggers
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_nested_and_recursive_triggers.htm
source: Advantage CHM
tags:
  - master
checksum: 70bdbeff35b9534a51f4dddbd6ae5fc66ab0ca7f
---

# Master Nested And Recursive Triggers

Nested and Recursive Triggers

Nested and Recursive Triggers

Advantage Concepts

| Nested and Recursive Triggers  Advantage Concepts |  |  |  |  |

Nested triggers (performing an operation in one trigger, which causes another trigger to fire) and recursive triggers are supported.

Nested and recursive triggers are limited to 64 levels of server re-entrance before an error is returned. This prevents a run-away trigger from hogging CPU time and an Advantage worker thread.

INSTEAD OF and AFTER triggers do not support recursion when called on the base table that they are assigned to. These triggers are allowed to operate on the base table without firing themselves again. However, if these triggers modify some other table that has a trigger, that trigger will be fired.
