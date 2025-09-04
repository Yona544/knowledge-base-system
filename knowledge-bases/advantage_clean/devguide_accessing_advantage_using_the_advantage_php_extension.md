---
title: Devguide Accessing Advantage Using The Advantage Php Extension
slug: devguide_accessing_advantage_using_the_advantage_php_extension
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_accessing_advantage_using_the_advantage_php_extension.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 9e56aa49c840dff2dc9ff5bc907d4ccca63b3a11
---

# Devguide Accessing Advantage Using The Advantage Php Extension

Accessing Advantage Using the Advantage PHP Extension

     Accessing Advantage Using the Advantage PHP Extension

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Accessing Advantage Using the Advantage PHP Extension  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

PHP (the PHP: Hypertext Preprocessor language) is an open source scripting language that can be embedded into HTML documents in order to generate dynamic content for the World Wide Web. PHP can be used with any Web server that supports the PHP scripting engine. Most PHP development is done with Apache server for Linux, but other Web servers, such as Microsoft's IIS (Internet Information Server) can be configured to support PHP.

When a properly configured Web server reads a text file containing PHP commands, it runs the PHP scripting engine to execute those commands. The Web server then replaces the PHP commands with whatever output the scripting instructions call for. In most cases, the scripting commands are replaced either by simple text, HTML, or both.

Unlike client-side scripting, such as browser-executed JavaScript (or JScript or VBScript), all of the PHP commands are processed on the server--the client browser never receives them. As a result, end users cannot discover the PHP commands that you include in your PHP files.

After installing the Advantage PHP Extension, you will need to configure your Web server to load the PHP extension. Refer to your Web server documentation or your PHP add-on documentation for information on how to configure your Web server to use the Advantage PHP Extension.

Once you have enabled the Advantage PHP Extension, you can call any of the Advantage extended functions from within your PHP files. Table 19-2 contains a list of these available functions.
