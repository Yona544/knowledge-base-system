---
title: Master Setting The Internet Port Configuration Parameter
slug: master_setting_the_internet_port_configuration_parameter
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_setting_the_internet_port_configuration_parameter.htm
source: Advantage CHM
tags:
  - master
checksum: f857ed105e357a274b9e310c88eae084ee12e146
---

# Master Setting The Internet Port Configuration Parameter

Setting the Internet Port Configuration Parameter

Setting the Internet Port Configuration Parameter

Advantage Database Server

| Setting the Internet Port Configuration Parameter  Advantage Database Server |  |  |  |  |

This parameter controls Internet access to the Advantage Database Server. If the Internet port is set to zero, Internet access to the Advantage Database Server is disabled.

For Windows:

| 1. | Start the Advantage Configuration Utility. |

| 2. | Select the Configuration Utility tab. |

| 3. | Select the Communications tab. |

| 4. | Enter the Internet Port number. |

| 5. | Click Apply. |

If the Advantage Database Server is running, it will need to be re-started before the changes take place.

For Linux:

| 1. | Open the ads.conf file in a text editor. |

| 2. | Look for the INTERNET\_PORT option. The port number is the decimal value of the port you want to listen to. |

| 3. | Save the file. |

| 4. | Kill and restart the ADS daemon. |
