Communication and Index Encryption




Advantage Database Server 12  

     Communication and Index Encryption

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Communication and Index Encryption  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Communication and Index Encryption Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Communication\_and\_Index\_Encryption Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Communication and Index Encryption / Dear Support Staff, |  |
| Communication and Index Encryption  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Another security-related setting for a data dictionary is associated with encryptionspecifically, encrypted communications and encrypted indexes. Both of these settings are available from the encryption section of the Security page of the Data Dictionary dialog box (shown previously in Figure 4-5), which you display by right-clicking on the data dictionary connection and selecting Properties from the context menu. These security settings are discussed in the following sections.

Encrypting Communications

When you enable the Encrypt Communication option, client/server communication across the local network is encrypted. Prior to Advantage 8, only Internet communication could be encrypted.

Encrypting communications over your internal network reduces the performance of your Advantage applications. As a result, you might wonder why anyone would enable this feature.

The answer is that not all internal networks are secure. For example, some companies permit employees to connect to their network over unsecure wireless connections. These communications might be visible to individuals in the proximate vicinity of the wireless access points.

While not common, there are also documented cases of disgruntled employees or "corporate spies" who are wired to the internal network and who trace network communications in order to access confidential data.

But there is another point. While encrypted tables are naturally transferred across a network in encrypted form, SQL queries and other similar communication are not normally encrypted. If you consider that SQL INSERT statements contain raw data, you will realize that working with encrypted tables and indexes is not sufficient to protect your data. By enabling encrypted communication, you ensure that all data is encrypted, including queries.

The bottom line is that if your Advantage applications include sensitive data and you want greater assurances that this data will not be accessed by unauthorized persons, the slight performance degradation resulting from encrypting network communications is worth the additional security that results.

Encrypting Indexes

Normally, indexes are not encrypted. In most applications where ADS is being used, these indexes are not accessible to end users anyway (so long as users do not have rights to the data directories on the server), so encryption is not really an issue.

However, when using ALS with local tables, or when using ADS where the data resides on the end user's machine, it may be possible for a user to view indexes using a simple file-viewing tool, even something like Microsoft's WordPad.

With Advantage 8, it is possible to encrypt indexes of data dictionarybound ADT tables. If some of your index expressions include confidential fields, and your data directories may be accessible to end users, enable the Encrypt Indexes checkbox on the Security page of the Data Dictionary dialog box.

If you enable encrypted indexes on existing tables with existing index definitions, you must explicitly re-index all of your tables in order to encrypt them.