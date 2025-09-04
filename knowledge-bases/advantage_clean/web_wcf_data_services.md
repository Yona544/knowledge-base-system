---
title: Web Wcf Data Services
slug: web_wcf_data_services
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_wcf_data_services.htm
source: Advantage CHM
tags:
  - web
checksum: eb68b2121f24266cdd7851d5ae063808aeb9baf3
---

# Web Wcf Data Services

Using WCF Data Services

Using WCF Data Services

Advantage Web Platform

| Using WCF Data Services  Advantage Web Platform |  |  |  |  |

Visual Studio 10.0 with the WCF Data Services 4.0 provides the ability to consume OData. With the Advantage Web Platform as the service, the use of these features is vastly simplified because it is not necessary to set up the data service with an Entity Framework model. All that is needed is to expose your database with the Advantage Web Platform service and then create the client application using the WCF Data Services Client Library.

In order to create the client application, to consume OData from the Advantage Web Platform, you need to add a service reference to your client application to point to your exposed database and then use the generated proxy classes in your code to read and update data.

Adding a Service Reference to a WCF Client

In a Visual Studio 10.0 application, you can add a service reference to the application to define proxy classes for the entities (tables) in your database. In the Solution Explorer, right click on References and choose Add Service Reference....

The resulting dialog has an edit field titled Address in which you type the URI for your exposed database (e.g., https://localhost:6282/adsweb/mydata/v1/). Click on the Go button to retrieve the data. It results in a $metadata GET request to be sent to the server. If it is successful, it will show the reference in the Services list box. Expand the item to view the entities discovered. Type in an appropriate name in the Namespace edit box for the model and press OK.

If you are using a self-signed certificate with SSL, the Add Service Reference will indicate that the certificate is not valid and may not proceed. If this happens and your database is in your own local working environment, you may want to temporarily expose a URL to the database that does not require SSL (then you could use http://localhost:6272/adsweb/mydata/v1/ as the URL to avoid the certificate problem when creating the service reference. Remember to restart the web service after modifying the configuration file for the changes to take affect.

An alternative method for generating the proxy classes is to use the datasvcutil.exe command line utility that ships with Visual Studio 10.0. The following command will produce the proxy classes and put them in a file named proxy.cs that you can add to your project:

datasvcutil /uri:http://localhost:6272/adsweb/mydata/$metadata /out:proxy.cs

This utility, though, does not provide any mechanism to specify user name and password, so the exposed database would only work with the utility if it has authentication turned off in the conf file:

DbAutentication None

Using the Proxy Classes

After adding a service reference to a Visual Studio 10.0 project, you can use the proxy classes that were generated to access the database. For example, if you specified the Namespace in the Add Service Reference dialog as mydata and your application is named ConsoleApplication1, then (in C#), you can add a using statement:

using ConsoleApplication1.mydata;

After doing that, the entities (tables) in the database can be accessed.  The following example shows a couple of updates and a read of the data. A couple of important things to note are the event handlers assigned to ServicePointManager.ServerCertificateValidationCallback and context.SendingRequest. The first causes the certificate checking to be bypassed. This is handy in a test environment if you are using a self-signed certificate, but you probably dont want to use that in a deployed application. The second (SendingRequest) assigns an event handler that adds basic authentication credentials to the request. More information about this can be found at <http://blogs.msdn.com/b/astoriateam/archive/2010/07/21/odata-and-authentication-part-6-custom-basic-authentication.aspx>.

Note that if a field name in the data being retrieved contains spaces, you will need to refer to the name using underscores in place of spaces. The server replaces spaces in field names with underscores prior to returning the data to the client.

using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using ConsoleApplication1.mydata;

using System.Data.Services.Client;

using System.Net;

using System.Security.Cryptography.X509Certificates;

 

 

namespace ConsoleApplication1

{

  class Program

  {

     private static bool kludgeForSelfSignedCert(object sender, X509Certificate cert,

                  X509Chain chain, System.Net.Security.SslPolicyErrors error)

     {

        return true;

     }

 

     static void OnSendingRequest(object sender, SendingRequestEventArgs e)

     {

     var credentials = Encoding.ASCII.GetBytes("user:password");

     var base64Creds = Convert.ToBase64String(credentials);

     e.RequestHeaders.Add("Authorization", "Basic " + base64Creds);

     }

 

     static public int Main(string[] args)

     {

        // If you are using a self-signed certificate, you may need this to

         // allow the certificate

        ServicePointManager.ServerCertificateValidationCallback += new

System.Net.Security.

 RemoteCertificateValidationCallback(kludgeForSelfSignedCert);

 

        try

        {

           Uri uri = new Uri("https://localhost:6282/adsweb/mydata/v1/");

           var context = new testddData(uri);

 

           // If you are using basic authentication, you can add this event handler to

           // add the credentials to the request

           context.SendingRequest += new EventHandler

                 <SendingRequestEventArgs>(OnSendingRequest);

 

           // create a new record

           Parent np = new Parent();

           np.value = "some info";

           context.AddToParent(np);

           context.SaveChanges();

 

      // update a couple existing records

           Parent rec1 = (from p in context.Parent

                          where p.pk == 5

                          select p).First();

           rec1.value = "new info";

           context.UpdateObject(rec1);

           rec1 = (from p in context.Parent

                          where p.pk == 6

                          select p).First();

           rec1.value = "updated info";

           context.UpdateObject(rec1);

 

           // Save both updates as a batch operation.  This causes the updates

           // to be run inside a transaction (if using ADS as opposed to local server)

           context.SaveChanges(SaveChangesOptions.Batch);

         

           // Dump the rows in the parent table

           IQueryable<Parent> ptbl = from t in context.Parent select t;

           foreach (var p in

              ptbl)

              Console.WriteLine("PK = {0}, value = {1}", p.pk, p.value);

 

        }

        catch (Exception ex)

        {

           Console.WriteLine("{0}", ex.Message);

           if (ex.InnerException != null)

              Console.WriteLine("{0}", ex.InnerException.Message);

        }

        return 0;

     }

  }

}
