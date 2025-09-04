Important Notes




Advantage Database Server 12  

Important Notes

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Important Notes  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Important Notes Advantage Database Server master\_Important\_notes Advantage Database Server > Introduction > Important Notes / Dear Support Staff, |  |
| Important Notes  Advantage Database Server |  |  |  |  |

Advantage Database Server

For best performance, the Windows 2000/2003 server running the Advantage Database Server should be configured so that foreground applications have NO performance boost. If foreground applications are given a performance boost, it is possible for the Advantage Database Server to "starve" and provide poor performance. With Windows 2000/2003, turn off foreground application performance boost by double-clicking the "System" icon in the control panel folder. With Windows 2000/2003, click on the "Advanced" tab and click the "Performance Options" button.

Advantage client to Advantage Database Server backwards compatibility is supported. Thus, the latest Advantage Database Server can be running on your server without having your application using the latest Advantage client libraries. However, if an application is not using the latest Advantage client libraries, new features in the client will not be available to your application. Also, new features in the Advantage Database Server may not be available to your application. If the version of the Advantage Database Server is older than the version of the Advantage client libraries used by your application, either an "Advantage Client incompatible with Advantage Server" error or an "Advantage Server not available" error will result. The ADSVER.EXE utility supplied in your Advantage directory can be used to determine the version of the Advantage Database Server executable and the Advantage Client libraries used by your application.

Advantage Local Server

The Advantage Local Server allows Advantage applications to access tables, index files, and memo files that are located on computers that are not running the Advantage Database Server. The Advantage Local Server does NOT provide a client/server solution in a networked environment like the Advantage Database Server does. Thus, the client/server benefits of drastically increased multi-user performance, integrity, and security, which are available with the Advantage Database Server client/server solution, are not available when using the Advantage Local Server in a networked environment.

By default, the only Advantage server types an Advantage application will attempt to connect to is the Advantage Database Server or the Advantage Internet Server. Thus, by default, an Advantage application will NOT attempt to connect to the Advantage Local Server, even if the connect is attempted on a PC on which the Advantage Database Server is not available. Refer to one of the Advantage client specific help files to determine how to enable use of the Local Server for the desired Advantage client.

If the Advantage server types in which to connect are specified as "either" the Advantage Database Server or the Advantage Local Server, the Advantage application will first attempt to connect to the Advantage Database Server and then to the Advantage Local Server if the Advantage Database Server is not available. The very first connect attempt to the Advantage Database Server MAY TAKE UP TO TWO SECONDS TO TIME OUT if the Advantage Database Server is not available before automatically attempting to connect to the Advantage Local Server. Any further connection attempts to the Advantage Database Server for that server will fail immediately. The two second timeout will only occur if the Advantage Database Server is not present on the specified server AND if the Advantage remote communication DLL (AXCWS32.DLL) is located in the client PC's search path. If the Advantage remote communication DLL is NOT located in the client PC's search path, the timeout of the connect to the Advantage Database Server will be immediate.

Transaction Processing is not supported in the Advantage Local Server. Use of Advantage Transaction Processing functionality may appear to complete successfully, but in fact, use of Transaction Processing features will be ignored.

ADSLOCAL.CFG is the Advantage Local Server configuration file. The Advantage Local Server reads this configuration file when the library is loaded. Values input after the keyword and equal sign are used to configure the local server. If no value is inserted after a keyword and equal sign, the default is used. This file must be located in each client PC's current working directory or in it is search path (e.g. the \WINDOWS\SYSTEM directory in Windows, or the /etc directory in Linux).

Language

The Advantage products (including software and documentation) are only available in English.