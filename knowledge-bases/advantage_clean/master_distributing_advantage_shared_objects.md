---
title: Master Distributing Advantage Shared Objects
slug: master_distributing_advantage_shared_objects
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_distributing_advantage_shared_objects.htm
source: Advantage CHM
tags:
  - master
checksum: 37b29420e2c9a1d5e00d2ed279f3a1dbf788224d
---

# Master Distributing Advantage Shared Objects

Distributing Advantage Shared Objects

Distributing Advantage Shared Objects

Advantage Concepts

| Distributing Advantage Shared Objects  Advantage Concepts |  |  |  |  |

If you application only uses the Advantage Database Server, and does not use any Advantage Local Server connections, the only shared object you will need to distribute is the libace.so.X.YY.Z file. If your application utilizes any local server connections you will also need to distribute the libadsloc.so.X.YY.Z file.

As with Windows DLLs, it is recommended you install the Advantage shared object files in the same directory with your application executable. This approach allows you to ignore the existing shared objects in the /usr/lib directory and always use the correct files.

Linux does not automatically load shared objects from the application directory, however. In order to use this technique you must modify the users LD\_LIBRARY\_PATH environment variable, which is used by the Linux shared object loader to search for objects. A simple script can accomplish this, and then your users will run this script instead of directly running your application. Below is an example of a script called "startmyapp":

#!/bin/bash

export LD\_LIBRARY\_PATH=/path/to/my/exe:$LD\_LIBRARY\_PATH

/path/to/my/exe/myapp $\*

For example, to distribute an application called "myapp" you would install the Advantage shared objects into the same directory as myapp, create symbolic links similar to those that exist in your /usr/lib directory that reference the driver, and include the small startup script described above. Your application directory might look something like the following:

lrwxrwxrwx 1 jeremym advantag 16 Dec 19 15:50 libace.so.6.11 -> libace.so.6.11.0

-rwxr-xr-x 1 jeremym advantag 5779730 Dec 19 16:07 libace.so.6.11.0

lrwxrwxrwx 1 jeremym advantag 19 Dec 19 16:07 libadsloc.so.6.11 -> libadsloc.so.6.11.0

-rwxr-xr-x 1 jeremym advantag 3879227 Dec 19 16:03 libadsloc.so.6.11.0

-rwxr-xr-x 1 jeremym advantag 829408 Dec 19 15:40 myapp

-rwxr--r-- 1 jeremym advantag 130 Dec 19 15:42 startmyapp

The ldd command in Linux can be used to see what shared objects your application depends on. Keep in mind this command will not display shared objects that are loaded by other shared objects. For example, the command "ldd myapp" might show a link to libace.6.11, but it will NOT tell you that libace also dynamically loads libadsloc.6.11 when you attempt a local server connection.

Note Your application probably also requires some Borland shared objects (the Qt libraries, for example). Read the Borland documentation on distributing applications for more details.
