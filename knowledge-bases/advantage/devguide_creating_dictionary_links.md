Creating Dictionary Links




Advantage Database Server 12  

     Creating Dictionary Links

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating Dictionary Links  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating Dictionary Links Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_Dictionary\_Links Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Creating Dictionary Links / Dear Support Staff, |  |
| Creating Dictionary Links  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You create a data dictionary link using the following steps. (Note that these steps are for descriptive purposes since we have not created another data dictionary for our example database).

1.        Right-click the LINKS node of the data dictionary connection in which you want to define a new data dictionary link. The Advantage Data Architect responds by displaying the Link dialog box shown in Figure 4-13.

|  |  |
| --- | --- |
| 2. | Set the Alias field to a name for your data dictionary link. This name, which cannot include spaces, can then be used in SQL statements to qualify table (and view) names from the data dictionary to which the link refers. |

|  |  |
| --- | --- |
| 3. | Set Linked Data Dictionary to the path of the data dictionary to which this link will refer. This path can be either a Windows path or a UNC path. Enable the Static Path checkbox if you want the data dictionary to save the fully qualified path. When Static Path is unchecked, only the relative path to the linked dictionary is saved in the data dictionary. |

Figure 4-13: The Link dialog box

4.        If you want to pass the user name and password of the connection that is accessing the link to the other data dictionary, enable Authenticate Active User. This setting is useful when you want to ensure that the same user names and passwords are valid for both data dictionaries (at least with respect to table and view rights that may participate in a link.) If you do not check Authenticate Active User, and the data dictionary to which you are linking requires user login, set the Name and the Password fields to a valid user for the data dictionary to which you are linking. This user must have rights to the tables to which you are linking.

|  |  |
| --- | --- |
| 5. | Click OK when you are done. |

Once you have defined a link, you must specifically grant rights to that link to all users (or to the groups to which they belong) who need access to the objects in the linked dictionary.