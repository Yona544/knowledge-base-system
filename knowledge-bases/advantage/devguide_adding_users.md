Adding Users




Advantage Database Server 12  

     Adding Users

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Adding Users  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Adding Users Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Adding\_Users Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Adding Users / Dear Support Staff, |  |
| Adding Users  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Adding users to a data dictionary is quite simple, as shown in the following steps:

1.        Make sure that DemoDictionary in the Connection Repository is expanded as shown in Figure 4-6.

|  |  |
| --- | --- |
| 2. | Next, right-click the USERS node and select Create. The Advantage Data Architect displays the User dialog box shown in Figure 4-7. |

|  |  |
| --- | --- |
| 3. | Set Name to adsuser. |

|  |  |
| --- | --- |
| 4. | Set both Password and Confirm Password to password. |

|  |  |
| --- | --- |
| 5. | Click the Enable Internet Access checkbox to permit this user to connect to the data dictionary over the Internet. |

|  |  |
| --- | --- |
| 6. | Next, click the Description tab and enter Basic user name for data access.  In some cases, you might return to the General page of the User dialog box, click Permissions, and then define this user's rights to the various objects of the data dictionary. We will use an alternative method in this example. Specifically, we will grant rights at the group level, and then add this user to that group. |

|  |  |
| --- | --- |
| 7. | Click the Create button. This creates the new user and then resets the User dialog box, permitting you to immediately create another user. We are done creating users for now, so simply close the User dialog box. An adsuser node will appear under the USERS node in the Connection Repository. |

Figure 4-7: The User dialog box

Any number of users can use the same user name and password at the same time, which is why you can get by with a single nonadministrative user if you want. But if you want more than one user, you can repeat steps 3 through 8 in the preceding list.

In addition to providing you with greater control over your application's security, having more than one user permits you to leverage another feature of data dictionaries. This feature is to check user rights, and it is discussed in the following section.