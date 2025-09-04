MDAC, OLE DB, ADO, Visual Basic, and Advantage




Advantage Database Server 12  

     MDAC, OLE DB, ADO, Visual Basic, and Advantage

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| MDAC, OLE DB, ADO, Visual Basic, and Advantage  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      MDAC, OLE DB, ADO, Visual Basic, and Advantage Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_MDAC\_OLE\_DB\_ADO\_Visual\_Basic\_and\_Advantage\_1 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 17 - MDAC, OLE DB, ADO > MDAC, OLE DB, ADO, Visual Basic, and Advantage / Dear Support Staff, |  |
| MDAC, OLE DB, ADO, Visual Basic, and Advantage  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

There are three layers to Universal Data Access, Microsoft's ambitious initiative to build a data access layer into the Windows operating system. At the lowest layer are data-providing applications and services. In most cases, such as with Advantage, these are client/server database servers. But in practice, they can be almost any type of application imaginable. Nonetheless, the one characteristic that all data providers and services share is that they provide access to information.

Above this lowest layer is OLE DB, which consists of a series of COM (component object model) interfaces. OLE DB provides a layer of abstraction between the data providers and the data consumers, which are your client applications in the traditional client/server architecture.

COM interfaces are simply API templates, which alone are useless unless they are implemented by objects. This is where OLE DB providers come in. OLE DB providers are the objects that implement the OLE DB interfaces, and which perform the physical communication with the data-providing applications and services. In the MDAC scheme of things, both OLE DB and OLE DB providers reside in this middle layer.

While it is conceivable for an application developer to program directly to the OLE DB API, doing so would be both time-consuming and complicated. This is because OLE DB, being a low-level interface, was not designed as a developer API. And this is where the third and highest layer comes in, ADO.

ADO consists of a collection of ActiveX data objects that encapsulate calls to OLE DB. By comparison to OLE DB, the ADO API is simple, providing client application developers with convenient access to the data supplied by the data providers and services.

MDAC is normally available on all 32-bit Windows machines (only Windows 95, which has not been supported by Microsoft for some time, did not come with MDAC already installed). Furthermore, the latest version of MDAC can be freely downloaded from Microsoft's Web site at http://msdn.microsoft.com/data/mdac/downloads/. The licensing for MDAC specifically permits you to distribute it with your applications, but that is rarely necessary (unless you are installing your applications on obsolete machines).

MDAC consists of all of the ActiveX data objects, as well as a collection of OLE DB providers. The standard providers include the Microsoft Jet 4.0 OLE DB Provider, the Microsoft OLE DB Provider for SQL Server, the Microsoft OLE DB Provider for Oracle, and the Microsoft OLE DB Provider for ODBC, just to name a few.

There are two critical characteristics of Microsoft's Universal Data Access that make this an appealing data access solution. First, regardless of which OLE DB provider you want to use, you access it through the one set of ActiveX data objects. They provide the common API.

The second is that you are not limited to using just the standard OLE DB providers that ship with MDAC. Any COM objects that correctly implement the necessary OLE DB interfaces can be installed on a Windows computer and executed through ADO. The Advantage OLE DB Provider is an example of such an implementation. After installing the Advantage OLE DB Provider, which automatically registers this provider with COM, you can use ADO to access your Advantage data.

There is one final issue that deserves mention before turning our attention to using Advantage through ADO: client-side cursors versus server-side cursors. In ADO, when you execute a command that returns a result set, you specify where the result set will reside using the CursorLocation property of a Connection or Recordset object. If you set CursorLocation to adUseClient, all records from the result set are downloaded from the server and stored in-memory on the client workstation. By comparison, if you set CursorLocation to adUseServer, the Advantage OLE DB Provider manages the access of data using ADS, retrieving to the client only those records required by your application. The default value of the CursorLocation property of Connection and Recordset objects is adUseServer.

When you load your data into a client-side cursor, operations such as sorting, finding, filtering, and the like are performed by the ADO client cursor engine, and do not involve ADS until you are ready to write changes back to the server. By comparison, when you use server-side cursors, you are leveraging the power and performance of ADS in operations that involve filters, indexes, seeks, and navigation. As a result, the examples discussed in this chapter make use of server-side cursors. If you are interested in learning more about client-side cursors and their features, refer to a book on ADO.

   
NOTE: Because client-side cursors require that all records be downloaded from the server into memory on your workstation before you can work with your data, you may experience significant delays when loading large result sets using client-side cursors. In most cases, you will achieve excellent performance with ADS and server-side cursors, making them a better solutionparticularly when your result sets are large.  
 

The remainder of this chapter shows you how to access Advantage using Visual Basic 6. These discussions are divided into three parts. The first part describes common tasks, such as connecting to Advantage and accessing data. The second part shows you how to perform simple navigation using ADO. The third and final part demonstrates several basic administrative tasks, such as creating tables and granting rights to them.

   
CODE DOWNLOAD: The VB project VB\_ADS.vbp can be found on this book's code download (see Appendix A).  
 

All of the examples presented here can be found in the VB\_ADO.vbp Visual Basic project. Figure 17-1 shows the main form of this project in Visual Studio.

Figure 17-1: The VB\_ADO project in Visual Studio

   
NOTE: The VB\_ADO project with the code download for this book was compiled with MDAC 2.8. If you are not using MDAC 2.8, you will get an error when you first try to run this project. If this happens, select Project | References. Use the displayed dialog box to uncheck the Microsoft ActiveX Data Objects Library 2.8 (if necessary). Then, scroll to find the version of the Microsoft ActiveX Data Objects Library that you want to use (this must be version 2.1 or later), and add a checkmark to it. Click OK when you are done.  
 

As is the case with all data access mechanisms described in Part III, the following discussion of Advantage programming with Visual Basic touches on just a few of the available techniques. For a more comprehensive discussion of ADO programming, you may want to pick up a book on ADO programming.

If you are creating a new project that uses ADO, you must add a reference to the Microsoft Data Access Objects library before you can use the Advantage OLE DB Provider with Visual Studio. To do this, use the following steps:

1.        From Visual Studio, select Projects | References. Visual Studio displays the References dialog box as shown in Figure 17-2.

|  |  |
| --- | --- |
| 2. | Scroll the Available References list until you see Microsoft ActiveX Data Objects Library. Place a checkmark next to the version with the highest major and minor version, as shown in Figure 17-2. |

|  |  |
| --- | --- |
| 3. | Click OK to close the References dialog box. |

Figure 17-2: Adding a reference to the Microsoft Data Access Objects library