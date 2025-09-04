What to Include in a Transaction




Advantage Database Server 12  

What to Include in a Transaction

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| What to Include in a Transaction  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - What to Include in a Transaction Advantage Concepts master\_What\_to\_include\_in\_a\_transaction Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| What to Include in a Transaction  Advantage Concepts |  |  |  |  |

A transaction consists of a command to begin the transaction, the steps to complete the transaction (your insert, update, and delete operations), and a command to end the transaction. Transactions should be limited in their complexity. In most applications, the only operations that should be included within transactions are insert, update, and delete operations. All operations that create files, open files, and receive user input should be excluded. In general, transactions should open/create files first, read/input the necessary information, begin the transaction, issue the insert and update operations, and finally, commit the transaction.