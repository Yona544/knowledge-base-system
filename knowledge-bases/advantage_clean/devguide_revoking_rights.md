---
title: Devguide Revoking Rights
slug: devguide_revoking_rights
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_revoking_rights.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 77a1c1acb8ff2e95c8e63eeec972414ef5bd9694
---

# Devguide Revoking Rights

Revoking Rights

     Revoking Rights

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Revoking Rights  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The syntax of the REVOKE SQL statement is nearly identical to the GRANT statement. The only differences are that you use the REVOKE keyword in place of GRANT, and FROM in place of TO. All other aspects of this statement are identical, including the use and applicability of the rights and the object to which they apply that appear in Table 14-11.

For example, to revoke the adsuser's SELECT rights from the Full Name field of the ACCOUNTS table, you can use the following statement:

REVOKE SELECT("Full Name") ON ACCOUNTS FROM adsuser

   
NOTE: If the SELECT rights to the Full Name field were the only field-level rights granted to the ACCOUNTS table, revoking those rights would restore to adsuser the access rights granted to the ACCOUNTS table, based on adsuser's table-level access rights to ACCOUNTS, including those inherited from the ALL group to which adsuser belongs. Field-level rights only apply when rights have been explicitly granted to one or more of the table's fields.  
 

To remove access rights to the ACCOUNTS table from the adsuser user altogether, you use the following statement:

REVOKE ALL ON ACCOUNTS FROM adsuser
