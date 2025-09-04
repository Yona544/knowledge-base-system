Linux Installation Notes




Advantage Database Server 12  

Linux Installation Notes

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Linux Installation Notes  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - Linux Installation Notes Advantage PHP Extension php\_Linux\_installation\_notes Advantage PHP Extension > Linux Installation Notes / Dear Support Staff, |  |
| Linux Installation Notes  Advantage PHP Extension |  |  |  |  |

To install the Advantage PHP Extension for Linux, follow these steps:

1) Untar and Unzip the PHP source.

#tar -zxvf php-5.x.x.tar.gz

2) Run the Advantage PHP Extension installer.

#setup.pl

or

#perl setup.pl

3) Follow the installer prompts.

4) In the PHP source directory type:

#./buildconf

This will include the Advantage PHP Extension in the PHP build and install.

5) Configure PHP with Advantage by using

--with-advantage=/your/to/path/ads/php/.

For example to install the Advantage Extension in Apache with PHP as a DSO type the following:

#./configure --with-advantage=/usr/local/ads/php --with-apxs --enable-track-vars

6) Make and Install PHP:

#make

#make install