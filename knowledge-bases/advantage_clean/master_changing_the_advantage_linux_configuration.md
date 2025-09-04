---
title: Master Changing The Advantage Linux Configuration
slug: master_changing_the_advantage_linux_configuration
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_changing_the_advantage_linux_configuration.htm
source: Advantage CHM
tags:
  - master
checksum: 242d5b992ab1e40250a76c284d2c41777d7b6bb0
---

# Master Changing The Advantage Linux Configuration

Changing the Advantage Linux Configuration

Changing the Advantage Linux Configuration

Advantage Database Server

| Changing the Advantage Linux Configuration  Advantage Database Server |  |  |  |  |

To change the Advantage Linux configuration via the command line, you must kill the Advantage daemon then restart it with new configuration parameters.

Example:

./adsd -C50 -W75 -D100 &
