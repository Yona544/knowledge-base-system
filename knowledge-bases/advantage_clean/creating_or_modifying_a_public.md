---
title: Creating Or Modifying A Public
slug: creating_or_modifying_a_public
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: creating_or_modifying_a_public.htm
source: Advantage CHM
tags:
  - creating
checksum: 9791beaf33e2d00c7b26fbb971dabb966921c937
---

# Creating Or Modifying A Public

Creating or Modifying a Publication

Creating or Modifying a Publication

Advantage Data Architect

| Creating or Modifying a Publication  Advantage Data Architect |  |  |  |  |

A group of articles to be replicated. In addition to the article names, it includes the columns for each article that are used to identify the record at the target database and an optional filter for each article.

To create or modify a Publication, open a database. See [Opening a Database](arc_opening_a_database2.md) for details. You must login to the database as a user with CREATE PUBLICATION or ALTER permissions on the specific publication in order to add or modify Publications in a database.

To add a new Publication, from the tree view within the Connection Repository, right-click the PUBLICATIONS icon and select Create.

To modify an existing Publication's properties, from the tree view within the Connection Repository, right-click the Publication's name icon and select Properties.

Publication Field Descriptions

Name (required)

Name of the publication.

Articles (required)

Tables to be published.

Description (optional)

Description for the publication.

Filter (optional)

Vertical AOF filter for selecting records to replicate.

SQL MERGE Statement (optional)

Uses and SQL MERGE statement instead of an SQL INSERT or SQL UPDATE statement.

New Article

Adds a new table to the publication.

Delete Article

Deletes an existing article.
