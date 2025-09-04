---
title: Error 2221 Cursor Already Open
slug: error_2221_cursor_already_open
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2221_cursor_already_open.htm
source: Advantage CHM
tags:
  - error
checksum: e8aa913cfbc3c46799d2ba34b112f25db4296ea6
---

# Error 2221 Cursor Already Open

2221 Cursor already open

2221 Cursor already open

Advantage Error Guide

| 2221 Cursor already open  Advantage Error Guide |  |  |  |  |

Problem: An SQL script statement is attempting to open a cursor that is already opened.

Solution: Check the error message for the location of the error in the script. Make sure the OPEN statement at that location is not attempting to open a cursor that has been opened by a statement executed prior to this statement.
