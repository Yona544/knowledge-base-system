Multi-Threading and Multiple Processors




Advantage Database Server 12  

Multi-Threading and Multiple Processors

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Multi-Threading and Multiple Processors  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Multi-Threading and Multiple Processors Advantage Concepts master\_Multi\_threading\_and\_multiple\_processors Advantage Concepts > Advantage Functionality > Multi-Threading and Multiple Processors / Dear Support Staff, |  |
| Multi-Threading and Multiple Processors  Advantage Concepts |  |  |  |  |

All versions of the Advantage Database Server are multi-threaded and will perform each user-requested database operations concurrently or in parallel if multiple processors are present. Advantage Database Server allows the configuration of the number of "worker" threads that are used to perform individual database operations. See [Number of Worker Threads (-T)](master_number_of_worker_threads_t_.htm) for more information on Advantage Database Server worker threads and how to configure the number of them.

The Advantage Database Server for Windows is a multi-threaded Win32 Service that will automatically use multiple CPUs if available. Thus, user-requested database operations will be performed in parallel on multi-CPU Windows servers.

The Advantage Database Server for Linux is a multi-threaded daemon that will automatically use multiple CPUs if available and if using a Linux kernel that supports multi-processing. Thus, user-requested database operations will be performed in parallel on multi-CPU Linux servers.