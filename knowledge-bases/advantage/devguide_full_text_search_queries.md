Full Text Search Queries




Advantage Database Server 12  

     Full Text Search Queries

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Full Text Search Queries  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Full Text Search Queries Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Full\_Text\_Search\_Queries Advantage Developer's Guide > Part II - Advantage SQL > Chapter 12 - SQL to Perform Common Tasks > Full Text Search Queries / Dear Support Staff, |  |
| Full Text Search Queries  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Full text search (FTS) was added to Advantage in version 7.0. With this capability, you can search string and BLOB (binary large object) fields for specific strings and patterns.

Queries that perform full text searches make use of either the CONTAINS scalar function, the SCORE or SCOREDISTINCT scalar functions, or both.

Using CONTAINS

You use the CONTAINS scalar function in the WHERE clause of your query. CONTAINS is passed two parameters and evaluates to a Boolean expression. CONTAINS returns True for each record where the search criteria is found in the index or fields being searched, and False otherwise.

The first parameter of CONTAINS is either the name of a field or \* (asterisk). If you pass the name of the field in the first parameter, only the named field will be searched. Depending on the size of the table, this search can be significantly improved if the field already has an FTS index. If you pass \* in the first parameter, CONTAINS will search all of the available FTS indexes for the table being queried for the search criteria. You must have at least one FTS index on the table to use the \* operator.

The second parameter is a string containing the search criteria. The search criteria can include one or more strings, and can include the AND, OR, NOT, and NEAR operators. For example, the following query selects all records for which the Notes FTS index contains the word "birthday":

SELECT \* FROM CUSTOMER   
  WHERE CONTAINS(Notes, 'birthday')

The following query returns all records where any of the FTS indexes (though there is only one FTS index on the CUSTOMER table) contain either the word "birthday" or the word "card":

SELECT \* FROM CUSTOMER   
  WHERE CONTAINS(\*, 'birthday OR card')

The next example returns all records from the CUSTOMER table where the Notes index contains the words "birthday" and "card," but only if they are located in close proximity to one another using the NEAR(x) operator where x specifies the number of words. If you do not include (x), the default for NEAR is eight words.

SELECT \* FROM CUSTOMER   
  WHERE CONTAINS(Notes, 'birthday NEAR card')

Using SCORE and SCOREDISTINCT

You use the SCORE and SCOREDISTINCT integer functions in the SELECT list, WHERE clause, or ORDER BY clause of a query. These functions return the number of matches to the search criteria located during the search.

There are two syntax options for both the SCORE and the SCOREDISTINCT functions. The first option accepts the same parameters as does the CONTAINS scalar function. SCORE will return the total number of matches to the values specified in the search criteria, and SCOREDISTINCT returns the number of unique matches.

For example, consider the following query:

SELECT RTRIM("First Name") + ' ' + RTRIM("Last Name")  
    AS "Full Name",  
    SCORE(Notes, 'birthday OR card') AS "Count"  
  FROM CUSTOMER   
  WHERE CONTAINS(Notes, 'birthday OR card')

This query will return the customer name as well as the total number of instances of either birthday or card in the Notes field. By comparison, the following query, which uses the SCOREDISTINCT function, will return a count of either 1 or 2.

SCOREDISTINCT doesnt count the instances of the search criteria. It simply returns the number of criteria that were matched. Multiple instances of either birthday or card will be counted only once. As a result, SCOREDISTINCT is only used when searching for two or more words.

SELECT RTRIM([First Name]) + ' ' + RTRIM([Last Name])  
    AS "Full Name",  
    SCOREDISTINCT(Notes, 'birthday OR card') AS [Count]  
  FROM CUSTOMER   
  WHERE CONTAINS(Notes, 'birthday OR card')

Instead of passing the same parameters to SCORE and SCOREDISTINCT as you would to CONTAINS, you can pass a single integer parameter. When you pass an integer, that integer refers to one of the CONTAINS functions in the same query. If you pass 1, SCORE or SCOREDISTINCT will use the parameters of the first CONTAINS function call, while passing 2 means that there are at least two CONTAINS function calls, and SCORE or SCOREDISTINCT should use the arguments of the second instance.

For example, the following query returns the same result set as the preceding one:

SELECT RTRIM([First Name]) + ' ' + RTRIM([Last Name])  
    AS [Full Name],  
    SCOREDISTINCT AS [Count]  
  FROM CUSTOMER   
  WHERE CONTAINS(Notes, 'birthday OR card')

   
NOTE: A static cursor is returned when you use SCORE or SCOREDISTINCT in a SELECT clause. However, SCORE and SCOREDISTINCT can be used in an ORDER BY statement to rank the results for a live cursor.