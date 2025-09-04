Advantage and Delphi




Advantage Database Server 12  

     Advantage and Delphi

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage and Delphi  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Advantage and Delphi Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved.  devguide\_Advantage\_and\_Delphi Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 15 - Using Advantage from Delphi > Advantage and Delphi / Dear Support Staff, |  |
| Advantage and Delphi  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Delphi has been the development environment of choice for Advantage developers for some time. While we anticipate that other languages, such as C#, will be the choice of a growing number of Advantage developers due to the availability of the Advantage .NET Data Provider, Delphi continues to be an excellent tool for working with Advantage.

There are two primary reasons why Advantage and Delphi go so well together. The first is the abundance of Advantage features that are available through the Advantage TDataSet Descendant classes. Using these components, it is extremely easy to access, change, and manage your Advantage data.

The second reason is that the data access model supported by the BDE (Borland Database Engine), and encapsulated in the TDataSet abstract class of the VCL (visual component library), fits beautifully with the navigational model that Advantage's ISAM architecture permits. This reason is actually closely related to the first. The ease with which Delphi developers can use Advantage is a direct result of the nearly seamless way in which the TDataSet interface and the Advantage API (application programming interface) interact.

But there is more. The Advantage components that descend from TDataSet do much more than simply conform to the TDataSet interface. They also expose a large number of functions in the ACE API. For example, you can call AdsStmtSetTablePassword on an AdsQuery to submit a free table's encryption password before attempting to query it. This method is not part of the TDataSet interface, but is exposed by this component to simplify your work with ADS without having to deal directly with ACE.

An interesting piece of evidence for this near perfect fit between Advantage and Delphi is that the Advantage Data Architect is written in Delphi. In fact, when you install the Advantage Data Architect, the Delphi source files and packages that are used to build the Advantage Data Architect are included. Indeed, these Delphi units can be a fascinating source of ideas if you need to perform some task that is out of the ordinary. (The Advantage Data Architect source files do not include some third-party components that were used to build the Advantage Data Architect. As a result, you cannot actually use these source files to recompile the Advantage Data Architect.)

That the Advantage Data Architect was written in Delphi presented a creative opportunity for integration between Advantage and Delphi. While working on the Advantage Data Architect, Advantage R&D Product Manager J.D. Mullin realized that he could create a property editor for the TAdsTable component in Delphi that could surface the Advantage Data Architect's Table Designer.

As a result, with the Advantage TDataSet Descendant (for Delphi 5-7) or the Advantage Data Access Components for Delphi (Delphi 2005 and 2006) installed, you can right-click a configured AdsTable in Delphi and select ALTER/Restructure Table. Doing so opens the Table Designer for the associated table, permitting you to change the table's structure, modify table properties, and configure table indexesall without having to load a separate copy of the Advantage Data Architect.