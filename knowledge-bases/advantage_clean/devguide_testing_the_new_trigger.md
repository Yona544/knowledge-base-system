---
title: Devguide Testing The New Trigger
slug: devguide_testing_the_new_trigger
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_testing_the_new_trigger.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: ee09aeaf38748ed27597f6af3fa6b69f69e39ed8
---

# Devguide Testing The New Trigger

Testing the New Trigger

     Testing the New Trigger

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Testing the New Trigger  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

With your new trigger assigned to the TriggerTest table, you are ready to demonstrate its use. Use the following steps to test the GenKey trigger:

Double-click the TriggerTest table in your DemoDictionary connection to open it in the Table Browser.

In the Name field enter Advantage, and in the Number field enter 1. Press the Down Arrow key. Your first record is posted, and your cursor moves to a newly inserted record. Since no data was entered in the field named Key, a GUID was assigned to that field by the trigger.

This time, enter Advantage in the Key field. Press Down Arrow once again to post this insert and move to a new record. This time a GUID was not written to the Key field. Your screen should look something like that shown in Figure 8-8.

Continue to test the trigger if you like. When you are done, close the Table Browser.

Figure 8-8: Testing the GenGuidID trigger
