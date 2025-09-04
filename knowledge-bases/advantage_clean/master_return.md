---
title: Master Return
slug: master_return
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_return.htm
source: Advantage CHM
tags:
  - master
checksum: 7192b3a0c64a5fc41845dd4b008a1361f2c59502
---

# Master Return

RETURN

RETURN

Advantage SQL Engine

| RETURN  Advantage SQL Engine |  |  |  |  |

Terminates the execution of the current script.

Syntax

RETURN [expr];

Description

The RETURN statement terminates the execution of the current script. The optional expr may be specified to return the result of a [user defined function](master_user_defined_function.md). If the script is not part of the user defined function, it is an error to specify expr.

Example 1

// This sample script opens a cursor. If there is an error opening the

// cursor, exit without returning an error

 

DECLARE cursor1 AS SELECT \* FROM #Inpupt;

 

TRY

 OPEN cursor1;

CATCH ALL

 RETURN;

END TRY;

 

// Other processing using the cursor

Example 2

// Create a user defined function calculates the square

// of an integer number

CREATE FUNCTION square( i Integer )

RETURNS Integer

BEGIN

 RETURN i \* i;

END;
