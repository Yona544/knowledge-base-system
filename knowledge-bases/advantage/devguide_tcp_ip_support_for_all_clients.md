TCP/IP Support for All Clients




Advantage Database Server 12  

     TCP/IP Support for All Clients

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TCP/IP Support for All Clients  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      TCP/IP Support for All Clients Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_TCP\_IP\_Support\_for\_All\_Clients Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > TCP/IP Support for All Clients / Dear Support Staff, |  |
| TCP/IP Support for All Clients  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Prior to Advantage 8, most communication between an Advantage client and ADS used UDP (user datagram protocol) over IP. Only the class 4 Java driver used TCP (transmission control protocol).

Advantage 8.1 now supports TCP for all client communications. The support for TCP is particularly valuable for those applications where it is not possible to open a UDP port in firewalls between the client and server.

Note, however, that Advantage's proprietary technology using UDP is exceptionally efficient compared to the more bandwidth-intensive TCP standard. As a result, performance using UDP is superior to that using TCP, making UDP the preferred protocol for Advantage communications.

 

In the next chapter you will learn about the various table types supported by Advantage.