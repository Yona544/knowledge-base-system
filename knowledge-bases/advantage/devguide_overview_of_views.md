Overview of Views




Overview of Views

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

A view is a customized row/column selection from one or more Advantage tables. Depending on how the view is defined, this result set may or may not be editable.

Views serve several valuable purposes. First of all, they provide a convenient way to define prepackaged queries that are available to all of your client applications. These queries reside on the server, and are executed from a client application by opening the view, just like you would open a table.

Because views are stored on the server, you can update them by updating the data dictionary in which they are defined. By comparison, when your data selections are defined in your client applications through SQL queries, any changes to those queries require that you update and redeploy all of your client applications.

Views also permit you to modularize data access in your application. This is possible because one view can select data from one or more other views. For example, you can create one view that includes all records but only selected fields from a table. Another view can query the first view, calculating statistics about the selected fields. A third view can select a subset of the calculations for the purpose of building a report. A fourth view can select a different subset of the calculations for use in a different report.

Another feature of views is that they permit you to work with ADT tables from two or more data dictionaries with a single connection. As you learned in Chapter 2, when an ADT table is bound to a data dictionary, you must connect to that data dictionary in order to access the table. Views, in conjunction with a feature called data dictionary links, permit you to access data in two or more data dictionaries through a single connection. (Views can also use tables from two or more data dictionaries using relative or fully qualified paths.)

Creating views that access data from multiple data dictionaries or data dictionary tables is described later in this chapter in the section "Views That Use Other Database Tables."