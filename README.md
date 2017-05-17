cricbuzz
========

For fetching Live Cricket Score from cricbuzz

Usage:
------

An example of how to get live scores.

    	   from cricbuzz import *    	   
    	   cric = CricbuzzParser()
    	   match = cric.getXml()
    	   details = cric.handleMatches(match) #Returns Match details as List of Dictionary. Parse it according to requirements.
    
ipl 
----
A console based python application to show score of the current ipl match. Score is updated after every ball. The application can used as a sticky small window at the top of the screen.

License:
--------
GNU General Public License v3 (GPLv3)

Bug Report:
-----------
Issue it here: https://github.com/psibi/cricbuzz/issues

