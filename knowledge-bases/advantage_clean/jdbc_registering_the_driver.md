---
title: Jdbc Registering The Driver
slug: jdbc_registering_the_driver
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: jdbc_registering_the_driver.htm
source: Advantage CHM
tags:
  - jdbc
checksum: 2a5ff1d5506b992793653a6bbb9dc0fbb55bf381
---

# Jdbc Registering The Driver

Registering the Driver

Registering the Driver

Advantage JDBC Driver

| Registering the Driver  Advantage JDBC Driver |  |  |  |  |

Registering the driver tells the JDBC driver manager which driver to load. When loading a driver using class.forName(), you must specify the name of the driver:

com.sap.jdbc.advantage.ADSDriver

For example:

Class.forName("com.sap.jdbc.advantage.ADSDriver");
