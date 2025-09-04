5185 AE\_LOCAL\_CONN\_RESTRICTED




Advantage Database Server 12  

5185 AE\_LOCAL\_CONN\_RESTRICTED

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5185 AE\_LOCAL\_CONN\_RESTRICTED  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5185 AE\_LOCAL\_CONN\_RESTRICTED Advantage Error Guide error\_5185\_ae\_local\_conn\_restricted Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5185 AE\_LOCAL\_CONN\_RESTRICTED  Advantage Error Guide |  |  |  |  |

Advantage Local Server connections are restricted when used from a web server, an application server, a terminal server, or any other type of middleware or server product used to access data on behalf of remote computers.

If you receive this error, it is because your application attempted to make a local server connection from one of these restricted environments. Please review the Advantage Local Server Connections portion of the end user license agreement (license.txt, Section B) for details.

It is possible to get this error when you are not violating the license agreement. If, for example, your web application accesses local data that it uses internally, but is never transferred to a client, that usage is legal.

If you are using the Advantage Local Server to access data in this manner (or some similar manner where no data is used or seen by a client), and you receive this error code, you can add the following line to the ads.ini file under the [SETTINGS] section to disable this check:

MTIER\_LOCAL\_CONNECTIONS=1

Note Disabling this check when in violation of permitted connection scenarios set forth in the end user license agreement is a material breach of the license agreement and places you liable to provide appropriate consideration and remedy to iAnywhere.

 

Note The ads.ini file can be placed in the same directory as the application, in order to modify this behavior on an application-specific basis.

The specific text in the Advantage end user license agreement regarding use of Advantage Local Server and middleware connections (Section B) is as follows. Refer to the Advantage license agreement, license.txt, for the complete EULA.

If an application using this SOFTWARE PRODUCT is distributed to work without the Advantage Database Server (i.e., it uses the Advantage Local Server to access data), the application must act as a "client" that directly accesses and uses the data. To be specific, only computers that have the Advantage Local Server DLL loaded into memory can have access to the data that is obtained by that Advantage Local Server DLL. The application cannot act as "middleware" or as a "server" by having the data forwarded by any means to a separate computer. In other words, it is illegal to use the Advantage Local Server with a web server, an application server, a terminal server, or any other type of middleware or server product to access data on behalf of remote computers. An Advantage Database Server (a.k.a., remote server) product must be purchased and used to allow this SOFTWARE PRODUCT to access data on behalf of applications running on remote computers.