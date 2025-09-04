---
title: Master Se Passwords
slug: master_se_passwords
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_se_passwords.htm
source: Advantage CHM
tags:
  - master
checksum: 20f93548e22bbdf78aec11dc6146fbbb7e3f6eb6
---

# Master Se Passwords

SE Passwords

SE\_Passwords

Advantage Database Server

| SE\_Passwords  Advantage Database Server |  |  |  |  |

The SE\_PASSWORDS configuration provides a mechanism for specifying "strong encryption" passwords for data dictionaries. If one or more passwords are provided, Advantage Database Server will generate and store the key data for each specified dictionary at startup time and store the necessary key data for using AES encryption on the dictionary and associated tables. If a [strongly-encrypted](master_encryption.md) dictionary is being used and this configuration parameter is not specified, then the first connection to the dictionary must provide the password via the [DDPassword connection](ace_adsconnect101.md) string option.

Specifying the SE\_PASSWORDS configuration parameter (or the equivalent SEPasswords command line parameter) possibly provides a more secure option over requiring applications to provide the DDPassword option in the connection string. One benefit is that neither the application nor the user need supply this password and it can remain more secure while the application will still require normal data dictionary logins and authentication. If you decide to provide the password in the connection string from the application, you may want to use [communications encryption](master_communications_encryption.md). The password is not sent in the clear over the wire; it is encrypted using the current encryption type but with a hard coded password, therefore it should only be considered a form of obfuscation. For true security, you should use encrypted communications.

The value is a semicolon-delimited list of filename=password pairs. Its primary use is to provide dictionary passwords. But it can also hold free table passwords for the purpose of failed transaction cleanup. If one of the values is a single entry (as opposed to a filename=password style entry), then that password is simply stored and is attempted for encrypted dictionaries and free tables for failed transaction cleanup (when no specific password is given). The passwords provided for specific files are not stored in memory after they are used (only the derived key data is kept). If the single "global" password is provided, it is kept in memory as long as Advantage Database Server is loaded. Please note that white space is significant in these values.

This example provides a single password for one specific dictionary:

SE\_PASSWORDS=c:\adsdata\sales.add=password

The next example provides passwords for two specific dictionaries, a "global" password to be used generically, and one specific free table password:

SE\_PASSWORDS=c:\path1\collection.add=somepassword;c:\path2\other.add=otherpassword;freetablepassword;c:\freetables\pictures.adt=kodak

 

This example provides just one single password that will be attempted for encrypted dictionaries and encrypted free tables for failed transaction cleanup. Note that the single global password is not used for dictionaries that are not encrypted (even if the tables in the dictionary are encrypted with AES).

SE\_PASSWORDS=onepassword

This option is equivalent to the command line parameter /SEPasswords
