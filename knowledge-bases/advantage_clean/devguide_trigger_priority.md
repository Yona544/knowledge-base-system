---
title: Devguide Trigger Priority
slug: devguide_trigger_priority
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_trigger_priority.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: aae2f47d412a66343aebc183608b606a6ef05a29
---

# Devguide Trigger Priority

Trigger Priority

     Trigger Priority

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Trigger Priority  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

When you define a trigger, you can assign a value to it that identifies the priority of the trigger. Trigger priority is used when you have two or more triggers of the same trigger type and event type on a given table. The trigger with a lower priority value gets executed before triggers with a higher priority value.

For example, imagine that you have two AFTER insert triggers on a particular table. If one of these triggers has a priority of 1, and the other has a priority of 2, the trigger with a priority of 1 will execute first, followed by the trigger with a priority of 2.

Trigger priority only applies to BEFORE and AFTER triggers. It does not apply to INSTEAD OF triggers. This is because you can have only one INSTEAD OF trigger for a given event type per table.
