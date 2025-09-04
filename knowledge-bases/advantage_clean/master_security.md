---
title: Master Security
slug: master_security
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_security.htm
source: Advantage CHM
tags:
  - master
checksum: 105919eccbd53a63e17a97b1519b9debb5b5082d
---

# Master Security

Security

Replication Security

Advantage Concepts

| Replication Security  Advantage Concepts |  |  |  |  |

While replication introduces many possibilities for flexible and innovative solutions, as well as possibilities for protecting valuable data, it also opens up security concerns. Because of this, Advantage only allows replication from and to Advantage Data Dictionaries. The following are some steps you can take to protect your data.

Require Authentication

Be sure to require logins in both source and target databases, and specify passwords for all user accounts. You can access this option in Advantage Data Architect in the Data Dictionary Properties dialog.

Encrypt the Replication Queue

The replication queue is an Advantage table. As part of the subscription definition, you specify the path for the queue; if the queue is in a location where access to it may be breached, you might consider encrypting the table. You can encrypt it the same way you encrypt any table. Specify the table encryption password in the Data Dictionary properties. In Advantage Data Architect, right-click on the replication queue table in the Connection Repository and choose Encrypt. The name of the replication queue will be the name of the subscription with which it is associated prefixed with two underscore characters (e.g., \_\_sub1).

Logging Data with Replication Failures

One of the subscription options is whether or not to log the data associated with replication failures. The default is to not log this information. When a replication update fails, the parameterized SQL statement that was used to attempt the update is logged to the Advantage Error Log. If the option is selected to log the data, then all searchable column data will be logged with the SQL statement. This can make it simpler to determine why the update failed. For example, you can look at the data for the WHERE clause to determine what target record should have been updated. However, if the replication data is sensitive, you may not want to include it in the error log.

Use Encrypted Communications

If the network connection between the source and target database is not secure and can possibly be compromised by network sniffing utilities, you should use [encrypted communications](master_communications_encryption.md) to reduce the risk of the data being viewed. If using the default encryption, you can choose the Encrypt Communication option in the Data Dictionary properties dialog in Advantage Data Architect. Note that this will cause all communications to be encrypted for all users connected to the target database. For Transport Layer Security (TLS) communications, choose TLS as the communications type and provide the TLSCertificate and TLSCommonName properties.

If some non-replication connections to the target are made over a more secure network that does not need encryption, you might consider using an AIS connection for the replication communications. At the target, you need to enable Internet access in the Data Dictionary properties dialog. Choose "Authenticate & Encrypt" for the security level. Remember to specify the Internet Port in the Advantage configuration.

If you are using an AIS connection for the replication communication, specify the IP and port in the connection path in the target database (e.g., \\198.102.102.1:2001\path\test.add), and choose Advantage Internet Server as the target connection type.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.md)
