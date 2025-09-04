---
title: Master Linux 6060 Errors
slug: master_linux_6060_errors
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_linux_6060_errors.htm
source: Advantage CHM
tags:
  - master
checksum: a5ef3bbc2414ae1eed50f334d15bcfaff1db1a3e
---

# Master Linux 6060 Errors

Linux 6060 Errors

Linux 6060 Errors

Advantage Concepts

| Linux 6060 Errors  Advantage Concepts |  |  |  |  |

It is possible to receive a 6060 error if the Advantage Database Server daemon started but had a problem registering for multicast discovery packets. If this happens, you will find a detailed error message in the ads\_log.txt file.

Following are known issues that can cause this behavior:

- No default gateway assigned. The server must have a default gateway or the multicast registration will not be successful.

- Some users have mentioned they had to enable ip forwarding to resolve this issue.

Other Linux-specific issues that can cause a 6060 error include the following:

- Invalid or incorrect IP address in the /etc/hosts file

- Incorrect hostname assigned. Verify the hostname returned by running the 'hostname' utility is the same as the name used in the connection string.

- If using Samba verify the directory you are sharing is located directly off of the root. For example the Samba share \\testserv\myshare must be sharing the /myshare directory.
