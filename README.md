cloaked-octo-ironman
====================

Some stuff: scripts, oddities. Probably not a very clean code. But may render useful someday to someone, methinks.


PONG shell script is a collection of destinations for ICMP echo tests (ping utility) used to probe internet connectivity. Two convenient (windows cmd and linux .sh) files.

CONTACT EXPAND is a simple Python script designed to create personal address books for every contact present in a CUCM address list. Takes contacts.csv as input and creates an output.csv which can be uploaded to CUCM.
N.B.: CUCM=="Cisco Unified Communications Manager" is True

CONFIG EXPAND is a simple Python script designed to generate long iterative configs from a csv table and a formatted template. Takes data.csv as input and configtemplate.py as source of config to generate. Originally created to make a long list of dial-peers for Cisco voice router (voip gateway, CUBE), but can be easily adapted to generate any iterative config, like a massive list of interfaces.

CALL-PATTERN-REGEX-GENERATOR is a simple Python script designed to generate call pattern Regular Expressions RegEx) for use with CUCM/CUBE. The script will try to aggregate patterns where possible. Input file phoneranges.csv is provided as an example (found by my colleague on the Internet) of a source table with cellular phone service provider number ranges in Russian Federation. The simple RegEx generating procedure, range_to_pattern, is adapted from range_regex.py by dimka665 (Dmitry Voronin), see: https://github.com/dimka665/range-regex/blob/master/range_regex/range_regex.py

ADBLOCK-FILTERS is a collection of filters for adblock I generally use. The motivation to create it came from personal dissatisfaction with many Ad-block filter subscriptions. Existing subscriptions quickly become bloated and slow Firefox to a noticeable degree. In the .min version of the filter list, I removed most of the filters which had a zero HitCount after about a year of using the general filter list. 
To those who would claim that blocking Ads on the Internet is somehow bad: I usually enable the "non-intrusive" option of Adblock; if you wish your ads displayed, make them behave. 

Google Python Exercises - this is me, trying to learn Python with the help of https://developers.google.com/edu/python/

MULTILOGGER - an exercise in using Python logging facility

SESSIONGEN - a way to generate session ID. Far from perfect, but might be useful to track down multiple streams in logs

SIMPLE-DH - a simple Diffie-Hellman key negotiation algorithm implementation made for demonstration and study purposes

SIMPLE-ERLANG - a simple Erlang calculation example for demonstration and study purposes

SIMPLE-BACKUP - a simple script useful for backing up


MISC - miscellaneous code snippets