Understanding the TDataSet Descendants




Advantage Database Server 12  

     Understanding the TDataSet Descendants

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Understanding the TDataSet Descendants  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Understanding the TDataSet Descendants Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Understanding\_the\_TDataSet\_Descendants Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 15 - Using Advantage from Delphi > Understanding the TDataSet Descendants / Dear Support Staff, |  |
| Understanding the TDataSet Descendants  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The name TDataSet descendant is actually something of a misnomer. While the TAdsTable, TAdsQuery, and TAdsStoredProc components do indeed descend from the TDataSet class, there are several other classes on the Advantage page of the Tool Palette in Delphi that do not descend from the TDataSet class. These include the TAdsBatchMove, TAdsConnection, TAdsDictionary, and TAdsSettings classes. Nonetheless, these components, which are shown in Figure 15-1, are generically referred to as TDataSet descendants.

Figure 15-1: The Advantage page of the Tool Palette in Delphi

That TAdsTable, TAdsQuery, and TAdsStoredProc all descend from TDataSet means that they share a common programming interface with all other standard Delphi data access components. This interface is largely navigational, although it also supports the entire range of set-based operations of Advantage SQL through the TAdsQuery class.

Because the TDataSet descendants share a common interface with other Delphi data access components, such as TTable, TSQLDataSet, TIBQuery, TClientDataSet, among others, converting an existing Delphi application to use Advantage is pretty straightforward. In fact, now that Borland has officially deprecated Borland SQL Links for Windows (the portion of the BDE based on DLLs that provided the BDE with access to many remote database servers), Advantage is an ideal option when choosing an alternative data access mechanism, especially if your application already uses the navigational model. (Migrating Delphi BDE applications to SQL-based remote database servers almost always involves a major update to the user interface, in order to accommodate the limitations of set-based SQL.)

The remainder of this chapter shows you how to access Advantage using Delphi. This discussion is divided into three parts. The first part describes common basic tasks, such as connecting to Advantage and accessing data. The second part shows you how to leverage the navigational model with Delphi and Advantage. The third part demonstrates several basic administrative tasks, such as creating tables and granting rights to them.

   
CODE DOWNLOAD: The Delphi project Delphi\_TDataSet.dpr can be found with this books code download (see Appendix A). This project was created using Delphi 7, but is compatible with Delphi versions 5 and later.  
 

All of the examples presented here can be found in a Delphi project named Delphi\_TDataSet. Figure 15-2 shows the main form of this project in Delphi 2006.

   
NOTE: This project is a Win32 project, and can be created with Delphi versions as far back as Delphi 5 (including Kylix, the Linux version of Delphi). Both Delphi 2006 and Delphi 2005 can also be used to create this same project either as a Win32 project or a .NET managed-code project using the VCL for .NET.  
 

Figure 15-2: The Delphi\_TDataSet project's main form

A final comment about this project is in order. Many of the operations performed in this project make use of the AdsTable component, which is pretty common for Delphi applications. Many of these same operations can be performed using a SQL query executed through an AdsQuery (or by calling stored procedures using the AdsStoredProc component). For examples of possible SQL alternatives, refer to Chapters 1619.