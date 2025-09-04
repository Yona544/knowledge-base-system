Advantage Data Architect




Advantage Database Server 12  

     Advantage Data Architect

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Data Architect  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Advantage Data Architect Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Advantage\_Data\_Architect Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > Advantage Data Architect / Dear Support Staff, |  |
| Advantage Data Architect  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The Advantage Data Architect, whose main screen is shown in Figure 1-8, is a graphical tool that simplifies the creation and configuration of your tables and databases. The Advantage Data Architect is also referred to as ARC. To launch the Advantage Data Architect in Windows, select the Start button, and then select Programs | Advantage Database Server | Advantage Data Architect.

The Advantage Data Architect includes a wide variety of support features, including the ability to import and export data, execute ad hoc queries, perform checks on your development environment, and much, much more. As a developer, you are likely to use the Advantage Data Architect more than any other tool that ships with Advantage.

Figure 1-8: The Advantage Data Architect

While the Advantage Data Architect makes it easy to design your tables and data dictionaries, there are alternatives. Specifically, all of the database-related configuration capabilities provided by Advantage Data Architect can also be performed using Advantage SQL, as well as by programming directly to the Advantage API using ACE (the Advantage Client Engine).

The Advantage Data Architect provides another benefit, albeit one that is not immediately obvious. It can provide you with insight on how to create and manage your tables and data dictionaries programmatically. The Advantage Data Architect was written in the Delphi language, and the source code for this Delphi project can be installed when you install the Advantage Data Architect. The Delphi language is easy to read, so even if you are not a Delphi developer, you can probably figure out how specific operations were performed.

Because the Advantage Data Architect is such a valuable tool for working with tables and data dictionaries, a large portion of this book discusses its use. In other words, there is no chapter that specifically discusses the Advantage Data Architect. Instead, almost all examples in this book where tables and data dictionaries are manipulated use the Advantage Data Architect.

   
NOTE: You can configure many aspects of how the Advantage Data Architect looks and behaves by selecting Tools | Arc Settings.  
 

Understanding Connections and the Connection Repository

If you are familiar with older versions of the Advantage Data Architect, one of the more obvious differences is the addition of the Connection Repository. The Connection Repository, which appears along the left side of the Advantage Data Architect in Figure 1-8, provides you with easy access to your Advantage tables and data dictionaries.

Each root node that appears in the Connection Repository is associated with a connection. A connection is associated with either a directory in which free tables are stored or a data dictionary. Each connection has a name and also has properties that instruct the Advantage Data Architect how you want to use the objects to which the connection refers. For example, a connection identifies whether to connect to the data using ADS or ALS, which Advantage table type to create by default, and locking mode.

Connection definitions, like those of their precursors, aliases, are defined in the ads.ini file. (This file appears in the Windows directory.)

By default, if a connection is open in the Connection Repository when you close the Advantage Data Architect, the Advantage Data Architect will attempt to reopen that connection when you load it again. If you have multiple connections open when closing the Advantage Data Architect, it will try to reopen each of them. Depending on how you have configured your data dictionaries, as well as your connections, the Advantage Data Architect may challenge you for each password for each connection it tries to reopen.

If you like, you can modify this automatic reopening of connections. To do this, select Tools | ARC Settings in the Data Architect to view the Connections page, and toggle the Reopen Connections at Startup option. Note that many other properties of the Advantage Data Architect can be configured from this ARC Settings dialog box.

Creating a Connection

There are several ways to create a connection, depending on whether or not you also need to create a data dictionary. You can use the New Connection Wizard, or you can use the Data Dictionary dialog box. Using the Data Dictionary dialog box is demonstrated in Chapter 4. Therefore, you will use the New Connection Wizard in this example.

Use the following steps to create a new, free table connection:

Begin by creating a new directory named FreeTabs. This directory should be a subdirectory of the one in which the sample tables that you will use in future chapters will be stored. (These files, and how you download them, are described in Appendix A.) Since we recommend that you place the sample files in a directory named c:\AdsBook, we suggest that you create the directory c:\AdsBook\FreeTabs.

Next, from the Advantage Data Architect main menu, select Connection | New Connection Wizard. The New or Existing Data page of the New Connection Wizard, shown in Figure 1-9 is displayed.

Leave the "Create a new connection to a new database" radio button selected and click Next. The Data Dictionary Connection or Free Table Connection page shown in Figure 1-10 is displayed.

Select the "Create a new connection to a directory that will contain free tables" radio button, and then click Next. The Connection Details page of the New Connection Wizard shown in Figure 1-11 is displayed.

Set DatabaseName to FreeTableConnection.

Use the ConnectionPath dropdown menu to select Browse for Directory. Use the displayed dialog box to select the subdirectory you created in step 1 (c:\AdsBook\FreeTabs) and then click OK.

Set ServerType to remote.

   
NOTE: We are assuming you are using ADS, Advantage Database Server. This is why you set ServerType to remote. If for some reason you are not using ADS and instead, are using ALS, Advantage Local Server, set ServerType to local. This applies to all examples in this book. Note however, that some of the examples, such as those shown using backup, replication, and Java, cannot be performed using ALS. You must use ADS in these situations.  
 

Click the Finish button to complete the creation of your new connection. The FreeTableConnection connection now appears in the Connection Repository of the Advantage Data Architect.

Figure 1-9: The New or Existing Data page of the New Connection Wizard

Figure 1-10: The Data Dictionary Connection or Free Table Connection page of the New Connection Wizard

Figure 1-11: The Connection Details page of the New Connection Wizard