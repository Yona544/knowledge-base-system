Advantage Database Server Versus Advantage Local Server




Advantage Database Server 12  

 

     Advantage Database Server Versus Advantage Local Server

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Database Server Versus Advantage Local Server  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Advantage Database Server Versus Advantage Local Server Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Advantage\_Database\_Server\_Versus\_Advantage\_Local\_Server Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > Advantage Database Server Versus Advantage Local Server / Dear Support Staff, |  |
| Advantage Database Server Versus Advantage Local Server  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

In addition to ADS, Sybase iAnywhere also provides a database engine called the Advantage Local Server (ALS). ALS is very similar to Microsoft's Jet Engine, which is used by MS Access, and Borland's BDE (Borland Database Engine) when the BDE is using local tables. All of these database engines are file-server database engines.

Unlike a database server, which is a stand-alone application, a database engine is essentially a library of data access routines that runs in the same process as the client application. Each client application loads its own copy of these database engine files, and each client application is responsible for all data manipulation.

Sybase iAnywhere makes ALS available to developers free of charge. Developers can use ALS with their stand-alone and small multiuser applications, and can even distribute these applications to their clients without paying any royalty fees. The only applications that you are prohibited from using ALS with are those applications that run on the Internet, such as CGI (common gateway interface) Web server extensions and Web services. For those types of applications, you must use ADS.

Why, you are probably wondering, should you use ADS if you can use ALS for free? The answer is simple. ADS is better.

Actually, the benefits of a database server like ADS over database engines like ALS are associated with four factors. These are reduced network traffic, improved performance, transactions, and unparalleled stability. Each of these factors is examined in the following sections.