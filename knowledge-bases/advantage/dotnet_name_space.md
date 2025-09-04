Name Space




Advantage Database Server 12  

Name Space

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name Space  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Name Space Advantage .NET Data Provider dotnet\_Name\_space Advantage .NET Data Provider > Introduction > Name Space / Dear Support Staff, |  |
| Name Space  Advantage .NET Data Provider |  |  |  |  |

The Advantage .NET Data Provider exists in the name space Advantage.Data.Provider. To access the various provider classes, you must either qualify them with the namespace or specify the name space in your code files. In C#, include the using Directive as follows in your code:

using Advantage.Data.Provider;

With Visual Basic .NET, include the imports statement as follows:

Imports Advantage.Data.Provider

Once the Advantage.Data.Provider namespace has been specified, the various classes such as AdsConnection and AdsCommand can be used without qualification. If any of the names of classes in the Advantage.Data.Provider namespace conflict with other classes, you can use the aliasing mechanism to qualify the names. For example, in C#, you could use the following directive with an alias to avoid name conflicts:

using ADP=Advantage.Data.Provider;

With that aliased namespace, you would refer to the classes using ADP as the qualifier (e.g., ADP.AdsConnection and ADP.AdsCommand).

The naming convention for .NET data providers is to begin each of the public class names with a common prefix. The prefix for all Advantage .NET Data Provider classes is "Ads".