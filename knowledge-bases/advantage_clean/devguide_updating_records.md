---
title: Devguide Updating Records
slug: devguide_updating_records
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_updating_records.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: ea953fff0127045570f189585995c6a68cd3ff28
---

# Devguide Updating Records

Updating Records

     Updating Records

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Updating Records  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You update records in a table using the UPDATE statement. When you use UPDATE, you must specify the name of the table whose records are being updated, as well as which fields you want to update. For example, the following query updates #TEMP, setting the credit limit field to 500 for all records:

UPDATE #TEMP SET "Credit Limit" = 500

The preceding statement updates all records in the table. In most cases, however, you will want to update only specific records. To specify which records to update, use a WHERE clause. For example, the following statement sets the Active field to False for those records where the Active field has not been assigned a value:

UPDATE #TEMP   
  SET [Active] = False  
  WHERE [Active] IS NULL

Here is another example:

UPDATE #TEMP   
  SET [Credit Limit] = 0  
  WHERE [Active] = False

The UPDATE statement also supports a FROM clause. You use FROM if you are using fields and expressions involving another table to perform the update. For example, the following UPDATE statement changes the Credit Limit field to 10000 for all records in #TEMP where the full name is associated with an employee record, and that employee's department code is 108:

UPDATE #TEMP   
  SET "Credit Limit" = 10000  
  FROM EMPLOYEE Emp INNER JOIN #TEMP ON  
    "Full Name" =   
      RTRIM(Emp."First Name") + ' ' + RTRIM(Emp."Last Name")  
  WHERE Emp."Department Code" = 108
