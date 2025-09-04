---
title: Master Nfs Mounts
slug: master_nfs_mounts
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_nfs_mounts.htm
source: Advantage CHM
tags:
  - master
checksum: 329ce073d78dcd469ac3ab6feb98eaf94127ae13
---

# Master Nfs Mounts

NFS Mounts

NFS Mounts

Advantage Concepts

| NFS Mounts  Advantage Concepts |  |  |  |  |

If using Advantage Local Server to access files over an NFS mount with multiple users, you must put the "sync" and "no\_wdelay" options in your export definition. Without these options aggressive caching will be done by the operating systems and corruption will be unavoidable. See the "exports" man page for more details.

Following is an example export entry showing how to export the /localtest directory safely:

/localtest (rw,sync,no\_wdelay)

Important Note Unless you have specific patches, locking across NFS mounts was never properly implemented in Linux until the 2.4 kernel. Advantage record locks across an NFS mount will fail if you are not using a kernel version of 2.4 or greater. It is also possible for an Advantage Local Server application to hang if it attempts some other form of lock (other than an explicit record lock) on pre-2.4 kernels. If this happens, write a small application to test a record lock. If the record lock fails, it is likely that your application is hanging because of this known locking problem in pre-2.4 kernels.
