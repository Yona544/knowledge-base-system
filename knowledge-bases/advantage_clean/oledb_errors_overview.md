---
title: Oledb Errors Overview
slug: oledb_errors_overview
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_errors_overview.htm
source: Advantage CHM
tags:
  - oledb
checksum: 3b160feb3f95a281e1cd0168063c2591aecc17e3
---

# Oledb Errors Overview

Errors Overview

Errors Overview

Advantage OLE DB Provider (for ADO)

| Errors Overview  Advantage OLE DB Provider (for ADO) |  |  |  |  |

COM objects report errors through the HRESULT return code of object member functions. A COM HRESULT is a bit-packed structure. COM provides macros that dereference structure members.

COM specifies the IErrorInfo interface. The interface exposes methods such as GetDescription, allowing clients to extract error detail from COM servers. OLE DB extends IErrorInfo to support the return of multiple error information packets on a single-member function execution.

The Advantage OLE DB Provider exposes the OLE DB recordenhanced IErrorInfo error object interface.
