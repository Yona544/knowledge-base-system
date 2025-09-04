7082 Internet access disabled




Advantage Database Server 12  

7082 Internet access disabled

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7082 Internet access disabled  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7082 Internet access disabled Advantage Error Guide error\_7082\_internet\_access\_disabled Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7082 Internet access disabled  Advantage Error Guide |  |  |  |  |

Problem: This error indicates that the Internet access has been disabled and can be caused by the following:

|  |  |
| --- | --- |
| · | The Advantage Data Dictionary does not have Internet access enabled. |

|  |  |
| --- | --- |
| · | The user object in the Advantage Data Dictionary does not have Internet access enabled. |

|  |  |
| --- | --- |
| · | An Internet user has failed a successful login after several consecutive failed attempts. This causes Internet access for that user to be disabled. |

Solution: Check the following:

|  |  |
| --- | --- |
| · | Make sure that the Advantage Data Dictionary is enabled for Internet access. |

|  |  |
| --- | --- |
| · | Make sure that the user in the Advantage Data Dictionary is enabled for Internet access. |

|  |  |
| --- | --- |
| · | If the user was disabled after several failed login attempts, someone may be trying to break in to the system. |