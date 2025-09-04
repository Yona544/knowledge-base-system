Creating a Package




Advantage Database Server 12  

     Creating a Package

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating a Package  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating a Package Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_a\_Package Advantage Developer's Guide > Part II - Advantage SQL > Chapter 13 - SQL Scripting Language > Creating a Package / Dear Support Staff, |  |
| Creating a Package  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You create a package by right-clicking the FUNCTION node in your data dictionary connection and selecting Create Package. You then use the Package dialog box to define the package name.

Use the following steps to create a package called Math:

1.        From your active and connected DemoDictionary connection, right-click the FUNCTION node and select Create Package. The Advantage Data Architect responds by displaying the Package dialog box shown in Figure 13-1.

Figure 13-1: The Package dialog box

2.        At Name, enter Math.

|  |  |
| --- | --- |
| 3. | Click OK to close the Package dialog box and create your new package. |

   
NOTE: In order to create a package, you must be connected to the data dictionary either on the ADSSYS administrative account or from a user who has create package rights.