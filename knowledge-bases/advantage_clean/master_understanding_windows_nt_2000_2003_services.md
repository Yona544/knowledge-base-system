---
title: Master Understanding Windows Nt 2000 2003 Services
slug: master_understanding_windows_nt_2000_2003_services
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_understanding_windows_nt_2000_2003_services.htm
source: Advantage CHM
tags:
  - master
checksum: d8f0baaf4c8550d667feb81410f17e15a76f0296
---

# Master Understanding Windows Nt 2000 2003 Services

Understanding Windows Services

Understanding Windows Services

Advantage Database Server

| Understanding Windows Services  Advantage Database Server |  |  |  |  |

In Windows, many server-side programs act as a service. Unlike regular applications, services run in the background providing application support and have no user interface of their own. Most services can be started, stopped, paused, and continued. Windows services are controlled through the Windows Service Control Manager. The Service Control Manager lists all installed services and their current status.

To access the Service Control Manager with Windows NT 4.0, open the Control Panel folder and double click the Services icon. To access the Service Control Manager with Windows 2000/2003, click the Start button, select Programs, Administrative Tools, Services, and finally double click on the Services icon. Among the information provided by the Service Control Manager is the following:

- Server statusrelates the current status of the service (started, stopped, or paused)

- Startup optionsallows you to select the startup type for the selected service (automatic or manual)

- Startup parametersthe startup parameters box allows you to specify startup parameters to a particular service

Advantage Database Server Service

The Advantage Database Server was designed as a service to provide the most robust and safest database management possible. As a service, Advantage has better control over how and when the program is started and shut down. For example, if the startup type Automatic was selected during installation of the Advantage Database Server, the Advantage Database Server service will automatically start when the server comes up again after being shut down. This provides a benefit over regular applications because it does not require a user to log in to get the Advantage Database Server service up and running again after a power failure or other unexpected shut down.

Starting and Stopping the Advantage Database Server Service

The Advantage Database Server Service must be started before applications can run using the Advantage Database Server. Administrative privileges are required to stop a service. The pause and continue features are not available with the Advantage Database Server Service.

To start and stop the Advantage Database Server Service for Windows NT 4.0:

| 1. | Open the Control Panel folder. |

| 2. | Double click the Services icon. |

| 3. | Choose the Advantage Database Server from the list provided. |

| 4. | Click either the Start or Stop button as required. |

To start and stop the Advantage Database Server Service for Windows 2000/2003:

| 1. | Click the Start button on the taskbar. |

| 2. | Select Programs, Administrative Tools, and Services. |

| 3. | Choose the Advantage Database Server from the list provided. |

| 4. | Click either the Start or Stop button as required. |
