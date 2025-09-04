---
title: Master Flush Frequency
slug: master_flush_frequency
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_flush_frequency.htm
source: Advantage CHM
tags:
  - master
checksum: d4384772785c0e859ddd2503d044bb107500ddb1
---

# Master Flush Frequency

Flush Frequency

Flush Frequency

Advantage Database Server

| Flush Frequency  Advantage Database Server |  |  |  |  |

Windows

Default = 600000 milliseconds (10 minutes). Range = 0 - 86400000 milliseconds (24 hours).

Database updates made on a Windows NT or 2000/2003 server are typically written to an internal buffer that the operating system writes to disk on a regular basis. But this "regular basis" is not specifically defined by Windows. If the Windows server crashes or shuts down due to power failure, the buffered data is lost and it may lead to database corruption. The Flush Frequency value determines how often an Advantage Database Server background thread will forcibly flush all buffered information for the specified file to disk on the Windows server. As this flush time interval decreases, the committing of file updates occurs more often, which can decrease Advantage Database Server performance, especially during heavy concurrency. The default value of 10 minutes is typically suitable for most installations. A value of zero disables the forcible flush to disk functionality.

Note that flushes of the Advantage Transaction Log File will occur every time data is added to the file no matter how the Flush Frequency configuration value is set. This will help to ensure Transaction Log File stability, but will cause updates during a transaction to occur more slowly than when not in a transaction.
