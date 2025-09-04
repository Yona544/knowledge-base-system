---
title: Master Reduced File Handle Usage
slug: master_reduced_file_handle_usage
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_reduced_file_handle_usage.htm
source: Advantage CHM
tags:
  - master
checksum: 00cc6246dc0c5023b7ea1d27b788cbd2d449b259
---

# Master Reduced File Handle Usage

Reduced File Handle Usage

Reduced File Handle Usage

Advantage Concepts

| Reduced File Handle Usage  Advantage Concepts |  |  |  |  |

The slowest operation that can be requested of an application is to open a file, especially in a network environment. Given this fact, writing fast database applications usually requires that once a table is opened, it remains open. However, complex database applications often require access to many files. This is a problem because database operating systems have a limited number of files that can be open at one time. Non-client/server application developers traditionally have had to open and close files as they are needed, unnecessarily slowing the application down with the opening overhead.

The Advantage Database Server eliminates this problem by providing a single point of access to the database. The Advantage Database Server opens data files and provides access to users. The need for local file handles is eliminated. The need for server file handles eliminated because the Advantage Database Server does not use any file handles to access a table shared among multiple users. For example, suppose you had an inventory control program with 25 users. If the program uses 16 tables, with an average of three index files each, it could require up to 64 file handles (i.e., 16 table handles + (3 index file handles X 16 tables) = 64 file handles being used). To keep all the files open, a typical non-client/server application would need 64 file handles at each workstation and 1600 file handles at the file server. The same application using the Advantage Database Server would require no file handles per workstation and only 64 file handles at the file server.
