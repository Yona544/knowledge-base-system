Advantage Web Platform Security




Advantage Database Server 12  

Advantage Web Platform Security

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Web Platform Security  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Advantage Web Platform Security Advantage Web Platform web\_security\_for\_awp Advantage Web Development > Advantage Web Platform > Security / Dear Support Staff, |  |
| Advantage Web Platform Security  Advantage Web Platform |  |  |  |  |

SSL Communications

By default all communication with the Advantage Web Platform is via a secure HTTPS connection. HTTP basic authentication is then tunneled through this secure connection. The installation will help you create a self-signed SSL certificate for testing purposes. Because this is a self-signed certificate, you will get warning messages from your web browser when you first access the service.

SSL and Trust Relationships

The programming interface you use to consume the service may also raise an exception and force you to implement a new callback function or some other mechanism in which you agree to consume this service even though it is not "trusted". For example, in .NET you have to use the ServicePointManager.ServerCertificateValidationCallback callback. Information on this process can be found in your framework documentation. Examples for a few common frameworks are included below.

.NET

Use the ServicePointManager.ServerCertificateValidationCallback (<http://msdn.microsoft.com/en-us/library/system.net.servicepointmanager.servercertificatevalidationcallback.aspx>)

.NET Compact Framework

Use the iCertificatePolicy interface (<http://msdn.microsoft.com/en-us/library/bb738067.aspx#SSLwiththe.NETCompactFramework>)

iOS

If using the Objective-C OData client, set the trustServer property of the WindowsCredential object.

If using NSURLConnection use the canAuthenticateAgainstProtectionSpace and didReceiveAuthenticationChallenge methods. See the Apple Authentication Challenges (<http://developer.apple.com/library/ios/#documentation/Cocoa/Conceptual/URLLoadingSystem/Articles/AuthenticationChallenges.html>) documentation for specific details. For example, to trust all servers:

/////////////////////////////////////////////////////////////////////////////////////

- (BOOL)connection:(NSURLConnection \*)connection canAuthenticateAgainstProtectionSpace:(NSURLProtectionSpace \*)protectionSpace {

  return ( ( [protectionSpace.authenticationMethod isEqualToString:NSURLAuthenticationMethodServerTrust] ) ||

          ( [protectionSpace.authenticationMethod isEqualToString:NSURLAuthenticationMethodHTTPBasic] ) );

 

}

 

/////////////////////////////////////////////////////////////////////////////////////

- (void)connection:(NSURLConnection \*)connection didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge \*)challenge {

  // NOTE SECURITY IMPLICATION HERE: Should only be used against trusted dev servers, as this allows connections to servers with invalid or self-signed SSL certificates

  if ( [challenge.protectionSpace.authenticationMethod isEqualToString:NSURLAuthenticationMethodServerTrust] )

     [challenge.sender useCredential:[NSURLCredential credentialForTrust:challenge.protectionSpace.serverTrust] forAuthenticationChallenge:challenge];

  else if ( [challenge.protectionSpace.authenticationMethod isEqualToString:NSURLAuthenticationMethodHTTPBasic] )

     [challenge.sender useCredential:authCredentials forAuthenticationChallenge:challenge ];

  else

     [challenge.sender continueWithoutCredentialForAuthenticationChallenge:challenge];

 

}