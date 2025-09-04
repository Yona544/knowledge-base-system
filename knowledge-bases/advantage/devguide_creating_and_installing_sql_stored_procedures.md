Creating and Installing SQL Stored Procedures




Advantage Database Server 12  

     Creating and Installing SQL Stored Procedures

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating and Installing SQL Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating and Installing SQL Stored Procedures Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_and\_Installing\_SQL\_Stored\_Procedures Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 7 - Stored Procedures > Creating and Installing SQL Stored Procedures / Dear Support Staff, |  |
| Creating and Installing SQL Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

SQL stored procedures are the easiest stored procedure types to create. You do not need a third-party compiler. In fact, everything you need is provided by the Advantage Data Architect.

You create a SQL stored procedure at the same time that you install it. As a result, both the creation and installation of a SQL stored procedure is described in the following steps.

Use the following steps to create and install a SQL stored procedure:

If the DemoDictionary connection is not connected, connect it now. (Active Connection should be DEMODICTIONARY to the right of the Advantage Data Architect toolbar.)

Right-click the STORED PROC node of the DemoDictionary connection and select Create. The Advantage Data Architect displays the Stored Procedure dialog box shown in Figure 7-1.

Figure 7-1: The Stored Procedure dialog box

At Name, enter SQLGet10Percent.

In the Parameters section, set Name to CustID, Type to input, and DataType to integer.

Press the Down Arrow key to create a new parameter. (Alternatively, you can click the + sign button to add a new line.) Set Name to InvoiceNo, Type to output, DataType to character, and Size to 12.

Leave the Script tab selected in the Container Type section. Next, enter the SQL script shown in Listing 7-1 into the Script pane:

Listing 7-1

   
CODE DOWNLOAD: This listing is also located in listing7-1.txt on this book's code download (see Appendix A).  
 

DECLARE Cur CURSOR;  
DECLARE @CustID Integer;  
DECLARE RecCount Integer;  
DECLARE i Integer;  
@CustID = (SELECT [CustID] FROM \_\_input);  
RecCount = (SELECT Count(\*) FROM [Invoice]   
  WHERE [Customer ID] = @CustID);  
IF RecCount < 10 THEN  
  INSERT INTO \_\_error VALUES (2501,   
    'There are less than 10 invoices for ' +  
    CONVERT(@CustID, SQL\_CHAR));  
  RETURN;  
END IF;  
OPEN Cur AS SELECT [Invoice No], RAND() AS   
  [Random] FROM [Invoice]   
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

Click the Verify Syntax button at the bottom of the Script pane. Correct any errors before continuing. When you are done, click OK to save your new stored procedure and close the Stored Procedure dialog box.