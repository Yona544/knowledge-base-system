The Error Table




Advantage Database Server 12  

     The Error Table

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| The Error Table  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      The Error Table Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_The\_Error\_Table Advantage Developer's Guide > Appendixes > Appendix B - Troubleshooting and Other Issues > The Error Table / Dear Support Staff, |  |
| The Error Table  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

ADS also keeps track of errors it encounters in a special ADT table named ads\_err.adt. The configuration of ADS specifies where this table is stored. To discover the location of this file, use the following steps:

1.        Open the Advantage Data Architect.

|  |  |
| --- | --- |
| 2. | Select Tools | Remote Server Info to display the Advantage Management Utility dialog box. |

|  |  |
| --- | --- |
| 3. | Set Server Drive to the drive or share where the server is running. Use a UNC (universal naming convention) path if the server is running on another machine on your network. Click the Connect button, which appears to the immediate right of the Server Drive field. |

|  |  |
| --- | --- |
| 4. | Once connected, click the Configuration Parameters tab, then click the Not Affecting Memory tab. The Error Log and Assert Log Path field displays the location where the ads\_err.dbf file is stored. |

Use the Advantage Data Architect to view this free ADT table, as described in the following steps:

1.        From the Advantage Data Architect's main menu, select File | Open Table.

|  |  |
| --- | --- |
| 2. | Set Path to the location where the ads\_err.adt file is stored. |

|  |  |
| --- | --- |
| 3. | Set Files to ads\_err.adt or use the Browse button to select the file. |

|  |  |
| --- | --- |
| 4. | Select the server type. Remember, all Advantage applications that are opening a single table (in this case, ads\_err.adt) should be using the same server type. Otherwise, 7008 errors are likely to occur. In other words, all applications that want to open the same table concurrently should either all be using ALS or all be using ADS to open that table. |

|  |  |
| --- | --- |
| 5. | Click OK. |

Once you select the ads\_err.adt file, all errors that have been saved can be viewed. The most recent errors appear at the end of this table.

   
NOTE: By default, only the last 1,000 errors are saved. In Windows you can change this value using the Misc. Page of the Advantage Configuration Utility (described in Chapter 1). For Linux installations, you control this value through the configuration file.