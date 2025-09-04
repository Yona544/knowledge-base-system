---
title: Error 5124 Ae Concurrent Problem
slug: error_5124_ae_concurrent_problem
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5124_ae_concurrent_problem.htm
source: Advantage CHM
tags:
  - error
checksum: 12090fbeae3918ae6e3b37f1c872f6b9eb074c17
---

# Error 5124 Ae Concurrent Problem

5124 AE\_CONCURRENT\_PROBLEM

5124 AE\_CONCURRENT\_PROBLEM

Advantage Error Guide

| 5124 AE\_CONCURRENT\_PROBLEM  Advantage Error Guide |  |  |  |  |

The application deleted an Advantage handle at the same time it attempted to use the handle.

Note to Advantage TDataSet Descendant users: If you are writing a multi-threaded application (for example, a Web application) it is possible to get this error if you have not uniquely named each TAdsConnection component. For further explanation and an example see the topic, Building Multi-Threaded Applications with TAdsQuery and TAdsTable in the Advantage TDataSet Descendant Help documentation (ADE.HLP). (Note that each of the Advantage products and their corresponding Help files are installed separately.)
