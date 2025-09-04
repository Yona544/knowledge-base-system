---
title: Arc Database Aliases
slug: arc_database_aliases
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_database_aliases.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 121cbb24a5dcff82cc9d8fe95d255faa2f58a21d
---

# Arc Database Aliases

Database Aliases

Database Aliases

Advantage Data Architect

| Database Aliases  Advantage Data Architect |  |  |  |  |

Database Aliases provide an easier way to access your database. For example, if you have many databases, and each one is in a different directory, it might be hard to remember all of the paths. Using an alias, you only have to remember the database name. Database aliases are kept in the ads.ini file. When you use the Connection Repository, it will automatically create an alias for you when a database is created. It will also remove the alias if you delete the database. You can also edit the ADS.INI file manually to create your own aliases.

Note The ads.ini file is typically stored in the \WINDOWS or \WINNT directories.

To create an alias in your ads.ini file manually:

Make sure there is a Databases section in the ads.ini file that looks like this:

[Databases]

Enter your aliases in that section. They look like this:

<AliasName>=<Full Path to the database >;D

Example:

MyDemoDictionary=d:\dd\sampledb.add;D

An example of an ADS.INI file with database aliases:

[Databases]

new=d:\dd\new.add;D

My First Database=d:\dd\DemoDatabase.add;D

Demo Database=d:\dd\\DemoDatabase.add;D
