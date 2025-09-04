Example init.d Script




Advantage Database Server 12  

Example init.d Script

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Example init.d Script  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Example init.d Script Advantage Database Server master\_Example\_init\_d\_script Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Example init.d Script  Advantage Database Server |  |  |  |  |

The following script is an example init.d script. This script was included in your installation, and can be found in the scripts directory (default /usr/local/advantage/scripts).

To install this script:

|  |  |
| --- | --- |
| 1. | Copy the following script text into a file and name the file "ads". |

|  |  |
| --- | --- |
| 2. | Move the file to the /etc/rc.d/init.d directory. |

|  |  |
| --- | --- |
| 3. | If you installed the Advantage daemon to a directory other than the default (/usr/local/advantage) modify all path references in the script to point to your installation directory. |

|  |  |
| --- | --- |
| 4. | Type the command "chkconfig --add ads". |

After installation the Advantage daemon will now automatically start as your Linux machine is booted.

The script has multiple options, the two most frequently used are "ads start" and "ads stop". These commands can be used to start and stop the Advantage daemon. Other options include "status" and "restart".

#!/bin/sh

#

# ads: Starts the Advantage DB Server

# by Michael Shigorin <michael\_shigorin@mail.univ.kiev.ua>

#

# chkconfig: 2345 99 10

# description: Starts and stops the Advantage DBS at boot time and

# shutdown.

#

# processname: adsd

# config: /usr/local/advantage/ads.conf

# pidfile: /var/run/adsd.pid

 

# Source function library.

. /etc/rc.d/init.d/functions

 

# btw, we could use these better ;)

 

start() {

echo -n "Starting Advantage Database Server: "

daemon /usr/local/advantage/adsd

RETVAL=$?

[ $RETVAL -eq 0 ] && {

 touch /var/lock/subsys/ads

 # get first PID

 pidof adsd | tr -cs '[a-zA-Z0-9]' '[\n\*]' \

 | sort -n | head -1 \

 > /var/run/adsd.pid

 echo\_success

 echo

} || echo\_failure

return $RETVAL

}

 

stop() {

echo -n "Shutting down Advantage Database Server: "

kill `cat /var/run/adsd.pid`

RETVAL=$?

[ $RETVAL -eq 0 ] && {

 # still unfinished, but working.

 rm -f /var/lock/subsys/ads

 rm -f /var/run/adsd.pid

 echo\_success

 echo

} || echo\_failure

return $RETVAL

}

 

RETVAL=0

 

# See how we were called.

case "$1" in

start)

 start

 ;;

stop)

 stop

 ;;

status)

 status adsd

 ;;

restart|reload)

 if [ -f /var/lock/subsys/ads ]; then

  stop

  start

 else

  start

 fi

;;

condstop)

 if [ -f "$LOCKFILE" ]; then

  stop

 fi

 ;;

condrestart)

 if [ -f "$LOCKFILE" ]; then

  restart

 fi

 ;;

\*)

 echo "\*\*\* Usage: ads {start|stop|restart|status}"

 exit 1

esac

 

exit $RETVAL