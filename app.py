# import CTMS
import sqlite3
import random
from itertools import combinations
import sys
from math import ceil, floor
from database import *
# from CTMS import *
from flask import Flask , render_template,url_for,abort
app = Flask(__name__)
sqliteConnect = sqlite3.connect('database.db', check_same_thread=False)


def get_db_connection():
    connection = sqlite3.connect('database.db', check_same_thread=False)
    connection.row_factory = sqlite3.Row
    return connection


@app.route('/')
def hello():
    
    return render_template('home.html')


@app.route('/frontpagereset')
def reset():
    global cursor, sqliteConnect
    init()
    resetDB()
    
    cursor = sqliteConnect.cursor()
    teams_data = cursor.execute('SELECT Teams, Logo, MatchesPlayed, MatchesWon, Last5Matches FROM TT ORDER BY MatchesWon DESC').fetchall()
    
    # Fetch match details
    # match_details = cursor.execute('''SELECT  a.Teams as TeamA, b.Teams as TeamB,
    #                                   FROM MD
    #                                   JOIN TT as a ON MD.TeamA = a.ID
    #                                   JOIN TT as b ON MD.TeamB = b.ID''').fetchall()

    match_details = cursor.execute('''SELECT MD.ID as id, a.Teams as TeamA, b.Teams as TeamB
                                        FROM MD
                                JOIN TT as a ON MD.TeamA = a.ID
                                JOIN TT as b ON MD.TeamB = b.ID''').fetchall()
    
    players_data = cursor.execute('SELECT ID, Name , Picture FROM PD').fetchall()

    runs,wickets=getTournamentStats()


    
    # Pass the teams_data and match_details to the template
    return render_template('frontpage.html', teams_data=teams_data, match_details=match_details, players_data=players_data,runs=runs,wickets=wickets)

@app.route('/frontpagereset/points')
def points_table():
    cursor = sqliteConnect.cursor()
    # Fetch the points table data
    # teams_data = cursor.execute('SELECT Teams, Logo, MatchesPlayed, MatchesWon, Last5Matches FROM TT ORDER BY MatchesWon DESC').fetchall()
    teams_data = cursor.execute('SELECT Teams, Logo, MatchesPlayed, MatchesWon, Last5Matches FROM TT ORDER BY MatchesWon DESC').fetchall()
    
    # Fetch match details
    # match_details = cursor.execute('''SELECT  a.Teams as TeamA, b.Teams as TeamB,
    #                                   FROM MD
    #                                   JOIN TT as a ON MD.TeamA = a.ID
    #                                   JOIN TT as b ON MD.TeamB = b.ID''').fetchall()

    match_details = cursor.execute('''SELECT MD.ID as id, a.Teams as TeamA, b.Teams as TeamB
                                        FROM MD
                                JOIN TT as a ON MD.TeamA = a.ID
                                JOIN TT as b ON MD.TeamB = b.ID''').fetchall()
    
    players_data = cursor.execute('SELECT ID, Name , Picture FROM PD').fetchall()
    runs,wickets=getT()
    return render_template('points_table.html', teams_data=teams_data, match_details=match_details, players_data=players_data,runs=runs,wickets=wickets)


@app.route('/frontpagereset/tournaments')
def tournaments_stats():
    cursor = sqliteConnect.cursor()
    # Fetch the points table data
    # teams_data = cursor.execute('SELECT Teams, Logo, MatchesPlayed, MatchesWon, Last5Matches FROM TT ORDER BY MatchesWon DESC').fetchall()
    teams_data = cursor.execute('SELECT Teams, Logo, MatchesPlayed, MatchesWon, Last5Matches FROM TT ORDER BY MatchesWon DESC').fetchall()
    
    # Fetch match details
    # match_details = cursor.execute('''SELECT  a.Teams as TeamA, b.Teams as TeamB,
    #                                   FROM MD
    #                                   JOIN TT as a ON MD.TeamA = a.ID
    #                                   JOIN TT as b ON MD.TeamB = b.ID''').fetchall()

    match_details = cursor.execute('''SELECT MD.ID as id, a.Teams as TeamA, b.Teams as TeamB
                                        FROM MD
                                JOIN TT as a ON MD.TeamA = a.ID
                                JOIN TT as b ON MD.TeamB = b.ID''').fetchall()
    
    players_data = cursor.execute('SELECT ID, Name , Picture FROM PD').fetchall()
    runs,wickets=getT()
    return render_template('tournament_stats.html', teams_data=teams_data, match_details=match_details, players_data=players_data,runs=runs,wickets=wickets)



