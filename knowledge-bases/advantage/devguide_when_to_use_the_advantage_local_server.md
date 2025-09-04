When to Use the Advantage Local Server




Advantage Database Server 12  

     When to Use the Advantage Local Server

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| When to Use the Advantage Local Server  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      When to Use the Advantage Local Server Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_When\_to\_Use\_the\_Advantage\_Local\_Server Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > When to Use the Advantage Local Server / Dear Support Staff, |  |
| When to Use the Advantage Local Server  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

If ADS is so much better than a database engine solution like ALS, why does Sybase iAnywhere bother making ALS available? There are several reasons, but they are all related to a simple fact. Not all applications require the benefits of ADS.

Imagine you have written a database application that you plan on licensing to many different clients. Your software is probably pretty expensive, and pricing may be an issue for some of your customers. For example, consider a customer who will have only one or two users on the system. The additional cost of an ADS license may make the difference between that customer buying your software or not. For those customers, you can deploy the application using ALS.

Imagine this same customer at some later time. Maybe they now have four simultaneous users, and they cannot tolerate the occasional corruption of an index due to a workstation crash. For a relatively small amount of money, you can upgrade their application to use the Advantage Database Server, and your customer can say "goodbye" to corrupt indexes.

For other customers, especially those who have a large number of users, there is no question about ityou will deploy their applications using ADS.

What is so great about this scenario is that there is no difference, from a development standpoint, between your application using ALS or ADS. The API (application programming interface) for ALS and ADS is exactly the same. And most of the time, upgrading an ALS application to use ADS is simply a matter of installing the server (a process that can be automated). Depending on how you designed your original application, it may not even be necessary to recompile the client application.

To put this another way, whether an application uses ALS or ADS is a deployment issue, not a development issue. You will write your application the same way regardless of which deployment option you choose.

Actually, there are a couple of differences, but they really serve more to underscore how similar the two interfaces are. As you have already learned, you can write your application to employ transactions, but only when you deploy with ADS will those statements actually do something.

There is another difference. If you are using the Java language and want to use the Advantage JDBC (Java database connectivity) Driver, you can only use ADS. This is because the Advantage JDBC Driver is a class 4 driver, which is to say that it communicates directly with the server without going through a client API. If you want to use Java with ALS, you must use the JDBC-ODBC bridge (a class 1 driver), in conjunction with the Advantage ODBC (open database connectivity) Driver.

The second difference is related to triggers and extended stored procedures. With ADS, both triggers and stored procedures execute on the server. Since ALS is not a remote database server, any triggers or stored procedures will actually execute on the client workstation, so you lose the major benefits of distributed computing and reduced network traffic.

The bottom line is that ALS is a wonderful option for database developers. It provides you with a low-cost deployment option that effortlessly scales to client/server when client/server features are required.

   
NOTE: In addition to the minor differences pointed out here, there are additional capabilities supported by ADS but not by ALS. These include online backup, replication, access from Web-based clients, and database access across the Internet.  
 

Throughout this book we will assume that you are going to deploy your applications using ADS. But we will try to point out when a feature we are describing works differently between ADS and ALS.