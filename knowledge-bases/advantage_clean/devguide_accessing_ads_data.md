---
title: Devguide Accessing Ads Data
slug: devguide_accessing_ads_data
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_accessing_ads_data.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 2708c89f493eb5eb110a384ecb7fc895b0c0bb0b
---

# Devguide Accessing Ads Data

Accessing ADS Data

     Accessing ADS Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Accessing ADS Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Part III of this book brings it all together by showing you how to access Advantage data from many of your favorite development tools. By design, each of these chapters is similar in structure to one another. Once you have read one chapter, you will be able to quickly absorb the remaining chapters that you are interested in.

Each chapter begins with an introduction to a specific data access mechanism supported by Advantage. This discussion includes any special features of the data access mechanism under consideration. Next, each chapter takes a look at a project that implements a number of common tasks that you will find in many client applications. These tasks include connecting to a server, executing a query, and binding data to query parameters, to name a few.

Next, each chapter takes a look at the navigational features supported by the data access mechanism of focus. While every data access mechanism supports forward navigation, at a minimum, some support much more than that. This is the section that is most different among the various chapters.

Finally, each chapter concludes with a look at tasks that you might include in a client application in order to perform basic data dictionary administrative operations, including adding a table to a data dictionary, granting rights to a newly added table, and permitting a user to change their password. Only in Chapter 19, where the Advantage PHP Extension is used to build a dynamic Web site, are these operations absent. (Administrative tasks are normally not exposed through Web applications, though it is possible to do so if necessary.)

Chapter 15 discusses the Advantage TDataSet Descendant, and how it is used in Delphi applications (as well as in Kylix and C++Builder applications). Java and the Advantage JDBC Driver are the focus of Chapter 16, and in Chapter 17 you learn how to access Advantage data from Visual Basic 6.0. Microsoft's .NET Framework Class Library and the Advantage .NET Data Provider are the focus of the C# project found in Chapter 18. Finally, Chapter 19 gives you insight into using the Advantage ODBC Driver, the Advantage PHP Extension, and the Advantage DBI Driver.

There is one more item to note about the chapters in this section. These chapters appeared in our earlier book on Advantage, Advantage Database Server: The Official Guide (Jensen and Anderson, 2003, McGraw-Hill/Osborne Media Group).

When we were working on the outline for this book we seriously considered removing these chapters altogether. However, when we asked for input from our readers, many replied that they found these chapters to be particularly useful, even if they only read one or two of the five chapters in this section.

As a result, we decided to keep these chapters in this book. We've included new comments, added additional connection string information, and updated descriptions where appropriate. However, we were very happy with the original content of these chapters, and consequently, we retained much from the original material.
