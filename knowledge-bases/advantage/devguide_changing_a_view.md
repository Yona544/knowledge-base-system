Changing a View




Advantage Database Server 12  

     Changing a View

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Changing a View  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Changing a View Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Changing\_a\_View Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 6 - Views > Changing a View / Dear Support Staff, |  |
| Changing a View  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You can change the SQL that defines a view so long as the new SQL that you provide is valid for a view. To change a view, right-click the view and select Properties from the displayed context menu. This reopens the View dialog box (shown in Figure 6-1), where you can change the SQL statement associated with the view. Click OK to save the view when you are done.

   
CAUTION: You should exercise caution when changing a view that is used by deployed client applications. If your client applications refer to specific fields by name or position in the result set, changes you make to column names or changes to the order and/or number of columns in the result set can cause errors in your client applications. Make sure to test all client applications before deploying data dictionaries with updated views where these types of changes have been applied.