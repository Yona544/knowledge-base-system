Data Dictionaries and Table Encryption




Advantage Database Server 12  

 

     Data Dictionaries and Table Encryption

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data Dictionaries and Table Encryption  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Data Dictionaries and Table Encryption Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Data\_Dictionaries\_and\_Table\_Encryption Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Data Dictionaries and Table Encryption / Dear Support Staff, |  |
| Data Dictionaries and Table Encryption  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Data dictionaries significantly simplify the process of working with encrypted tables. With free tables, each table can have a different password, and this password must be submitted to Advantage prior to accessing the associated table.

With data dictionaries, a single password is applied to all encrypted tables. Better still, there is no longer any need to pass the table password to Advantage prior to accessing an encrypted database table. Instead, Advantage reads the password from the data dictionary. Data dictionaries also encrypt your data dictionary objects such as views and stored procedures.

Both Advantage servers and clients support table encryption using an industry standard 160-bit encryption algorithm. In addition to encrypting the data in the table, with ADT tables, the tables field headers are also encrypted.

Advantage 8 adds two additional levels of encryption: communication encryption and index encryption. Communication encryption encrypts all client/server communication transmitted over a network (although encrypted tables are sent over networks encrypted whether you are using data dictionaries or free tables). Note that while table encryption is designed to protect tables on disk, communication encryption is designed to protect client/server communications over the wire. Communication encryption and index encryption are covered later in this chapter.