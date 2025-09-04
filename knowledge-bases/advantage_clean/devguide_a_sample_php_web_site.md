---
title: Devguide A Sample Php Web Site
slug: devguide_a_sample_php_web_site
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_a_sample_php_web_site.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 9de81bada0e2f893226f7a85006595901fef7e0a
---

# Devguide A Sample Php Web Site

A Sample PHP Web Site

     A Sample PHP Web Site

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| A Sample PHP Web Site  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

In order to demonstrate the basic use of Advantage using PHP, we have provided you with a simple PHP-based Web site with this book's code download. The main page of this site is named index.htm, and it produces the page shown in Figure 19-3 when rendered in a Web browser.

Figure 19-3: The main page of a PHP-based Web site

   
CODE DOWNLOAD: The examples in this chapter can be found in the PHP directory on this book's code download (see Appendix A).  
 

This Web page contains five different HTML forms, each of which submits an HTTP (Hypertext Transfer Protocol) GET request to an associated PHP file. The following is the contents of this HTML file:

<html>  
<head>  
<title>Advantage Database Server</title>  
</head>  
<body>  
<form method="GET" action="getcustomer.php"     
  name="getcustomer">

 <h1 align="center">  
   Advantage Database Server: A Developer's Guide</h1>  
  <h2 align="center">PHP Demonstration</h2>  
  <p align="center">  
  <img border="0" src="advantage\_logo.png"></p>  
  Get a customer record<br>  
  Customer Number   
    <input type="text" name="custnumber" size="7"><br>  
  <input type="submit" value="Submit" name="B1">  
    <input type="reset" value="Reset" name="B2"><br>  
</form>  
<form method="GET" action="storedproc.php"   
  Name="storedproc">  
  <hr>  
  Execute a stored procedure<br>  
  Return 10% of invoices for Customer Number   
    <input type="text" name="custnumber" size="7"><br>  
  <input type="submit" value="Submit" name="B1">  
    <input type="reset" value="Reset" name="B2"><br>  
</form>  
<form method="GET" action="changeaddress.php"   
  Name="changeaddress">  
  <hr>  
  Change an address in the customer table <br>  
  Customer Number   
    <input type="text" name="custnumber" size="7"><br>  
  New Address <input type="text" name="newaddress"   
  Size="50"><br>  
  <input type="submit" value="Submit" name="UpdateAddress">  
    <input type="reset" value="Reset" name="B1"><br>  
</form>  
<form method="GET" action="showproducts.php">  
  <hr>  
  Build product selection page<br>  
  <input type="submit" value="Submit" name="B1"><br>  
</form>  
<form method="GET" action="showtables.php"   
  Name="showtables">  
  <hr>  
  Show table names<br>  
  <input type="submit" value="Submit" name="B1"><br>  
</form>  
   
</body>  
</html>

   
NOTE: These forms were submitted using the HTTP GET method so that you can see any submitted data in the URL displayed in your Web browser. Many Web developers prefer to submit forms using the POST method.  
 

There is another characteristic of these examples that is worth noting. Several of these example PHP files expect user input, which is then incorporated into SQL queries. Parameterized queries are used when user input is incorporated into the SQL queries in these examples. As you learned in Chapter 11, since Advantage version 7.0 you can execute SQL scripts that contain two or more SQL statements, separated by semicolons. While this is convenient, it exposes a potential security risk if you do not use parameterized queries. Because all user input is incorporated into queries using parameters, this security risk is eliminated.
