@echo off
echo PING GOOGLE
ping 8.8.8.8
ping 8.8.4.4
echo ==========================
echo PING LEVEL3
ping 4.2.2.1
ping 4.2.2.2
rem ping 4.2.2.3
rem ping 4.2.2.4
rem ping 4.2.2.5
rem ping 4.2.2.6
echo ==========================
echo PING AUSTRALIA ns1.telstra.net
ping 139.130.4.5
echo ==========================
echo PING OpenDNS
ping 208.67.222.222
ping 208.67.220.220
echo ==========================
echo PING MSK-IX NTP stratum-1 server --- better not to do this often
rem ping 194.190.168.1
echo ==========================
echo next tests require DNS to be working
echo ==========================
echo PING YANDEX
ping ya.ru
echo ==========================
echo PING INFOBOX:
echo ------------- AMSTERDAM (EUROPE)
ping ams.sandbox.infobox.ru
echo ------------- SPB (NORTH-WEST RUSSIA)
ping spb.sandbox.infobox.ru
echo ------------- KRASNOYARSK (SIBERIAN RUSSIA)
ping krs.sandbox.infobox.ru
echo ==========================
echo PING WIKIPEDIA
ping wikipedia.org
echo ==========================
echo PING USA
ping whitehouse.gov
echo ==========================
echo PONG complete
echo ==========================
 
