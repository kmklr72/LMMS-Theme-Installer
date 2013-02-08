*LMMS Theme Installer*
======================
This project aims to make installing themes easier for everyone. It handles the download, extraction, and installation of themes from the sharing platform.

Currently tested on Windows 7 and Linux Mint 14


*Dependencies*
--------------
* Python 2.7
* PySide 1.1.2
* BeautifulSoup 4
* Beaker 1.6.4


*Usage*
-------
1. Run theme-installer.py:
	* On Windows use:
	<pre>python theme-installer.py</pre>
	* On Linux use:
	<pre>sudo python theme-installer.py</pre>

2. Configure the theme directory (Edit > Options):
	* Windows default:
	<pre>C:\Program Files\LMMS\data\themes</pre>
	* Linux default:
	<pre>/usr/share/lmms/themes</pre>


*Todo*
------
* Implement splashscreen for when the SourceForge servers are running slow.
* Caching mechanism for the files so we don't need to download as much (maybe HTML too?).