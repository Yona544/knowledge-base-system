---
title: Error 7099 The Full Text Search Condition Has An Invalid Distance Specified For The Near Operator
slug: error_7099_the_full_text_search_condition_has_an_invalid_distance_specified_for_the_near_operator
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7099_the_full_text_search_condition_has_an_invalid_distance_specified_for_the_near_operator.htm
source: Advantage CHM
tags:
  - error
checksum: cfff00b15da908deaebf629c23074837ae2a4283
---

# Error 7099 The Full Text Search Condition Has An Invalid Distance Specified For The Near Operator

7099 The full text search condition has an invalid distance specified for the NEAR operator

7099 The full text search condition has an invalid distance specified for the NEAR operator

Advantage Error Guide

| 7099 The full text search condition has an invalid distance specified for the NEAR operator  Advantage Error Guide |  |  |  |  |

Problem: The full text search condition specified in a CONTAINS() function has an invalid distance parameter specified for the NEAR operator.

Solution: Verify that the NEAR parameter value is numeric. The NEAR operator can have an optional distance value specified in parentheses. The distance value must be a numeric value. For example, the following search condition is not valid because the parser expects the distance operator to be given:

dog near (cat and mouse)

The following search conditions are valid:

dog near() (cat and mouse)

dog near(5) cat

dog near cat
