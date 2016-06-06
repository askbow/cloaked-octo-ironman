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
    # TODO: add some IXes from https://www.euro-ix.net/tools/ixp-directory/
    # TODO: add some more Russian and Ukranian IXes from https://ru.wikipedia.org/wiki/%D0%A2%D0%BE%D1%87%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BC%D0%B5%D0%BD%D0%B0_%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82-%D1%82%D1%80%D0%B0%D1%84%D0%B8%D0%BA%D0%BE%D0%BC
    #     some Russian Internet eXchanges (IX):
    #     SPB-IX (Saint-Peterbourg/north-west Russia) (Part of MSK-IX association)
    verbose_ping("194.226.100.100")
    verbose_ping("194.226.102.100")
    #     MSK-IX (Moscow/central Russia) (Part of MSK-IX association)
    verbose_ping("195.208.208.100")
    verbose_ping("195.208.215.100")
    #     RND-IX (Rostov/southern Russia) (Part of MSK-IX association)
    verbose_ping("193.232.140.100")
    #verbose_ping("193.232.140.100") # only one route server at RND-IX
    #     EKT-IX (Ural) (Part of MSK-IX association)
    verbose_ping("194.85.107.100")
    verbose_ping("194.85.107.200")
    #     VLV-IX (Vladivostok/far east Russia) (Part of MSK-IX association)
    verbose_ping("193.232.136.100")
    #verbose_ping("193.232.136.100") # only one route server at VLV-IX
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
