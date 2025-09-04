---
title: Master Advantage Linux Configuration File
slug: master_advantage_linux_configuration_file
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_linux_configuration_file.htm
source: Advantage CHM
tags:
  - master
checksum: 695dd6bb9c899d34e3f7642470eb2b7aef1d4e06
---

# Master Advantage Linux Configuration File

Advantage Linux Configuration File

Advantage Linux Configuration File

Advantage Database Server

| Advantage Linux Configuration File  Advantage Database Server |  |  |  |  |

A configuration file, ads.conf, is installed with the Advantage daemon to assist in defining configuration parameters.

The parameters can be changed by editing the file ads.conf with a standard text editor. The configuration file is used when loading the Advantage daemon. If the Advantage daemon is already running, you must kill and then restart the daemon on the file server to use the newly changed settings.

The CREATEMASK configuration parameter should be of special interest to Advantage Database Server for Linux users. This parameter can be used to specify the file-system mask that will be used when the Advantage Database Server creates new files. The default mask is 0600, which gives the "advantage" user read and write privileges to the new file. A common alternative is 0660, which also gives the "advantage" group read and write privileges to the file. This is often necessary if you would like to add users to the "advantage" group and allow them to manipulate table/index/memo files with file-system commands such as 'cp', 'mv', etc.
