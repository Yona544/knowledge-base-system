---
title: Devguide Overview Of Stored Procedures
slug: devguide_overview_of_stored_procedures
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_overview_of_stored_procedures.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 06dc5108e9e407fb06caee47333ef73f163baffc
---

# Devguide Overview Of Stored Procedures

Overview of Stored Procedures

 

     Overview of Stored Procedures

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Overview of Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A stored procedure is a code routine that can be loaded by Advantage and executed at the request of a client application. These routines are very flexible, in that you can pass any number of parameters to the stored procedure, which in turn can use these parameters to identify how it should perform its task. In turn, the stored procedure can return data, which can be as simple as a single value or as complicated as an entire record setsimilar to the result set returned by a view or query.

To say that stored procedures are useful is a gross understatement. Simply put, stored procedures provide your applications with speed, efficiency, and power, all in a reusable package that can be updated independently of your client applications.

The following is a list of the benefits that stored procedures provide your applications:

•        Any client that has permission to use a stored procedure can execute it. This ensures that the operations embodied in the stored procedure are performed consistently regardless of which client application invokes the procedure. By comparison, if those same operations were performed by client applications, it would be up to you to ensure that each client performs the task the same way.

| • | You can design your stored procedure to accept parameters, and then use those parameters to customize the operation that the procedure performs. For example, you can design a stored procedure to perform some operation on records associated with a particular customer. This stored procedure would likely require at least one parameter, which would identify the customer whose records the procedure should process.  A given stored procedure has a fixed number of parameters, but how many it has is something that you define when you register it in a data dictionary. These parameters can be of any data type supported by ADT tables. |

| • | You can design your stored procedure to return data. This data is in the form of a result set consisting of rows and columns. In fact, when a stored procedure returns a result set, that result set can be treated like a readonly table. |

| • | Your stored procedure can perform any operation supported by the development environment in which it was written, even if that same operation is not supported by your client application's development environment. For example, if you write your stored procedure using a language that can spawn new threads, the stored procedure can spawn a new thread even if a language that does not support multithreaded development (such as Visual Basic 6) invokes the procedure. |

| • | Stored procedures can be updated and deployed without requiring changes to your client applications. So long as you do not change the number of parameters that your stored procedure accepts, or the number of columns your stored procedure returns in its result set, your existing client applications can invoke the updated stored procedure and immediately benefit from your updates. |

| • | For many types of data-intensive operations, stored procedures can dramatically reduce network traffic compared to performing those same operations from your client applications. For example, imagine that you need to generate a report that prints 100,000 records. If you print that report from your client application, it will need to retrieve all 100,000 records from the server. By comparison, printing that report from the stored procedure invoked from ADS means that no records need to be transferred across the network in order to format the report. |

| • | The use of stored procedures permits you to benefit from distributed computing. Your client applications run on the individual workstations, but the stored procedures execute on the server. |

| • | With ADS 7.0 and later, stored procedures have unlimited access to the objects in a data dictionary. This permits you to define tables and views, for example, that a user cannot access directly, but can be accessed through the controlled environment of a stored procedure. |

   
NOTE: Using stored procedures with ALS (Advantage Local Server) does not provide all of the benefits realized when using stored procedures with ADS. When used with ALS, stored procedures execute on the workstation with your client application. As a result, you do not benefit from reduced network traffic and distributed computing. However, the use of stored procedures with ALS ensures that these benefits will be gained when you scale your application to use ADS.
