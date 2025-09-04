Testing the New Trigger




Advantage Database Server 12  

     Testing the New Trigger

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Testing the New Trigger  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Testing the New Trigger Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Testing\_the\_New\_Trigger Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 8 - Triggers > Testing the New Trigger / Dear Support Staff, |  |
| Testing the New Trigger  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

With your new trigger assigned to the TriggerTest table, you are ready to demonstrate its use. Use the following steps to test the GenKey trigger:

Double-click the TriggerTest table in your DemoDictionary connection to open it in the Table Browser.

In the Name field enter Advantage, and in the Number field enter 1. Press the Down Arrow key. Your first record is posted, and your cursor moves to a newly inserted record. Since no data was entered in the field named Key, a GUID was assigned to that field by the trigger.

This time, enter Advantage in the Key field. Press Down Arrow once again to post this insert and move to a new record. This time a GUID was not written to the Key field. Your screen should look something like that shown in Figure 8-8.

Continue to test the trigger if you like. When you are done, close the Table Browser.

Figure 8-8: Testing the GenGuidID trigger