@app.route('/frontpagereset/matches')
def match_schedule():
    cursor = sqliteConnect.cursor()
    # Fetch the points table data
    # teams_data = cursor.execute('SELECT Teams, Logo, MatchesPlayed, MatchesWon, Last5Matches FROM TT ORDER BY MatchesWon DESC').fetchall()
    teams_data = cursor.execute('SELECT Teams, Logo, MatchesPlayed, MatchesWon, Last5Matches FROM TT ORDER BY MatchesWon DESC').fetchall()
    
    # Fetch match details
    # match_details = cursor.execute('''SELECT  a.Teams as TeamA, b.Teams as TeamB,
    #                                   FROM MD
    #                                   JOIN TT as a ON MD.TeamA = a.ID
    #                                   JOIN TT as b ON MD.TeamB = b.ID''').fetchall()

    match_details = cursor.execute('''SELECT MD.ID as id,
                                        a.Teams as TeamA,
                                        b.Teams as TeamB,
                                        MD.DetailsGenerated as ISG
                                  FROM MD
                                  JOIN TT as a ON MD.TeamA = a.ID
                                  JOIN TT as b ON MD.TeamB = b.ID''').fetchall()
    
    players_data = cursor.execute('SELECT ID, Name , Picture FROM PD').fetchall()
    runs,wickets=getT()
    return render_template('matches.html', teams_data=teams_data, match_details=match_details, players_data=players_data,runs=runs,wickets=wickets)

    



@app.route('/frontpagereset/teams/<team_name>')
def team_details(team_name):

    cursor = sqliteConnect.cursor()
    
    query = f"SELECT * FROM '{team_name}'"  # Be very cautious with this approach
    team_details = cursor.execute(query).fetchall()
    # select the row from the TT table with the team name
    query1 = f"SELECT * FROM TT WHERE Teams = '{team_name}'"
    team_details1 = cursor.execute(query1).fetchone()
    cursor.execute("SELECT * FROM TT WHERE Teams = ?", (team_name,))
    team_details1 = cursor.fetchone()

        
        
        # Extract the highest run scorer and wicket taker IDs from the team details
    highest_runs_scorer_id = team_details1[5] 
    highest_wickets_taker_id = team_details1[6] 
    if team_details is None:
        # If no data is found for the given team, return a 404 error.
        abort(404)

    # Render a template with the team details.
    return render_template('team_details.html', team_details=team_details,team_name=team_name, highest_runs_scorer_id=highest_runs_scorer_id, highest_wickets_taker_id=highest_wickets_taker_id)



@app.route('/frontpagereset/players/player<int:player_id>')
def player_details(player_id):
    # Connect to the database and create a cursor
    cursor = sqliteConnect.cursor()

    # Query the PD table for the player details using the player_id
    query = f"SELECT * FROM PD WHERE ID = ?"
    cursor.execute(query, (player_id,))
    player_detail = cursor.fetchone()

    if player_detail is None:
        # If no data is found for the given player_id, return a 404 error.
        abort(404)

    # Render a template with the player details.
    attributes = ['PID','Name', 'Age', 'Team ID', 'Matches Played', 'Runs Scored', 'Balls Scored', 'Balls Faced', 'Balls Bowled', 'Wickets Taken']
    teamname=get_team_name(player_detail[4])
    # Render a template with the player details and attribute headers
    if(player_detail[3]==1):
        hand="Right"
    else:
        hand="Left"    
    return render_template('player_details.html', player_detail=player_detail, attributes=attributes,teamname=teamname,hand=hand)



@app.route('/frontpagereset/matches/MD<int:match_id>')





