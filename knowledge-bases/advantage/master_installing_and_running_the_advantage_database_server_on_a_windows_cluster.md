Installing and Running the Advantage Database Server on a Windows Cluster




Advantage Database Server 12  

Installing and Running the Advantage Database Server on a Windows Cluster

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Installing and Running the Advantage Database Server on a Windows Cluster  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Installing and Running the Advantage Database Server on a Windows Cluster Advantage Database Server master\_Installing\_and\_running\_the\_advantage\_database\_server\_on\_a\_windows\_cluster Advantage Database Server > Installing the Advantage Database Server > Installing and Running the Advantage Database Server on a Windows Cluster / Dear Support Staff, |  |
| Installing and Running the Advantage Database Server on a Windows Cluster  Advantage Database Server |  |  |  |  |

Step 1: Install the Advantage Database Server

Install ADS on each cluster node using a unique serial number and validation code according to the "[Installing the Advantage Database Server Service for Windows](master_installing_the_advantage_database_server_service_for_windows_nt_2000_2003.htm)" instructions. During the startup, choose "Manual Startup" on the "Product Information" dialog in the startup. If you have already installed ADS with automatic startup, you can go to the Services manager (control panel, administrative tools) and change the Startup type for the Advantage Database Server service to manual. The cluster manager will handle the startup of the service.

Note If Advantage is running on one cluster node and you attempt to install Advantage Database Server on another node with the same serial number, Advantage will produce a serial number violation error. Advantage Database Server can be running on only one node at a time. The cluster service will start the Advantage Database Server service.

After installing Advantage Database Server on a node, it may be desirable to set the [Suppress\_Message\_Boxes](master_suppress_message_boxes.htm) configuration parameter. You can access this setting via the Advantage Configuration Utility (Configuration Utility tab, Misc Settings tab, click the Suppress Message Boxes checkbox and click Apply). This will prevent Advantage Database Server from displaying message boxes on the desktop and thus allows the cluster administrator to start and stop Advantage Database Server as needed without human interaction. If you turn this configuration parameter on, then messages such as serial number violations, exceptions, etc. will only be logged in the Application Event Log.

Step 2: Create a Virtual Server for Advantage Database Server

Once Advantage Database Server is installed on all the nodes in the cluster, you need to create a cluster group and resource to manage the Advantage Database Server service.

It is generally best to use a separate resource group because this allows the cluster manager to move the group between cluster nodes as necessary independent of other resource groups.

The following are the steps to use the Cluster Application Wizard under Windows Server 2003 to create a new cluster resource for Advantage in a new resource group.

|  |  |
| --- | --- |
| 1. | Start the Cluster Administrator (under Administrative Tools). |

|  |  |
| --- | --- |
| 2. | Choose menu File\Configure Application. Click Next on the wizard. |

|  |  |
| --- | --- |
| 3. | Choose "Create a new virtual server". Click Next. |

|  |  |
| --- | --- |
| 4. | Choose "Create a new resource group". Click Next. |

|  |  |
| --- | --- |
| 5. | Specify a name for the resource group (e.g., ADSGroup). Click Next. |

|  |  |
| --- | --- |
| 6. | Specify a network name for the virtual server. It can be the same as the group. Specify an IP address. Click Next. |

|  |  |
| --- | --- |
| 7. | Click Next on the Advanced Properties dialog. |

|  |  |
| --- | --- |
| 8. | Choose "Yes, create a cluster resource for my application now". Click Next. |

|  |  |
| --- | --- |
| 9. | Choose "Generic Service" from the combo box on the Application Resource Type dialog. Click Next. |

|  |  |
| --- | --- |
| 10. | Specify a resource name (e.g., ADSResource). Click Next. |

|  |  |
| --- | --- |
| 11. | Type "advantage" as the service name on the Generic Service Parameters dialog. Click Next. |

|  |  |
| --- | --- |
| 12. | Click Next again (no registry information is necessary). |

|  |  |
| --- | --- |
| 13. | Click Finish. |

|  |  |
| --- | --- |
| 14. | Click Next to finish. Once this step is complete, you should be able to see a new group (e.g., ADSGroup) under the Groups folder in the Cluster Administrator. |

|  |  |
| --- | --- |
| 15. | Open properties of the ADSResource (service resource). Go to Dependencies tab. Click "Modify" and add the IP Address and Name to the Dependencies. This will make sure that the IP Address resource and the UNC name associated with the ADS group move to the new node before the ADS service starts up. |

|  |  |
| --- | --- |
| 16. | If applicable, configure NAS on each node. See [Network Attached Storage (NAS) Device](master_network_attached_storage_nas_devices.htm) topic. |

After finishing, right click on the new group and choose "Bring Online" to start the Advantage Database Server.

Step 3: Connect to the Advantage Database Server on a Cluster Node

Version 7.1 or greater of Advantage Database Server for Windows will recognize the cluster name in multicast discovery requests. This allows a client to use the cluster name to connect generically to Advantage Database Server running in a clustered environment.

It is also possible to connect directly to the cluster IP address you assigned when creating the virtual server for Advantage Database Server. To do this, specify the LAN [IP Port](master_ip_port.htm) number in the Advantage Configuration Utility under the Communications tab. The connection string then should include the IP address and port number (e.g., \\123.111.111.222:2000\datapath).

If clients have problems connecting to Advantage Database Server when using the cluster name, you may consider using the [LAN IP Address](master_lan_ip_address.htm) configuration parameter and set it to the IP address you specified with creating the virtual server and cluster group for Advantage Database Server.