---
title: Devguide Stored Procedures Versus Advantage Extended Procedures
slug: devguide_stored_procedures_versus_advantage_extended_procedures
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_stored_procedures_versus_advantage_extended_procedures.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: c7ca082f48e63b54e1a1483c89f943f785e9a81d
---

# Devguide Stored Procedures Versus Advantage Extended Procedures

Stored Procedures Versus Advantage Extended Procedures

 

     Stored Procedures Versus Advantage Extended Procedures

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Stored Procedures Versus Advantage Extended Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The term stored procedure is a general term for any routine for which you create a stored procedure object in your data dictionary. Advantage supports stored procedures in two distinct forms: SQL stored procedures and Advantage Extended Procedures. Advantage Extended Procedures are often referred to as AEPs for short.

AEPs are compiled modules in the form of Windows DLLs, Linux shared object (so) libraries, .NET managed assemblies, or COM objects. All AEPs, regardless of how they are compiled, share a number of specific characteristics, including when they are loaded, how they are initialized, and what housekeeping tasks they perform internally.

By comparison, SQL stored procedures are not precompiled. They are SQL scripts that are loaded and executed by Advantage in response to a client's invocation of the corresponding stored procedure object. SQL stored procedures were first introduced in Advantage 8.

The following sections provide you with a detailed description of the structural characteristics of both AEPs and SQL stored procedures.
