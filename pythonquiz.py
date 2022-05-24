from enum import Flag
import re
import os
import random
import datetime
import dbmanage
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
total_questions = 5
conn = dbmanage.connecttodb()
#always to remain false unless user logged in or first time signed in 
#do not alter outside of login and signup functions

global authorizedentry 
authorizedentry= False


class Quiz:
    allQuiz = {}
    def __init__(self, id, question, player, answer, tries,score = 0 ):
        self.qid = id
        self.question = question
        self.player = player
        self.answer = answer
        self.tries = tries
        self.score = score
    def calculate_score(self, reply):
        #score calculation
        #exact formula for score calculation to be discussed
        if reply == self.answer:
            self.score = self.score + 1
            return True
        
    def __str__(self):
        pass




class Player:
    players = {}
    
    
    def set_password(self,password):
        # password for player object
        self.password_hash = generate_password_hash(password)
        #print(check_password_hash(self.password_hash,password))


    @staticmethod
    def load_players(self):
        pass
    def __init__(self, name, password,update=True):
        self.name = name
        self.password = password
        self.set_password(password)
        self.values = [name,self.password_hash,0]

    def check_password(self):
        #checks password on db
        passondb = dbmanage.fetchplayer(conn,self.values)[0][1]
        authorizedentry =  check_password_hash(passondb,self.password)
        return authorizedentry
        
    def new_game(self, score, update=True):
        pass
    #updates the database with current inputed player if conditions met
    def update_players(self):
        #hashes the password for safe store on db
        if dbmanage.fetchplayer(conn,self.values):
            #user already exists block signup
            return False
        self.values[1] = self.password_hash
        dbmanage.insertplayer(conn,self.values )
        authorizedentry = True
        return authorizedentry
    ##only to happen after authorization
    def update_player_stats(self):
    
        dbmanage.editplayer(conn,self.values)


    def __str__(self):
        pass
    def receiveperformance(self,grade):
        self.values[2] = grade

def makeplayer(username,password):
    #makes player object 
    #not currently usefull
    return Player(username,password)
#quiz contains question id,questin text and player playing
def load_quiz(player):
    global quiz 
    q = dbmanage.takequestion(conn)
    quiz = Quiz(q[0],q[1],player,q[2],0)
    return quiz
    ## load players
    #Player.load_players()

def play_quiz(quiz,response):
    #plays quiz
    #checks if response is correct
    #if correct, adds to score
    #adds to tries
    #implement using while loop?
    if quiz.tries < total_questions:
        quiz.tries = quiz.tries + 1
        quiz.calculate_score(response)
        q = dbmanage.takequestion(conn)
        quiz.id = q[0]
        quiz.question = q[1]
        quiz.answer = q[2]
        return False#quiz not over
    else:
        quiz.calculate_score(response)
        quiz.player.values[2] = quiz.score
        quiz.player.update_player_stats()
        return True#quiz over
#will be used after request is imported
def newresponse():
    #new response will take input from the html page
    if request.method == "POST":
        response = request.form["response"]
        return response
    pass


def recursivequiz(quiz,response):
    #plays quiz until quiz is over
    while(not play_quiz(quiz,response)):
        #new response will take input from the html page
        response = newresponse()
        
if __name__ == "__main__":
    pass
    #load_quiz()
    #play_quiz()



#####################TEST#########TEST######################
testplay = makeplayer("carmalo","!@balana243")
print(testplay.update_players())
authorizedentry= testplay.check_password()
print(authorizedentry)
testplay.receiveperformance(16)
if authorizedentry:
    testplay.update_player_stats()

print(dbmanage.fetchplayer(conn,testplay.values))





