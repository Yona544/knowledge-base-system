---
title: Devguide Enhanced Security
slug: devguide_enhanced_security
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_enhanced_security.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 62436fa807c8c1edfcf49235d51e8ba77b6ee906
---

# Devguide Enhanced Security

Enhanced Security

     Enhanced Security

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Enhanced Security  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

While already strong on security, Advantage 8 introduces several additional security enhancements. The first of these is the option to encrypt indexes. Normally, database tables and indexes are invisible to the user, being stored on secure directories on the server. Now, those stand-alone applications where the data resides on the user's machine can use encrypted indexes to prevent sensitive fields participating in the index from being viewed.

The second security enhancement is the option to encrypt client/server communication on local networks. Prior to the Advantage 8 release, only those clients connecting to ADS over the Internet had an option to employ encrypted communication.

   
NOTE: When a client accesses encrypted tables and indexes, the decryption occurs on the client. Consequently, the security benefits of encrypted network communications applies to non-encrypted tables and indexes.  
 

Encrypted indexes and encrypted network communication are only available to applications that use data dictionaries.
