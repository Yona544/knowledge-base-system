6425 An Advantage Data Dictionary connection is required for Internet connections




Advantage Database Server 12  

6425 An Advantage Data Dictionary connection is required for Internet connections

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6425 An Advantage Data Dictionary connection is required for Internet connections  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6425 An Advantage Data Dictionary connection is required for Internet connections Advantage Error Guide error\_6425\_an\_advantage\_data\_dictionary\_connection\_is\_required\_for\_internet\_connections Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6425 An Advantage Data Dictionary connection is required for Internet connections  Advantage Error Guide |  |  |  |  |

Problem: When connecting to the Advantage Database Server through an Internet connection, a 6425 error occurs.

Solution: The Advantage Data Dictionary contains user names, passwords, and other needed information required for a secure connection over the Internet. All Internet connections require an Advantage Data Dictionary connection.

In the connection path, specify the full path and file name of the Advantage Data Dictionary.

If you are trying to connect using the Advantage Management Utility, it will not work because Internet connections through this utility have not been implemented. The code for the Advantage Management Utility can be modified to use an Internet-enabled Advantage Data Dictionary connection instead of a management connection. (See AdsConnect60() for details on obtaining an Internet Advantage Data Dictionary Connection.)