Troubleshooting Advantage Internet Connections




Advantage Database Server 12  

Troubleshooting Advantage Internet Connections

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Troubleshooting Advantage Internet Connections  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Troubleshooting Advantage Internet Connections Advantage Concepts master\_Troubleshooting\_advantage\_internet\_server Troubleshooting and Technical Support > Troubleshooting > Troubleshooting Advantage Internet Connections / Dear Support Staff, |  |
| Troubleshooting Advantage Internet Connections  Advantage Concepts |  |  |  |  |

If the client is unable to connect to the Advantage Database Server over the Internet, verify the following:

|  |  |
| --- | --- |
| · | The correct DLLs are being used on the client. |

|  |  |
| --- | --- |
| · | The ADS.INI file exists in the \WINDOWS directory, the \WINNT directory, or in the applications search path. |

|  |  |
| --- | --- |
| · | The client has an Internet connection by pinging the Advantage Internet Server host computer. Reference the ADS.INI file to get the IP address of the PC running the Advantage Internet Server. Example: C:\ ping 199.103.103.202. |

|  |  |
| --- | --- |
| · | The server name in which the database application is trying to use is in the ADS.INI file. |

|  |  |
| --- | --- |
| · | Drive letter mappings are correctly defined in the ADS.INI file. |

|  |  |
| --- | --- |
| · | The target Advantage Database Server is version 6.1 or greater. |

|  |  |
| --- | --- |
| · | The LAN computer that will be running ADS and the remote client computers that will access ADS have the IP protocol enabled and can communicate with each other across the Internet/intranet. |

|  |  |
| --- | --- |
| · | An Internet port has been specified on the Advantage Database Server. |

|  |  |
| --- | --- |
| · | An Advantage Data Dictionary has been properly created and Internet access to the Advantage Data Dictionary has been enabled. |

|  |  |
| --- | --- |
| · | The port specified for the server in the ADS.INI matches the Internet port number specified on the Advantage Database Server. |

|  |  |
| --- | --- |
| · | The connection is being made to an Advantage Data Dictionary. |

|  |  |
| --- | --- |
| · | The user within the Advantage Data Dictionary has Internet access enabled. |