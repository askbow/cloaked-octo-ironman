#!/usr/bin/env python

"""
    A python PONG implementation based on python-verbose_ping("script by George Notaras.
    Refer to python-ping.py for comments and authorship: http://www.g-loaded.eu/2009/10/30/python-ping/

	This file only calls python-ping functions in the same
	manner and order other PONG scripts do in their particular languages.

"""
import python-ping


if __name__ == '__main__':
    #     GOOGLE
    verbose_ping("8.8.8.8")
    verbose_ping("8.8.4.4")
    #    ==========================
    #     LEVEL3
    verbose_ping("4.2.2.1")
    verbose_ping("4.2.2.2")
    #   verbose_ping("4.2.2.3")
    #   verbose_ping("4.2.2.4")
    #   verbose_ping("4.2.2.5")
    #   verbose_ping("4.2.2.6")
    #    ==========================
    #     AUSTRALIA ns1.telstra.net
    verbose_ping("139.130.4.5")
    #    ==========================
    #     OpenDNS
    verbose_ping("208.67.222.222")
    verbose_ping("208.67.220.220")
    #    ==========================
    #     MSK-IX NTP stratum-1 server --- better not to do this often
    #   verbose_ping("194.190.168.1
    #    ==========================
    #    next tests require DNS to be working
    #    ==========================
    #     YANDEX
    verbose_ping("ya.ru")
    #    ==========================
    #     INFOBOX:
    #    ------------- AMSTERDAM (EUROPE)
    verbose_ping("ams.sandbox.infobox.ru")
    #    ------------- SPB (NORTH-WEST RUSSIA)
    verbose_ping("spb.sandbox.infobox.ru")
    #    ------------- KRASNOYARSK (SIBERIAN RUSSIA)
    verbose_ping("krs.sandbox.infobox.ru")
    #    ==========================
    #    verbose_ping("WIKIPEDIA
    verbose_ping("wikipedia.org")
    #    ==========================
    #    verbose_ping("USA
    verbose_ping("whitehouse.gov")
