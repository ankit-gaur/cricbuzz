from cricbuzz import *
from time import sleep


seriesName = "Indian Premier League, 2017"

currentBall = "0.0" #to track change in balls/over
currentMatchStatus = "" #to track change in match status, if raining or whatever

class Tags():
	PlayingTeams = "Team"
	BattingTeam = "Batting team"
	BowlingTeam = "Bowling team"
	BowlingTeamOvers = "Bowling Team Overs"
	BattingTeamOvers = "Batting Team Overs"
	BowlingTeamWickets = "Bowling Team Wickets" 
	BattingTeamWickets = "Batting Team Wickets"
	BowlingTeamRuns = "Bowling Team Runs"
	BattingTeamRuns = "Batting Team Runs"
	MatchState = "Match State"



def ballChanged(match_detail):
	global currentBall
	if match_detail[Tags.BattingTeamOvers] != currentBall:
		currentBall = match_detail[Tags.BattingTeamOvers]
		return True
	else :
		return False	

def printProgressIfChanged(match_detail):
	global currentMatchStatus
	if currentMatchStatus == "":
		currentMatchStatus = match_detail[Tags.MatchState]
		return 
	if match_detail[Tags.MatchState] != currentMatchStatus:
		currentMatchStatus = match_detail[Tags.MatchState]
		print "Match Status Changed, "+match_detail[Tags.MatchState]


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
	        		print match_detail[Tags.PlayingTeams]
	        		print match_detail[Tags.BattingTeam] + " " + match_detail[Tags.BattingTeamRuns] + "/" + match_detail[Tags.BattingTeamWickets]
	        		print "Overs: " + match_detail[Tags.BattingTeamOvers]
	        		if match_detail[Tags.BowlingTeamRuns] is not None:
	        			print "Target: "+ (int(match_detail[Tags.BowlingTeamRuns])+1) 
	        		else :
	        			print "Batting First"
	        		print 	match_detail[Tags.MatchState]
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



