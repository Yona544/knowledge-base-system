---
title: Web Geturis Service
slug: web_geturis_service
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_geturis_service.htm
source: Advantage CHM
tags:
  - web
checksum: 2155d6ad2aa66b75682356c9eb7c148685d10f48
---

# Web Geturis Service

\_\_GetURIs Service Operation

\_\_GetURIs Service Operation

Advantage Web Platform

| \_\_GetURIs Service Operation  Advantage Web Platform |  |  |  |  |

The Advantage Web Platform provides the capability to enumerate and retrieve a list of exposed Locations in the adsweb.conf file through the \_\_GetURIs service operation. This operation can only be run against the [root dictionary](master_root_dictionary.md).  It will return all Locations that are flagged with the [DbEnableGetURIs](web_installing_the_awp.md) directive.

For example, this request:

https://localhost:6282/adsweb/rootdd/v1/\_\_GetURIs?$format=json

Will return a result set like this:

{

 "d": {

   "results": [

     {

       "Location": "/adsweb/example\_db"

     },

     {

       "Location": "/adsweb/myDB"

     }

   ]

 }

}

This service operation is used by the Advantage Web Administrator utility to more easily display a list of available databases for configuration purposes. While any valid Location can be enumerated, the general purpose is to enumerate any root dictionaries available in an environment that contains multiple instances of Advantage Database Server.
