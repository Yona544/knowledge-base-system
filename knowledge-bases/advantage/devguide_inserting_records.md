Inserting Records




Advantage Database Server 12  

     Inserting Records

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Inserting Records  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Inserting Records Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Inserting\_Records Advantage Developer's Guide > Part II - Advantage SQL > Chapter 12 - SQL to Perform Common Tasks > Inserting Records / Dear Support Staff, |  |
| Inserting Records  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You insert data into a table using the INSERT SQL statement. At a minimum, you must specify which table data is being inserted into, as well as the values to insert into fields of the table, in order of the table's structure. For example, consider the following SQL script:

CREATE TABLE #TEMP (  
  [Full Name] CHAR(50),  
  [Number of Visits] SHORT,  
  [Credit Limit] MONEY,  
  [Active] LOGICAL);  
INSERT INTO #TEMP VALUES ('Bob Smith', 1, 1000, True);

The first statement creates a temporary table named #TEMP. The INSERT statement then inserts a single record into this table.

Using this syntax, you must supply a value for each field in the table. If you want to leave a particular field blank, use the NULL keyword. To insert default values into fields (when default values are defined for those fields in the data dictionary), use the DEFAULT keyword. This is shown in the following statements:

INSERT INTO #TEMP VALUES ('Julie Jones', NULL, NULL, NULL);  
INSERT INTO #TEMP VALUES ('Lee Singh', DEFAULT,   
  DEFAULT, DEFAULT);

If you want to insert data into only specific fields, you can follow the table name with a comma-separated list of the fields into which you want to insert data. This list of field names must be enclosed in parentheses. For example, the following query inserts data into the Full Name and Active fields:

INSERT INTO #TEMP ([Full Name], [Active])  
  VALUES ('Jose Luiz', True)

If the data you want to insert can be found in another table, you can replace the VALUES list with a subquery. For example, the following query inserts data from the EMPLOYEE table into #TEMP:

INSERT INTO #TEMP ([Full Name], [Active])  
  SELECT RTRIM([First Name]) + ' ' +   
      RTRIM([Last Name]), True   
    FROM EMPLOYEE  
    WHERE EMPLOYEE."Department Code" = 108

If the fields in the SELECT list match the type, order, and number of fields in the structure of the table you are inserting into, you can omit the list of fields being inserted into. This is demonstrated in the following query:

INSERT INTO #TEMP  
  SELECT RTRIM([First Name]) + ' ' + RTRIM([Last Name]),   
      1, 1000, True   
    FROM EMPLOYEE  
    WHERE EMPLOYEE.[Department Code] = 104

   
NOTE: You can both create and insert records in a single SELECT statement, as discussed earlier in this chapter in the section "Creating Tables."