Advantage Troubleshooting Tools




Advantage Database Server 12  

Advantage Troubleshooting Tools

Troubleshooting

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Troubleshooting Tools  Troubleshooting |  |  | Feedback on: Advantage Database Server 12 - Advantage Troubleshooting Tools Troubleshooting master\_Advantage\_troubleshooting\_tools Troubleshooting and Technical Support > Troubleshooting > Advantage Troubleshooting Tools / Dear Support Staff, |  |
| Advantage Troubleshooting Tools  Troubleshooting |  |  |  |  |

The following tools will help assist in product development and troubleshooting.

Advantage Data Architect (ARC32.EXE)

This data management tool provides an interface for common table management tasks and many other useful features. Some of the functionality of this tool include:

|  |  |
| --- | --- |
| · | Complete data management functionality such as table creation, restructuring, indexing, packing, etc. |

|  |  |
| --- | --- |
| · | Importing and converting other table types such as Paradox and Access tables. |

|  |  |
| --- | --- |
| · | Testing filter expressions to determine the level at which they will be optimized. |

|  |  |
| --- | --- |
| · | Testing Advantage SQL engine queries. |

|  |  |
| --- | --- |
| · | Testing ODBC SQL queries. |

|  |  |
| --- | --- |
| · | Environment checking which can be used to test and diagnose connection issues with the Advantage Database Server. |

|  |  |
| --- | --- |
| · | Checking server activity with the built in Advantage Management utility. With this functionality, you can verify that files are actually opened by the Advantage Database Server. You can also remotely determine which index files are opened, which users are connected, what installation parameters where selected, what files or records are locked, and how many transactions are in progress. |

|  |  |
| --- | --- |
| · | Creating aliases. An alias configuration utility is included in the Advantage Data Architect. This functionality in ARC allows you to set up aliases similar to Delphi database aliases. |

|  |  |
| --- | --- |
| · | Creating queries using a built in visual query designer |

16MODMAN.EXE and 32MODMAN.EXE

The Modman utilities are used to show which DLLs are being loaded by currently running executables. This is useful in determining if the intended DLL is being loaded, or if a DLL is being loaded from an unexpectedly directory which may cause unexpected behavior or version mismatch errors.

ADSVER.EXE

The installation of the Advantage Database Server includes a file called ADSVER.EXE. This can be used to determine the version of Advantage that is linked into a CA-Clipper application, the version of an Advantage client DLL, Library, or RDD, or the version of an Advantage Database Server NLM, EXE, or DLL.

TEST43.EXE

When comparing the performance of Advantage with another driver, it's important to realize that Advantage will always read a record's contents across the network when you skip to it, because it assumes that you have moved to it for a reason. Other drivers may only change the position of the record pointer, so performance comparisons will be misleading. TEST43.EXE is a CA-Clipper application that demonstrates a simple example of how to do an accurate performance test.

Readme and Help Files

Documentation for all Advantage products is continuously being improved with each new release. Always check the latest Readme and Help file for the most up to date information.

Advantage Internet Server Demo

The AIS demo can be used to demonstrate the Advantage Internet Server to your customers from anywhere in the world, since it will connect to an Advantage Database Server here at iAnywhere via the Internet. The Advantage Data Architect can also be used to test an Internet connection to the Advantage Database Server on your network or over the Internet.

Advantage Developer Zone Web Site

The main Advantage Web site can found at www.AdvantageDatabase.com. This is where you can find product information, performance benchmark test results, and customer success stories. From this page there is a link to the Advantage Developer Zone Web site, http://DevZone.AdvantageDatabase.com, where you will find many valuable troubleshooting resources, such as the information knowledge base, developer newsgroups, and an FTP site containing all Advantage troubleshooting tools, sample code, documentation, and service updates.