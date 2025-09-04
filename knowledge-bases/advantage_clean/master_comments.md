---
title: Master Comments
slug: master_comments
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_comments.htm
source: Advantage CHM
tags:
  - master
checksum: f236e82a51125356eeca88703e251e06da69d92c
---

# Master Comments

Comments

Comments

Advantage SQL Engine

| Comments  Advantage SQL Engine |  |  |  |  |

Comment text can be embedded in the SQL statements. Advantage SQL engine supports 3 types of comment text:

- Comments starting with the "/\*" delimiter and ending with the "\*/" delimiter. Example:

SELECT Lastname, Firstname FROM Employee ORDER BY 1, 2 /\* sort on the lastname and firstname \*/

- Comments starting with the "--" delimiter and ending at the next new-line character or at the end of the statement. Example:

SELECT \* FROM Employees -- Employee information table

WHERE Lastname > 'W'

- Comments starting with the "//" delimiter and ending at the next new-line character or at the end of the statement. Example:

SELECT \* FROM Employees // Employee information table

WHERE Lastname > 'W'
