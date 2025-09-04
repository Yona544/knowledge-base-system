Setting up Advantage for the Internet




Advantage Database Server 12  

Setting up Advantage for the Internet

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Setting up Advantage for the Internet  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Setting up Advantage for the Internet Advantage Database Server master\_Setting\_up\_advantage\_for\_the\_internet Advantage Database Server > Advantage Internet Server > Introduction and Initial Setup > Setting up Advantage for the Internet / Dear Support Staff, |  |
| Setting up Advantage for the Internet  Advantage Database Server |  |  |  |  |

The Advantage Internet Server is integrated into the Advantage Database Server. In order to utilize this new feature there are a few steps you will need to take.

Step 1: You will need to designate the port that Advantage will listen on for incoming Internet connections. See [Setting the Internet Port Configuration Parameter](master_setting_the_internet_port_configuration_parameter.htm) for instructions.

Step 2: [Enabling Internet Access in the Data Dictionary](master_enabling_internet_access_in_the_data_dictionary.htm)

Step 3: [Connecting Clients Through the Internet to Advantage](master_connecting_clients_through_the_internet_to_advantage.htm)

Important To use the new Internet functionality you will need to create a data dictionary. The Internet server will use the data dictionary to validate users. Free Tables (tables not in a Data Dictionary) can be opened through an Internet connection. To deny a users rights to a table, the table needs to be added to the Data Dictionary and the users rights removed from the table.