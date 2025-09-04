---
title: Devguide Testing Aeps
slug: devguide_testing_aeps
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_testing_aeps.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 690b17315762ca19f2b3d69fb6b85b327988239b
---

# Devguide Testing Aeps

Testing AEPs

     Testing AEPs

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Testing AEPs  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

After you create your stored procedure objects, you will want to test them to make sure that they are doing what you want. One of the easiest ways to test a new stored procedure from the Advantage Data Architect is to execute it using the SQL Utility. The following steps show you how:

1.        Make DemoDictionary the active and current connection.

| 2. | Expand the STORED PROCS node in the Connection Repository and double-click the stored procedure you want to test. The Advantage Data Architect generates a parameterized call to the stored procedure and displays this SQL in the SQL Utility. |

| 3. | You now have two choices. You can either right-click in the SQL pane and select parameters to display the Parameters dialog box (which you use to define the names, data types, and values for each parameter in the parameterized query), or you can replace the parameter with a literal value in the SQL pane. Actually, if you leave the originally generated parameter and try to run the query, the Parameters dialog box will be displayed by default.     In this case, delete the parameter :CustID from the SQL pane and replace it with the value 12037. Next, click the Execute button in the SQL Utility toolbar or press F5. When the query has completed executing, the SQL Utility should look something like that shown in Figure 7-6. |

Figure 7-6: The result set returned from the SQLGet10Percent stored procedure
