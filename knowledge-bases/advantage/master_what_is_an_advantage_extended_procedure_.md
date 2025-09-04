What is an Advantage Extended Procedure?




Advantage Database Server 12  

What is an Advantage Extended Procedure?

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| What is an Advantage Extended Procedure?  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - What is an Advantage Extended Procedure? Advantage Concepts master\_What\_is\_an\_advantage\_extended\_procedure\_ Advantage Concepts > Advantage Functionality > Advantage Extended Procedures > What is an Advantage Extended Procedure? / Dear Support Staff, |  |
| What is an Advantage Extended Procedure?  Advantage Concepts |  |  |  |  |

Compared to Traditional Stored Procedures

In order to understand the flexibility and benefits that Advantage Extended Procedures offer, lets take a look at traditional stored procedures. Some database engines provide functionality for database administrators to encapsulate a set of database commands that perform logical tasks from the server. This encapsulated code is called a stored procedure.

Typically, stored procedures are written in the language of the server. They run independent of an application and generate predefined output when called from an application. By placing the execution code as close to the data as possible, data-intensive calls and tasks from the client are handled swiftly and efficiently on the server, without bogging down the network.

However, traditional stored procedures have a few drawbacks:

|  |  |
| --- | --- |
| · | They may require the purchase of add-on software or equipment. |

|  |  |
| --- | --- |
| · | They often must be written and integrated by the Database Administrator (DBA), not the application developer. |

|  |  |
| --- | --- |
| · | They often must be written using the servers proprietary scripting language. |

|  |  |
| --- | --- |
| · | The process of creating them can be tedious and time consuming. |

Move to a New Level of Database Development

The Advantage Database Server streamlines the creation and use of stored procedures. Like other products on the market, Advantage Database Server allows you to develop stored procedures that enable you to quickly execute logical tasks as they are performed on the server where the data is located. Unlike other products on the market, however, you can take full advantage of your existing development products and knowledge to write and execute stored procedures on the fly. Theres no downtime needed to familiarize you with a custom add-in or scripting language. Developers write and maintain the stored procedures themselves. Because our version of stored procedures goes above and beyond what traditional stored procedures can do, weve named them "Extended Procedures".

And there are no limits to what you can do with Advantage Extended Procedures. But why would you want to include them in your application development? Here are some of the most compelling reasons:

|  |  |
| --- | --- |
| · | You are not limited simply to what the database can doyou can write an Advantage Extended Procedure to accomplish anything that any programming tool can do. |

|  |  |
| --- | --- |
| · | They remove data-intensive tasks from the workstations as they are performed on the server. This reduces the network traffic to a single send and receive operation. |

|  |  |
| --- | --- |
| · | They centralize the code sets so multiple applications can share them. |

|  |  |
| --- | --- |
| · | Developers create and maintain the Advantage Extended Procedures without the aid of a Database Administrator. |

|  |  |
| --- | --- |
| · | Developers use their development language of choice, shortening ramp-up time and practically eliminating any learning curve. |

|  |  |
| --- | --- |
| · | Advantage offers an all-in-one solution that automates the typical Advantage Extended Procedure tasks of writing a dynamic link library (DLL), COM library, or shared object (in Linux) and registering it on the server. |

|  |  |
| --- | --- |
| · | Advantage Extended Procedures pack a lot of punch but leave a small impression on the overall server and workstation space. |

Power of Extended Procedures Exposes Server to Risks

Advantage loads Extended Procedures as in-process DLLs. This provides the best performance, but also exposes the Advantage server to any errors inside your procedures. If for example a procedure overwrites memory, it will be overwriting memory in the Advantage server process, not just in the procedure DLL. Also if a procedure DLL is not thread-safe, it can expose the server to many problems because the Advantage server is a multi-threaded process, this can also result in server crashes. Great care must be taken when writing Extended Procedures to ensure the integrity of the Advantage server.