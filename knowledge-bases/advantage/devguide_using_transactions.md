Using Transactions




Advantage Database Server 12  

 

     Using Transactions

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Transactions  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Using Transactions Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Using\_Transactions Advantage Developer's Guide > Part II - Advantage SQL > Chapter 12 - SQL to Perform Common Tasks > Using Transactions / Dear Support Staff, |  |
| Using Transactions  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You use transactions with Advantage to guarantee that changes that you want to apply to two or more records are performed in an all or none fashion. You begin a transaction using the BEGIN TRAN or BEGIN TRANSACTION keywords. Once the transaction has been started, you execute one or more queries to make changes to the data in your tables.

   
NOTE: The Advantage Local Server (ALS) ignores transaction-related instructions. In order to use transactions, you must use ADS.  
 

If the changes can be applied successfully, you issue the COMMIT WORK or COMMIT statement to make those changes permanent and to end the transaction. If at least one of the SQL statements failed, you issue a ROLLBACK WORK or ROLLBACK statement. ROLLBACK (or ROLLBACK WORK) restores any changes made during the transaction and ends the transaction.

From the perspective of ADS, it does not matter whether the transaction is controlled using SQL or calls to the Advantage Client Engine (ACE) APIboth are equivalent. For example, you can begin a transaction using BEGIN TRAN, and end a transaction by calling the AdsCommitTransaction function of the ACE API.

There are two approaches that you can take when using transactions in Advantage SQL. The first is to use an explicit transaction, and the other is to use an automatic transaction. Automatic transactions are discussed later in this section.

For most developers, the explicit transaction is the more useful one. In this usage, a transaction is started, two or more changes are made to the data, and then the transaction is committed. If, for whatever reason, all changes cannot be completed successfully (for example, an insert query raises an exception), the transaction should be rolled back.

How you manage the flow of the transaction depends on how you are making your changes to your data. If you are making all of your changes using a SQL script, you might begin and then commit or roll back your transaction entirely within the script. This can be accomplished using a TRY CATCH clause, like that shown in the following script:

BEGIN TRANSACTION;  
TRY  
  INSERT INTO #TEMP VALUES('Gordon Hall', NULL, 1000, True);  
  INSERT INTO #TEMP VALUES('Marti Schultz', NULL,   
    1000, True);  
  COMMIT WORK;  
CATCH ALL  
  ROLLBACK WORK;  
END;

Exception handling in SQL scripts using TRY CATCH is discussed in detail in Chapter 13.

On the other hand, you might manage the transaction through exception handling from your client programming language. For example, the following, which is in the Delphi language, demonstrates essentially the same process as in the preceding SQL script:

AdsConnection1.BeginTransaction;  
try  
  AdsTable1.AppendRecord(['Gordon Hall', nil, 1000, True]);  
  AdsTable1.AppendRecord(['Marti Schultz', nil,   
    1000, True]);  
  AdsConnection1.Commit;  
except  
  AdsConnection1.Rollback;  
end;

With explicit transactions, your code (however you decide to implement it) is responsible for beginning and committing the transaction, and rolling back the transaction if committing the transaction is not possible.