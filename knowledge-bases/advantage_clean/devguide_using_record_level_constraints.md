---
title: Devguide Using Record Level Constraints
slug: devguide_using_record_level_constraints
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_using_record_level_constraints.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 3322033a2cdeda6cc00be223a1a6a0efb4d76ab5
---

# Devguide Using Record Level Constraints

Using Record-Level Constraints

     Using Record-Level Constraints

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Using Record-Level Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Record-level constraints are more flexible than field-level constraints in that they can include some basic conditional logic. For example, a record-level constraint can be used to verify that a credit card field has been assigned a value, but only when the payment type is credit card.

The problem with record-level constraints is that it can be challenging to embody a complicated condition using a Boolean expression. When you must use a complicated Boolean expression with several conditional parts, it is very important to test the expression thoroughly to ensure that it does not reject records that are valid, and at the same time does not accept invalid records.

An alternative to using a complex record-level constraint is a trigger. Triggers can be written in a variety of high-level languages that can express complex conditional logic more easily than a Boolean expression. In addition, you can embed comments in your trigger code that identify what exactly your conditions are testing for. This is not something that you can do with a record-level constraint. Using triggers is described in Chapter 8.
