---
title: Error 6634 The Inter Process Communications Ipc Object Is No Longer Valid
slug: error_6634_the_inter_process_communications_ipc_object_is_no_longer_valid
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6634_the_inter_process_communications_ipc_object_is_no_longer_valid.htm
source: Advantage CHM
tags:
  - error
checksum: 1eaafbd65cf697c3251afdf609d2e55b807a6f0e
---

# Error 6634 The Inter Process Communications Ipc Object Is No Longer Valid

6634 The inter-process communications (IPC) object is no longer valid

6634 The inter-process communications (IPC) object is no longer valid

Advantage Error Guide

| 6634 The inter-process communications (IPC) object is no longer valid  Advantage Error Guide |  |  |  |  |

Problem: This error indicates that the connection to the server has been lost while using inter-process communications. The communications channel has been given to another client.

Solution: Close the connection and open a new one. It is expected that this error would only occur if the server was stopped and restarted while the client was still running.
