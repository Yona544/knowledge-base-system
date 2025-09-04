Integrating TPS into Advantage Applications




Advantage Database Server 12  

Integrating TPS into Advantage Applications

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Integrating TPS into Advantage Applications  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Integrating TPS into Advantage Applications Advantage Concepts master\_Integrating\_tps\_into\_advantage\_applications Advantage Concepts > Advantage Functionality > Transaction Processing System (TPS) > Integrating TPS into Advantage Applications / Dear Support Staff, |  |
| Integrating TPS into Advantage Applications  Advantage Concepts |  |  |  |  |

Before integrating Advantage TPS into an Advantage application, what warrants a "transaction" within the confines of the application should be defined. If updates and appends involve multiple records in one or more tables, consider handling the appends and updates as one transaction. Because Advantage provides extensive table locking and update flexibility, there are certain factors to keep in mind when introducing Advantage TPS into your applications.

In general, care should be taken to keep the transaction duration as short as possible. This will help improve concurrency between clients updating the same records, as well as help make changes visible to other users sooner. User interface I/O should not be part of a transaction.

[Data Locking and Transaction Processing](master_data_locking_and_transaction_processing.htm)

See the following topics in the Advantage Client Engine help (ACE.HLP) (Note that each of the Advantage products and their corresponding Help files are installed separately.):

|  |  |
| --- | --- |
| · | Capturing Errors and Error Recovery with the Advantage Client Engine API |

|  |  |
| --- | --- |
| · | Advantage Client Engine Transaction Processing APIs |

|  |  |
| --- | --- |
| · | Advantage Client Engine API TPS Examples |