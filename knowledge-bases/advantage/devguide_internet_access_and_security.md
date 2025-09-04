Internet Access and Security




Advantage Database Server 12  

     Internet Access and Security

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Internet Access and Security  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Internet Access and Security Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Internet\_Access\_and\_Security Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Internet Access and Security / Dear Support Staff, |  |
| Internet Access and Security  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You also enable Internet access and define Internet access rights and encryption through your data dictionary. To enable Internet access, display the Security page of the Data Dictionary dialog box (shown in Figure 4-5), and enable the Internet Access checkbox. At Security Level, you can choose No Authentication, Authenticate, or Authenticate & Encrypt. You also specify the maximum number of user login attempts for the Authenticate and Authenticate & Encrypt security levels in the Max Login Attempts field.

Advantage uses the more restrictive authentication requirement between the Logins Required property and the Internet Security Level setting on the Security page of the Advantage Data Dictionary. For example, since the DemoDictionary has Logins Required checked, user login is still mandatory even if you enable Internet access, but select a No Authentication security level.

Note that compression of data over the Internet is the default. The Advantage team recommends testing various server and client settings for compression for your particular applications as compression reduces network traffic requirements, but incurs more server and/or client overhead. In most cases, the overhead of compression is minor compared to the performance improvements realized through compression. See "Communications Compression" in the Advantage help for a detailed discussion of communication and compression issues.