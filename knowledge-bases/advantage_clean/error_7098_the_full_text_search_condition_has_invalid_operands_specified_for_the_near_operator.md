---
title: Error 7098 The Full Text Search Condition Has Invalid Operands Specified For The Near Operator
slug: error_7098_the_full_text_search_condition_has_invalid_operands_specified_for_the_near_operator
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7098_the_full_text_search_condition_has_invalid_operands_specified_for_the_near_operator.htm
source: Advantage CHM
tags:
  - error
checksum: 076ec348c059bc295c317b6967c465e30fd38e13
---

# Error 7098 The Full Text Search Condition Has Invalid Operands Specified For The Near Operator

7098 The full text search condition has invalid operands specified for the NEAR operator

7098 The full text search condition has invalid operands specified for the NEAR operator

Advantage Error Guide

| 7098 The full text search condition has invalid operands specified for the NEAR operator  Advantage Error Guide |  |  |  |  |

Problem: The full text search condition specified in a CONTAINS() function has invalid operands specified for the NEAR operator. The NEAR operator cannot have a NOT condition as an operand..

Solution: Verify the operands to the NEAR operator do not contain NOT conditions. For example, the following two search conditions are not valid:

"(medical and not doctor) near hospital"

"landscaping near () (not shrubbery)"

The following two are valid:

"medical near hospital and not (doctor near hospital)"

"not (landscaping near shrubbery)"
