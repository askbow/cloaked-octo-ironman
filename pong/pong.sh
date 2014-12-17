#!/bin/bash
echo PING GOOGLE
ping -c 4 8.8.8.8
ping -c 4 8.8.4.4
echo ==========================
echo PING LEVEL3
ping -c 4 4.2.2.1
ping -c 4 4.2.2.2
# ping -c 4 4.2.2.3
# ping -c 4 4.2.2.4
# ping -c 4 4.2.2.5
# ping -c 4 4.2.2.6
echo ==========================
echo PING AUSTRALIA ns1.telstra.net
ping -c 4 139.130.4.5
echo ==========================
echo PING OpenDNS
ping -c 4 208.67.222.222
ping -c 4 208.67.220.220
echo ==========================
echo PING MSK-IX NTP stratum-1 server --- better not to do this often
# ping -c 4 194.190.168.1
echo ==========================
echo next tests require DNS to be working
echo ==========================
echo PING YANDEX
ping -c 4 ya.ru
echo ==========================
echo PING INFOBOX:
echo ------------- AMSTERDAM (EUROPE)
ping -c 4 ams.sandbox.infobox.ru
echo ------------- SPB (NORTH-WEST RUSSIA)
ping -c 4 spb.sandbox.infobox.ru
echo ------------- KRASNOYARSK (SIBERIAN RUSSIA)
ping -c 4 krs.sandbox.infobox.ru
echo ==========================
echo PING WIKIPEDIA
ping -c 4 wikipedia.org
echo ==========================
echo PING USA
ping -c 4 whitehouse.gov
echo ==========================
echo PONG complete
echo ==========================
 
