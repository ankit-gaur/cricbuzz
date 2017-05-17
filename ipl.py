from cricbuzz import *
from time import sleep
import tags


seriesName = "Indian Premier League, 2017"

currentBall = "0.0" #to track change in balls/over
currentMatchStatus = "" #to track change in match status, if raining or whatever



def ballChanged(match_detail):
	global currentBall
	if match_detail[tags.BattingTeamOvers] != currentBall:
		currentBall = match_detail[tags.BattingTeamOvers]
		return True
	else :
		return False	

def printProgressIfChanged(match_detail):
	global currentMatchStatus
	if currentMatchStatus == "":
		currentMatchStatus = match_detail[tags.MatchState]
		return 
	if match_detail[tags.MatchState] != currentMatchStatus:
		currentMatchStatus = match_detail[tags.MatchState]
		print "Match Status Changed, "+match_detail[tags.MatchState]


def printIplDetails():
	cric = CricbuzzParser()
	matches = cric.getXml()
	for match in matches:
	    mchDesc = match.getAttribute("mchDesc")
	    series = match.getAttribute("srs")
	    if series == seriesName:
	        series = match.getAttribute("srs") 
	        match_detail = cric.handleMatch(match)
	        if match_detail is not None :
	        	if ballChanged(match_detail):
	        		print(chr(27) + "[2J") #clear screen
	        		print match_detail[tags.PlayingTeams]
	        		print match_detail[tags.BattingTeam] + " " + match_detail[tags.BattingTeamRuns] + "/" + match_detail[tags.BattingTeamWickets]
	        		print "Overs: " + match_detail[tags.BattingTeamOvers]
	        		if match_detail[tags.BowlingTeamRuns] is not None:
	        			print "Target: "+ (int(match_detail[tags.BowlingTeamRuns])+1) 
	        		else :
	        			print "Batting First"
	        		print 	match_detail[tags.MatchState]
	        	printProgressIfChanged(match_detail) #print match status if it changed, delayed due to rain etc.			
	        else :
	        	print "match details not found"
	        	break
	    	break

              		
def loop():
	printIplDetails()
	sleep(10) #sleep for 10 seconds 
	loop()


loop()



