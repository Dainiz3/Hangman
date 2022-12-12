from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Blueprint, flash, jsonify, url_for, render_template, request, redirect, session
from flask_login import login_required, current_user
from .models import User
from . import db
from website import functions

hangman = Blueprint('hangman', __name__)

secret_word = None
word_set = None
to_display = None
tries = None
blanks = None


@hangman.route('/game')
@login_required
def game():
	global secret_word
	global word_set
	global to_display
	global tries
	global blanks	
	secret_word = functions.get_random_word()
	word_set = "abcdefghijklmnopqrstuvwxyz"
	blanks = 0
	to_display = []
	for char in enumerate(secret_word):
		if char==" ":
			to_display.append(" ")
			
		else:
			to_display.append("_")
			blanks+=1

	tries = 0
	return render_template('game.html',user=current_user, to_display=to_display,word_set=word_set,tries="/static/img/hangman%d.png"%tries)


@hangman.route('/add_char',methods=["POST"])
@login_required
def add_char():
	global secret_word
	global word_set
	global to_display
	global tries
	global blanks	

	letter = request.form["letter"]
	user = request.form.get('user')

	chance_lost = True
	for show_letter,char in enumerate(secret_word):
		if char==letter:
			chance_lost = False
			to_display[show_letter] = letter
			blanks-=1

	word_set = word_set.replace(letter,'')
	print("blanks",blanks)
	if chance_lost==True:
		tries += 1
		if tries==10:
			user = User.query.filter_by(id=current_user.id).first()
			user.losses += 1
			user.games_played += 1
			db.session.add(user)
			db.session.commit()
			return redirect('/game_lost')

	if blanks==0:
		user = User.query.filter_by(id=current_user.id).first()
		user.wins += 1
		user.games_played += 1
		db.session.add(user)
		db.session.commit()
		return redirect('/game_won')

	return render_template('game.html',user=current_user,to_display=to_display,word_set=word_set,tries="/static/img/hangman%d.png"%tries)

@hangman.route('/game_lost')
@login_required
def game_lost_landing():
	return render_template('game_lost.html',user=current_user,)

@hangman.route('/game_won')
@login_required
def game_won_landing():
	return render_template('game_won.html',user=current_user,)


