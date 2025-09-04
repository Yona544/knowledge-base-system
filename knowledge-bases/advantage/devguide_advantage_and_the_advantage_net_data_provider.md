Advantage and the Advantage .NET Data Provider




Advantage Database Server 12  

     Advantage and the Advantage .NET Data Provider

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage and the Advantage .NET Data Provider  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Advantage and the Advantage .NET Data Provider Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Advantage\_and\_the\_Advantage\_NET\_Data\_Provider Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 18 - The .NET Data Provider > Advantage and the Advantage .NET Data Provider / Dear Support Staff, |  |
| Advantage and the Advantage .NET Data Provider  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Things change, and in the computer software industry things change fast. But one thing that hasn't changed is your need to access data. It's the way you access data that has changed.

The most recent data access mechanism, at least for now, is ADO.NET, the data access layer of the .NET FCL (framework class library). This technology is significant, and sooner or later you'll probably be using it if you are not already using it. And when you do, you'll be glad to find that Advantage is there with you.

This chapter provides you with an introduction to data access using the .NET FCL, specifically ADO.NET. It begins with an overview of ADO.NET and the Advantage .NET Data Provider. It continues with a look at accessing your Advantage data using Advantage and ADO.NET.

In keeping with the language-agnostic nature of Advantage, data access is demonstrated in this chapter using C#, one of the newest object-oriented languages. Keep in mind, however, that .NET classes are .NET classes, regardless of which .NET-enabled language you use. Consequently, all the data access techniques demonstrated in this chapter can be used from any .NET language, including VB for .NET, C#Builder, Delphi for .NET, and Visual J# for .NET, to name a few.