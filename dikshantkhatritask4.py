import sys   #sys module is imported
values = sys.argv[1:]
import csv
results = open("results.csv","r+")
scores = csv.reader(results)
lea_teams = ["England","Wales",
            "Mexico", "Sweden",
             "Ireland", "Serbia"]
results_list = []
c = 0
for allscores in scores:
    c =c + 1
    results_list.append(allscores)

#Class league will oversee the stats
class Leaguee:
    def __init__(self, name, gwon, glost, gdrawn, gos, goc,points):
        self.name = name
        self.gwon = gwon
        self.glost = glost
        self.gdrawn = gdrawn
        self.gos = gos
        self.goc = goc
        self.points = points

#teams stats before scores
teams = [Leaguee(lea_teams[0],0,0,0,0,0,0), Leaguee(lea_teams[1],0,0,0,0,0,0),
        Leaguee(lea_teams[2],0,0,0,0,0,0), Leaguee(lea_teams[3],0,0,0,0,0,0),
        Leaguee(lea_teams[4],0,0,0,0,0,0), Leaguee(lea_teams[5],0,0,0,0,0,0)]

def aboutgame(team1,goal1,team2,goal2):
        y = 0
        for x in range(len(lea_teams)):
                
                if team1 == teams[x].name:
                    teams[x].gos = teams[x].gos + int(goal1)
                    teams[x].goc = teams[x].goc + int(goal2)
                    if goal1 > goal2:
                        teams[x].gwon  = teams[x].gwon + int(1)
                        teams[x].points = teams[x].points + int(3)
                    if goal1 == goal2:
                        teams[x].gdrawn = teams[x].gdrawn + int(1)
                        teams[x].points = teams[x].points + int(1)

                    if goal2 > goal1:
                        teams[x].glost = teams[x].glost + int(1)    

                if team2 == teams[y].name:
                    teams[y].gos = teams[y].gos + int(goal2)
                    teams[y].goc = teams[y].goc + int(goal1)
                    
                    if goal2 > goal1:
                        teams[y].gwon  = teams[y].gwon + int(1)  
                        teams[y].points = teams[y].points + int(3)

                    if goal1 > goal2:
                        teams[y].glost = teams[y].glost + int(1)

                    if goal1 == goal2:                        
                        teams[y].points = teams[y].points + int(1)
                        teams[y].gdrawn = teams[y].gdrawn + int(1)
                y = y + 1

#LOOP for passing scores            
for looop in range(len(results_list)):
    aboutgame(results_list[looop][0],results_list[looop][1],results_list[looop][2],results_list[looop][3])

#the process for table formation and sorting
table = []
for an in range(len(lea_teams)):
    ans = (teams[an].name, (len(lea_teams)-1),teams[an].gwon, teams[an].gdrawn, teams[an].glost, teams[an].gos, teams[an].goc, teams[an].gos - teams[an].goc, teams[an].points)
    table.append(ans)

updated_stats= sorted(table, key = lambda seq: (int(seq[-1]), int(seq[-2]), int(seq[-4]))) #reverse = True)
updated_stats.reverse()

if values == ["League","Table"]: # for cmd input
    print("-------------")
    print("League Table")
    print("-------------\n")
    print("{: <25} {: <5} {: <5} {: <5} {: <5} {: <5} {: <5} {: <5} {: <5}".format("Teams", "P", "W", "D", "L", "GS", "GC", "GD", "Points"))
    for rank in updated_stats:
        print("{: <25} {: <5} {: <5} {: <5} {: <5} {: <5} {: <5} {: <5} {: <5}".format(rank[0],rank[1],rank[2],rank[3],rank[4],rank[5],rank[6],rank[7],rank[8]))
else:
    print("{: <25} {: <5} {: <5} {: <5} {: <5} {: <5} {: <5} {: <5} {: <5}".format("Teams", "P", "W", "D", "L", "GS", "GC", "GD", "Points"))
    for rank in updated_stats:
        print("{: <25} {: <5} {: <5} {: <5} {: <5} {: <5} {: <5} {: <5} {: <5}".format(rank[0],rank[1],rank[2],rank[3],rank[4],rank[5],rank[6],rank[7],rank[8]))
            
results.close()            