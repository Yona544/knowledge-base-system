Creating the Client Applications




Advantage Database Server 12  

     Creating the Client Applications

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating the Client Applications  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating the Client Applications Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_the\_Client\_Applications Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > Creating the Client Applications / Dear Support Staff, |  |
| Creating the Client Applications  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The Advantage Data Architect is a pretty powerful piece of software. You will learn as you work through the later chapters in this book that not only does the Advantage Data Architect provide you with the tools to design a database, but also that it permits you to work with the database. Specifically, using the Advantage Data Architect, you can add new records to your tables, change existing records, and delete records. It also provides you with a number of tools to test queries against your data, verify that your indexes are optimized for the searches you want to perform on your data, and so forth. It even permits you to export your data to HTML (hypertext markup language), which you can then print, using this feature as a simple reporting mechanism.

Here is another way to look at it. The Advantage Data Architect is an Advantage client application. However, it is a very general Advantage client whose primary purpose is to give you the ability to easily design and test your database. In most cases, you will create one or more custom client applications to work with your Advantage databases.

Custom client applications are all about making your data accessible to your end users. While an end user could use the Advantage Data Architect to view their data, the interface would lack the customization that is the hallmark of a client application. Similarly, while an end user could export the results of a SQL query to HTML, and then print this from a Web browser, the output would lack the quality and sophistication that most people want to see in a report.

With a custom client application, your end users are presented with data options that make sense in the context of the data. For example, your application can display a form from which the end user enters a customer account number. Once the number is entered, your application can perform a query to select the data for that customer, and display the customer data in a context-meaningful format. Similarly, your application can include a menu item that, when selected, creates and prints an attractive report that makes the data easily digestible.

You can create custom client applications that use Advantage from almost any application development platform. Examples of languages from which you can access Advantage include Visual Basic, Visual Basic for .NET, Visual C++, Visual C# for .NET, FoxPro, Visual J# for .NET, Delphi, Delphi for .NET, C++Builder, C#Builder, Kylix, JBuilder, VisualAge for Java, Eclipse, Clipper, Visual Objects, Xbase++, xHarbor, Paradox, PHP, and Perl, and this list is not even close to being complete.

In short, you can use any application development environment for which Advantage supplies a data access mechanism. Fortunately, Advantage supplies a large number of data access mechanisms. (Xbase++ actually supplies its own Advantage connectivity drivers). These are listed in Table 1-1, which includes a description of the development environments best suited for each mechanism.

 

|  |  |
| --- | --- |
| Data Access Mechanism | Supported Development Environments |
| Advantage TDataSet Descendant | Any language that supports Borland's VCL (visual component library) or CLX (component library cross-platform). These include Delphi 3-7, Delphi 2005 and Delphi 2006, C++Builder, and Kylix. There is also a VCL for .NET version, which can be used by Delphi for .NET (8, 2005, and 2006). |
| Advantage ODBC Driver | Any language that supports ODBC drivers. These include almost all Windows-based development environments such as Visual Basic, Visual C++, Visual FoxPro, Delphi, and C++Builder, to name a few. There is also a Linux ODBC version for ODBC-enabled Linux applications. |

Table 1-1: The Available Advantage Data Access Mechanisms