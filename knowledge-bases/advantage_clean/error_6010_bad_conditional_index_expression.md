---
title: Error 6010 Bad Conditional Index Expression
slug: error_6010_bad_conditional_index_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6010_bad_conditional_index_expression.htm
source: Advantage CHM
tags:
  - error
checksum: 5704a9b456881474453617c57387744a37857e07
---

# Error 6010 Bad Conditional Index Expression

6010 Bad conditional index expression

6010 Bad conditional index expression

Advantage Error Guide

| 6010 Bad conditional index expression  Advantage Error Guide |  |  |  |  |

Problem: An invalid expression was encountered while creating or opening an index.

Solution: Make sure the key expression (and FOR condition expression, if applicable) is a valid Xbase expression. If a User-Defined Function (UDF) is used in an expression, verify it is available in all applications that use the index.
