---
title: Php Windows Installation Notes
slug: php_windows_installation_notes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_windows_installation_notes.htm
source: Advantage CHM
tags:
  - php
checksum: 003d3097a90feb6a7c38e624312324b63b60af38
---

# Php Windows Installation Notes

Windows Installation Notes

Windows Installation Notes

Advantage PHP Extension

| Windows Installation Notes  Advantage PHP Extension |  |  |  |  |

Compiled versions of the Advantage PHP Extension are provided for the most recent versions of PHP available at the time of the Advantage release. Unfortunately PHP extensions are not forward or backward compatible.

PHP 5

1] Verify the file version of the compiled extension matches the version of PHP installed on the machine. The default location of the extension is \Program Files\Advantage X.x\PHP\.

The extension is name php\_advantage.dll.5.x.y, which should correspond to the version of PHP on the computer.

2] Copy the php\_advantage.dll.5.x.y to the PHP extension directory with the name php\_advantage.dll.

3] Locate the php.ini file and add the following entry under the Windows Extensions section:

extension=php\_advantage.dll

4] Restart the web server.
