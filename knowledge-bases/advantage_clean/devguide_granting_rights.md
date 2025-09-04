---
title: Devguide Granting Rights
slug: devguide_granting_rights
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_granting_rights.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 56406bd04d57afb50ba97490ecf56903f734efc7
---

# Devguide Granting Rights

Granting Rights

     Granting Rights

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Granting Rights  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

If you configure your data dictionary to check user rights, any new objects that you add to your data dictionary must have rights granted to the groups and users who need to work with those objects. With Advantage SQL, you grant rights to objects using the SQL GRANT statement. Granting rights is something that can be performed using the administrative account or any user account with the appropriate WITH GRANT permissions (meaning that the user can grant specific rights to others).

You follow the GRANT keyword with the types of rights you want to convey. The types of rights are followed by the ON keyword, which you follow with the object to which you are granting the rights. You complete the GRANT statement using the TO keyword followed by the name of the user or group to whom you are granting the rights.

   
NOTE: All rights can be granted to either users or groups, with the exception of INHERIT. INHERIT can only be granted to a user.  
 

For example, if you have a table named TEMP and you want to convey SELECT and INSERT rights to the ALL group, but not UPDATE and DELETE rights, you could execute the following SQL script:

GRANT INSERT ON TEMP TO [ALL];  
GRANT SELECT ON TEMP TO [ALL]

   
NOTE: The group named ALL is enclosed in delimiters since ALL is an SQL reserved keyword.  
 

Similarly, if you have a table named ACCOUNTS in your data dictionary, and you want to grant all rights to the adsuser user, use the following statement:

GRANT ALL ON ACCOUNTS TO adsuser

Granting rights to a table explicitly grants those same rights to every field in the table as well.

Rights can be granted for tables, table columns, data dictionaries, functions, groups, data dictionary links, packages, publications, stored procedures, subscriptions, users, and views. Which rights can be granted depends on the object to which rights are being conveyed. Table 14-11 lists the type of rights and the objects to which those rights can be granted.
