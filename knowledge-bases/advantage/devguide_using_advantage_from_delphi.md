Using Advantage from Delphi




Advantage Database Server 12  

     Using Advantage from Delphi

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Advantage from Delphi  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Using Advantage from Delphi Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Using\_Advantage\_from\_Delphi Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 15 - Using Advantage from Delphi > Using Advantage from Delphi / Dear Support Staff, |  |
| Using Advantage from Delphi  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Without a doubt, Delphi developers have the richest choice of options for accessing Advantage. In addition to being able to use ACE (Advantage Client Engine), Delphi developers can use the Advantage ODBC Driver, the Advantage OLE DB Provider, and the Advantage .NET Data Provider. But there is one data access mechanism that beats them allthe Advantage TDataSet Descendant. Using the TDataSet descendant classes, Delphi developers, as well as Kylix and C++Builder developers, can utilize almost every feature available in Advantage. Only ACE provides access to more capabilities, but at the expense of being significantly more complicated to use.

   
NOTE: If you are using C++Builder or Kylix, install the Advantage TDataSet Descendant for either C++Builder or Kylix, respectively. The TDataSet descendant classes are identical to those described in this chapter. The Kylix code is identical to the Delphi code with few exceptions, all due to working in Linux. For C++Builder code, the methods and properties are the same, but the syntax of C++ is different.  
 

This chapter provides you with examples of using the Advantage TDataSet Descendant classes to perform a wide range of common data-related tasks using Delphi. As is the case with the other chapters in Part III, this discussion assumes that you are already familiar with the development environment being described. Instead, the focus is on code that works with the data dictionary you have been using throughout this book.

   
NOTE: If you need to create .NET managed assemblies, you have two options. You can use the Advantage TDataSet Descendant for the VCL for .NET or you can use the Advantage .NET Data Provider. The examples in this chapter apply to the Advantage TDataSet Descendant for VCL for .NET. For information about using the Advantage .NET Data Provider, refer to Chapter 18.