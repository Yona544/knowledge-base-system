---
title: Web Administrator Setup
slug: web_administrator_setup
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_administrator_setup.htm
source: Advantage CHM
tags:
  - web
checksum: 5bca9b868ebfec7a8561294f8be18afbfba7fe95
---

# Web Administrator Setup

Advantage Web Administrator Setup

Advantage Web Administrator Setup

Advantage Web Platform

| Advantage Web Administrator Setup  Advantage Web Platform |  |  |  |  |

The [Advantage Web Platform installation](web_installing_the_awp.md) includes a copy of the web administrator files (a number of JavaScript, HTML, and related files). They are copied by the installer to the a folder named adsconfig under the htdocs folder (e.g., C:\Program Files\Advantage NN.n\adsweb\apache\htdocs\adsconfig).

If you specify that location with a URL in a web browser, it will open the opening page (index.html), however there are some steps that you must first take in order to use the administrator utility.

| 1. | Specify a [root dictionary](master_root_dictionary.md). The web administrator uses a number system procedures for configuration purposes and system procedures can only be run against the root dictionary when used with the Advantage Web Platform (for security reasons). Note that Advantage Database Server must be restarted after specifying the root dictionary configuration parameter. |

| 2. | Add a [Location](web_installing_the_awp.md) for the root dictionary to the adsweb.conf file (e.g., in C:\Program Files\Advantage NN.n\adsweb\apache\conf\adsweb.conf). The Advantage Web Platform must be restarted for it to recognize new locations. |

| 3. | Edit configOptions.js (e.g., C:\Program Files\Advantage NN.n\adsweb\apache\htdocs\adsconfig\configOptions.js) and specify the startup root dictionary variable rootDB.  For example, if you chose to add the example DB during the web platform install and subsequently specified it as the root dictionary, change the rootDB variable initialization to: |

var rootDB = "/adsweb/example\_db";

For enhanced security, post ADS12, access to the Advantage Web Configuration Utility by default will be allowed only via HTTPS connections. To use your SSL certificate, you need to edit the file conf/extra/httpd-ssl.conf. Point your SSLCertificateFile variable to use your certificate file and the SSLCertificateKeyFile to use your key file. Open the file conf/httpd.conf and uncomment the line (remove leading #):

#Include conf/extra/httpd-ssl.conf

Restart the Advantage Web Platform Server. At this point, you should be able to access the web administrator from a web browser.  For example, you could use the URL https://yourserver:6282/adsconfig. Or if you are testing with a browser on the local machine, you could specify the URL https://localhost:6282/adsconfig.

If you don't have an SSL certificate available and chose not to generate a self-signed certificate for testing during the web platform install, you can also use HTTP requests. Remove (or comment out) the SSLRequireSSL directive in the location and directory specifications in adsweb.conf.  After restarting the web platform, the URL http://localhost:6272/adsconfig could then be used. Note that for production use, you should use SSL, otherwise all credentials and all information will be visible on the wire.

<Directory "/path/to/adsweb/Apache24/htdocs/adsconfig/">

AllowOverride None

Options None

Require all granted

#SSLRequireSSL

</Directory>

.

.

<Location /adsweb/example\_db>

SetHandler adsweb

#SSLRequireSSL

.

.

.

</Location>

The default ports on which Apache listens with the Advantage Web Platform are 6282 for SSL and 6272 for non-SSL connections. The Listen directive for SSL can be found in the file apache/conf/extra/httpd-ssl.conf, and the non-SSL Listen directive is in apache/conf/httpd.conf.  If you change these, restart the Advantage Web Platform (Apache) for the change to take effect.

Running SQL Statements

One potentially useful feature available in the web administrator is the ability to execute SQL statements against a data dictionary. This may be useful for any number of administrative functions. However, for security reasons, that functionality is not enabled by default. You must explicitly enable the \_\_query service by adding the [DbEnableQueryService](web_installing_the_awp.md) directive to the root dictionary Location in adsweb.conf.

Multiple Servers and Dictionaries

A single installation of the Advantage Web Platform with the administrator utility running on it can be used to manage multiple Advantage Database Server installations and multiple data dictionaries on a server. In general, you need a [root dictionary](master_root_dictionary.md) on each server that you wish to access from the web administrator. If you have the \_\_query service enabled with the [DbEnableQueryService](web_installing_the_awp.md) directive on the root dictionary, it is also possible to run queries against the other non-root dictionaries on a server. To do this, you must create links to those dictionaries from the root dictionary and enable pass-through queries on the linked dictionaries.

| 1. | Create a link in the root dictionary to each additional dictionary. This can be done with Advantage Data Architect or with the system procedure [sp\_CreateLink](master_sp_createlink.md). Alternatively you can use the Connection String setting in the Settings menu to manually set a connection string to a dictionary instead of creating a link to it. This setting is not persisted across closing and reopening the Web Administrator. |

| 2. | Enable pass-through queries on the non-root dictionaries. For security reasons, the default behavior is to disallow queries to the linked dictionaries. See the [root dictionary](master_root_dictionary.md) and [pass-through query](web_pass_through_queries.md) topics for details on enabling pass-through queries. |

When you open the server repository (by clicking the Server button in the upper left corner), it shows the list of data dictionaries that have been marked with the [DbEnableGetURIs](web_installing_the_awp.md) directive. The expected usage is that each root dictionary location in adsweb.conf would be marked with the DbEnableGetURIs directive. For example, if you had multiple installations of Advantage Database Server, each of those could have a root dictionary exposed in adsweb.conf with DbEnableGetURIs. After connecting to one of the dictionaries (specified by the rootDB variable in configOptions.js), the web administrator will retrieve the list of other root dictionaries to populate the server repository.

Once the web administrator has retrieved the root dictionaries marked with DbEnableGetURIs and then retrieved the links from each root dictionary, you can navigate to any of those dictionaries in the server repository by expanding the "Server" control (in the upper left of the screen). A root dictionary with links should display as a tree node that can be expanded to show the links. Clicking on one of the links will make that the active dictionary for subsequent operations.

If any non-root dictionary locations contain the DbEnableGetURIs directive, they will be displayed in the server repository at the top level. When you select such a dictionary, though, very little functionality will be available because most requests made against the dictionary will be through system procedures that can only be called on root dictionaries. 5132 errors will be returned and shown in the footer. It is possible, though, to execute queries against such an exposed dictionary with the SQL Utility if the dictionary location contains the DbEnableQueryService directive.
