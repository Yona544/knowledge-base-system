---
title: Devguide Exception Handling
slug: devguide_exception_handling
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_exception_handling.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 12cbc33aa236dd627d8fb5ee2600aa190b4f4169
---

# Devguide Exception Handling

Exception Handling

     Exception Handling

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Exception Handling  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage SQL scripts employ an exception model of error handling. With an exception model, you define blocks of code in which an exception may be raised. You can then provide several additional related blocks of code. These blocks can be designed to catch exceptions that are raised, or they can be designed to execute cleanup code that is unconditionally executed, whether or not an exception occurs.

If you do not implement exception handling in an Advantage SQL script and an exception is raised, your script will immediately terminate abnormally. By including exception handling in your script, you can manage any conditions that cause an exception and permit your script to continue executing normally (or you can programmatically decide to terminate your script). You can also effectively manage resources that would otherwise be at risk if an exception were encountered.

You use the keyword TRY to define the beginning of an exception-handling block. Complete the block using one of the following keywords: END, ENDTRY, or END TRY.

TRY blocks can be nested. Specifically, one or more TRY blocks may appear within a TRY block.

You also need to define one or more additional blocks at the end of the TRY block. As has already been mentioned, these additional blocks are used to either catch exceptions or unconditionally execute cleanup code. These blocks are described in the following sections.

Catching Exceptions

Advantage SQL scripts provide two types of exception-catching blocks. The first of these is designed to catch a specific type of exception, and a TRY block may contain zero or more of these blocks. The second is designed to catch any and all exceptions. Let's begin by considering the first type of block.

You use the CATCH keyword to define an exception-catching block that catches a specific type of exception. You follow the CATCH keyword with an identifier indicating which exception type you want to catch within the block. The most common type of exception is a runtime exception. You use the identifier ADS\_SCRIPT\_EXCEPTION to catch this type of exception.

All other types of exceptions are associated with exceptions explicitly raised by your code. The specific identifier you use for these exceptions is the identifier you define in your call to the keyword RAISE. RAISE is described later in this section.

Within a CATCH block, you can use the readonly \_ \_errcode, \_ \_errclass, and \_ \_errtext system variables to obtain detailed information about the exception. (The names of each of these system variables begin with two consecutive underscore characters.) Furthermore, \_ \_errclass and \_ \_errtext are String variables, while \_ \_errcode is an integer.

The \_ \_errclass variable contains the name of the type of exception. When a runtime exception is caught, this string contains the value ADS\_SCRIPT\_EXCEPTION. For exceptions raised explicitly in your code, this is the name of the raised exception.

For runtime exceptions, the \_ \_errcode variable contains the Advantage error code associated with the exception, and \_ \_errtext contains the corresponding error message. For explicitly raised exceptions, \_ \_errcode and \_ \_errtext contain the error code and error message of the raised exception, respectively.

The second form of the CATCH statement uses the CATCH ALL keywords. This CATCH block will catch any and all exceptions that occur within the TRY block. You can then use the \_ \_errcode, \_ \_errclass, and \_ \_errtext system variables to determine what exception has occurred and how to deal with it.

When two or more CATCH blocks appear in a TRY statement, the CATCH blocks are processed in order of appearance. Once one of the CATCH blocks catches the exception, no additional catch blocks are evaluated.

Furthermore, while it is possible to combine both CATCH and CATCH ALL in the same TRY statement, CATCH ALL should be the last catch block. Otherwise, no CATCH statement will be evaluated (since CATCH ALL, by definition, will catch any exception).

When an exception is handled by a CATCH or CATCH ALL block, the exception condition is canceled and the script will continue executing normally as though no exception occurred, unless the exception is re-raised from within the processing CATCH or CATCH ALL block. Re-raising an exception is described later in this section.

Using a FINALLY Block

A TRY block can have an optional FINALLY block. A FINALLY block is one that is designed to execute regardless of whether or not an exception occurred within the TRY block.

In most cases, FINALLY blocks are used for cleanup. For example, if you open a cursor in a TRY block, you can close the cursor in the FINALLY block.

