---
title: Devguide Writing Sql Scripts
slug: devguide_writing_sql_scripts
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_writing_sql_scripts.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 4c7144f0abf0c97c56bebfd9327f3ea9b2f8cec5
---

# Devguide Writing Sql Scripts

Writing SQL Scripts

 

     Writing SQL Scripts

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Writing SQL Scripts  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage SQL scripts are text strings that contain two or more SQL statements, separated by semicolons. You can write them using any text editor, such as Notepad.exe, Wordpad.exe, or emacs.

However, when you are using the Advantage Data Architect, you will most likely write your Advantage SQL scripts using the SQL Utility. Not only does the SQL Utility permit you to write and edit your Advantage SQL scripts, but it also permits you to verify their syntax as well as execute the scripts.

The following is an example of an Advantage SQL script:

DECLARE ProdCur CURSOR AS SELECT \* FROM PRODUCTS;  
DECLARE SqlStmt String;  
OPEN ProdCur;  
WHILE FETCH ProdCur DO  
  IF ProdCur.[Retail Price] < 100 THEN  
    SqlStmt = 'UPDATE PRODUCTS '+  
      'SET [Retail Price] = [Retail Price] \* 1.2 ' +  
      'WHERE [Product Code] = ''' +   
        TRIM(ProdCur.[Product Code]) + '''';  
    EXECUTE IMMEDIATE SqlStmt;  
  ELSEIF ProdCur.[Retail Price] < 200 THEN  
    SqlStmt = 'UPDATE PRODUCTS '+  
      'SET [Retail Price] = [Retail Price] \* 1.1 ' +  
      'WHERE [Product Code] = ''' +   
        TRIM(ProdCur.[Product Code]) + '''';  
    EXECUTE IMMEDIATE SqlStmt;  
  ELSE  
    SqlStmt = 'UPDATE PRODUCTS '+  
     'SET [Retail Price] = [Retail Price] \* 1.05 ' +  
     'WHERE [Product Code] = ''' +   
       TRIM(ProdCur.[Product Code]) + '''';  
    EXECUTE IMMEDIATE SqlStmt;  
  END IF;  
END WHILE;

Note that the preceding script is not formally declared in a block such as a BEGIN END block, or a { ... } block. Only when the Advantage SQL script is being created as part of a CREATE PROCEDURE, CREATE TRIGGER, or CREATE FUNCTION statement do the script's contents need to be delimited. Specifically, when using the CREATE SQL statement, the Advantage SQL script appears between the BEGIN and END keywords. For example, the following is the CREATE TRIGGER declaration for the SQLGet10Percent stored procedure that you created in Chapter 7:

CREATE PROCEDURE SQLGet10Percent(CustID INTEGER,   
  InvoiceNo CHAR ( 12 ) OUTPUT)  
BEGIN   
  DECLARE Cur CURSOR;  
  DECLARE @CustID Integer;  
  DECLARE RecCount Integer;  
  DECLARE i Integer;  
  @CustID = (SELECT [CustID] FROM \_\_input);  
  RecCount = (SELECT Count(\*) FROM [Invoice] WHERE   
    [Customer   ID] = @CustID);   
  IF RecCount < 10 THEN  
    INSERT INTO \_\_error VALUES (2501,   
      'There are less than 10 invoices for ' +  
      CONVERT(@CustID, SQL\_CHAR));  
    RETURN;  
  END IF;  
  OPEN Cur AS SELECT [Invoice No], RAND() AS [Random]   
    FROM Invoice]   
    WHERE [Customer ID] = @CustID ORDER BY [Random];  
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
    INSERT INTO \_\_error VALUES (\_\_errcode, \_\_errtext);  
  FINALLY  
    CLOSE Cur;  
  END TRY;  
END

In addition to SQL statements, like those described in Chapters 12 and 14, Advantage SQL scripts can include variable declarations, variable assignment, control structures, cursors, exception handling, and customized statement caching. Each of these capabilities is described in the following sections. Advantage SQL scripts can also include calls to user defined functions. User defined functions are described later in this chapter.
