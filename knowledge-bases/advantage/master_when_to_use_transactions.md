When to Use Transactions




Advantage Database Server 12  

When to Use Transactions

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| When to Use Transactions  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - When to Use Transactions Advantage Concepts master\_When\_to\_use\_transactions Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| When to Use Transactions  Advantage Concepts |  |  |  |  |

Before implementing Advantage TPS, you should define what warrants a "transaction" within the confines of your application. In most applications, a transaction is a request by a user to save the information entered in a given screen. If the data entry screen only asks for a persons name and address, the information collected in the screen is probably stored in one record. Though this is technically a "transaction", you may not necessarily implement this save operation as a transaction using Advantage TPS. On the other hand, if the data entry screen is a customer order form, there is a good chance that the data captured in the screen gets saved to a number of records in one or more tables. You would implement this save operation as a transaction since you want to ensure that either all the updates are made or that none are made.

In general, users are not aware of how an application saves information. Nevertheless, the strength of the application and its ability to ensure database stability is based on the programmers method for saving information. Defining what makes a transaction in your application is part of the methodology that will give your application strength and stability. Usually, if insertions and updates involve multiple records in one or more tables, you should consider handling the insertions and updates as one transaction.