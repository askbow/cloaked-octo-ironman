===Iperf-transpone===

Builds a more useful timeseries table from iperf's client default output.

Inputs: iperf-extracted-timeseries.csv
Outputs: iperf-transposed-timeseries.csv

Usual iperf output looks something like this:

<code>[ ID] Interval       Transfer     Bandwidth
[208]  1.0- 2.0 sec  6816 KBytes  55837 Kbits/sec
[224]  1.0- 2.0 sec  7096 KBytes  58130 Kbits/sec
[176]  1.0- 2.0 sec  6784 KBytes  55575 Kbits/sec
[240]  1.0- 2.0 sec  6792 KBytes  55640 Kbits/sec
[264]  1.0- 2.0 sec  7256 KBytes  59441 Kbits/sec
[232]  1.0- 2.0 sec  7256 KBytes  59441 Kbits/sec
[168]  1.0- 2.0 sec  7296 KBytes  59769 Kbits/sec
[164]  1.0- 2.0 sec  7136 KBytes  58458 Kbits/sec
[248]  1.0- 2.0 sec  7392 KBytes  60555 Kbits/sec
[280]  1.0- 2.0 sec  7368 KBytes  60359 Kbits/sec
[216]  1.0- 2.0 sec  7360 KBytes  60293 Kbits/sec
[192]  1.0- 2.0 sec  7096 KBytes  58130 Kbits/sec
[256]  1.0- 2.0 sec  7136 KBytes  58458 Kbits/sec
[SUM]  1.0- 2.0 sec  114160 KBytes  935199 Kbits/sec
[248]  2.0- 3.0 sec  7120 KBytes  58327 Kbits/sec
[200]  2.0- 3.0 sec  6680 KBytes  54723 Kbits/sec
[280]  2.0- 3.0 sec  7120 KBytes  58327 Kbits/sec
[216]  2.0- 3.0 sec  7104 KBytes  58196 Kbits/sec
[224]  2.0- 3.0 sec  7168 KBytes  58720 Kbits/sec
[240]  2.0- 3.0 sec  6528 KBytes  53477 Kbits/sec
[ ID] Interval       Transfer     Bandwidth
[232]  2.0- 3.0 sec  6688 KBytes  54788 Kbits/sec
[176]  2.0- 3.0 sec  6528 KBytes  53477 Kbits/sec
[272]  2.0- 3.0 sec  6544 KBytes  53608 Kbits/sec
[168]  2.0- 3.0 sec  6712 KBytes  54985 Kbits/sec
[264]  2.0- 3.0 sec  6736 KBytes  55181 Kbits/sec
[208]  2.0- 3.0 sec  6544 KBytes  53608 Kbits/sec
[184]  2.0- 3.0 sec  7120 KBytes  58327 Kbits/sec
...</code>
(a few thousand lines like this)

With a text editor  
<code>sed -r 's/^(\[[SUM0-9]*\])[ ]+([0-9]{1,5})\.0-.+[ ]+([0-9]+).[KMG]*bits.sec$/\1;\2;\3/' log.txt > iperf-extracted-timeseries.csv</code>

it is trivial to turn that into something like this:
<code>[192];3;55378
[164];3;55837
[256];3;55575
[SUM];3;894632
[184];4;58589
[248];4;58786
[224];4;58130
[232];4;56492
[240];4;55181
[200];4;56623
[264];4;56754
[272];4;55181
[208];4;55247
[168];4;56558
[176];4;55312
[216];4;58655
[280];4;58589
[256];4;57999
[164];4;58065
...</code>

(this is iperf-extracted-timeseries.csv)

What this script does is it turns it into a table which is easy to analyse with conventional table processing tools, i.e.:

<code>time;[248];[184];[164];[168];[216];[256];[200];[280];[176];[272];[240];[208];[232];[264];[224];[192];[SUM]
0;59179;58917;58982;58720;58851;59048;58851;58786;57999;57868;57868;57868;58851;58917;58851;58982;938541
1;60555;60359;58458;59769;60293;58458;59376;60359;55575;55378;55640;55837;59441;59441;58130;58130;935199
2;58327;58327;59310;54985;58196;59179;54723;58327;53477;53608;53477;53608;54788;55181;58720;58917;903152
3;57213;56754;55837;56623;57344;55575;57541;57344;53871;54133;54198;54133;56492;56295;55902;55378;894632
4;58786;58589;58065;56558;58655;57999;56623;58589;55312;55181;55181;55247;56492;56754;58130;58065;914227
5;58720;58458;58393;56164;58524;58393;56033;58524;54788;54788;54788;54591;56361;56295;58327;58327;911475
...</code>
(this is iperf-transposed-timeseries.csv)