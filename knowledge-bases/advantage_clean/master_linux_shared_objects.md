---
title: Master Linux Shared Objects
slug: master_linux_shared_objects
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_linux_shared_objects.htm
source: Advantage CHM
tags:
  - master
checksum: 33d8a75a1da49b4a2d9eaa33e8d2d6222b942984
---

# Master Linux Shared Objects

Linux Shared Objects

Linux Shared Objects

Advantage Concepts

| Linux Shared Objects  Advantage Concepts |  |  |  |  |

The Advantage Client Engine (ACE) and the Advantage Local Server (ALS) are distributed as Linux shared objects. Although not identical, shared objects are very similar to Windows DLLs. The default installation directory for the Advantage libraries is the /usr/lib directory.

Although a full explanation of shared objects is beyond the scope of this Help documentation, a short explanation is in order. After installing Advantage, a directory listing of "ls l libace\*" while in the /usr/lib directory might look like this:

lrwxrwxrwx 1 root root 41 Nov 30 09:45 libace.so -> libace.so.6.11

lrwxrwxrwx 1 root root 41 Nov 30 09:45 libace.so.6.11 -> libace.so.6.11.0

-rwxr-xr-x 1 root root 2110762 Nov 30 09:45 libace.so.6.11.0

Note that libace.so and libace.so.6.11 are merely soft links to the actual driver, which is the libace.so.6.11.0 file. Soft links are a very powerful tool when determining which shared object your application will load. All Advantage clients link directly to the shared object with a file name that matches their version. For example, the Advantage TDataSet Descendant version 6.11 links to the ACE library libace.so.6.11, which in turn has a soft link that points to the libace.so.6.11.0 file.

Because your application does not link directly to the driver file, updates are simple. If Advantage releases a bug fix or some other update you would simply replace libace.so.6.11.0 with the updated file (libace.so.6.11.1, for example). Another nice feature of Linux is the shared object can be replaced on disk even while an application has the current object loaded. This allows you to replace the driver without forcing all of the current users to close the application. The next time they open the application they will automatically start using the updated shared object.

This versioning system also allows you to have multiple versions of shared object libraries in the same directory. For example, if you have one application that uses Advantage 6.11, and another that uses Advantage 6.2, you do not need to put the ACE shared objects into separate directories like you would in Windows (although this method is still recommended). In Linux you could have a /usr/lib directory that looked like this, and both Advantage-enable applications would load the correct shared object:

lrwxrwxrwx 1 root root 41 Mar 22 10:40 libace.so -> libace.so.6.20

lrwxrwxrwx 1 root root 41 Mar 22 10:40 libace.so.6.20 -> libace.so.6.20.0

-rwxr-xr-x 1 root root 2690132 Mar 22 10:40 libace.so.6.20.0

lrwxrwxrwx 1 root root 41 Nov 30 09:45 libace.so.6.11 -> libace.so.6.11.0

-rwxr-xr-x 1 root root 2110762 Nov 30 09:45 libace.so.6.11.0

The Advantage Local Server shared object is named libadsloc.so.X.YY.Z, where X, Y, and Z are version numbers (just as they are in the ACE shared object).

See Also

[Distributing Advantage Shared Objects](master_distributing_advantage_shared_objects.md)
