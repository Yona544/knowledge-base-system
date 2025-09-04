---
title: Ace Integrating The Advantage Client Engine Into Your Application
slug: ace_integrating_the_advantage_client_engine_into_your_application
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_integrating_the_advantage_client_engine_into_your_application.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 3867cf143eb2ac046f92a58adf7fe77397983af9
---

# Ace Integrating The Advantage Client Engine Into Your Application

Integrating the Advantage Client Engine Into Your Application

Integrating the Advantage Client Engine into Your Application

Advantage Client Engine

| Integrating the Advantage Client Engine into Your Application  Advantage Client Engine |  |  |  |  |

Because the Advantage Client Engine is DLL and shared object based, the Advantage Client Engine API is accessible to any Windows or Linux-based development platform that allows DLL or shared object calls. Although virtually any environment can call the Advantage Client Engine, the methods they use vary widely. This section outlines steps to enable Advantage Client Engine calls in a few representative development environments. If you are using a platform not listed here, refer to that platform's documentation on making DLL or shared object calls.

Microsoft C/C++

In order to compile your application using the Advantage Client Engine, you will need to #include "ACE.H" in all source files that use the Advantage Client Engine API. Please note that ace.h uses some macros that are in <windows.h>, so be sure to #include <windows.h> (or an equivalent header file) before the include of ace.h for each file.

To link, specify the exports library ACE32.LIB or ACE64.LIB in the project makefile or from the command line for the compiler or linker. Please see your compiler documentation for examples on linking external libraries.

Note The libraries that ship with the Advantage Client Engine are compiled using Microsoft C/C++ version 6.0. If your linker is not compatible with these libraries contact Advantage Technical Support for assistance.

It is also possible to load the Advantage Client Engine DLLs at runtime by using the LoadLibrary and GetProcAddress Windows functions if desired.

GNU C/C++

In order to compile your application using the Advantage Client Engine, you will need to #include "ace.h" in all source files that use the Advantage Client Engine API.

To link, specify the ACE shared object using the l option. For example:

gcc o mytest main.c -lace

To link to a specific version of the Advantage Client Engine, specify the soname with version information. For example, to require your application to use version 6.11 of ACE use the following command:

gcc o mytest main.c lace.6.11

It is also possible to load the Advantage Client Engine shared object at runtime by using the dlopen and dlsym functions if desired.

Borland Delphi/Kylix

Using the Advantage Client Engine with Delphi/Kylix requires specifying the Advantage Client Engine in the 'Uses' statement. Make sure to include the ace.pas file in your project or copy the .pas file into a directory in Kylix/Delphi's Library Path (reachable from the Environment Options-Library Tab)