def match_details(match_id):

    if match_id==1: resetDB1()
    if match_id==2: resetDB2()
    if match_id==3: resetDB3()
    if match_id==4: resetDB4()
    if match_id==5: resetDB5()
    if match_id==6: resetDB6()
    if match_id==7: resetDB7()
    if match_id==8: resetDB8()
    if match_id==9: resetDB9()
    if match_id==10: resetDB10()
    if match_id==11: resetDB11()
    if match_id==12: resetDB12()
    if match_id==13: resetDB13()
    if match_id==14: resetDB14()
    if match_id==15: resetDB15()
    if match_id==16: resetDB16()
    if match_id==17: resetDB17()
    if match_id==18: resetDB18()
    if match_id==19: resetDB19()
    if match_id==20: resetDB20()
    if match_id==21: resetDB21()
    if match_id==22: resetDB22()
    if match_id==23: resetDB23()
    if match_id==24: resetDB24()
    if match_id==25: resetDB25()
    if match_id==26: resetDB26()
    if match_id==27: resetDB27()
    if match_id==28: resetDB28()
    if match_id==29: resetDB29()
    if match_id==30: resetDB30()
    if match_id==31: resetDB31()
    if match_id==32: resetDB32()
    if match_id==33: resetDB33()
    if match_id==34: resetDB34()
    if match_id==35: resetDB35()
    if match_id==36: resetDB36()
    if match_id==37: resetDB37()
    if match_id==38: resetDB38()
    if match_id==39: resetDB39()
    if match_id==40: resetDB40()
    if match_id==41: resetDB41()
    if match_id==42: resetDB42()
    if match_id==43: resetDB43()
    if match_id==44: resetDB44()    
    if match_id==45: resetDB45()
    
    connection = sqlite3.connect('database.db', check_same_thread=False)
    cursor = connection.cursor()
    # Get match details from the database
    table_name = f"MD{match_id}"
    query = f"SELECT * FROM {table_name}"
    try:
        raw_match_details = cursor.execute(query).fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        abort(404)  # Handle database errors gracefully

    if not raw_match_details:
        abort(404)  # Handle no data found gracefully
    # Convert match details into a dictionary
    match_details = []
    for detail in raw_match_details:
        player_id = detail[0]
        player_name = get_player_name(player_id)
        match_details.append({
            "PlayerID": player_id,
            "PlayerName": player_name,
            "RunsScored": detail[1],
            "BallsFaced": detail[2],
            "WicketsTaken": detail[3],
            "BallsBowled": detail[4]
        })    
    teamaid,teambid=get_team_names(match_id)
    teama=get_team_name(teamaid)
    teamb=get_team_name(teambid)
    # Calculate team totals and winner
    team1_runs = sum(item['RunsScored'] for item in match_details[:11])
    team1_wickets=0
    for i in range(11,22):
        team1_wickets+=int(match_details[i]['WicketsTaken'])
    team2_runs = sum(item['RunsScored'] for item in match_details[11:22])
    team2_wickets=0
    for i in range(11):
        team2_wickets+=int(match_details[i]['WicketsTaken'])
    if team1_runs > team2_runs:
        winner = teama
    elif team2_runs > team1_runs:
        winner = teamb

    else:
        winner = "Draw"
    

    query1= f"SELECT TeamA, TeamB FROM MD WHERE ID = {match_id}"
    
    return render_template('match_details.html', match_id=match_id, match_details=match_details,
                           team1_runs=team1_runs, team1_wickets=team1_wickets,
                           team2_runs=team2_runs, team2_wickets=team2_wickets, winner=winner,teama=teama,teamb=teamb)



@app.route('/frontpagenoreset')

def noreset():
    global cursor, sqliteConnect
    init()
    # resetDB()
    
    cursor = sqliteConnect.cursor()
    teams_data = cursor.execute('SELECT Teams, Logo, MatchesPlayed, MatchesWon, Last5Matches FROM TT ORDER BY MatchesWon DESC').fetchall()
    
    # Fetch match details
    # match_details = cursor.execute('''SELECT  a.Teams as TeamA, b.Teams as TeamB,
    #                                   FROM MD
    #                                   JOIN TT as a ON MD.TeamA = a.ID
    #                                   JOIN TT as b ON MD.TeamB = b.ID''').fetchall()

    match_details = cursor.execute('''SELECT MD.ID as id, a.Teams as TeamA, b.Teams as TeamB
                                        FROM MD
                                JOIN TT as a ON MD.TeamA = a.ID
                                JOIN TT as b ON MD.TeamB = b.ID''').fetchall()
    
    players_data = cursor.execute('SELECT ID, Name , Picture FROM PD').fetchall()

    runs,wickets=getTournamentStats()


    
    # Pass the teams_data and match_details to the template
    return render_template('frontpage.html', teams_data=teams_data, match_details=match_details, players_data=players_data,runs=runs,wickets=wickets)



if __name__ == '__main__':
    app.run(debug= True)