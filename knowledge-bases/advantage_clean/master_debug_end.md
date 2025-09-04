---
title: Master Debug End
slug: master_debug_end
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_debug_end.htm
source: Advantage CHM
tags:
  - master
checksum: 445a902bcc6154041068dd34bf61785ff686e5b6
---

# Master Debug End

DEBUG END

DEBUG END

Advantage SQL Engine

| DEBUG END  Advantage SQL Engine |  |  |  |  |

Stops the debugger session on the current connection.

Syntax

DEBUG END

Remark

The DEBUG END statement terminates the debugger session that was started with the [DEBUG BEGIN](master_debug_end.md) statement on the current connection. An error will be returned if the statement is not executed in an active debugger session. Execution of this statement will terminate all debuggee sessions owned by this debugger all break points will be cleared and debuggee connections will resume normal execution. After the successful execution of this statement, all debug related temporary tables will be deleted and no longer available.

See Also

[DEBUG BEGIN](master_debug_begin.md)
