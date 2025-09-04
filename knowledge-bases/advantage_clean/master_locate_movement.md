---
title: Master Locate Movement
slug: master_locate_movement
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_locate_movement.htm
source: Advantage CHM
tags:
  - master
checksum: df518a7e9d6984e66b285807bb55c27a08217e90
---

# Master Locate Movement

Locate (Find)

Locate (Find)

Advantage Concepts

| Locate (Find)  Advantage Concepts |  |  |  |  |

An ISAM Locate (not to be confused with a TDataSet Locate) is a slow and inefficient way to search for data in the table. An ISAM Locate does a simple sequential search for data. An ISAM Locate will position to the record containing the data if it is found. Avoid using the ISAM Locate operation if possible. Seek is the preferred method of searching for data.

Note If you are using the Advantage TDataSet Descendant, do not confuse an ISAM Locate with a TDataSet Locate. A TDataSet Locate determines the best possible way to search for a piece of data and performs the search in that manner. An ISAM Locate always does a sequential search and is very inefficient and slow. A TDataSet Locate is usually very efficient and fast.
