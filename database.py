import sqlite3
import random
import sys
from math import ceil, floor
from itertools import combinations  

global_arr = [0] * 50

# Initialize database
def init():
    print("Initializing database...")
    global sqliteConnect, cursor
    try:
        sqliteConnect = sqlite3.connect(r'database.db')
    except Exception as e:
        print(f'Could not connect to database. Error: {e}')
        sys.exit(0)
    cursor = sqliteConnect.cursor()
    # Updated TT table schema to include a Logo column
    cursor.execute('''CREATE TABLE IF NOT EXISTS TT(
                      ID INTEGER PRIMARY KEY, Teams TEXT, Logo TEXT,
                      MatchesPlayed INTEGER DEFAULT 0, MatchesWon INTEGER DEFAULT 0,
                      HighestRunScorer INT DEFAULT 0, HighestWicketTaker INT DEFAULT 0,
                      Last5Matches TEXT DEFAULT "NA")''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS MD(
                      ID INTEGER PRIMARY KEY, TeamA INT NOT NULL, TeamB INT NOT NULL,
                      DetailsGenerated BOOLEAN NOT NULL DEFAULT 0, Result INT,
                      BatFirst BOOLEAN, TeamARuns INT, TeamAWickets INT, TeamABalls INT,
                      TeamBRuns INT, TeamBWickets INT, TeamBBalls INT,
                      FOREIGN KEY(TeamA) REFERENCES TT(ID),
                      FOREIGN KEY(TeamB) REFERENCES TT(ID))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS PD(
                      ID INTEGER PRIMARY KEY, Name TEXT, Age INT, Hand BOOLEAN,
                      TeamID INT NOT NULL, MatchesPlayed INTEGER DEFAULT 0,
                      RunsScored INTEGER DEFAULT 0, BallsFaced INTEGER DEFAULT 0,
                      BallsBowled INTEGER DEFAULT 0, WicketsTaken INTEGER DEFAULT 0,
                      FOREIGN KEY(TeamID) REFERENCES TT(ID))''')
    sqliteConnect.commit()

# This function simulates resetting the database.
def resetDB():
    print("Resetting database...")
    global sqliteConnect, cursor
    tables_to_drop = ['TT', 'MD', 'PD', '"Hawks Elite"', '"Thunder Bats"', '"Oceanic Guardians"', '"Elephant Chargers"', '"Royal Pioneers"', '"Desert Falcons"','"Jungle Kings"',
                      '"Swift Strikers"','"Solar Gladiators"','"Panther Prowlers"','"Neon Knights"','"Electric Eagles"','"Quantum Quokkas"','"Cosmic Cheetahs"','"Galactic Gazelles"']

    # Drop each table, using quotes for table names with spaces
    for table in tables_to_drop:
        # print(table)
        cursor.execute(f'DROP TABLE IF EXISTS {table}')
    for i in range(45):
        # print(table)
        cursor.execute(f'DROP TABLE IF EXISTS "MD{i+1}"')
    sqliteConnect.commit()
    
    sqliteConnect.commit()
    init()
    generateTeams(10)
    generateMatches()
    # for i in range(numMatches()):
    #     generateDetails(i+1)

