---
title: Master Tmp File Pool Size
slug: master_tmp_file_pool_size
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_tmp_file_pool_size.htm
source: Advantage CHM
tags:
  - master
checksum: 378d1f37fbf2d3c6fb6798440f0cad9afac2c14c
---

# Master Tmp File Pool Size

TMP\_FILE\_POOL\_SIZE

TMP\_FILE\_POOL\_SIZE

Advantage Database Server

| TMP\_FILE\_POOL\_SIZE  Advantage Database Server |  |  |  |  |

Default = 200

This configuration entry specifies the size of the [temporary file pool](master_temporary_file_pooling.md).  If this value is set to 0, the temporary file pool will not be used.  The lifetime of temporary files that are in the pool is typically only a few seconds.  Their primary purpose is to enhance performance of a very busy system.

To specify the size of the temporary file pool, perform one of the following where "x" is replaced by the actual integer size of the pool. To disable the temporary file pool, specify a value of zero.

 

For Windows NT/2000/2003:

Add or modify the following DWORD value using the Registry Editor (REGEDIT.EXE):

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\TMP\_FILE\_POOL\_SIZE=x

 

For Linux:

Add or modify the following line in the Advantage Database Server configuration file (adsd.conf):

TMP\_FILE\_POOL\_SIZE=x

 

For Local Server:

Add or modify the following line in the Advantage Local Server configuration file (adlocal.cfg):

TMP\_FILE\_POOL\_SIZE=x

 

See Also

[Temporary File Pooling](master_temporary_file_pooling.md)
