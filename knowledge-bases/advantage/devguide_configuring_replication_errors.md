Configuring Replication Errors




Advantage Database Server 12  

     Configuring Replication Errors

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Configuring Replication Errors  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Configuring Replication Errors Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Configuring\_Replication\_Errors Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 10 - Replication > Configuring Replication Errors / Dear Support Staff, |  |
| Configuring Replication Errors  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You can use the Advanced page of the Subscription dialog box to instruct Advantage to ignore replication failures. When Advantage ignores errors, it removes the error-causing record from the replication queue and continues to process replications.

By default, the errors that are ignored are 7137 errors. These errors indicate that an unexpected number of records were affected by the replication. In the case of updates, exactly one record should be affected by replication.

It is possible to configure which errors Advantage ignores by adjusting the configuration registry settings (Windows) or the ads.conf (Linux). You do this by adding the PERMITTED\_REP\_ERRORS key under the Configuration key or section. The value for this key should be a delimited list of the Advantage error codes to ignore. Valid delimiters are spaces, commas, and semicolons.

Note that adding this key overrides the default behavior. Specifically, if you add this key, and still want 7137 errors to be ignored (which you probably do), you must include the 7137 error in the list. The following is an example of an ads.conf configuration entry demonstrating this key:

PERMITTED\_REP\_ERRORS= 7137,7057