TAdsEvent




Advantage Database Server 12  

TAdsEvent

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsEvent  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsEvent Advantage TDataSet Descendant ade\_TAdsEvent Advantage TDataSet Descendant > Advantage Components > TAdsEvent / Dear Support Staff, |  |
| TAdsEvent  Advantage TDataSet Descendant |  |  |  |  |

|  |  |
| --- | --- |
| [Properties](ade_tadsevent_properties.htm) | [Events](ade_tadsevent_events.htm) |

The TAdsEvent component provides a client side encapsulation of the Advantage Database Server's notification functionality. See [Events (Notifications)](master_events_notifications_.htm) for details.

Unit

AdsEventHandler

 

Description

Use TAdsEvent to enable notifications in your application. TAdsEvent creates a background thread and waits for notifications of any of the assigned events. If any configured event is signaled, the assigned OnNotification event is fired. The notification thread creates its own internal TAdsConnection for use, so waiting on an event will not block the main thread of the application.

TAdsEvent clones the AdsConnection component it points to, which means any property changes to the AdsConnection instance will not be reflected in the connection the TAdsEvent component is using until the [TAdsEvent.Active](ade_tadsevent_active.htm) property is cycled to false and back to true.