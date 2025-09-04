Advantage Ruby API Support




Advantage Database Server 12  

Advantage Ruby API Support

Advantage Ruby API Support

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Ruby API Support  Advantage Ruby API Support |  |  | Feedback on: Advantage Database Server 12 - Advantage Ruby API Support Advantage Ruby API Support web\_Advantage\_Ruby\_API\_Support Advantage Web Development > Advantage Ruby API Support > Advantage Ruby API Support / Dear Support Staff, |  |
| Advantage Ruby API Support  Advantage Ruby API Support |  |  |  |  |

Advantage Ruby API Support

There are two different Ruby APIs supported by Advantage.  First, there is the Advantage Ruby API.  This API provides a Ruby wrapping over the interface exposed by ACE (Advantage Client Engine).  Second, there is support for ActiveRecord, an object-relational mapper popularized by being part of the Ruby on Rails web development framework.

The two separate packages are available as RubyGems.  The packages can be obtained by running the following commands:  
    gem install advantage  
    gem install activerecord-advantage-adapter

In addition to obtaining the packages, the Advantage Client Engine (ACE) must also be installed.

 

Advantage Native Ruby Driver:  
advantage - This package is a low-level driver that allows Ruby Code to interface with Advantage databases.  This package provides a Ruby wrapping over ACE and is written in C.

Example:  
This script makes a connection, prints Successful Ruby Connection to Advantage, then disconnects.

  # load the Advantage gem

  begin

    require 'rubygems'

    gem 'advantage'

    unless defined? Advantage

      require 'advantage'

    end

  end

 

  # create an interface

  api = Advantage::AdvantageInterface.new()

 

  # initialize the interface (loads the DLL/SO)

  Advantage::API.ads\_initialize\_interface( api )

 

  # initialize our api object

  api.ads\_init()

 

  # create a connection

  conn = api.ads\_new\_connection()

 

  # establish a connection

  api.ads\_connect(conn, "data source=c:\\test\\ruby.add;user id=adssys;")

 

  # execute a query without a result set

  api.ads\_execute\_immediate(conn, "select 'Successful Ruby Connection' from system.iota;")

 

  # disconnect from the database

  api.ads\_disconnect(conn)

 

  # free the connection resources

  api.ads\_free\_connection(conn)

 

  # free resources the api object uses

  api.ads\_fini()

 

  # close the interface

  Advantage::API.ads\_finalize\_interface( api )

 

 

Advantage ActiveRecord Adapter

activerecord-advantage-adapter - This package is an adapter that allows ActiveRecord to communicate with Advantage.  ActiveRecord is an object-relational mapper, popularized by being part of the Ruby on Rails web development framework.  The package is written in pure Ruby and uses (and has a dependency on) the advantage gem.

The following code is a sample database configuration object.

 ActiveRecord::Base.configurations = {

   'arunit' => {

     :adapter  => 'advantage',

     :database => 'c:/test/arunit.add',   #equivalent to the "Data Source" parameter

     :username => 'adssys',               #equivalent to the "UserID" parameter

     :password =>                         #equivalent to the "Password" parameter

 }