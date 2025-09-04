Backup and Restore Canned Procedure Result Sets




Advantage Database Server 12  

Backup and Restore Canned Procedure Result Sets

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Backup and Restore Canned Procedure Result Sets  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Backup and Restore Canned Procedure Result Sets Advantage Concepts master\_Backup\_and\_restore\_canned\_procedure\_result\_sets Advantage Concepts > Advantage Functionality > Backup > Backup and Restore Canned Procedure Result Sets / Dear Support Staff, |  |
| Backup and Restore Canned Procedure Result Sets  Advantage Concepts |  |  |  |  |

The backup and restore canned procedures return a result set with one or more rows of the following format. If an empty set is returned, the operation was a success and there were no warnings or errors to report.

Severity,Integer

Error Code,Integer

Error Message,Memo

Table Name,Memo

Additional Info,Memo

Source File,char,32

Source Line,Integer

 

Severity

An integer representation of the severity of the result set error/warning. The value of this field will range between 0 and 10, with 0 being the lowest severity, and 10 being the highest.

Error Code

The Advantage error code for this entry.

Error Message

A text message for this error or warning.

Table Name

The name of the table that generated this entry.

Additional Info

Additional information (if available) about this entry.

Source File

Internal source file that generated this entry.

Source Line

Internal source line that generated this entry.