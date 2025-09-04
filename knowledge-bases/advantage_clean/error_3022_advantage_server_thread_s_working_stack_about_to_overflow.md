---
title: Error 3022 Advantage Server Thread S Working Stack About To Overflow
slug: error_3022_advantage_server_thread_s_working_stack_about_to_overflow
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3022_advantage_server_thread_s_working_stack_about_to_overflow.htm
source: Advantage CHM
tags:
  - error
checksum: 74c242bc942742421361d25fb3842bdc9f22bc24
---

# Error 3022 Advantage Server Thread S Working Stack About To Overflow

3022 Advantage server thread's working stack about to overflow

3022 Advantage server thread's working stack about to overflow

Advantage Error Guide

| 3022 Advantage server thread's working stack about to overflow  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The Advantage server thread's working stack was about to overflow. The problem is most likely due to an expression with a very large nesting of parentheses (hundreds of levels deep). This can occur when evaluating an Advantage Optimized Filter expression with a large number of OR operators on fields that are not indexed. It can also occur when evaluating the IN clause of an SQL statement on a field that is not indexed. For example, a query of the form "select \* from T where F in (1, 2, 3, 4, .... 3000 )" could produce a very deep nesting if the field "F" is not indexed.

Solution: Either reduce the number of items in the filter or query, or create an index on the field so that it is fully optimized.
