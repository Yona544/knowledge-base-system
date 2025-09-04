---
title: Master Task 1 Copy Test Data And Application
slug: master_task_1_copy_test_data_and_application
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_task_1_copy_test_data_and_application.htm
source: Advantage CHM
tags:
  - master
checksum: 24f9b34bd7a99cba0526ae05c2e126a8ba3a181a
---

# Master Task 1 Copy Test Data And Application

Task 1: Copy Test Data and Application

Task 1: Copy Test Data and Application

Advantage Concepts

| Task 1: Copy Test Data and Application  Advantage Concepts |  |  |  |  |

This tutorial uses a simplified order-entry database, which can be found in the aep\_tutorial\task1 directory of your installation (default is: c:\Program Files\Advantage X.x\TDataSet\examples\aep\_tutorial\task1). Copy the contents of this directory to a working directory, which will be referred to as x:\data throughout this tutorial.

Take a few moments to open this database using the Advantage Data Architect (ARC) and become familiar with the tables and their contents. The ADSSYS login password is empty.

A simple test application is also included with the database, tester.dpr. Tester.dpr uses a TAdsStoredProc object to call the stored procedure we are going to create. It should be noted that tester.exe (or "tester" in Linux) will need to be compiled, and will not function correctly until you have finished Task 6 of this tutorial.
