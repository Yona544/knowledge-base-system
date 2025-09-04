Setting the Internet Port Configuration Parameter




Advantage Database Server 12  

Setting the Internet Port Configuration Parameter

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Setting the Internet Port Configuration Parameter  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Setting the Internet Port Configuration Parameter Advantage Database Server master\_Setting\_the\_internet\_port\_configuration\_parameter Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Setting the Internet Port Configuration Parameter  Advantage Database Server |  |  |  |  |

This parameter controls Internet access to the Advantage Database Server. If the Internet port is set to zero, Internet access to the Advantage Database Server is disabled.

For Windows:

|  |  |
| --- | --- |
| 1. | Start the Advantage Configuration Utility. |

|  |  |
| --- | --- |
| 2. | Select the Configuration Utility tab. |

|  |  |
| --- | --- |
| 3. | Select the Communications tab. |

|  |  |
| --- | --- |
| 4. | Enter the Internet Port number. |

|  |  |
| --- | --- |
| 5. | Click Apply. |

If the Advantage Database Server is running, it will need to be re-started before the changes take place.

For Linux:

|  |  |
| --- | --- |
| 1. | Open the ads.conf file in a text editor. |

|  |  |
| --- | --- |
| 2. | Look for the INTERNET\_PORT option. The port number is the decimal value of the port you want to listen to. |

|  |  |
| --- | --- |
| 3. | Save the file. |

|  |  |
| --- | --- |
| 4. | Kill and restart the ADS daemon. |