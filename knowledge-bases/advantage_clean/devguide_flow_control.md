---
title: Devguide Flow Control
slug: devguide_flow_control
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_flow_control.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 60f9c8f40397d876e63487e6bba23553d7d11ec4
---

# Devguide Flow Control

Flow Control

     Flow Control

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Flow Control  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Control structures are keywords that provide for the conditional execution of code. Control structures do this by evaluating an expression, and based on the resulting Boolean value, either executing or not executing a block of code.

There are two types of control structures: branching and looping. A branching control structure evaluates a Boolean expression. If the expression evaluates to True, a block of one or more lines of code is executed. Branching control structures can also include additional blocks of one or more statements that are conditionally executed if the expression evaluates to False.

A looping control structure repeats a block of one or more statements zero or more times. A Boolean expression controls how many times the code block executes.

Advantage SQL scripts support one branching control structure and one looping control structure. These are described in the following sections.

Branching with IF

You use the IF control structure to conditionally execute a block of code. The IF statement begins with the keyword IF, followed by a Boolean expression and the keyword THEN. If the Boolean expression evaluates to True, the one or more statements that follow the THEN keyword are executed. The IF statement is terminated by any one of the following keywords: END, ENDIF, or END IF.

The IF statement can optionally include one or more ELSEIF statements and/or an ELSE statement. When ELSEIF appears, it is followed by another Boolean expression, the THEN keyword, and another statement block. The statements that follow ELSEIF are executed if the Boolean expression following IF evaluates to False and the expression following ELSEIF is True. If there are more than one ELSEIF statements, they are evaluated in order. Once one of the ELSEIF expressions evaluates to True, no remaining ELSEIF conditions are evaluated and the IF statement terminates.

While there may be more than one ELSEIF statement, there can be only one optional ELSE statement. ELSE, when present, can be followed by one or more statements, after which the END, ENDIF, or END IF keywords must appear. The statements that follow ELSE execute if and only if the expression following IF evaluates to False, and all ELSEIF expressions, if present, also evaluate to False.

The following is a code segment that demonstrates an IF statement:

DECLARE Length Integer;  
SET Length = (SELECT COUNT(\*) FROM CUSTOMER);  
CREATE TABLE #TEMP (Data CICHAR(40));  
If Length < 5 THEN  
  INSERT INTO #TEMP VALUES('Less than five');  
ELSEIF Length < 10 THEN  
  INSERT INTO #TEMP VALUES('Between five and ten');  
ELSE   
  INSERT INTO #TEMP VALUES('More than nine');  
ENDIF;  
SELECT Data FROM #TEMP;

Looping with WHILE

You use the WHILE looping control structure to execute a block of code zero or more times. The WHILE keyword is followed by a Boolean expression and the keyword DO. If the expression evaluates to True, the statements that follow DO are executed.

The WHILE control structure is terminated by one of the following keywords: END, ENDWHILE, or END WHILE. When the Boolean expression following WHILE evaluates to True and the code segment is executed, control returns to the WHILE expression when execution reaches the END, ENDWHILE, or END WHILE keywords. At that point the Boolean expression is re-evaluated.

The loop created by the WHILE keyword will repeat until the Boolean expression evaluates to False or the LEAVE keyword is executed inside the loop.

LEAVE is one of two special keywords that can appear inside of a looping control structure. As mentioned in the preceding paragraph, a looping control structure terminates immediately if the LEAVE keyword is executed inside the loop. By comparison, when the CONTINUE keyword is executed inside of the loop, all remaining statements in the loop are ignored and control returns to the top of the loop where the Boolean expression is re-evaluated.

The following is an example of a WHILE loop:

DECLARE Times Integer;  
Times = 1;  
WHILE Times < 10 DO  
  Times = Times + 1;  
END WHILE;

Nested Control Structures

Control structures can be nested. Specifically, a looping control structure can appear within a conditional code block, and a conditional code block can appear within a loop. Similarly, one looping control structure can appear within another and a conditional code block can appear within a conditional code block.

When control structures are nested, they must appear entirely within a single code block. For example, when a WHILE statement is nested within an IF statement, the END, ENDWHILE, or END WHILE keywords must appear in the same code block as the WHILE keyword, appearing before the next ELSEIF, ELSE, or ENDIF (or END or END IF) keywords of the IF statement.

Using RETURN

There is one more keyword that is not technically a control structure, although it does perform a flow-control-related task. This keyword is RETURN.

When RETURN executes, the script immediately terminates normally, with one exception. If RETURN is executed within one or more TRY blocks, and those TRY blocks contain one or more FINALLY blocks, all relevant FINALLY blocks will execute before the script terminates.

TRY and FINALLY blocks are discussed later in this section.
