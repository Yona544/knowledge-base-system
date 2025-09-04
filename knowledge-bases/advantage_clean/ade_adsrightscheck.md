---
title: Ade Adsrightscheck
slug: ade_adsrightscheck
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsrightscheck.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8fb08937e50c7eb028b8e4853c378ce238d55cee
---

# Ade Adsrightscheck

AdsRightsCheck

AdsTableOptions.AdsRightsCheck

Advantage TDataSet Descendant

| AdsTableOptions.AdsRightsCheck  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.md)

Indicates if the Advantage Database Server should perform network operating system access rights checking during file opens for free connections).

Beginning with version 10.0, the client no longer performs rights checking by default. See [Check Rights](master_check_rights.md).

Syntax

property AdsTableOptions.AdsRightsCheck;

Description

Indicates if the client should perform file access rights checking during file opens for free connections. Options are True and False. If True is given, the client will check to see if the client workstation has visibility to the file path when creating or opening a file. If the user does not have rights to the directory or server, then the operation will fail. If AdsRightsCheck is False, the client will not perform the existence check. This allows an application developer to allow only Advantage-based applications to access specific data. See [Database Security](master_database_security.md) for more information on rights checking.

AdsRightsCheck is ignored when used with Advantage Local Server. AdsRightsCheck is effectively treated as if it is set to True.

AdsRightsCheck is ignored with database connections. User Account database security is used for database connections). See the "Flexible User Access Control" section in [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information.