def check_table_exists(db_path, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query to check for the table existence
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?;"
    
    # Execute the query
    cursor.execute(query, (table_name,))
    
    # Fetch the result
    result = cursor.fetchone()
    
    # Close the connection
    conn.close()
    
    # Return True if the table exists, False otherwise
    return result is not None
  

def resetDB1():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD1'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[1] == 0:
    generateDetails(1)
    global_arr[1] = 1

def resetDB2():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD2'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[2] == 0:
    generateDetails(2)
    global_arr[2] = 1
def resetDB3():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD3'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[3] == 0:
    generateDetails(3)
    global_arr[3] = 1
def resetDB4():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD4'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[4] == 0:
    generateDetails(4)
    global_arr[4] = 1
def resetDB5():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD5'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[5] == 0:
    generateDetails(5)
    global_arr[5] = 1
def resetDB6():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD6'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[6] == 0:
    generateDetails(6)
    global_arr[6] = 1
def resetDB7():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD7'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[7] == 0:
    generateDetails(7)
    global_arr[7] = 1 
def resetDB8(): 
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD8'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[8] == 0:
    generateDetails(8)
    global_arr[8] = 1
def resetDB9():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD9'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[9] == 0:
    generateDetails(9)
    global_arr[9] = 1
def resetDB10():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD10'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[10] == 0:
    generateDetails(10)
    global_arr[10] = 1
def resetDB11():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD11'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[11] == 0:
    generateDetails(11)
    global_arr[11] = 1
def resetDB12():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD12'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[12] == 0:
    generateDetails(12)
    global_arr[12] = 1
def resetDB13():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD13'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[13] == 0:
    generateDetails(13)
    global_arr[13] = 1
def resetDB14():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD14'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[14] == 0:
    generateDetails(14)
    global_arr[14] = 1
def resetDB15():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD15'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[15] == 0:
    generateDetails(15)
    global_arr[15] = 1
def resetDB16():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD16'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[16] == 0:
    generateDetails(16)
    global_arr[16] = 1
def resetDB17():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD17'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[17] == 0:
    generateDetails(17)
    global_arr[17] = 1
def resetDB18(): 
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD18'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[18] == 0:
    generateDetails(18)
    global_arr[18] = 1
def resetDB19():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD19'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[19] == 0:
    generateDetails(19)
    global_arr[19] = 1
def resetDB20():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD20'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[20] == 0:
    generateDetails(20)
    global_arr[20] = 1
def resetDB21():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD21'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[21] == 0:
    generateDetails(21)
    global_arr[21] = 1
def resetDB22():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD22'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[22] == 0:
    generateDetails(22)
    global_arr[22] = 1
def resetDB23():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD23'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[23] == 0:
    generateDetails(23)
    global_arr[23] = 1
def resetDB24():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD24'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[24] == 0:
    generateDetails(24)
    global_arr[24] = 1
def resetDB25():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD25'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[25] == 0:
    generateDetails(25)
    global_arr[25] = 1
def resetDB26():  
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD26'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[26] == 0:
    generateDetails(26)
    global_arr[26] = 1
def resetDB27():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD27'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[27] == 0:
    generateDetails(27)
    global_arr[27] = 1
def resetDB28():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD28'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[28] == 0:
    generateDetails(28)
    global_arr[28] = 1
def resetDB29():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD29'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[29] == 0:
    generateDetails(29)
    global_arr[29] = 1
def resetDB30():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD30'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[30] == 0:
    generateDetails(30)
    global_arr[30] = 1  
def resetDB31():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD31'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[31] == 0:
    generateDetails(31)
    global_arr[31] = 1
def resetDB32():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD32'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[32] == 0:
    generateDetails(32)
    global_arr[32] = 1
def resetDB33():  
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD33'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[33] == 0:
    generateDetails(33)
    global_arr[33] = 1
def resetDB34():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD34'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[34] == 0:
    generateDetails(34)
    global_arr[34] = 1
def resetDB35():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD35'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[35] == 0:
    generateDetails(35)
    global_arr[35] = 1
def resetDB36():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD36'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[36] == 0:
    generateDetails(36)
    global_arr[36] = 1
def resetDB37():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD37'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[37] == 0:
    generateDetails(37)
    global_arr[37] = 1
def resetDB38():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD38'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[38] == 0:
    generateDetails(38)
    global_arr[38] = 1
def resetDB39():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD39'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[39] == 0:
    generateDetails(39)
    global_arr[39] = 1
def resetDB40():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD40'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[40] == 0:
    generateDetails(40)
    global_arr[40] = 1
def resetDB41():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD41'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[41] == 0:
    generateDetails(41)
    global_arr[41] = 1
def resetDB42():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD42'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[42] == 0:
    generateDetails(42)
    global_arr[42] = 1
def resetDB43():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD43'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[43] == 0:
    generateDetails(43)
    global_arr[43] = 1
def resetDB44():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD44'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[44] == 0:
    generateDetails(44)
    global_arr[44] = 1
def resetDB45():
  db_path = './database.db'  # Replace with your database file path
  table_name = 'MD45'
  table_exists = check_table_exists(db_path, table_name)
  if not table_exists and global_arr[45] == 0:
    generateDetails(45)
    global_arr[45] = 1
                        
                                                    

def addPictureColumnToPD():
    global sqliteConnect, cursor
    try:
        # Step 1: Add the Picture column to the PD table
        cursor.execute("ALTER TABLE PD ADD COLUMN Picture TEXT DEFAULT 'NA'")
        print("Picture column added to PD table successfully.")
        
        # Step 2: Update the Picture column for each player
        cursor.execute("SELECT ID, Name FROM PD")
        players = cursor.fetchall()

        for player in players:
            playerID, playerName = player
            # Assuming the playerName does not need to be sanitized or modified to match file names
            picturePath = f"assets/PlayerImages/Images/{playerName}.webp"
            
            # Update the Picture column for the player
            cursor.execute("UPDATE PD SET Picture = ? WHERE ID = ?", (picturePath, playerID))
        
        sqliteConnect.commit()
        print("Picture paths updated for all players in PD table.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sqliteConnect.rollback()




def generateTeams(n=10):
    global sqliteConnect, cursor
    # Ensure that the sqliteConnect and cursor are properly initialized before calling this function
    try:
        with open("assets/names/teamnames.txt", "r") as f:
            teamList = [line.strip() for line in f if line.strip()]  # Read and clean team names
        random.shuffle(teamList)

        with open("assets/names/playernames.txt", "r") as f:
            playerList = [line.strip() for line in f if line.strip()]  # Read and clean player names
        if len(playerList) < n * 11:  # Ensure there are enough player names for the teams
            raise ValueError("Not enough player names in the file.")
        random.shuffle(playerList)
        
        for teamIndex, team in enumerate(teamList[:n]):
            logo_filename = f"assets/logos/{team}.webp"
            cursor.execute('INSERT INTO TT(Teams, Logo) VALUES(?, ?)', (team, logo_filename))
            teamID = cursor.lastrowid

            # Create a table for each team using the team's name for table naming
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS "{team}" (
                                PlayerID INTEGER PRIMARY KEY,
                                Name TEXT,
                                Age INT,
                                Hand BOOLEAN,
                                isCaptain BOOLEAN,
                                isBatsman BOOLEAN,
                                isBowler BOOLEAN,
                                isWK BOOLEAN,
                                FOREIGN KEY(PlayerID) REFERENCES PD(ID))''')
            sqliteConnect.commit()  # Commit immediately after table creation

            captainIndex = random.randint(0, 10)
            batsmenCount = random.randint(4, 6)
            allroundersCount = random.randint(1, 3)
            wkIndex = random.randint(0, batsmenCount - 1)  # Assuming wkIndex is within batsmen

            for playerIndex in range(11):
                playerName = playerList.pop(0)
                playerAge = random.randint(18, 35)
                playerHand = random.choice([True, False])
                isCaptain = (playerIndex == captainIndex)
                isBatsman = (playerIndex < batsmenCount or playerIndex < allroundersCount + batsmenCount)
                isBowler = (playerIndex >= batsmenCount)
                isWK = (playerIndex == wkIndex and isBatsman)

                # Insert player into PD table
                cursor.execute('INSERT INTO PD(Name, Age, Hand, TeamID) VALUES(?, ?, ?, ?)', (playerName, playerAge, playerHand, teamID))
                playerID = cursor.lastrowid  # Get the last inserted ID

                # Now insert the player with PlayerID into the team table
                cursor.execute(f'INSERT INTO "{team}" (PlayerID, Name, Age, Hand, isCaptain, isBatsman, isBowler, isWK) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', 
                               (playerID, playerName, playerAge, playerHand, isCaptain, isBatsman, isBowler, isWK))

        sqliteConnect.commit()  # Commit after all inserts
        addPictureColumnToPD()
        print(f"Teams, players, roles, and logos generated successfully for {n} teams.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sqliteConnect.rollback()

# Example usage
# generateTeams(10)



import itertools

def generateMatches():
    global sqliteConnect, cursor
    numT = numTeams()
    TeamsArr = [x for x in range(1, numT+1)]
    
    # Generate all possible unique pairs (combinations) of teams
    all_combinations = list(itertools.combinations(TeamsArr, 2))
    random.shuffle(all_combinations)
    
    # Insert each pair into the database
    for a, b in all_combinations:
        cursor.execute('INSERT INTO MD(TeamA, TeamB) VALUES(?, ?)', (a, b))
    
    sqliteConnect.commit()


def getTournamentStats():
  global sqliteConnect, cursor
  print("Top 5 Run Scorers:")
  print("Player Name\t\wtTeam\t\tRuns Scored")
  
  global runs
  runs = cursor.execute('SELECT PD.ID ,PD.Name, PD.Picture, TT.Teams, TT.Logo, PD.RunsScored FROM PD LEFT JOIN TT ON PD.TeamID = TT.ID ORDER BY PD.RunsScored DESC LIMIT 5').fetchall()
  # for i in runs:
  #   print(i[0], "\t\t", i[1], "\t\t", i[2], sep="")
  # print()
  # print("Top 5 Wicket Takers:")
  # print("Player Name\t\tTeam\t\tWickets Taken")
  global wickets
  wickets = cursor.execute('SELECT PD.ID ,PD.Name, PD.Picture, TT.Teams, TT.Logo, PD.WicketsTaken FROM PD LEFT JOIN TT ON PD.TeamID = TT.ID ORDER BY PD.WicketsTaken DESC LIMIT 5').fetchall()
  # for i in wickets:
  return runs,wickets
  #   print(i[0], "\t\t", i[1], "\t\t", i[2], sep="")
  # print()



def numTeams():
  global sqliteConnect, cursor
  try: 
    cursor.execute('SELECT COUNT(*) FROM TT')
    return cursor.fetchone()[0]
  except:
    # If TT table does not exist
    return 0

# Get the number of matches
def numMatches():
  global sqliteConnect, cursor
  try: 
    cursor.execute('SELECT COUNT(*) FROM MD')
    return cursor.fetchone()[0]
  except:
    # If MD table does not exist
    return 0
  
# Get the number of players
def numPlayers():
  global sqliteConnect, cursor
  try:
    cursor.execute('SELECT COUNT(*) FROM PD')
    return cursor.fetchone()[0]
  except:
    # IF PD table does not exist
    return 0  
  
def getT():
  x,y=getTournamentStats()
  return x,y
  

def updateHighScores(teamID):
  global sqliteConnect, cursor
  highScore = cursor.execute('SELECT PD1.RunsScored, PD2.WicketsTaken FROM TT LEFT JOIN PD PD1 ON PD1.ID = TT.HighestRunScorer LEFT JOIN PD PD2 ON PD2.ID = TT.HighestWicketTaker WHERE TT.ID = ?', (teamID,)).fetchone()
  teamHighRuns = cursor.execute('SELECT PD.ID, PD.RunsScored FROM TT LEFT JOIN PD ON PD.TeamID = TT.ID WHERE TT.ID = ? ORDER BY PD.RunsScored DESC LIMIT 1', (teamID,)).fetchone()
  teamHighWickets = cursor.execute('SELECT PD.ID, PD.WicketsTaken FROM TT LEFT JOIN PD ON PD.TeamID = TT.ID WHERE TT.ID = ? ORDER BY PD.WicketsTaken DESC LIMIT 1', (teamID,)).fetchone()
  if (highScore[0] == None):
    cursor.execute('UPDATE TT SET HighestRunScorer = ? WHERE ID = ?', (teamHighRuns[0], teamID))
    cursor.execute('UPDATE TT SET HighestWicketTaker = ? WHERE ID = ?', (teamHighWickets[0], teamID))
    sqliteConnect.commit()
    return
  if (teamHighRuns[1] > highScore[0]):
    cursor.execute('UPDATE TT SET HighestRunScorer = ? WHERE ID = ?', (teamHighRuns[0], teamID))
  if (teamHighWickets[1] > highScore[1]):
    cursor.execute('UPDATE TT SET HighestWicketTaker = ? WHERE ID = ?', (teamHighWickets[0], teamID))
  sqliteConnect.commit()


def generateDetails(matchID):
  global sqliteConnect2, cursor
  # Decide who bats first
  batFirst = random.randint(0, 1)
  teamAruns = 0
  teamAballs = 0
  teamAwickets = 0
  teamBruns = 0
  teamBwickets = 0
  teamBballs = 0
  winner = 0
  # Decide the details of the first batting team. If the team is all out, the number of balls is decided randomly.
  # Then, decide the details of the second batting team. Decide number of balls and wickets carefully.
  # If A scores more, it wins (1). If B scores more, it wins(2). If A and B score the same, it is a tie(0).
  if (batFirst == 0):
    teamAruns = random.randint(80, 200)
    teamAwickets = random.randint(0, 10)
    teamAballs = 0
    if (teamAwickets == 10):
      teamAballs = random.randint(round(teamAruns/6), 120)
    else:
      teamAballs = 120
    teamBruns = random.randint(60, teamAruns+6)
    if (teamBruns > teamAruns):
      teamBwickets = random.randint(0, 9)
      teamBballs = random.randint(round(teamBruns/6), 120)
      winner = 2
    elif (teamBruns < teamAruns):
      teamBwickets = random.randint(0, 10)
      winner = 1
      if (teamBwickets == 10):
        teamBballs = random.randint(round(teamBruns/6), 120)
      else:
        teamBballs = 120
    else:
      teamBwickets = random.randint(0, 9)
      winner = 0
      teamBballs = random.randint(round(teamBruns/6), 120)
  else:
    teamBruns = random.randint(80, 200)
    teamBwickets = random.randint(0, 10)
    teamBballs = 0
    if (teamBwickets == 10):
      teamBballs = random.randint(round(teamBruns/6), 120)
    else:
      teamBballs = 120
    teamAruns = random.randint(0, teamBruns+6)
    if (teamAruns > teamBruns):
      teamAwickets = random.randint(0, 9)
      teamAballs = random.randint(round(teamAruns/6), 120)
      winner = 1
    elif (teamAruns < teamBruns):
      teamAwickets = random.randint(0, 10)
      winner = 2
      if (teamAwickets == 10):
        teamAballs = random.randint(round(teamAruns/6), 120)
      else:
        teamAballs = 120
    else:
      teamAwickets = random.randint(0, 9)
      winner = 0
      teamAballs = random.randint(round(teamAruns/6), 120)
  print(1)
  cursor.execute('UPDATE MD SET DetailsGenerated = 1, BatFirst = ?, TeamARuns = ?, TeamABalls = ?, TeamAWickets = ?, TeamBRuns = ?, TeamBBalls = ?, TeamBWickets = ?, Result = ? WHERE ID = ?', (batFirst, teamAruns, teamAballs, teamAwickets, teamBruns, teamBballs, teamBwickets, winner, matchID))
  # Get the teams playing the match
  print(2)
  cursor.execute(f'SELECT TeamA, TeamB FROM MD WHERE ID = {matchID}')
  print(3)
  matchteams = cursor.fetchall()
  tAid = matchteams[0][0]
  print(tAid)
  tBid = matchteams[0][1]
  print(tBid)
  cursor.execute('SELECT Teams FROM TT WHERE ID = ?', (tAid,))
  team1= cursor.fetchone()[0]
#   print(teamA)
  cursor.execute('SELECT Teams FROM TT WHERE ID = ?', (tBid,))
  team2= cursor.fetchone()[0]
#   print(teamB)
  cursor.execute('UPDATE TT SET MatchesPlayed = MatchesPlayed + 1 WHERE ID = ?', (tAid,))
  cursor.execute('UPDATE TT SET MatchesPlayed = MatchesPlayed + 1 WHERE ID = ?', (tBid,))
  if (winner == 1):
    cursor.execute('UPDATE TT SET MatchesWon = MatchesWon + 1 WHERE ID = ?', (tAid,))
    tAlast5 = cursor.execute('SELECT Last5Matches FROM TT WHERE ID = ?', (tAid,)).fetchone()[0]
    if (tAlast5 == "NA"): tAlast5 = ""
    if (len(tAlast5) == 5): tAlast5 = tAlast5[1:]+'W'
    else: tAlast5 += 'W'
    cursor.execute('UPDATE TT SET Last5Matches = ? WHERE ID = ?', (tAlast5, tAid))
    tBlast5 = cursor.execute('SELECT Last5Matches FROM TT WHERE ID = ?', (tBid,)).fetchone()[0]
    if (tBlast5 == "NA"): tBlast5 = ""
    if (len(tBlast5) == 5): tBlast5 = tBlast5[1:]+'L'
    else: tBlast5 += 'L'
    cursor.execute('UPDATE TT SET Last5Matches = ? WHERE ID = ?', (tBlast5, tBid))
  elif (winner == 2):
    cursor.execute('UPDATE TT SET MatchesWon = MatchesWon + 1 WHERE ID = ?', (tBid,))
    tAlast5 = cursor.execute('SELECT Last5Matches FROM TT WHERE ID = ?', (tAid,)).fetchone()[0]
    if (tAlast5 == "NA"): tAlast5 = ""
    if (len(tAlast5) == 5): tAlast5 = tAlast5[1:]+'L'
    else: tAlast5 += 'L'
    cursor.execute('UPDATE TT SET Last5Matches = ? WHERE ID = ?', (tAlast5, tAid))
    tBlast5 = cursor.execute('SELECT Last5Matches FROM TT WHERE ID = ?', (tBid,)).fetchone()[0]
    if (tBlast5 == "NA"): tBlast5 = ""
    if (len(tBlast5) == 5): tBlast5 = tBlast5[1:]+'W'
    else: tBlast5 += 'W'
    cursor.execute('UPDATE TT SET Last5Matches = ? WHERE ID = ?', (tBlast5, tBid))
  else:
    tAlast5 = cursor.execute('SELECT Last5Matches FROM TT WHERE ID = ?', (tAid,)).fetchone()[0]
    if (tAlast5 == "NA"): tAlast5 = ""
    if (len(tAlast5) == 5): tAlast5 = tAlast5[1:]+'D'
    else: tAlast5 += 'D'
    cursor.execute('UPDATE TT SET Last5Matches = ? WHERE ID = ?', (tAlast5, tAid))
    tBlast5 = cursor.execute('SELECT Last5Matches FROM TT WHERE ID = ?', (tBid,)).fetchone()[0]
    if (tBlast5 == "NA"): tBlast5 = ""
    if (len(tBlast5) == 5): tBlast5 = tBlast5[1:]+'D'
    else: tBlast5 += 'D'
    cursor.execute('UPDATE TT SET Last5Matches = ? WHERE ID = ?', (tBlast5, tBid))
  # Create the table for the match scorecard
  cursor.execute(f'CREATE TABLE IF NOT EXISTS MD{matchID} (PlayerID INTEGER PRIMARY KEY, RunsScored INTEGER, BallsFaced INTEGER, WicketsTaken INTEGER, BallsBowled INTEGER, FOREIGN KEY(PlayerID) REFERENCES PD(ID))')
  sqliteConnect.commit()
  # Arrays to hold the runs scored, balls faced, wickets taken, balls bowled by each player
  tArsArr = []
  tBrsArr = []
  tAbfArr = []
  tBbfArr = []
  tAwtArr = []
  tBwtArr = []
  tAbbArr = []
  tBbbArr = []
  # RUNS SCORED (Weight reduces as we go down the order)
  # Team A
  sumA = 0
  for i in range(11):
    if (i <= teamAwickets): tArsArr.append(random.randint(0, 200-11*i))
    else: tArsArr.append(0)
    sumA += tArsArr[i]
  if sumA==0: sumA+=1
  tempsum = 0
  for i in range(11):
    tArsArr[i] = round(tArsArr[i]*teamAruns/sumA)
    tempsum += tArsArr[i]
  if (tempsum != teamAruns):
    tArsArr[0] += teamAruns - tempsum
  # Team B
  sumB = 0
  for i in range(11):
    if (i<= teamBwickets): tBrsArr.append(random.randint(0, 200-11*i))
    else: tBrsArr.append(0)
    sumB += tBrsArr[i]
  tempsum = 0
  if sumB==0: sumB+=1
  for i in range(11):
    tBrsArr[i] = round(tBrsArr[i]*teamBruns/sumB)
    tempsum += tBrsArr[i]
  if (tempsum != teamBruns):
    tBrsArr[0] += teamBruns - tempsum
  # BALLS FACED
  # Team A
  sumA = 0
  for i in range(11):
    tAbfArr.append(random.randint(ceil(tArsArr[i]/6), tArsArr[i]))
    sumA += tAbfArr[i]
  tempsum = 0
  if sumA==0: sumA+=1
  for i in range(11):
    tAbfArr[i] = ceil(tAbfArr[i]*teamAballs/sumA)
    tempsum += tAbfArr[i]
  if (tempsum < teamAballs):
    tAbfArr[0] += teamAballs - tempsum
  elif (tempsum > teamAballs):
    max_val = max(tAbfArr)
    max_ind = tAbfArr.index(max_val)
    tAbfArr[max_ind] += teamAballs - tempsum
  # Team B
  sumB = 0
  for i in range(11):
    tBbfArr.append(random.randint(ceil(tBrsArr[i]/6), tBrsArr[i]))
    sumB += tBbfArr[i]
  tempsum = 0
  if sumB==0: sumB+=1
  for i in range(11):
    tBbfArr[i] = ceil(tBbfArr[i]*teamBballs/sumB)
    tempsum += tBbfArr[i]
  if (tempsum < teamBballs):
    tBbfArr[0] += teamBballs - tempsum
  elif (tempsum > teamBballs):
    max_val = max(tBbfArr)
    max_ind = tBbfArr.index(max_val)
  # Get if player is a bowler or not
  cursor.execute(f'SELECT PlayerID, isBowler FROM "{team1}"')
  teamA = cursor.fetchall()
  cursor.execute(f'SELECT PlayerID, isBowler FROM "{team2}"')
  teamB = cursor.fetchall()
  # WICKETS TAKEN
  # Team A
  sumA = 0
  for i in range(11):
    if(teamA[i][1] == 1): tAwtArr.append(random.randint(0, 10))
    else: tAwtArr.append(0)
    sumA += tAwtArr[i]
  tempsum = 0
  if sumA==0: sumA+=1
  for i in range(11):
    if (tempsum < teamAwickets): tAwtArr[i] = floor(tAwtArr[i]*teamBwickets/sumA)
    else: tAwtArr[i] = 0
    tempsum += tAwtArr[i]
  if (tempsum != teamBwickets):
    tAwtArr[10] += teamBwickets - tempsum
  # Team B
  sumB = 0
  for i in range(11):
    if(teamB[i][1] == 1): tBwtArr.append(random.randint(0, 10))
    else: tBwtArr.append(0)
    sumB += tBwtArr[i]
  tempsum = 0
  if sumB==0: sumB+=1
  for i in range(11):
    if (tempsum < teamBwickets): tBwtArr[i] = floor(tBwtArr[i]*teamAwickets/sumB)
    else: tBwtArr[i] = 0
    tempsum += tBwtArr[i]
  if (tempsum != teamAwickets):
    tBwtArr[10] += teamAwickets - tempsum
  # BALLS BOWLED (Max 30 balls per bowler)
  # Team A
  sumA = 0
  for i in range(11):
    if(teamA[i][1] == 1): tAbbArr.append(random.randint(6, 120))
    else: tAbbArr.append(0)
    sumA += tAbbArr[i]
  tempsum = 0
  if sumA==0: sumA+=1
  for i in range(11):
    tAbbArr[i] = floor(tAbbArr[i]*teamBballs/sumA/6)*6
    if (tAbbArr[i] > 30): tAbbArr[i] = 30
    tempsum += tAbbArr[i]
  if (tempsum != teamBballs):
    tAbbArr[10] += teamBballs - tempsum
  # Team B
  sumB = 0
  for i in range(11):
    if(teamB[i][1] == 1): tBbbArr.append(random.randint(6, 120))
    else: tBbbArr.append(0)
    sumB += tBbbArr[i]
  tempsum = 0
  if sumB==0: sumB+=1
  for i in range(11):
    tBbbArr[i] = floor(tBbbArr[i]*teamAballs/sumB/6)*6
    if (tBbbArr[i] > 30): tBbbArr[i] = 30
    tempsum += tBbbArr[i]
  if (tempsum != teamAballs):
    tBbbArr[10] += teamAballs - tempsum
  # Store the data in the MD table

  for i in range(11):
    cursor.execute(f'UPDATE PD SET MatchesPlayed = MatchesPlayed + 1, RunsScored = RunsScored + {tArsArr[i]}, BallsFaced = BallsFaced + {tAbfArr[i]}, WicketsTaken = WicketsTaken + {tAwtArr[i]}, BallsBowled = BallsBowled + {tAbbArr[i]} WHERE ID = {(tAid-1)*11+i+1}')
    cursor.execute(f'INSERT INTO MD{matchID} VALUES(?, ?, ?, ?, ?)', ((tAid-1)*11+i+1, tArsArr[i], tAbfArr[i], tAwtArr[i], tAbbArr[i]))
  for i in range(11):
    cursor.execute(f'UPDATE PD SET MatchesPlayed = MatchesPlayed + 1, RunsScored = RunsScored + {tBrsArr[i]}, BallsFaced = BallsFaced + {tBbfArr[i]}, WicketsTaken = WicketsTaken + {tBwtArr[i]}, BallsBowled = BallsBowled + {tBbbArr[i]} WHERE ID = {(tBid-1)*11+i+1}')
    cursor.execute(f'INSERT INTO MD{matchID} VALUES(?, ?, ?, ?, ?)', ((tBid-1)*11+i+1, tBrsArr[i], tBbfArr[i], tBwtArr[i], tBbbArr[i]))
  updateHighScores(tAid)
  updateHighScores(tBid)
  sqliteConnect.commit()

def get_player_name(player_id):
    # Assuming a function to get player name by their ID
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Name FROM PD WHERE ID = ?", (player_id,))
    result = cursor.fetchone()
    connection.close()
    return result[0] if result else "Unknown Player"
def get_team_name(team_id):
    # Assuming a function to get team name by their ID
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Teams FROM TT WHERE ID = ?", (team_id,))
    result = cursor.fetchone()
    connection.close()
    print(result)
    return result[0] if result else "Unknown Team"
def get_team_names(match_id):
    # Establish a connection to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # SQL query to select TeamA and TeamB from the MD table for a specific match_id
    query = f"SELECT TeamA, TeamB FROM MD WHERE ID = ?"
    
    try:
        # Execute the query with safe parameter substitution
        cursor.execute(query, (match_id,))
        result = cursor.fetchone()  # fetchone() as we expect only one row for each match_id
        if result:
            team_a, team_b = result
            return team_a, team_b
        else:
            print("No match found with the given ID.")
            return None, None
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None, None
    finally:
        # Close the database connection
        conn.close()