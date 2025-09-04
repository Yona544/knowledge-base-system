---
title: Devguide Creating Constraints
slug: devguide_creating_constraints
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_constraints.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 5593241425f8b1db5a86a65220bea7d6937eabd0
---

# Devguide Creating Constraints

Creating Constraints

 

     Creating Constraints

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Data dictionaries support three types of constraint definitions: field-level, record-level, and referential integrity. While there are some similarities between these various types of constraints, the steps you take to implement them are quite different. As a result, the creation of each constraint type is described in its own section.

Both field-level and record-level constraints are actually properties of dictionary-bound tables. There are other field and table-related properties as well. The need to discuss constraints provides us with a fine opportunity to consider these properties in general.
