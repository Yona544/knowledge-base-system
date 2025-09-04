---
title: Master Fts Quick Start
slug: master_fts_quick_start
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_fts_quick_start.htm
source: Advantage CHM
tags:
  - master
checksum: f0b18ef8be3461bee882cab68db7bb5f2be9cec3
---

# Master Fts Quick Start

FTS Quick Start

FTS Quick Start

Advantage Concepts

| FTS Quick Start  Advantage Concepts |  |  |  |  |

One of the simplest ways to try out the full text search functionality to see if it will be useful in your application is to run some SQL queries in Advantage Data Architect.

You should first create full text search (FTS) indexes on the fields you plan to search. It is still possible to perform full text searches on fields that do not have FTS indexes, but Advantage has to search the physical record data in that case, and it can be much slower. You can create an index either through SQL via the CREATE INDEX statement or through the Index Management utility in Advantage Data Architect.

To create an FTS index with SQL using all the default settings, execute a statement such as the following using the SQL utility in Advantage Data Architect (menu Tools / Native SQL Utility):

CREATE INDEX testfts ON thetable( thefield ) CONTENT

The CONTENT keyword specifies that a full text search index is to be created. For a full description of the various options, see [CREATE INDEX](master_create_index.md).

To create an FTS index with the Index Management utility in Advantage Data Architect, open a table and go to the Index Management screen (menu Tools / Index Management). Choose the Create New FTS Index tab and specify the desired options.

It is also possible to call the ACE API directly to create FTS indexes. See AdsCreateFTSIndex in the Advantage Client Engine Help documentation (ACE.hlp).

Once you have created the desired indexes, you can run some SQL queries that use the CONTAINS() function in the WHERE clause. The first parameter to the CONTAINS() function can be a specific field name to search or an asterisk (\*), which means all fields that have FTS indexes are to be searched.

SELECT \* FROM thetable WHERE CONTAINS( \*, search words )

If you open a table directly with Advantage Data Architect, you can specify a full text search condition using the same syntax in the filter edit box at the bottom of the table window. For example, you can specify "CONTAINS( \*, search words )" as the filter expression.
