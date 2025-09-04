---
title: Master Dll Caching
slug: master_dll_caching
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_dll_caching.htm
source: Advantage CHM
tags:
  - master
checksum: d5595140c9e438e3d4871eb0cd7a9ebe2dfc4119
---

# Master Dll Caching

DLL Caching

DLL Caching

Advantage Concepts

| DLL Caching  Advantage Concepts |  |  |  |  |

What is DLL Caching?

DLL caching is a mechanism that allows AEP and trigger containers to be replaced (updated) without disconnecting all database users.

How does it work?

With DLL caching enabled, before Advantage loads an AEP or trigger container, it makes a temporary copy of the container and loads the copy rather than the original. This leaves the original container free to be replaced with a different version. Once a container is loaded, Advantage will compare the date/time and version (when available) of the original and the copy to check if the container has been updated. This check occurs each time a function (AEP or trigger) is used from a container. If the container has been updated, Advantage will make a new copy of the container, load that copy, and then transition each user of that container to the new copy the next time they use a function in that container.

AEP Startup and Shutdown Functions

To properly transition users from an old copy of a container to a new copy, Advantage will call the old container's shutdown function, then the new container's startup function (if the startup or shutdown functions exist in the AEP). This means that the startup and shutdown functions of an AEP may be called in between calls to AEP functions. Consequently, the startup and shutdown functions should initialize and finalize any state information required by all AEP functions.

What does the temporary container file name represent?

The file name of a container copy is based on the original name plus version information derived from the file's modification date and time, and version information (if available).

When and How to Disable DLL Caching

The ADS\_DD\_DISABLE\_DLL\_CACHING database property can be used to disable DLL caching. This is provided primarily for use when debugging containers. It may also be necessary if a container's Startup or Shutdown functions are not designed to be called between calls to an AEP or trigger function (such as when a container is reloaded). You might also want to disable DLL caching for performance reasons as the extra checking of the container's date/time and version does take extra time.

To disable DLL caching use the sp\_ModifyDatabase or AdsDDSetDatabaseProperty ACE API and the DISABLE\_DLL\_CACHING or ADS\_DD\_DISABLE\_DLL\_CACHING properties respectively. Set the property to TRUE to disable DLL caching. By default, DLL caching is enabled.

Limitations

- DLL caching only applies to Win32 DLL and Linux shared object containers.

- Changes to the ADS\_DD\_DISABLE\_DLL\_CACHING database property will not affect already connected users. They must disconnect and reconnect for the change to take effect.

- Version information of a container is only available with Win32 DLL containers.

- DLL Caching is not available with [Advantage Local Server](master_advantage_local_server_configuration.md).