A FINALLY block, when present, is the last block in a TRY block. If an exception occurs within the TRY block, and there are no CATCH blocks, the code in the FINALLY block will execute, after which the TRY block will terminate. If the TRY block is contained within another TRY block, the outer TRY block will process the exception. For example, if an appropriate CATCH block is present in the outer TRY block, it will process the exception.

If an exception is raised in a TRY block and not caught by an appropriate CATCH block, the FINALLY block, if present, will execute. When the FINALLY block exits, if there is no outer TRY block, the script will immediately terminate abnormally.

A FINALLY block also executes if a TRY completes without an exception being raised. In this case, once the FINALLY block exits, the script will continue executing with the first statement after the END, ENDTRY, or END TRY keywords.

The following script segment demonstrates the use of TRY, CATCH, and FINALLY. It also demonstrates the use of RAISE. RAISE is discussed in the following section:

 

TRY  
  WHILE FETCH Cur DO  
    i = 1;  
    WHILE FETCH Cur DO  
      i = i + 1;  
      IF i = 10 THEN  
        LEAVE;  
      END IF;   
    END WHILE;  
    IF i < 10 THEN  
      RETURN;  
    END IF;  
    INSERT INTO \_\_output Values(Cur.[Invoice No]);  
  END WHILE;  
CATCH ALL  
  INSERT INTO [ErrorLog] VALUES (\_\_errcode, \_\_errtext);

 RAISE;  
FINALLY  
  CLOSE Cur;  
END TRY;

   
NOTE: The preceding code segment assumes that there were previously defined variables, i and Cur, and that a table named ErrorLog exists containing an integer field and a string field. Presumably, this ErrorLog table is used to log application errors.  
 

Raising or Re-Raising Exceptions

When a runtime error occurs in your Advantage SQL script, an exception identified by the ADS\_SCRIPT\_EXCEPTION identifier is raised. You can also raise exceptions explicitly in code.

To raise an exception, use the RAISE keyword followed by your custom exception identifier. The custom exception identifier must be a valid variable name. The variable name, however, does not get explicitly declared in a DECLARE statement. Also, the identifier must be followed by an error code and error string, enclosed in parentheses.

For example, the following statement raises an exception that is identified by the custom Empty\_Table identifier. The custom error code and message of the exception are 2500 and Empty table not expected:

RAISE Empty\_Table(2500, 'Empty table not expected');

If you raise a custom exception from within a TRY block, there must either be a CATCH ALL block at the end of that TRY block or a specific CATCH for your custom exception. When the exception is caught, the \_ \_errclass system variable will contain the name of your custom identifier, and \_ \_errcode and \_ \_errtext will contain the integer and the string you passed in the call to RAISE, respectively. For example, when creating a CATCH block for the exception raised in the preceding code sample, you would use something similar to the following:

CATCH Empty\_Table  
  //statements here to handle the empty table condition  
  //\_\_errcode will be equal to 2500   
  //and \_\_errtext will be Empty table not excepted

Exceptions can also be raised outside of a TRY block, in which case, they will not be caught. These exceptions cause the script to terminate abnormally, which raises an exception in your invoking client application. Furthermore, raising an uncaught exception from within a SQL stored procedure or SQL trigger has the same effect as writing to the \_ \_error table.

There is a special use of RAISE that is specific to CATCH blocks. That is, if within a CATCH or CATCH ALL block you determine that you cannot handle the exception (and therefore cannot permit the script to continue executing normally), you execute the RAISE keyword. In this situation, you use the RAISE keyword alone, without an identifier, error code, or error message.

This use of RAISE is called re-raising. Re-raising promotes the exception outside of the TRY block in which the exception was caught.

If the TRY block from which an exception is re-raised is itself contained within another TRY block, and there exists an appropriate CATCH block, that CATCH block will then process the exception (which may also include re-raising the exception again). In all cases, however, if a CATCH block re-raises an exception, and the TRY block contains a FINALLY block, the FINALLY block is executed first, before the exception reaches the outer TRY block.

If you re-raise an exception and the catching TRY block is not wrapped in an outer TRY block, a state of exception exists, and the script will terminate abnormally after processing the FINALLY block (if present).
