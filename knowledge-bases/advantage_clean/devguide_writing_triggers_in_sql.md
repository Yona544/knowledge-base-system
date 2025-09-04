---
title: Devguide Writing Triggers In Sql
slug: devguide_writing_triggers_in_sql
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_writing_triggers_in_sql.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 3f2f02e8dd6926fedb0c9d7f612b6cfb3d29eb1a
---

# Devguide Writing Triggers In Sql

Writing Triggers in SQL

     Writing Triggers in SQL

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Writing Triggers in SQL  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Triggers that are implemented using SQL scripts are easy to create and maintain in your data dictionary, and do not require any additional tools to create them. From within a SQL script, you can write one or more SQL statements (with the statements being separated by semicolons). These SQL statements can reference the tables of your data dictionary, free tables, and tables in other data dictionaries for which your data dictionary has defined links.

Your SQL statements also are likely to make use of the \_ \_old table (for DELETE, UPDATE, and ON CONFLICT triggers) and the \_ \_new table (for INSERT, UPDATE, and ON CONFLICT triggers).

Use the following steps to create two triggers, one for archiving customer table records and the other to restore archived customer records:

1.        With the DemoDictionary connection open and active in the Connection Repository, expand the TABLES node (if it is not already expanded).

| 2. | Right-click the CUSTOMER table and select Triggers. The Advantage Data Architect responds by displaying the Triggers dialog box shown in Figure 8-2. |

Figure 8-2: The Triggers dialog box

3.         Set Trigger Type to INSTEAD OF, and Event Type to DELETE. Leave Priority set to 1.

| 4. | Enter the following SQL statement into the Script pane (The Script tab should be selected): |

Listing 8-1

   
CODE DOWNLOAD: This listing is also located in listing8-1.txt on this book's code download (see Appendix A).  
 

DECLARE @CustID Integer;  
DECLARE @RecCount Integer;  
   
//Get the Customer ID  
@CustID = (SELECT [Customer ID] from \_\_old);  
@RecCount = (SELECT COUNT(\*) FROM INVOICE   
             WHERE [Customer ID] = @CustID   
             AND [Date Payment Received] IS NULL);  
   
   
IF @RecCount > 0 THEN  
  //Customer has unpaid invoices  
  RAISE OutstandingInvoices(2502,   
    'Customer ' + TRIM(CONVERT(@CustID, SQL\_CHAR)) +   
    ' has outstanding invoices. Cannot archive');  
END IF;  
   
//Move record to archive  
INSERT INTO CUST\_BAK   
      ([Customer ID], [First Name], [Last Name],  
      [Address], [City], [State], [Zip Code],  
      [Phone Number], [Notes], [Date Archived])   
  SELECT [Customer ID], [First Name], [Last Name],  
      [Address], [City], [State], [Zip Code],  
      [Phone Number], [Notes], CurDate() FROM \_\_old;  
   
//Remove record from CUSTOMER  
DELETE FROM [CUSTOMER]   
  WHERE [Customer ID] = @CustID;

5.        Since the CUSTOMER table includes a MEMO field, it is essential that both the "Include VALUES (\_ \_old and \_ \_new) tables" option and the "Include memo and blob data in VALUES tables" option are checked. Uncheck the "Use implicit transactions to maintain data integrity" option.

| 6. | Click OK. The Advantage Data Architect displays the Trigger Name dialog box. Set the trigger's name to Archive Customer and click OK. |

| 7. | Now right-click the CUST\_BAK table and select Triggers. |

| 8. | Set Trigger Type to INSTEAD OF, and set Event Type to DELETE. |

| 9. | Enter the following SQL statement in the Script pane: |

Listing 8-2

   
CODE DOWNLOAD: This listing is also located in listing8-2.txt on this book's code download (see Appendix A).  
 

DECLARE Cur CURSOR as SELECT [Customer ID]   
                        FROM CUSTOMER   
                        WHERE [Customer ID] =   
                        (SELECT [Customer ID]   
                           FROM \_\_old);  
   
//Check if Customer ID already in Customer table  
OPEN Cur;  
TRY  
  IF FETCH Cur THEN  
    RAISE CustomerExists(5551, 'Customer ' +  
      TRIM(CONVERT(Cur.[Customer Id], SQL\_CHAR)) +  
      ' already exists in CUSTOMER table');  
  END IF;  
FINALLY  
  CLOSE Cur;  
END;  
   
//Move Customer record back to Customer table  
INSERT INTO CUSTOMER ([Customer ID], [Last Name],   
  [First Name], [Address], [City], [State],  
  [Zip Code], [Phone Number], [Notes])   
  SELECT [Customer ID], [Last Name], [First Name],  
    [Address], [City], [State], [Zip Code],  
    [Phone Number], [Notes]   
  FROM \_\_old;  
   
//Remove the record from CUST\_BAK  
DELETE FROM CUST\_BAK WHERE [Customer ID] IN   
  (SELECT [Customer ID] FROM \_\_old);

10.        Ensure that the "Include VALUES (\_ \_old and \_ \_new) tables" option and the "Include memo and blob data in VALUES tables" option are checked. Uncheck the "Use implicit transactions to maintain data integrity" option.

| 11. | Click OK. When the Trigger Name dialog box is displayed, set the trigger name to Restore Customer and click OK. |

These two triggers are now created and configured. If you want to test how they work, you can open the CUSTOMER table in the Table Browser. Insert a new record and enter a unique customer ID, and a first and last name. Click the Post button in the navigator to save the new record.

With your cursor on the newly inserted record, click the Delete button in the navigator. Two things happen. First, the record is deleted from the CUSTOMER table. Second, this record is inserted into the CUST\_BAK table, along with the date that the record was archived. You can see this by opening the CUST\_BAK table in the Table Browser.

   
CAUTION: SQL Triggers are cached until all users who have executed it disconnect. If you change a SQL trigger, the updated trigger will not be employed until all users who have executed the old version have disconnected from the data dictionary.
