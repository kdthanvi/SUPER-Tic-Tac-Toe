import sys
from PyQt4 import QtGui, QtCore, uic

form_class = uic.loadUiType("super_layout.ui")[0]

player_x = [0,0,0,0,0,0,0,0,0,0]
player_o = [0,0,0,0,0,0,0,0,0,0]

player_b2_x = [0,0,0,0,0,0,0,0,0,0]
player_b2_o = [0,0,0,0,0,0,0,0,0,0]
player_b3_x = [0,0,0,0,0,0,0,0,0,0]
player_b3_o = [0,0,0,0,0,0,0,0,0,0]
player_b4_x = [0,0,0,0,0,0,0,0,0,0]
player_b4_o = [0,0,0,0,0,0,0,0,0,0]
player_b5_x = [0,0,0,0,0,0,0,0,0,0]
player_b5_o = [0,0,0,0,0,0,0,0,0,0]
player_b6_x = [0,0,0,0,0,0,0,0,0,0]
player_b6_o = [0,0,0,0,0,0,0,0,0,0]
player_b7_x = [0,0,0,0,0,0,0,0,0,0]
player_b7_o = [0,0,0,0,0,0,0,0,0,0]
player_b8_x = [0,0,0,0,0,0,0,0,0,0]
player_b8_o = [0,0,0,0,0,0,0,0,0,0]
player_b9_x = [0,0,0,0,0,0,0,0,0,0]
player_b9_o = [0,0,0,0,0,0,0,0,0,0]

final_player_x = [0,0,0,0,0,0,0,0,0,0]
final_player_o = [0,0,0,0,0,0,0,0,0,0]

turn = 'x'


class MyWindowClass(QtGui.QMainWindow, form_class):
	def __init__(self, parent=None):
		
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		
		self.b1_1.clicked.connect(self.b1_1_clicked)
		self.b1_2.clicked.connect(self.b1_2_clicked)
		self.b1_3.clicked.connect(self.b1_3_clicked)
		self.b1_4.clicked.connect(self.b1_4_clicked)
		self.b1_5.clicked.connect(self.b1_5_clicked)
		self.b1_6.clicked.connect(self.b1_6_clicked)
		self.b1_7.clicked.connect(self.b1_7_clicked)
		self.b1_8.clicked.connect(self.b1_8_clicked)
		self.b1_9.clicked.connect(self.b1_9_clicked)
		
		self.b2_1.clicked.connect(self.b2_1_clicked)
		self.b2_2.clicked.connect(self.b2_2_clicked)
		self.b2_3.clicked.connect(self.b2_3_clicked)
		self.b2_4.clicked.connect(self.b2_4_clicked)
		self.b2_5.clicked.connect(self.b2_5_clicked)
		self.b2_6.clicked.connect(self.b2_6_clicked)
		self.b2_7.clicked.connect(self.b2_7_clicked)
		self.b2_8.clicked.connect(self.b2_8_clicked)
		self.b2_9.clicked.connect(self.b2_9_clicked)
		
		self.b3_1.clicked.connect(self.b3_1_clicked)
		self.b3_2.clicked.connect(self.b3_2_clicked)
		self.b3_3.clicked.connect(self.b3_3_clicked)
		self.b3_4.clicked.connect(self.b3_4_clicked)
		self.b3_5.clicked.connect(self.b3_5_clicked)
		self.b3_6.clicked.connect(self.b3_6_clicked)
		self.b3_7.clicked.connect(self.b3_7_clicked)
		self.b3_8.clicked.connect(self.b3_8_clicked)
		self.b3_9.clicked.connect(self.b3_9_clicked)
		
		self.b4_1.clicked.connect(self.b4_1_clicked)
		self.b4_2.clicked.connect(self.b4_2_clicked)
		self.b4_3.clicked.connect(self.b4_3_clicked)
		self.b4_4.clicked.connect(self.b4_4_clicked)
		self.b4_5.clicked.connect(self.b4_5_clicked)
		self.b4_6.clicked.connect(self.b4_6_clicked)
		self.b4_7.clicked.connect(self.b4_7_clicked)
		self.b4_8.clicked.connect(self.b4_8_clicked)
		self.b4_9.clicked.connect(self.b4_9_clicked)
	
		self.b5_1.clicked.connect(self.b5_1_clicked)
		self.b5_2.clicked.connect(self.b5_2_clicked)
		self.b5_3.clicked.connect(self.b5_3_clicked)
		self.b5_4.clicked.connect(self.b5_4_clicked)
		self.b5_5.clicked.connect(self.b5_5_clicked)
		self.b5_6.clicked.connect(self.b5_6_clicked)
		self.b5_7.clicked.connect(self.b5_7_clicked)
		self.b5_8.clicked.connect(self.b5_8_clicked)
		self.b5_9.clicked.connect(self.b5_9_clicked)
	
		self.b6_1.clicked.connect(self.b6_1_clicked)
		self.b6_2.clicked.connect(self.b6_2_clicked)
		self.b6_3.clicked.connect(self.b6_3_clicked)
		self.b6_4.clicked.connect(self.b6_4_clicked)
		self.b6_5.clicked.connect(self.b6_5_clicked)
		self.b6_6.clicked.connect(self.b6_6_clicked)
		self.b6_7.clicked.connect(self.b6_7_clicked)
		self.b6_8.clicked.connect(self.b6_8_clicked)
		self.b6_9.clicked.connect(self.b6_9_clicked)
		
		self.b7_1.clicked.connect(self.b7_1_clicked)
		self.b7_2.clicked.connect(self.b7_2_clicked)
		self.b7_3.clicked.connect(self.b7_3_clicked)
		self.b7_4.clicked.connect(self.b7_4_clicked)
		self.b7_5.clicked.connect(self.b7_5_clicked)
		self.b7_6.clicked.connect(self.b7_6_clicked)
		self.b7_7.clicked.connect(self.b7_7_clicked)
		self.b7_8.clicked.connect(self.b7_8_clicked)
		self.b7_9.clicked.connect(self.b7_9_clicked)
		
		self.b8_1.clicked.connect(self.b8_1_clicked)
		self.b8_2.clicked.connect(self.b8_2_clicked)
		self.b8_3.clicked.connect(self.b8_3_clicked)
		self.b8_4.clicked.connect(self.b8_4_clicked)
		self.b8_5.clicked.connect(self.b8_5_clicked)
		self.b8_6.clicked.connect(self.b8_6_clicked)
		self.b8_7.clicked.connect(self.b8_7_clicked)
		self.b8_8.clicked.connect(self.b8_8_clicked)
		self.b8_9.clicked.connect(self.b8_9_clicked)
		
		self.b9_1.clicked.connect(self.b9_1_clicked)
		self.b9_2.clicked.connect(self.b9_2_clicked)
		self.b9_3.clicked.connect(self.b9_3_clicked)
		self.b9_4.clicked.connect(self.b9_4_clicked)
		self.b9_5.clicked.connect(self.b9_5_clicked)
		self.b9_6.clicked.connect(self.b9_6_clicked)
		self.b9_7.clicked.connect(self.b9_7_clicked)
		self.b9_8.clicked.connect(self.b9_8_clicked)
		self.b9_9.clicked.connect(self.b9_9_clicked)
		
		#self.bRestart.clicked.connect(self.bRestart_clicked)
		self.lplayer.setText("RED's Turn!")
		self.cross_pixmap = QtGui.QPixmap("/media/karan/3666D8C766D888CF/study/Python/super TicTacToe/cross.png")
		self.circle_pixmap = QtGui.QPixmap("/media/karan/3666D8C766D888CF/study/Python/super TicTacToe/circle.png")
		
	def b1_1_clicked(self):
		global player_x
		global player_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b1_1.setEnabled(False)
		if turn == 'x':
			self.b1_1.setStyleSheet("background-color: tomato")
			player_x[1] = 1;
			turn = 'o'
			self.lplayer.setText(" GREEN's Turn !")
			if player_x[2] == player_x[3] == 1 or player_x[4] == player_x[7] == 1 or player_x[5] == player_x[9] == 1:
		
				self.disable_b1()
				self.lImage_1.setPixmap(self.cross_pixmap)
				final_player_x[1] = 1
				if final_player_x[2] == final_player_x[3] == 1 or final_player_x[4] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[9] == 1:
					
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			self.b1_1.setStyleSheet("background-color: palegreen")
			player_o[1] = 1;
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_o[2] == player_o[3] == 1 or player_o[4] == player_o[7] == 1 or player_o[5] == player_o[9] == 1:
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.circle_pixmap)
				final_player_o[1] = 1
				if final_player_o[2] == final_player_o[3] == 1 or final_player_o[4] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[9] == 1:			
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b1_2_clicked(self):
		global player_x
		global player_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b1_2.setEnabled(False)
		if turn == 'x':
			self.b1_2.setStyleSheet("background-color: tomato")
			player_x[2] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_x[1] == player_x[3] == 1 or player_x[5] == player_x[8] == 1 :
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.cross_pixmap)
				final_player_x[1] = 1
				if final_player_x[2] == final_player_x[3] == 1 or final_player_x[4] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[9] == 1:
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
				
		else :
			player_o[2] = 1;
			self.b1_2.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_o[1] == player_o[3] == 1 or player_o[5] == player_o[8] == 1 :
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.circle_pixmap)
				final_player_o[1] = 1
				if final_player_o[2] == final_player_o[3] == 1 or final_player_o[4] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
					
				
				
	def b1_3_clicked(self):
		global player_x
		global player_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b1_3.setEnabled(False)
		if turn == 'x':
			self.b1_3.setStyleSheet("background-color: tomato")
			player_x[3] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_x[2] == player_x[1] == 1 or player_x[5] == player_x[7] == 1 or player_x[6] == player_x[9] == 1:
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.cross_pixmap)
				final_player_x[1] = 1
				if final_player_x[2] == final_player_x[3] == 1 or final_player_x[4] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_o[3] = 1;
			self.b1_3.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_o[2] == player_o[1] == 1 or player_o[5] == player_o[7] == 1 or player_o[6] == player_o[9] == 1:
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.circle_pixmap)
				final_player_o[1] = 1
				if final_player_o[2] == final_player_o[3] == 1 or final_player_o[4] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b1_4_clicked(self):
		global player_x
		global player_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b1_4.setEnabled(False)
		if turn == 'x':
			self.b1_4.setStyleSheet("background-color: tomato")
			player_x[4] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_x[1] == player_x[7] == 1 or player_x[5] == player_x[6] == 1 :
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.cross_pixmap)
				final_player_x[1] = 1
				if final_player_x[2] == final_player_x[3] == 1 or final_player_x[4] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_o[4] = 1;
			self.b1_4.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_o[1] == player_o[7] == 1 or player_o[5] == player_o[6] == 1 :
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.circle_pixmap)
				final_player_o[1] = 1
				if final_player_o[2] == final_player_o[3] == 1 or final_player_o[4] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
					self.disable_all()
				
	
	def b1_5_clicked(self):
		global player_x
		global player_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b1_5.setEnabled(False)
		if turn == 'x':
			self.b1_5.setStyleSheet("background-color: tomato")
			player_x[5] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_x[2] == player_x[8] == 1 or player_x[4] == player_x[6] == 1 or player_x[1] == player_x[9] == 1:
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.cross_pixmap)
				final_player_x[1] = 1
				if final_player_x[2] == final_player_x[3] == 1 or final_player_x[4] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_o[5] = 1;
			self.b1_5.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_o[2] == player_o[8] == 1 or player_o[4] == player_o[6] == 1 or player_o[1] == player_o[9] == 1:
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.circle_pixmap)
				final_player_o[1] = 1
				if final_player_o[2] == final_player_o[3] == 1 or final_player_o[4] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b1_6_clicked(self):
		global player_x
		global player_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b1_6.setEnabled(False)
		if turn == 'x':
			self.b1_6.setStyleSheet("background-color: tomato")
			player_x[6] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_x[4] == player_x[5] == 1 or player_x[3] == player_x[9] == 1 :
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.cross_pixmap)
				final_player_x[1] = 1
				if final_player_x[2] == final_player_x[3] == 1 or final_player_x[4] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_o[6] = 1;
			self.b1_6.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_o[4] == player_o[5] == 1 or player_o[3] == player_o[9] == 1:
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.circle_pixmap)
				final_player_o[1] = 1
				if final_player_o[2] == final_player_o[3] == 1 or final_player_o[4] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
					
	
	def b1_7_clicked(self):
		global player_x
		global player_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b1_7.setEnabled(False)
		if turn == 'x':
			self.b1_7.setStyleSheet("background-color: tomato")
			player_x[7] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_x[1] == player_x[4] == 1 or player_x[3] == player_x[5] == 1 or player_x[8] == player_x[9] == 1:
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.cross_pixmap)
				final_player_x[1] = 1
				if final_player_x[2] == final_player_x[3] == 1 or final_player_x[4] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else:	
			player_o[7] = 1;
			self.b1_7.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_o[1] == player_o[4] == 1 or player_o[3] == player_o[5] == 1 or player_o[8] == player_o[9] == 1:
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.circle_pixmap)
				final_player_o[1] = 1
				if final_player_o[2] == final_player_o[3] == 1 or final_player_o[4] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b1_8_clicked(self):
		global player_x
		global player_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b1_8.setEnabled(False)
		if turn == 'x':
			self.b1_8.setStyleSheet("background-color: tomato")
			player_x[8] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_x[2] == player_x[5] == 1 or player_x[7] == player_x[9] == 1:
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.cross_pixmap)
				final_player_x[1] = 1
				if final_player_x[2] == final_player_x[3] == 1 or final_player_x[4] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_o[8] = 1;
			self.b1_8.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_o[2] == player_o[5] == 1 or player_o[7] == player_o[9] == 1:
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.circle_pixmap)
				final_player_o[1] = 1
				if final_player_o[2] == final_player_o[3] == 1 or final_player_o[4] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b1_9_clicked(self):
		global player_x
		global player_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b1_9.setEnabled(False)
		if turn == 'x':
			self.b1_9.setStyleSheet("background-color: tomato")
			player_x[9] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_x[1] == player_x[5] == 1 or player_x[3] == player_x[6] == 1 or player_x[7] == player_x[8] == 1:
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.cross_pixmap)
				final_player_x[1] = 1
				if final_player_x[2] == final_player_x[3] == 1 or final_player_x[4] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_o[9] = 1;
			self.b1_9.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_o[1] == player_o[5] == 1 or player_o[3] == player_o[6] == 1 or player_o[7] == player_o[8] == 1:
				
				self.disable_b1()
				self.lImage_1.setPixmap(self.circle_pixmap)
				final_player_o[1] = 1
				if final_player_o[2] == final_player_o[3] == 1 or final_player_o[4] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
		
	def b2_1_clicked(self):
		global player_b2_x
		global player_b2_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b2_1.setEnabled(False)
		
		if turn == 'x':
			self.b2_1.setStyleSheet("background-color: tomato")
			player_b2_x[1] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b2_x[2] == player_b2_x[3] == 1 or player_b2_x[4] == player_b2_x[7] == 1 or player_b2_x[5] == player_b2_x[9] == 1:
		
				self.disable_b2()
				self.lImage_2.setPixmap(self.cross_pixmap)
				final_player_x[2] = 1
				if final_player_x[1] == final_player_x[3] == 1 or final_player_x[5] == final_player_x[8] == 1 :	
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			self.b2_1.setStyleSheet("background-color: palegreen")
			player_b2_o[1] = 1;
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b2_o[2] == player_b2_o[3] == 1 or player_b2_o[4] == player_b2_o[7] == 1 or player_b2_o[5] == player_b2_o[9] == 1:
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.circle_pixmap)
				final_player_o[2] = 1
				if final_player_o[1] == final_player_o[3] == 1 or final_player_o[5] == final_player_o[8] == 1 :			
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
		
				
	def b2_2_clicked(self):
		global player_b2_x
		global player_b2_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b2_2.setEnabled(False)
		if turn == 'x':
			self.b2_2.setStyleSheet("background-color: tomato")
			player_b2_x[2] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b2_x[1] == player_b2_x[3] == 1 or player_b2_x[5] == player_b2_x[8] == 1 :
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.cross_pixmap)
				final_player_x[2] = 1
				if final_player_x[1] == final_player_x[3] == 1 or final_player_x[5] == final_player_x[8] == 1 :
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
				
		else :
			player_b2_o[2] = 1;
			self.b2_2.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b2_o[1] == player_b2_o[3] == 1 or player_b2_o[5] == player_b2_o[8] == 1 :
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.circle_pixmap)
				final_player_o[2] = 1
				if final_player_o[1] == final_player_o[3] == 1 or final_player_o[5] == final_player_o[8] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b2_3_clicked(self):
		global player_b2_x
		global player_b2_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b2_3.setEnabled(False)
		if turn == 'x':
			self.b2_3.setStyleSheet("background-color: tomato")
			player_b2_x[3] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b2_x[2] == player_b2_x[1] == 1 or player_b2_x[5] == player_b2_x[7] == 1 or player_b2_x[6] == player_b2_x[9] == 1:
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.cross_pixmap)
				final_player_x[2] = 1
				if final_player_x[1] == final_player_x[3] == 1 or final_player_x[5] == final_player_x[8] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b2_o[3] = 1;
			self.b2_3.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b2_o[2] == player_b2_o[1] == 1 or player_b2_o[5] == player_b2_o[7] == 1 or player_b2_o[6] == player_b2_o[9] == 1:
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.circle_pixmap)
				final_player_o[2] = 1
				if final_player_o[1] == final_player_o[3] == 1 or final_player_o[5] == final_player_o[8] == 1 :			
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b2_4_clicked(self):
		global player_b2_x
		global player_b2_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b2_4.setEnabled(False)
		if turn == 'x':
			self.b2_4.setStyleSheet("background-color: tomato")
			player_b2_x[4] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b2_x[1] == player_b2_x[7] == 1 or player_b2_x[5] == player_b2_x[6] == 1 :
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.cross_pixmap)
				final_player_x[2] = 1
				if final_player_x[1] == final_player_x[3] == 1 or final_player_x[5] == final_player_x[8] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b2_o[4] = 1;
			self.b2_4.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b2_o[1] == player_b2_o[7] == 1 or player_b2_o[5] == player_b2_o[6] == 1 :
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.cirlce_pixmap)
				final_player_o[2] = 1
				if final_player_o[1] == final_player_o[3] == 1 or final_player_o[5] == final_player_o[8] == 1 :			
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b2_5_clicked(self):
		global player_b2_x
		global player_b2_o
		global final_player_x
		global final_player_o
		global turn
		
		self.b2_5.setEnabled(False)
		if turn == 'x':
			self.b2_5.setStyleSheet("background-color: tomato")
			player_b2_x[5] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b2_x[2] == player_b2_x[8] == 1 or player_b2_x[4] == player_b2_x[6] == 1 or player_b2_x[1] == player_b2_x[9] == 1:
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.cross_pixmap)
				final_player_x[2] = 1
				if final_player_x[1] == final_player_x[3] == 1 or final_player_x[5] == final_player_x[8] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b2_o[5] = 1;
			self.b2_5.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b2_o[2] == player_b2_o[8] == 1 or player_b2_o[4] == player_b2_o[6] == 1 or player_b2_o[1] == player_b2_o[9] == 1:
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.circle_pixmap)
				final_player_o[2] = 1
				if final_player_o[1] == final_player_o[3] == 1 or final_player_o[5] == final_player_o[8] == 1 :			
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b2_6_clicked(self):
		global player_b2_x
		global player_b2_o
		global final_player_x
		global final_player_o
		global turn
		self.b2_6.setEnabled(False)
		if turn == 'x':
			self.b2_6.setStyleSheet("background-color: tomato")
			player_b2_x[6] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b2_x[4] == player_b2_x[5] == 1 or player_b2_x[3] == player_b2_x[9] == 1 :
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.cross_pixmap)
				final_player_x[2] = 1
				if final_player_x[1] == final_player_x[3] == 1 or final_player_x[5] == final_player_x[8] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b2_o[6] = 1;
			self.b2_6.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b2_o[4] == player_b2_o[5] == 1 or player_b2_o[3] == player_b2_o[9] == 1:
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.circle_pixmap)
				final_player_o[2] = 1
				if final_player_o[1] == final_player_o[3] == 1 or final_player_o[5] == final_player_o[8] == 1 :			
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
					
	
	def b2_7_clicked(self):
		global player_b2_x
		global player_b2_o
		global final_player_x
		global final_player_o
		global turn
		self.b2_7.setEnabled(False)
		if turn == 'x':
			self.b2_7.setStyleSheet("background-color: tomato")
			player_b2_x[7] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b2_x[1] == player_b2_x[4] == 1 or player_b2_x[3] == player_b2_x[5] == 1 or player_b2_x[8] == player_b2_x[9] == 1:
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.cross_pixmap)
				final_player_x[2] = 1
				if final_player_x[1] == final_player_x[3] == 1 or final_player_x[5] == final_player_x[8] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else:	
			player_b2_o[7] = 1;
			self.b2_7.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b2_o[1] == player_b2_o[4] == 1 or player_b2_o[3] == player_b2_o[5] == 1 or player_b2_o[8] == player_b2_o[9] == 1:
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.circle_pixmap)
				final_player_o[2] = 1
				if final_player_o[1] == final_player_o[3] == 1 or final_player_o[5] == final_player_o[8] == 1 :			
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b2_8_clicked(self):
		global player_b2_x
		global player_b2_o
		global final_player_x
		global final_player_o
		global turn
		self.b2_8.setEnabled(False)
		if turn == 'x':
			self.b2_8.setStyleSheet("background-color: tomato")
			player_b2_x[8] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b2_x[2] == player_b2_x[5] == 1 or player_b2_x[7] == player_b2_x[9] == 1:
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.cross_pixmap)
				final_player_x[2] = 1
				if final_player_x[1] == final_player_x[3] == 1 or final_player_x[5] == final_player_x[8] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b2_o[8] = 1;
			self.b2_8.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b2_o[2] == player_b2_o[5] == 1 or player_b2_o[7] == player_b2_o[9] == 1:
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.circle_pixmap)
				final_player_o[2] = 1
				if final_player_o[1] == final_player_o[3] == 1 or final_player_o[5] == final_player_o[8] == 1 :			
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
		
				
	def b2_9_clicked(self):
		global player_b2_x
		global player_b2_o
		global final_player_x
		global final_player_o
		global turn
		self.b2_9.setEnabled(False)
		if turn == 'x':
			self.b2_9.setStyleSheet("background-color: tomato")
			player_b2_x[9] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b2_x[1] == player_b2_x[5] == 1 or player_b2_x[3] == player_b2_x[6] == 1 or player_b2_x[7] == player_b2_x[8] == 1:
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.cross_pixmap)
				final_player_x[2] = 1
				if final_player_x[1] == final_player_x[3] == 1 or final_player_x[5] == final_player_x[8] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b2_o[9] = 1;
			self.b2_9.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b2_o[1] == player_b2_o[5] == 1 or player_b2_o[3] == player_b2_o[6] == 1 or player_b2_o[7] == player_b2_o[8] == 1:
				
				self.disable_b2()
				self.lImage_2.setPixmap(self.circle_pixmap)
				final_player_o[2] = 1
				if final_player_o[1] == final_player_o[3] == 1 or final_player_o[5] == final_player_o[8] == 1 :			
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
	
				
	def b3_1_clicked(self):
		global player_b3_x
		global player_b3_o
		global final_player_x
		global final_player_o
		global turn
		self.b3_1.setEnabled(False)
		if turn == 'x':
			self.b3_1.setStyleSheet("background-color: tomato")
			player_b3_x[1] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b3_x[2] == player_b3_x[3] == 1 or player_b3_x[4] == player_b3_x[7] == 1 or player_b3_x[5] == player_b3_x[9] == 1:
		
				self.disable_b3()
				self.lImage_3.setPixmap(self.cross_pixmap)
				final_player_x[3] = 1
				if final_player_x[2] == final_player_x[1] == 1 or final_player_x[5] == final_player_x[7] == 1 or final_player_x[6] == final_player_x[9] == 1:
					
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			self.b3_1.setStyleSheet("background-color: palegreen")
			player_b3_o[1] = 1;
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b3_o[2] == player_b3_o[3] == 1 or player_b3_o[4] == player_b3_o[7] == 1 or player_b3_o[5] == player_b3_o[9] == 1:
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.circle_pixmap)
				final_player_o[3] = 1
				if final_player_o[2] == final_player_o[1] == 1 or final_player_o[5] == final_player_o[7] == 1 or final_player_o[6] == final_player_o[9] == 1:
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b3_2_clicked(self):
		global player_b3_x
		global player_b3_o
		global final_player_x
		global final_player_o
		global turn
		self.b3_2.setEnabled(False)
		if turn == 'x':
			self.b3_2.setStyleSheet("background-color: tomato")
			player_b3_x[2] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b3_x[1] == player_b3_x[3] == 1 or player_b3_x[5] == player_b3_x[8] == 1 :
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.cross_pixmap)
				final_player_x[3] = 1
				if final_player_x[2] == final_player_x[1] == 1 or final_player_x[5] == final_player_x[7] == 1 or final_player_x[6] == final_player_x[9] == 1:
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
				
		else :
			player_b3_o[2] = 1;
			self.b3_2.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b3_o[1] == player_b3_o[3] == 1 or player_b3_o[5] == player_b3_o[8] == 1 :
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.circle_pixmap)
				final_player_o[3] = 1
				if final_player_o[2] == final_player_o[1] == 1 or final_player_o[5] == final_player_o[7] == 1 or final_player_o[6] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b3_3_clicked(self):
		global player_b3_x
		global player_b3_o
		global final_player_x
		global final_player_o
		global turn
		self.b3_3.setEnabled(False)
		if turn == 'x':
			self.b3_3.setStyleSheet("background-color: tomato")
			player_b3_x[3] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b3_x[2] == player_b3_x[1] == 1 or player_b3_x[5] == player_b3_x[7] == 1 or player_b3_x[6] == player_b3_x[9] == 1:
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.cross_pixmap)
				final_player_x[3] = 1
				if final_player_x[2] == final_player_x[1] == 1 or final_player_x[5] == final_player_x[7] == 1 or final_player_x[6] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b3_o[3] = 1;
			self.b3_3.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b3_o[2] == player_b3_o[1] == 1 or player_b3_o[5] == player_b3_o[7] == 1 or player_b3_o[6] == player_b3_o[9] == 1:
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.circle_pixmap)
				final_player_o[3] = 1
				if final_player_o[2] == final_player_o[1] == 1 or final_player_o[5] == final_player_o[7] == 1 or final_player_o[6] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b3_4_clicked(self):
		global player_b3_x
		global player_b3_o
		global final_player_x
		global final_player_o
		global turn
		self.b3_4.setEnabled(False)
		if turn == 'x':
			self.b3_4.setStyleSheet("background-color: tomato")
			player_b3_x[4] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b3_x[1] == player_b3_x[7] == 1 or player_b3_x[5] == player_b3_x[6] == 1 :
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.cross_pixmap)
				final_player_x[3] = 1
				if final_player_x[2] == final_player_x[1] == 1 or final_player_x[5] == final_player_x[7] == 1 or final_player_x[6] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b3_o[4] = 1;
			self.b3_4.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b3_o[1] == player_b3_o[7] == 1 or player_b3_o[5] == player_b3_o[6] == 1 :
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.circle_pixmap)
				final_player_o[3] = 1
				if final_player_o[2] == final_player_o[1] == 1 or final_player_o[5] == final_player_o[7] == 1 or final_player_o[6] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b3_5_clicked(self):
		global player_b3_x
		global player_b3_o
		global final_player_x
		global final_player_o
		global turn
		self.b3_5.setEnabled(False)
		if turn == 'x':
			self.b3_5.setStyleSheet("background-color: tomato")
			player_b3_x[5] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b3_x[2] == player_b3_x[8] == 1 or player_b3_x[4] == player_b3_x[6] == 1 or player_b3_x[1] == player_b3_x[9] == 1:
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.cross_pixmap)
				final_player_x[3] = 1
				if final_player_x[2] == final_player_x[1] == 1 or final_player_x[5] == final_player_x[7] == 1 or final_player_x[6] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b3_o[5] = 1;
			self.b3_5.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b3_o[2] == player_b3_o[8] == 1 or player_b3_o[4] == player_b3_o[6] == 1 or player_b3_o[1] == player_b3_o[9] == 1:
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.circle_pixmap)
				final_player_o[3] = 1
				if final_player_o[2] == final_player_o[1] == 1 or final_player_o[5] == final_player_o[7] == 1 or final_player_o[6] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b3_6_clicked(self):
		global player_b3_x
		global player_b3_o
		global final_player_x
		global final_player_o
		global turn
		self.b3_6.setEnabled(False)
		if turn == 'x':
			self.b3_6.setStyleSheet("background-color: tomato")
			player_b3_x[6] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b3_x[4] == player_b3_x[5] == 1 or player_b3_x[3] == player_b3_x[9] == 1 :
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.cross_pixmap)
				final_player_x[3] = 1
				if final_player_x[2] == final_player_x[1] == 1 or final_player_x[5] == final_player_x[7] == 1 or final_player_x[6] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b3_o[6] = 1;
			self.b3_6.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b3_o[4] == player_b3_o[5] == 1 or player_b3_o[3] == player_b3_o[9] == 1:
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.circle_pixmap)
				final_player_o[3] = 1
				if final_player_o[2] == final_player_o[1] == 1 or final_player_o[5] == final_player_o[7] == 1 or final_player_o[6] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
					
	
	def b3_7_clicked(self):
		global player_b3_x
		global player_b3_o
		global final_player_x
		global final_player_o
		global turn
		self.b3_7.setEnabled(False)
		if turn == 'x':
			self.b3_7.setStyleSheet("background-color: tomato")
			player_b3_x[7] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b3_x[1] == player_b3_x[4] == 1 or player_b3_x[3] == player_b3_x[5] == 1 or player_b3_x[8] == player_b3_x[9] == 1:
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.cross_pixmap)
				final_player_x[3] = 1
				if final_player_x[2] == final_player_x[1] == 1 or final_player_x[5] == final_player_x[7] == 1 or final_player_x[6] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else:	
			player_b3_o[7] = 1;
			self.b3_7.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b3_o[1] == player_b3_o[4] == 1 or player_b3_o[3] == player_b3_o[5] == 1 or player_b3_o[8] == player_b3_o[9] == 1:
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.circle_pixmap)
				final_player_o[3] = 1
				if final_player_o[2] == final_player_o[1] == 1 or final_player_o[5] == final_player_o[7] == 1 or final_player_o[6] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b3_8_clicked(self):
		global player_b3_x
		global player_b3_o
		global final_player_x
		global final_player_o
		global turn
		self.b3_8.setEnabled(False)
		if turn == 'x':
			self.b3_8.setStyleSheet("background-color: tomato")
			player_b3_x[8] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b3_x[2] == player_b3_x[5] == 1 or player_b3_x[7] == player_b3_x[9] == 1:
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.cross_pixmap)
				final_player_x[8] = 1
				if final_player_x[2] == final_player_x[1] == 1 or final_player_x[5] == final_player_x[7] == 1 or final_player_x[6] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b3_o[8] = 1;
			self.b3_8.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b3_o[2] == player_b3_o[5] == 1 or player_b3_o[7] == player_b3_o[9] == 1:
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.circle_pixmap)
				final_player_o[3] = 1
				if final_player_o[2] == final_player_o[1] == 1 or final_player_o[5] == final_player_o[7] == 1 or final_player_o[6] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b3_9_clicked(self):
		global player_b3_x
		global player_b3_o
		global final_player_x
		global final_player_o
		global turn
		self.b3_9.setEnabled(False)
		if turn == 'x':
			self.b3_9.setStyleSheet("background-color: tomato")
			player_b3_x[9] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b3_x[1] == player_b3_x[5] == 1 or player_b3_x[3] == player_b3_x[6] == 1 or player_b3_x[7] == player_b3_x[8] == 1:
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.cross_pixmap)
				final_player_x[3] = 1
				if final_player_x[2] == final_player_x[1] == 1 or final_player_x[5] == final_player_x[7] == 1 or final_player_x[6] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b3_o[9] = 1;
			self.b3_9.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b3_o[1] == player_b3_o[5] == 1 or player_b3_o[3] == player_b3_o[6] == 1 or player_b3_o[7] == player_b3_o[8] == 1:
				
				self.disable_b3()
				self.lImage_3.setPixmap(self.circle_pixmap)
				final_player_o[9] = 1
				if final_player_o[2] == final_player_o[1] == 1 or final_player_o[5] == final_player_o[7] == 1 or final_player_o[6] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()

	
	def b4_1_clicked(self):
		global player_b4_x
		global player_b4_o
		global final_player_x
		global final_player_o
		global turn
		self.b4_1.setEnabled(False)
		if turn == 'x':
			self.b4_1.setStyleSheet("background-color: tomato")
			player_b4_x[1] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b4_x[2] == player_b4_x[3] == 1 or player_b4_x[4] == player_b4_x[7] == 1 or player_b4_x[5] == player_b4_x[9] == 1:
		
				self.disable_b4()
				self.lImage_4.setPixmap(self.cross_pixmap)
				final_player_x[4] = 1
				if final_player_x[1] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[6] == 1 :
					
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			self.b4_1.setStyleSheet("background-color: palegreen")
			player_b4_o[1] = 1;
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b4_o[2] == player_b4_o[3] == 1 or player_b4_o[4] == player_b4_o[7] == 1 or player_b4_o[5] == player_b4_o[9] == 1:
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.circle_pixmap)
				final_player_o[4] = 1
				if final_player_o[1] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[6] == 1 :
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b4_2_clicked(self):
		global player_b4_x
		global player_b4_o
		global final_player_x
		global final_player_o
		global turn
		self.b4_2.setEnabled(False)
		if turn == 'x':
			self.b4_2.setStyleSheet("background-color: tomato")
			player_b4_x[2] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b4_x[1] == player_b4_x[3] == 1 or player_b4_x[5] == player_b4_x[8] == 1 :
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.cross_pixmap)
				final_player_x[4] = 1
				if final_player_x[1] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[6] == 1 :
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
				
		else :
			player_b4_o[2] = 1;
			self.b4_2.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b4_o[1] == player_b4_o[3] == 1 or player_b4_o[5] == player_b4_o[8] == 1 :
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.circle_pixmap)
				final_player_o[4] = 1
				if final_player_o[1] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b4_3_clicked(self):
		global player_b4_x
		global player_b4_o
		global final_player_x
		global final_player_o
		global turn
		self.b4_3.setEnabled(False)
		if turn == 'x':
			self.b4_3.setStyleSheet("background-color: tomato")
			player_b4_x[3] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b4_x[2] == player_b4_x[1] == 1 or player_b4_x[5] == player_b4_x[7] == 1 or player_b4_x[6] == player_b4_x[9] == 1:
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.cross_pixmap)
				final_player_x[4] = 1
				if final_player_x[1] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b4_o[3] = 1;
			self.b4_3.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b4_o[2] == player_b4_o[1] == 1 or player_b4_o[5] == player_b4_o[7] == 1 or player_b4_o[6] == player_b4_o[9] == 1:
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.circle_pixmap)
				final_player_o[4] = 1
				if final_player_o[1] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b4_4_clicked(self):
		global player_b4_x
		global player_b4_o
		global final_player_x
		global final_player_o
		global turn
		self.b4_4.setEnabled(False)
		if turn == 'x':
			self.b4_4.setStyleSheet("background-color: tomato")
			player_b4_x[4] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b4_x[1] == player_b4_x[7] == 1 or player_b4_x[5] == player_b4_x[6] == 1 :
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.cross_pixmap)
				final_player_x[4] = 1
				if final_player_x[1] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b4_o[4] = 1;
			self.b4_4.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b4_o[1] == player_b4_o[7] == 1 or player_b4_o[5] == player_b4_o[6] == 1 :
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.circle_pixmap)
				final_player_o[4] = 1
				if final_player_o[1] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b4_5_clicked(self):
		global player_b4_x
		global player_b4_o
		global final_player_x
		global final_player_o
		global turn
		self.b4_5.setEnabled(False)
		if turn == 'x':
			self.b4_5.setStyleSheet("background-color: tomato")
			player_b4_x[5] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b4_x[2] == player_b4_x[8] == 1 or player_b4_x[4] == player_b4_x[6] == 1 or player_b4_x[1] == player_b4_x[9] == 1:
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.cross_pixmap)
				final_player_x[4] = 1
				if final_player_x[1] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b4_o[5] = 1;
			self.b4_5.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b4_o[2] == player_b4_o[8] == 1 or player_b4_o[4] == player_b4_o[6] == 1 or player_b4_o[1] == player_b4_o[9] == 1:
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.circle_pixmap)
				final_player_o[4] = 1
				if final_player_o[1] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b4_6_clicked(self):
		global player_b4_x
		global player_b4_o
		global final_player_x
		global final_player_o
		global turn
		self.b4_6.setEnabled(False)
		if turn == 'x':
			self.b4_6.setStyleSheet("background-color: tomato")
			player_b4_x[6] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b4_x[4] == player_b4_x[5] == 1 or player_b4_x[3] == player_b4_x[9] == 1 :
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.cross_pixmap)
				final_player_x[4] = 1
				if final_player_x[1] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b4_o[6] = 1;
			self.b4_6.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b4_o[4] == player_b4_o[5] == 1 or player_b4_o[3] == player_b4_o[9] == 1:
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.circle_pixmap)
				final_player_o[4] = 1
				if final_player_o[1] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
					
	
	def b4_7_clicked(self):
		global player_b4_x
		global player_b4_o
		global final_player_x
		global final_player_o
		global turn
		self.b4_7.setEnabled(False)
		if turn == 'x':
			self.b4_7.setStyleSheet("background-color: tomato")
			player_b4_x[7] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b4_x[1] == player_b4_x[4] == 1 or player_b4_x[3] == player_b4_x[5] == 1 or player_b4_x[8] == player_b4_x[9] == 1:
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.cross_pixmap)
				final_player_x[4] = 1
				if final_player_x[1] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else:	
			player_b4_o[7] = 1;
			self.b4_7.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b4_o[1] == player_b4_o[4] == 1 or player_b4_o[3] == player_b4_o[5] == 1 or player_b4_o[8] == player_b4_o[9] == 1:
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.circle_pixmap)
				final_player_o[4] = 1
				if final_player_o[1] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b4_8_clicked(self):
		global player_b4_x
		global player_b4_o
		global final_player_x
		global final_player_o
		global turn
		self.b4_8.setEnabled(False)
		if turn == 'x':
			self.b4_8.setStyleSheet("background-color: tomato")
			player_b4_x[8] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b4_x[2] == player_b4_x[5] == 1 or player_b4_x[7] == player_b4_x[9] == 1:
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.cross_pixmap)
				final_player_x[4] = 1
				if final_player_x[1] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b4_o[8] = 1;
			self.b4_8.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b4_o[2] == player_b4_o[5] == 1 or player_b4_o[7] == player_b4_o[9] == 1:
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.circle_pixmap)
				final_player_o[4] = 1
				if final_player_o[1] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b4_9_clicked(self):
		global player_b4_x
		global player_b4_o
		global final_player_x
		global final_player_o
		global turn
		self.b4_9.setEnabled(False)
		if turn == 'x':
			self.b4_9.setStyleSheet("background-color: tomato")
			player_b4_x[9] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b4_x[1] == player_b4_x[5] == 1 or player_b4_x[3] == player_b4_x[6] == 1 or player_b4_x[7] == player_b4_x[8] == 1:
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.cross_pixmap)
				final_player_x[4] = 1
				if final_player_x[1] == final_player_x[7] == 1 or final_player_x[5] == final_player_x[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b4_o[9] = 1;
			self.b4_9.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b4_o[1] == player_b4_o[5] == 1 or player_b4_o[3] == player_b4_o[6] == 1 or player_b4_o[7] == player_b4_o[8] == 1:
				
				self.disable_b4()
				self.lImage_4.setPixmap(self.circle_pixmap)
				final_player_o[4] = 1
				if final_player_o[1] == final_player_o[7] == 1 or final_player_o[5] == final_player_o[6] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()

	
	def b5_1_clicked(self):
		global player_b5_x
		global player_b5_o
		global final_player_x
		global final_player_o
		global turn
		self.b5_1.setEnabled(False)
		if turn == 'x':
			self.b5_1.setStyleSheet("background-color: tomato")
			player_b5_x[1] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b5_x[2] == player_b5_x[3] == 1 or player_b5_x[4] == player_b5_x[7] == 1 or player_b5_x[5] == player_b5_x[9] == 1:
		
				self.disable_b5()
				self.lImage_5.setPixmap(self.cross_pixmap)
				final_player_x[5] = 1
				if final_player_x[2] == final_player_x[8] == 1 or final_player_x[4] == final_player_x[6] == 1 or final_player_x[1] == final_player_x[9] == 1 :
					
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			self.b5_1.setStyleSheet("background-color: palegreen")
			player_b5_o[1] = 1;
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b5_o[2] == player_b5_o[3] == 1 or player_b5_o[4] == player_b5_o[7] == 1 or player_b5_o[5] == player_b5_o[9] == 1:
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.circle_pixmap)
				final_player_o[5] = 1
				if final_player_o[2] == final_player_o[8] == 1 or final_player_o[4] == final_player_o[6] == 1 or final_player_o[1] == final_player_o[9] == 1:
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b5_2_clicked(self):
		global player_b5_x
		global player_b5_o
		global final_player_x
		global final_player_o
		global turn
		self.b5_2.setEnabled(False)
		if turn == 'x':
			self.b5_2.setStyleSheet("background-color: tomato")
			player_b5_x[2] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b5_x[1] == player_b5_x[3] == 1 or player_b5_x[5] == player_b5_x[8] == 1 :
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.cross_pixmap)
				final_player_x[5] = 1
				if final_player_x[2] == final_player_x[8] == 1 or final_player_x[4] == final_player_x[6] == 1 or final_player_x[1] == final_player_x[9] == 1 :
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
				
		else :
			player_b5_o[2] = 1;
			self.b5_2.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b5_o[1] == player_b5_o[3] == 1 or player_b5_o[5] == player_b5_o[8] == 1 :
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.circle_pixmap)
				final_player_o[5] = 1
				if final_player_o[2] == final_player_o[8] == 1 or final_player_o[4] == final_player_o[6] == 1 or final_player_o[1] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b5_3_clicked(self):
		global player_b5_x
		global player_b5_o
		global final_player_x
		global final_player_o
		global turn
		self.b5_3.setEnabled(False)
		if turn == 'x':
			self.b5_3.setStyleSheet("background-color: tomato")
			player_b5_x[3] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b5_x[2] == player_b5_x[1] == 1 or player_b5_x[5] == player_b5_x[7] == 1 or player_b5_x[6] == player_b5_x[9] == 1:
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.cross_pixmap)
				final_player_x[5] = 1
				if final_player_x[2] == final_player_x[8] == 1 or final_player_x[4] == final_player_x[6] == 1 or final_player_x[1] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b5_o[3] = 1;
			self.b5_3.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b5_o[2] == player_b5_o[1] == 1 or player_b5_o[5] == player_b5_o[7] == 1 or player_b5_o[6] == player_b5_o[9] == 1:
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.circle_pixmap)
				final_player_o[5] = 1
				if final_player_o[2] == final_player_o[8] == 1 or final_player_o[4] == final_player_o[6] == 1 or final_player_o[1] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b5_4_clicked(self):
		global player_b5_x
		global player_b5_o
		global final_player_x
		global final_player_o
		global turn
		self.b5_4.setEnabled(False)
		if turn == 'x':
			self.b5_4.setStyleSheet("background-color: tomato")
			player_b5_x[4] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b5_x[1] == player_b5_x[7] == 1 or player_b5_x[5] == player_b5_x[6] == 1 :
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.cross_pixmap)
				final_player_x[5] = 1
				if final_player_x[2] == final_player_x[8] == 1 or final_player_x[4] == final_player_x[6] == 1 or final_player_x[1] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b5_o[4] = 1;
			self.b5_4.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b5_o[1] == player_b5_o[7] == 1 or player_b5_o[5] == player_b5_o[6] == 1 :
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.circle_pixmap)
				final_player_o[5] = 1
				if final_player_o[2] == final_player_o[8] == 1 or final_player_o[4] == final_player_o[6] == 1 or final_player_o[1] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b5_5_clicked(self):
		global player_b5_x
		global player_b5_o
		global final_player_x
		global final_player_o
		global turn
		self.b5_5.setEnabled(False)
		if turn == 'x':
			self.b5_5.setStyleSheet("background-color: tomato")
			player_b5_x[5] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b5_x[2] == player_b5_x[8] == 1 or player_b5_x[4] == player_b5_x[6] == 1 or player_b5_x[1] == player_b5_x[9] == 1:
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.cross_pixmap)
				final_player_x[5] = 1
				if final_player_x[2] == final_player_x[8] == 1 or final_player_x[4] == final_player_x[6] == 1 or final_player_x[1] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b5_o[5] = 1;
			self.b5_5.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b5_o[2] == player_b5_o[8] == 1 or player_b5_o[4] == player_b5_o[6] == 1 or player_b5_o[1] == player_b5_o[9] == 1:
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.circle_pixmap)
				final_player_o[5] = 1
				if final_player_o[2] == final_player_o[8] == 1 or final_player_o[4] == final_player_o[6] == 1 or final_player_o[1] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b5_6_clicked(self):
		global player_b5_x
		global player_b5_o
		global final_player_x
		global final_player_o
		global turn
		self.b5_6.setEnabled(False)
		if turn == 'x':
			self.b5_6.setStyleSheet("background-color: tomato")
			player_b5_x[6] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b5_x[4] == player_b5_x[5] == 1 or player_b5_x[3] == player_b5_x[9] == 1 :
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.cross_pixmap)
				final_player_x[5] = 1
				if final_player_x[2] == final_player_x[8] == 1 or final_player_x[4] == final_player_x[6] == 1 or final_player_x[1] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b5_o[6] = 1;
			self.b5_6.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b5_o[4] == player_b5_o[5] == 1 or player_b5_o[3] == player_b5_o[9] == 1:
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.circle_pixmap)
				final_player_o[5] = 1
				if final_player_o[2] == final_player_o[8] == 1 or final_player_o[4] == final_player_o[6] == 1 or final_player_o[1] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
					
	
	def b5_7_clicked(self):
		global player_b5_x
		global player_b5_o
		global final_player_x
		global final_player_o
		global turn
		self.b5_7.setEnabled(False)
		if turn == 'x':
			self.b5_7.setStyleSheet("background-color: tomato")
			player_b5_x[7] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b5_x[1] == player_b5_x[4] == 1 or player_b5_x[3] == player_b5_x[5] == 1 or player_b5_x[8] == player_b5_x[9] == 1:
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.cross_pixmap)
				final_player_x[5] = 1
				if final_player_x[2] == final_player_x[8] == 1 or final_player_x[4] == final_player_x[6] == 1 or final_player_x[1] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else:	
			player_b5_o[7] = 1;
			self.b5_7.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b5_o[1] == player_b5_o[4] == 1 or player_b5_o[3] == player_b5_o[5] == 1 or player_b5_o[8] == player_b5_o[9] == 1:
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.circle_pixmap)
				final_player_o[5] = 1
				if final_player_o[2] == final_player_o[8] == 1 or final_player_o[4] == final_player_o[6] == 1 or final_player_o[1] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b5_8_clicked(self):
		global player_b5_x
		global player_b5_o
		global final_player_x
		global final_player_o
		global turn
		self.b5_8.setEnabled(False)
		if turn == 'x':
			self.b5_8.setStyleSheet("background-color: tomato")
			player_b5_x[8] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b5_x[2] == player_b5_x[5] == 1 or player_b5_x[7] == player_b5_x[9] == 1:
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.cross_pixmap)
				final_player_x[5] = 1
				if final_player_x[2] == final_player_x[8] == 1 or final_player_x[4] == final_player_x[6] == 1 or final_player_x[1] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b5_o[8] = 1;
			self.b5_8.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b5_o[2] == player_b5_o[5] == 1 or player_b5_o[7] == player_b5_o[9] == 1:
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.circle_pixmap)
				final_player_o[5] = 1
				if final_player_o[2] == final_player_o[8] == 1 or final_player_o[4] == final_player_o[6] == 1 or final_player_o[1] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b5_9_clicked(self):
		global player_b5_x
		global player_b5_o
		global final_player_x
		global final_player_o
		global turn
		self.b5_9.setEnabled(False)
		if turn == 'x':
			self.b5_9.setStyleSheet("background-color: tomato")
			player_b5_x[9] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b5_x[1] == player_b5_x[5] == 1 or player_b5_x[3] == player_b5_x[6] == 1 or player_b5_x[7] == player_b5_x[8] == 1:
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.cross_pixmap)
				final_player_x[5] = 1
				if final_player_x[2] == final_player_x[8] == 1 or final_player_x[4] == final_player_x[6] == 1 or final_player_x[1] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b5_o[9] = 1;
			self.b5_9.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b5_o[1] == player_b5_o[5] == 1 or player_b5_o[3] == player_b5_o[6] == 1 or player_b5_o[7] == player_b5_o[8] == 1:
				
				self.disable_b5()
				self.lImage_5.setPixmap(self.circle_pixmap)
				final_player_o[5] = 1
				if final_player_o[2] == final_player_o[8] == 1 or final_player_o[4] == final_player_o[6] == 1 or final_player_o[1] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()

	
	def b6_1_clicked(self):
		global player_b6_x
		global player_b6_o
		global final_player_x
		global final_player_o
		global turn
		self.b6_1.setEnabled(False)
		if turn == 'x':
			self.b6_1.setStyleSheet("background-color: tomato")
			player_b6_x[1] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b6_x[2] == player_b6_x[3] == 1 or player_b6_x[4] == player_b6_x[7] == 1 or player_b6_x[5] == player_b6_x[9] == 1:
		
				self.disable_b6()
				self.lImage_6.setPixmap(self.cross_pixmap)
				final_player_x[6] = 1
				if final_player_x[4] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[9] == 1 :					
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			self.b6_1.setStyleSheet("background-color: palegreen")
			player_b6_o[1] = 1;
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b6_o[2] == player_b6_o[3] == 1 or player_b6_o[4] == player_b6_o[7] == 1 or player_b6_o[5] == player_b6_o[9] == 1:
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.circle_pixmap)
				final_player_o[6] = 1
				if final_player_o[4] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b6_2_clicked(self):
		global player_b6_x
		global player_b6_o
		global final_player_x
		global final_player_o
		global turn
		self.b6_2.setEnabled(False)
		if turn == 'x':
			self.b6_2.setStyleSheet("background-color: tomato")
			player_b6_x[2] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b6_x[1] == player_b6_x[3] == 1 or player_b6_x[5] == player_b6_x[8] == 1 :
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.cross_pixmap)
				final_player_x[6] = 1
				if final_player_x[4] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[9] == 1 :
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
				
		else :
			player_b6_o[2] = 1;
			self.b6_2.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b6_o[1] == player_b6_o[3] == 1 or player_b6_o[5] == player_b6_o[8] == 1 :
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.circle_pixmap)
				final_player_o[6] = 1
				if final_player_o[4] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b6_3_clicked(self):
		global player_b6_x
		global player_b6_o
		global final_player_x
		global final_player_o
		global turn
		self.b6_3.setEnabled(False)
		if turn == 'x':
			self.b6_3.setStyleSheet("background-color: tomato")
			player_b6_x[3] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b6_x[2] == player_b6_x[1] == 1 or player_b6_x[5] == player_b6_x[7] == 1 or player_b6_x[6] == player_b6_x[9] == 1:
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.cross_pixmap)
				final_player_x[6] = 1
				if final_player_x[4] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b6_o[3] = 1;
			self.b6_3.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b6_o[2] == player_b6_o[1] == 1 or player_b6_o[5] == player_b6_o[7] == 1 or player_b6_o[6] == player_b6_o[9] == 1:
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.circle_pixmap)
				final_player_o[6] = 1
				if final_player_o[4] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b6_4_clicked(self):
		global player_b6_x
		global player_b6_o
		global final_player_x
		global final_player_o
		global turn
		self.b6_4.setEnabled(False)
		if turn == 'x':
			self.b6_4.setStyleSheet("background-color: tomato")
			player_b6_x[4] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b6_x[1] == player_b6_x[7] == 1 or player_b6_x[5] == player_b6_x[6] == 1 :
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.cross_pixmap)
				final_player_x[6] = 1
				if final_player_x[4] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b6_o[4] = 1;
			self.b6_4.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b6_o[1] == player_b6_o[7] == 1 or player_b6_o[5] == player_b6_o[6] == 1 :
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.circle_pixmap)
				final_player_o[6] = 1
				if final_player_o[4] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b6_5_clicked(self):
		global player_b6_x
		global player_b6_o
		global final_player_x
		global final_player_o
		global turn
		self.b6_5.setEnabled(False)
		if turn == 'x':
			self.b6_5.setStyleSheet("background-color: tomato")
			player_b6_x[5] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b6_x[2] == player_b6_x[8] == 1 or player_b6_x[4] == player_b6_x[6] == 1 or player_b6_x[1] == player_b6_x[9] == 1:
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.cross_pixmap)
				final_player_x[6] = 1
				if final_player_x[4] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b6_o[5] = 1;
			self.b6_5.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b6_o[2] == player_b6_o[8] == 1 or player_b6_o[4] == player_b6_o[6] == 1 or player_b6_o[1] == player_b6_o[9] == 1:
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.circle_pixmap)
				final_player_o[6] = 1
				if final_player_o[4] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b6_6_clicked(self):
		global player_b6_x
		global player_b6_o
		global final_player_x
		global final_player_o
		global turn
		self.b6_6.setEnabled(False)
		if turn == 'x':
			self.b6_6.setStyleSheet("background-color: tomato")
			player_b6_x[6] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b6_x[4] == player_b6_x[5] == 1 or player_b6_x[3] == player_b6_x[9] == 1 :
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.cross_pixmap)
				final_player_x[6] = 1
				if final_player_x[4] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b6_o[6] = 1;
			self.b6_6.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b6_o[4] == player_b6_o[5] == 1 or player_b6_o[3] == player_b6_o[9] == 1:
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.circle_pixmap)
				final_player_o[6] = 1
				if final_player_o[4] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
					
	
	def b6_7_clicked(self):
		global player_b6_x
		global player_b6_o
		global final_player_x
		global final_player_o
		global turn
		self.b6_7.setEnabled(False)
		if turn == 'x':
			self.b6_7.setStyleSheet("background-color: tomato")
			player_b6_x[7] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b6_x[1] == player_b6_x[4] == 1 or player_b6_x[3] == player_b6_x[5] == 1 or player_b6_x[8] == player_b6_x[9] == 1:
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.cross_pixmap)
				final_player_x[6] = 1
				if final_player_x[4] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else:	
			player_b6_o[7] = 1;
			self.b6_7.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b6_o[1] == player_b6_o[4] == 1 or player_b6_o[3] == player_b6_o[5] == 1 or player_b6_o[8] == player_b6_o[9] == 1:
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.circle_pixmap)
				final_player_o[6] = 1
				if final_player_o[4] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b6_8_clicked(self):
		global player_b6_x
		global player_b6_o
		global final_player_x
		global final_player_o
		global turn
		self.b6_8.setEnabled(False)
		if turn == 'x':
			self.b6_8.setStyleSheet("background-color: tomato")
			player_b6_x[8] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b6_x[2] == player_b6_x[5] == 1 or player_b6_x[7] == player_b6_x[9] == 1:
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.cross_pixmap)
				final_player_x[6] = 1
				if final_player_x[4] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b6_o[8] = 1;
			self.b6_8.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b6_o[2] == player_b6_o[5] == 1 or player_b6_o[7] == player_b6_o[9] == 1:
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.circle_pixmap)
				final_player_o[6] = 1
				if final_player_o[4] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b6_9_clicked(self):
		global player_b6_x
		global player_b6_o
		global final_player_x
		global final_player_o
		global turn
		self.b6_9.setEnabled(False)
		if turn == 'x':
			self.b6_9.setStyleSheet("background-color: tomato")
			player_b6_x[9] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b6_x[1] == player_b6_x[5] == 1 or player_b6_x[3] == player_b6_x[6] == 1 or player_b6_x[7] == player_b6_x[8] == 1:
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.cross_pixmap)
				final_player_x[6] = 1
				if final_player_x[4] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[9] == 1 :
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b6_o[9] = 1;
			self.b6_9.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b6_o[1] == player_b6_o[5] == 1 or player_b6_o[3] == player_b6_o[6] == 1 or player_b6_o[7] == player_b6_o[8] == 1:
				
				self.disable_b6()
				self.lImage_6.setPixmap(self.circle_pixmap)
				final_player_o[6] = 1
				if final_player_o[4] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()

	
	def b7_1_clicked(self):
		global player_b7_x
		global player_b7_o
		global final_player_x
		global final_player_o
		global turn
		self.b7_1.setEnabled(False)
		if turn == 'x':
			self.b7_1.setStyleSheet("background-color: tomato")
			player_b7_x[1] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b7_x[2] == player_b7_x[3] == 1 or player_b7_x[4] == player_b7_x[7] == 1 or player_b7_x[5] == player_b7_x[9] == 1:
		
				self.disable_b7()
				self.lImage_7.setPixmap(self.cross_pixmap)
				final_player_x[7] = 1
				if final_player_x[1] == final_player_x[4] == 1 or final_player_x[3] == final_player_x[5] == 1 or final_player_x[8] == final_player_x[9] == 1:
					
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			self.b7_1.setStyleSheet("background-color: palegreen")
			player_b7_o[1] = 1;
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b7_o[2] == player_b7_o[3] == 1 or player_b7_o[4] == player_b7_o[7] == 1 or player_b7_o[5] == player_b7_o[9] == 1:
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.circle_pixmap)
				final_player_o[7] = 1
				if final_player_o[1] == final_player_o[4] == 1 or final_player_o[3] == final_player_o[5] == 1 or final_player_o[8] == final_player_o[9] == 1:		
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b7_2_clicked(self):
		global player_b7_x
		global player_b7_o
		global final_player_x
		global final_player_o
		global turn
		self.b7_2.setEnabled(False)
		if turn == 'x':
			self.b7_2.setStyleSheet("background-color: tomato")
			player_b7_x[2] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b7_x[1] == player_b7_x[3] == 1 or player_b7_x[5] == player_b7_x[8] == 1 :
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.cross_pixmap)
				final_player_x[7] = 1
				if final_player_x[1] == final_player_x[4] == 1 or final_player_x[3] == final_player_x[5] == 1 or final_player_x[8] == final_player_x[9] == 1:
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
				
		else :
			player_b7_o[2] = 1;
			self.b7_2.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b7_o[1] == player_b7_o[3] == 1 or player_b7_o[5] == player_b7_o[8] == 1 :
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.circle_pixmap)
				final_player_o[7] = 1
				if final_player_o[1] == final_player_o[4] == 1 or final_player_o[3] == final_player_o[5] == 1 or final_player_o[8] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b7_3_clicked(self):
		global player_b7_x
		global player_b7_o
		global final_player_x
		global final_player_o
		global turn
		self.b7_3.setEnabled(False)
		if turn == 'x':
			self.b7_3.setStyleSheet("background-color: tomato")
			player_b7_x[3] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b7_x[2] == player_b7_x[1] == 1 or player_b7_x[5] == player_b7_x[7] == 1 or player_b7_x[6] == player_b7_x[9] == 1:
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.cross_pixmap)
				final_player_x[7] = 1
				if final_player_x[1] == final_player_x[4] == 1 or final_player_x[3] == final_player_x[5] == 1 or final_player_x[8] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b7_o[3] = 1;
			self.b7_3.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b7_o[2] == player_b7_o[1] == 1 or player_b7_o[5] == player_b7_o[7] == 1 or player_b7_o[6] == player_b7_o[9] == 1:
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.circle_pixmap)
				final_player_o[7] = 1
				if final_player_o[1] == final_player_o[4] == 1 or final_player_o[3] == final_player_o[5] == 1 or final_player_o[8] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b7_4_clicked(self):
		global player_b7_x
		global player_b7_o
		global final_player_x
		global final_player_o
		global turn
		self.b7_4.setEnabled(False)
		if turn == 'x':
			self.b7_4.setStyleSheet("background-color: tomato")
			player_b7_x[4] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b7_x[1] == player_b7_x[7] == 1 or player_b7_x[5] == player_b7_x[6] == 1 :
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.cross_pixmap)
				final_player_x[7] = 1
				if final_player_x[1] == final_player_x[4] == 1 or final_player_x[3] == final_player_x[5] == 1 or final_player_x[8] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b7_o[4] = 1;
			self.b7_4.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b7_o[1] == player_b7_o[7] == 1 or player_b7_o[5] == player_b7_o[6] == 1 :
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.circle_pixmap)
				final_player_o[7] = 1
				if final_player_o[1] == final_player_o[4] == 1 or final_player_o[3] == final_player_o[5] == 1 or final_player_o[8] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b7_5_clicked(self):
		global player_b7_x
		global player_b7_o
		global final_player_x
		global final_player_o
		global turn
		self.b7_5.setEnabled(False)
		if turn == 'x':
			self.b7_5.setStyleSheet("background-color: tomato")
			player_b7_x[5] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b7_x[2] == player_b7_x[8] == 1 or player_b7_x[4] == player_b7_x[6] == 1 or player_b7_x[1] == player_b7_x[9] == 1:
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.cross_pixmap)
				final_player_x[7] = 1
				if final_player_x[1] == final_player_x[4] == 1 or final_player_x[3] == final_player_x[5] == 1 or final_player_x[8] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b7_o[5] = 1;
			self.b7_5.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b7_o[2] == player_b7_o[8] == 1 or player_b7_o[4] == player_b7_o[6] == 1 or player_b7_o[1] == player_b7_o[9] == 1:
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.circle_pixmap)
				final_player_o[7] = 1
				if final_player_o[1] == final_player_o[4] == 1 or final_player_o[3] == final_player_o[5] == 1 or final_player_o[8] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b7_6_clicked(self):
		global player_b7_x
		global player_b7_o
		global final_player_x
		global final_player_o
		global turn
		self.b7_6.setEnabled(False)
		if turn == 'x':
			self.b7_6.setStyleSheet("background-color: tomato")
			player_b7_x[6] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b7_x[4] == player_b7_x[5] == 1 or player_b7_x[3] == player_b7_x[9] == 1 :
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.cross_pixmap)
				final_player_x[7] = 1
				if final_player_x[1] == final_player_x[4] == 1 or final_player_x[3] == final_player_x[5] == 1 or final_player_x[8] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b7_o[6] = 1;
			self.b7_6.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b7_o[4] == player_b7_o[5] == 1 or player_b7_o[3] == player_b7_o[9] == 1:
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.circle_pixmap)
				final_player_o[7] = 1
				if final_player_o[1] == final_player_o[4] == 1 or final_player_o[3] == final_player_o[5] == 1 or final_player_o[8] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
					
	
	def b7_7_clicked(self):
		global player_b7_x
		global player_b7_o
		global final_player_x
		global final_player_o
		global turn
		self.b7_7.setEnabled(False)
		if turn == 'x':
			self.b7_7.setStyleSheet("background-color: tomato")
			player_b7_x[7] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b7_x[1] == player_b7_x[4] == 1 or player_b7_x[3] == player_b7_x[5] == 1 or player_b7_x[8] == player_b7_x[9] == 1:
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.cross_pixmap)
				final_player_x[7] = 1
				if final_player_x[1] == final_player_x[4] == 1 or final_player_x[3] == final_player_x[5] == 1 or final_player_x[8] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else:	
			player_b7_o[7] = 1;
			self.b7_7.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b7_o[1] == player_b7_o[4] == 1 or player_b7_o[3] == player_b7_o[5] == 1 or player_b7_o[8] == player_b7_o[9] == 1:
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.circle_pixmap)
				final_player_o[7] = 1
				if final_player_o[1] == final_player_o[4] == 1 or final_player_o[3] == final_player_o[5] == 1 or final_player_o[8] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b7_8_clicked(self):
		global player_b7_x
		global player_b7_o
		global final_player_x
		global final_player_o
		global turn
		self.b7_8.setEnabled(False)
		if turn == 'x':
			self.b7_8.setStyleSheet("background-color: tomato")
			player_b7_x[8] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b7_x[2] == player_b7_x[5] == 1 or player_b7_x[7] == player_b7_x[9] == 1:
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.cross_pixmap)
				final_player_x[7] = 1
				if final_player_x[1] == final_player_x[4] == 1 or final_player_x[3] == final_player_x[5] == 1 or final_player_x[8] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b7_o[8] = 1;
			self.b7_8.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b7_o[2] == player_b7_o[5] == 1 or player_b7_o[7] == player_b7_o[9] == 1:
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.circle_pixmap)
				final_player_o[7] = 1
				if final_player_o[1] == final_player_o[4] == 1 or final_player_o[3] == final_player_o[5] == 1 or final_player_o[8] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b7_9_clicked(self):
		global player_b7_x
		global player_b7_o
		global final_player_x
		global final_player_o
		global turn
		self.b7_9.setEnabled(False)
		if turn == 'x':
			self.b7_9.setStyleSheet("background-color: tomato")
			player_b7_x[9] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b7_x[1] == player_b7_x[5] == 1 or player_b7_x[3] == player_b7_x[6] == 1 or player_b7_x[7] == player_b7_x[8] == 1:
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.cross_pixmap)
				final_player_x[7] = 1
				if final_player_x[1] == final_player_x[4] == 1 or final_player_x[3] == final_player_x[5] == 1 or final_player_x[8] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b7_o[9] = 1;
			self.b7_9.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b7_o[1] == player_b7_o[5] == 1 or player_b7_o[3] == player_b7_o[6] == 1 or player_b7_o[7] == player_b7_o[8] == 1:
				
				self.disable_b7()
				self.lImage_7.setPixmap(self.circle_pixmap)
				final_player_o[7] = 1
				if final_player_o[1] == final_player_o[4] == 1 or final_player_o[3] == final_player_o[5] == 1 or final_player_o[8] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()

	
	def b8_1_clicked(self):
		global player_b8_x
		global player_b8_o
		global final_player_x
		global final_player_o
		global turn
		self.b8_1.setEnabled(False)
		if turn == 'x':
			self.b8_1.setStyleSheet("background-color: tomato")
			player_b8_x[1] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b8_x[2] == player_b8_x[3] == 1 or player_b8_x[4] == player_b8_x[7] == 1 or player_b8_x[5] == player_b8_x[9] == 1:
		
				self.disable_b8()
				self.lImage_8.setPixmap(self.cross_pixmap)
				final_player_x[8] = 1
				if final_player_x[2] == final_player_x[5] == 1 or final_player_x[7] == final_player_x[9] == 1:
					
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			self.b8_1.setStyleSheet("background-color: palegreen")
			player_b8_o[1] = 1;
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b8_o[2] == player_b8_o[3] == 1 or player_b8_o[4] == player_b8_o[7] == 1 or player_b8_o[5] == player_b8_o[9] == 1:
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.circle_pixmap)
				final_player_o[8] = 1
				if final_player_o[2] == final_player_o[5] == 1 or final_player_o[7] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b8_2_clicked(self):
		global player_b8_x
		global player_b8_o
		global final_player_x
		global final_player_o
		global turn
		self.b8_2.setEnabled(False)
		if turn == 'x':
			self.b8_2.setStyleSheet("background-color: tomato")
			player_b8_x[2] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b8_x[1] == player_b8_x[3] == 1 or player_b8_x[5] == player_b8_x[8] == 1 :
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.cross_pixmap)
				final_player_x[8] = 1
				if final_player_x[2] == final_player_x[5] == 1 or final_player_x[7] == final_player_x[9] == 1:
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
				
		else :
			player_b8_o[2] = 1;
			self.b8_2.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b8_o[1] == player_b8_o[3] == 1 or player_b8_o[5] == player_b8_o[8] == 1 :
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.circle_pixmap)
				final_player_o[8] = 1
				if final_player_o[2] == final_player_o[5] == 1 or final_player_o[7] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b8_3_clicked(self):
		global player_b8_x
		global player_b8_o
		global final_player_x
		global final_player_o
		global turn
		self.b8_3.setEnabled(False)
		if turn == 'x':
			self.b8_3.setStyleSheet("background-color: tomato")
			player_b8_x[3] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b8_x[2] == player_b8_x[1] == 1 or player_b8_x[5] == player_b8_x[7] == 1 or player_b8_x[6] == player_b8_x[9] == 1:
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.cross_pixmap)
				final_player_x[8] = 1
				if final_player_x[2] == final_player_x[5] == 1 or final_player_x[7] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b8_o[3] = 1;
			self.b8_3.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b8_o[2] == player_b8_o[1] == 1 or player_b8_o[5] == player_b8_o[7] == 1 or player_b8_o[6] == player_b8_o[9] == 1:
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.circle_pixmap)
				final_player_o[8] = 1
				if final_player_o[2] == final_player_o[5] == 1 or final_player_o[7] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b8_4_clicked(self):
		global player_b8_x
		global player_b8_o
		global final_player_x
		global final_player_o
		global turn
		self.b8_4.setEnabled(False)
		if turn == 'x':
			self.b8_4.setStyleSheet("background-color: tomato")
			player_b8_x[4] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b8_x[1] == player_b8_x[7] == 1 or player_b8_x[5] == player_b8_x[6] == 1 :
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.cross_pixmap)
				final_player_x[8] = 1
				if final_player_x[2] == final_player_x[5] == 1 or final_player_x[7] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b8_o[4] = 1;
			self.b8_4.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b8_o[1] == player_b8_o[7] == 1 or player_b8_o[5] == player_b8_o[6] == 1 :
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.circle_pixmap)
				final_player_o[8] = 1
				if final_player_o[2] == final_player_o[5] == 1 or final_player_o[7] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b8_5_clicked(self):
		global player_b8_x
		global player_b8_o
		global final_player_x
		global final_player_o
		global turn
		self.b8_5.setEnabled(False)
		if turn == 'x':
			self.b8_5.setStyleSheet("background-color: tomato")
			player_b8_x[5] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b8_x[2] == player_b8_x[8] == 1 or player_b8_x[4] == player_b8_x[6] == 1 or player_b8_x[1] == player_b8_x[9] == 1:
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.cross_pixmap)
				final_player_x[8] = 1
				if final_player_x[2] == final_player_x[5] == 1 or final_player_x[7] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b8_o[5] = 1;
			self.b8_5.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b8_o[2] == player_b8_o[8] == 1 or player_b8_o[4] == player_b8_o[6] == 1 or player_b8_o[1] == player_b8_o[9] == 1:
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.circle_pixmap)
				final_player_o[8] = 1
				if final_player_o[2] == final_player_o[5] == 1 or final_player_o[7] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b8_6_clicked(self):
		global player_b8_x
		global player_b8_o
		global final_player_x
		global final_player_o
		global turn
		self.b8_6.setEnabled(False)
		if turn == 'x':
			self.b8_6.setStyleSheet("background-color: tomato")
			player_b8_x[6] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b8_x[4] == player_b8_x[5] == 1 or player_b8_x[3] == player_b8_x[9] == 1 :
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.cross_pixmap)
				final_player_x[8] = 1
				if final_player_x[2] == final_player_x[5] == 1 or final_player_x[7] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b8_o[6] = 1;
			self.b8_6.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b8_o[4] == player_b8_o[5] == 1 or player_b8_o[3] == player_b8_o[9] == 1:
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.circle_pixmap)
				final_player_o[8] = 1
				if final_player_o[2] == final_player_o[5] == 1 or final_player_o[7] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
					
	
	def b8_7_clicked(self):
		global player_b8_x
		global player_b8_o
		global final_player_x
		global final_player_o
		global turn
		self.b8_7.setEnabled(False)
		if turn == 'x':
			self.b8_7.setStyleSheet("background-color: tomato")
			player_b8_x[7] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b8_x[1] == player_b8_x[4] == 1 or player_b8_x[3] == player_b8_x[5] == 1 or player_b8_x[8] == player_b8_x[9] == 1:
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.cross_pixmap)
				final_player_x[8] = 1
				if final_player_x[2] == final_player_x[5] == 1 or final_player_x[7] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else:	
			player_b8_o[7] = 1;
			self.b8_7.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b8_o[1] == player_b8_o[4] == 1 or player_b8_o[3] == player_b8_o[5] == 1 or player_b8_o[8] == player_b8_o[9] == 1:
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.circle_pixmap)
				final_player_o[8] = 1
				if final_player_o[2] == final_player_o[5] == 1 or final_player_o[7] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b8_8_clicked(self):
		global player_b8_x
		global player_b8_o
		global final_player_x
		global final_player_o
		global turn
		self.b8_8.setEnabled(False)
		if turn == 'x':
			self.b8_8.setStyleSheet("background-color: tomato")
			player_b8_x[8] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b8_x[2] == player_b8_x[5] == 1 or player_b8_x[7] == player_b8_x[9] == 1:
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.cross_pixmap)
				final_player_x[8] = 1
				if final_player_x[2] == final_player_x[5] == 1 or final_player_x[7] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b8_o[8] = 1;
			self.b8_8.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b8_o[2] == player_b8_o[5] == 1 or player_b8_o[7] == player_b8_o[9] == 1:
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.circle_pixmap)
				final_player_o[8] = 1
				if final_player_o[2] == final_player_o[5] == 1 or final_player_o[7] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b8_9_clicked(self):
		global player_b8_x
		global player_b8_o
		global final_player_x
		global final_player_o
		global turn
		self.b8_9.setEnabled(False)
		if turn == 'x':
			self.b8_9.setStyleSheet("background-color: tomato")
			player_b8_x[9] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b8_x[1] == player_b8_x[5] == 1 or player_b8_x[3] == player_b8_x[6] == 1 or player_b8_x[7] == player_b8_x[8] == 1:
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.cross_pixmap)
				final_player_x[8] = 1
				if final_player_x[2] == final_player_x[5] == 1 or final_player_x[7] == final_player_x[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b8_o[9] = 1;
			self.b8_9.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b8_o[1] == player_b8_o[5] == 1 or player_b8_o[3] == player_b8_o[6] == 1 or player_b8_o[7] == player_b8_o[8] == 1:
				
				self.disable_b8()
				self.lImage_8.setPixmap(self.circle_pixmap)
				final_player_o[8] = 1
				if final_player_o[2] == final_player_o[5] == 1 or final_player_o[7] == final_player_o[9] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()

	
	def b9_1_clicked(self):
		global player_b9_x
		global player_b9_o
		global final_player_x
		global final_player_o
		global turn
		self.b9_1.setEnabled(False)
		if turn == 'x':
			self.b9_1.setStyleSheet("background-color: tomato")
			player_b9_x[1] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b9_x[2] == player_b9_x[3] == 1 or player_b9_x[4] == player_b9_x[7] == 1 or player_b9_x[5] == player_b9_x[9] == 1:
		
				self.disable_b9()
				self.lImage_9.setPixmap(self.cross_pixmap)
				final_player_x[9] = 1
				if final_player_x[1] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[6] == 1 or final_player_x[7] == final_player_x[8] == 1:
					
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			self.b9_1.setStyleSheet("background-color: palegreen")
			player_b9_o[1] = 1;
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b9_o[2] == player_b9_o[3] == 1 or player_b9_o[4] == player_b9_o[7] == 1 or player_b9_o[5] == player_b9_o[9] == 1:
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.circle_pixmap)
				final_player_o[9] = 1
				if final_player_o[1] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[6] == 1 or final_player_o[7] == final_player_o[8] == 1:
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b9_2_clicked(self):
		global player_b9_x
		global player_b9_o
		global final_player_x
		global final_player_o
		global turn
		self.b9_2.setEnabled(False)
		if turn == 'x':
			self.b9_2.setStyleSheet("background-color: tomato")
			player_b9_x[2] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b9_x[1] == player_b9_x[3] == 1 or player_b9_x[5] == player_b9_x[8] == 1 :
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.cross_pixmap)
				final_player_x[9] = 1
				if final_player_x[1] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[6] == 1 or final_player_x[7] == final_player_x[8] == 1:
				
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
				
		else :
			player_b9_o[2] = 1;
			self.b9_2.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b9_o[1] == player_b9_o[3] == 1 or player_b9_o[5] == player_b9_o[8] == 1 :
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.circle_pixmap)
				final_player_o[9] = 1
				if final_player_o[1] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[6] == 1 or final_player_o[7] == final_player_o[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b9_3_clicked(self):
		global player_b9_x
		global player_b9_o
		global final_player_x
		global final_player_o
		global turn
		self.b9_3.setEnabled(False)
		if turn == 'x':
			self.b9_3.setStyleSheet("background-color: tomato")
			player_b9_x[3] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b9_x[2] == player_b9_x[1] == 1 or player_b9_x[5] == player_b9_x[7] == 1 or player_b9_x[6] == player_b9_x[9] == 1:
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.cross_pixmap)
				final_player_x[9] = 1
				if final_player_x[1] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[6] == 1 or final_player_x[7] == final_player_x[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b9_o[3] = 1;
			self.b9_3.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b9_o[2] == player_b9_o[1] == 1 or player_b9_o[5] == player_b9_o[7] == 1 or player_b9_o[6] == player_b9_o[9] == 1:
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.circle_pixmap)
				final_player_o[9] = 1
				if final_player_o[1] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[6] == 1 or final_player_o[7] == final_player_o[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b9_4_clicked(self):
		global player_b9_x
		global player_b9_o
		global final_player_x
		global final_player_o
		global turn
		self.b9_4.setEnabled(False)
		if turn == 'x':
			self.b9_4.setStyleSheet("background-color: tomato")
			player_b9_x[4] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b9_x[1] == player_b9_x[7] == 1 or player_b9_x[5] == player_b9_x[6] == 1 :
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.cross_pixmap)
				final_player_x[9] = 1
				if final_player_x[1] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[6] == 1 or final_player_x[7] == final_player_x[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b9_o[4] = 1;
			self.b9_4.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b9_o[1] == player_b9_o[7] == 1 or player_b9_o[5] == player_b9_o[6] == 1 :
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.circle_pixmap)
				final_player_o[9] = 1
				if final_player_o[1] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[6] == 1 or final_player_o[7] == final_player_o[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b9_5_clicked(self):
		global player_b9_x
		global player_b9_o
		global final_player_x
		global final_player_o
		global turn
		self.b9_5.setEnabled(False)
		if turn == 'x':
			self.b9_5.setStyleSheet("background-color: tomato")
			player_b9_x[5] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b9_x[2] == player_b9_x[8] == 1 or player_b9_x[4] == player_b9_x[6] == 1 or player_b9_x[1] == player_b9_x[9] == 1:
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.cross_pixmap)
				final_player_x[9] = 1
				if final_player_x[1] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[6] == 1 or final_player_x[7] == final_player_x[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b9_o[5] = 1;
			self.b9_5.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b9_o[2] == player_b9_o[8] == 1 or player_b9_o[4] == player_b9_o[6] == 1 or player_b9_o[1] == player_b9_o[9] == 1:
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.circle_pixmap)
				final_player_o[9] = 1
				if final_player_o[1] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[6] == 1 or final_player_o[7] == final_player_o[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	
	def b9_6_clicked(self):
		global player_b9_x
		global player_b9_o
		global final_player_x
		global final_player_o
		global turn
		self.b9_6.setEnabled(False)
		if turn == 'x':
			self.b9_6.setStyleSheet("background-color: tomato")
			player_b9_x[6] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b9_x[4] == player_b9_x[5] == 1 or player_b9_x[3] == player_b9_x[9] == 1 :
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.cross_pixmap)
				final_player_x[9] = 1
				if final_player_x[1] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[6] == 1 or final_player_x[7] == final_player_x[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b9_o[6] = 1;
			self.b9_6.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b9_o[4] == player_b9_o[5] == 1 or player_b9_o[3] == player_b9_o[9] == 1:
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.circle_pixmap)
				final_player_o[9] = 1
				if final_player_o[1] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[6] == 1 or final_player_o[7] == final_player_o[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
					
	
	def b9_7_clicked(self):
		global player_b9_x
		global player_b9_o
		global final_player_x
		global final_player_o
		global turn
		self.b9_7.setEnabled(False)
		if turn == 'x':
			self.b9_7.setStyleSheet("background-color: tomato")
			player_b9_x[7] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b9_x[1] == player_b9_x[4] == 1 or player_b9_x[3] == player_b9_x[5] == 1 or player_b9_x[8] == player_b9_x[9] == 1:
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.cross_pixmap)
				final_player_x[9] = 1
				if final_player_x[1] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[6] == 1 or final_player_x[7] == final_player_x[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else:	
			player_b9_o[7] = 1;
			self.b9_7.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b9_o[1] == player_b9_o[4] == 1 or player_b9_o[3] == player_b9_o[5] == 1 or player_b9_o[8] == player_b9_o[9] == 1:
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.circle_pixmap)
				final_player_o[9] = 1
				if final_player_o[1] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[6] == 1 or final_player_o[7] == final_player_o[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
				
	def b9_8_clicked(self):
		global player_b9_x
		global player_b9_o
		global final_player_x
		global final_player_o
		global turn
		self.b9_8.setEnabled(False)
		if turn == 'x':
			self.b9_8.setStyleSheet("background-color: tomato")
			player_b9_x[8] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b9_x[2] == player_b9_x[5] == 1 or player_b9_x[7] == player_b9_x[9] == 1:
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.cross_pixmap)
				final_player_x[9] = 1
				if final_player_x[1] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[6] == 1 or final_player_x[7] == final_player_x[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b9_o[8] = 1;
			self.b9_8.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b9_o[2] == player_b9_o[5] == 1 or player_b9_o[7] == player_b9_o[9] == 1:
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.circle_pixmap)
				final_player_o[9] = 1
				if final_player_o[1] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[6] == 1 or final_player_o[7] == final_player_o[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()
				
	def b9_9_clicked(self):
		global player_b9_x
		global player_b9_o
		global final_player_x
		global final_player_o
		global turn
		self.b9_9.setEnabled(False)
		if turn == 'x':
			self.b9_9.setStyleSheet("background-color: tomato")
			player_b9_x[9] = 1;
			turn = 'o'
			self.lplayer.setText("GREEN's Turn !")
			if player_b9_x[1] == player_b9_x[5] == 1 or player_b9_x[3] == player_b9_x[6] == 1 or player_b9_x[7] == player_b9_x[8] == 1:
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.cross_pixmap)
				final_player_x[9] = 1
				if final_player_x[1] == final_player_x[5] == 1 or final_player_x[3] == final_player_x[6] == 1 or final_player_x[7] == final_player_x[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: tomato")
					self.disable_all()
		else :
			player_b9_o[9] = 1;
			self.b9_9.setStyleSheet("background-color: palegreen")
			turn = 'x'
			self.lplayer.setText("RED's Turn!")
			if player_b9_o[1] == player_b9_o[5] == 1 or player_b9_o[3] == player_b9_o[6] == 1 or player_b9_o[7] == player_b9_o[8] == 1:
				
				self.disable_b9()
				self.lImage_9.setPixmap(self.circle_pixmap)
				final_player_o[9] = 1
				if final_player_o[1] == final_player_o[5] == 1 or final_player_o[3] == final_player_o[6] == 1 or final_player_o[7] == final_player_o[8] == 1:
					self.lresult.setText("GREEN Player Wins!")
					self.lresult.setStyleSheet("background-color: palegreen")
					self.disable_all()

	
	 	
	def disable_b1(self):
		self.b1_1.setEnabled(False)
		self.b1_2.setEnabled(False)
		self.b1_3.setEnabled(False)
		self.b1_4.setEnabled(False)
		self.b1_5.setEnabled(False)
		self.b1_6.setEnabled(False)
		self.b1_7.setEnabled(False)
		self.b1_8.setEnabled(False)
		self.b1_9.setEnabled(False)
	
	def disable_b2(self):
		self.b2_1.setEnabled(False)
		self.b2_2.setEnabled(False)
		self.b2_3.setEnabled(False)
		self.b2_4.setEnabled(False)
		self.b2_5.setEnabled(False)
		self.b2_6.setEnabled(False)
		self.b2_7.setEnabled(False)
		self.b2_8.setEnabled(False)
		self.b2_9.setEnabled(False)
	
	def disable_b3(self):
		self.b3_1.setEnabled(False)
		self.b3_2.setEnabled(False)
		self.b3_3.setEnabled(False)
		self.b3_4.setEnabled(False)
		self.b3_5.setEnabled(False)
		self.b3_6.setEnabled(False)
		self.b3_7.setEnabled(False)
		self.b3_8.setEnabled(False)
		self.b3_9.setEnabled(False)
	
	def disable_b4(self):
		self.b4_1.setEnabled(False)
		self.b4_2.setEnabled(False)
		self.b4_3.setEnabled(False)
		self.b4_4.setEnabled(False)
		self.b4_5.setEnabled(False)
		self.b4_6.setEnabled(False)
		self.b4_7.setEnabled(False)
		self.b4_8.setEnabled(False)
		self.b4_9.setEnabled(False)
	
	def disable_b5(self):
		self.b5_1.setEnabled(False)
		self.b5_2.setEnabled(False)
		self.b5_3.setEnabled(False)
		self.b5_4.setEnabled(False)
		self.b5_5.setEnabled(False)
		self.b5_6.setEnabled(False)
		self.b5_7.setEnabled(False)
		self.b5_8.setEnabled(False)
		self.b5_9.setEnabled(False)
		
	def disable_b6(self):
		self.b6_1.setEnabled(False)
		self.b6_2.setEnabled(False)
		self.b6_3.setEnabled(False)
		self.b6_4.setEnabled(False)
		self.b6_5.setEnabled(False)
		self.b6_6.setEnabled(False)
		self.b6_7.setEnabled(False)
		self.b6_8.setEnabled(False)
		self.b6_9.setEnabled(False)
		
	def disable_b7(self):
		self.b7_1.setEnabled(False)
		self.b7_2.setEnabled(False)
		self.b7_3.setEnabled(False)
		self.b7_4.setEnabled(False)
		self.b7_5.setEnabled(False)
		self.b7_6.setEnabled(False)
		self.b7_7.setEnabled(False)
		self.b7_8.setEnabled(False)
		self.b7_9.setEnabled(False)		
		
	def disable_b8(self):
		self.b8_1.setEnabled(False)
		self.b8_2.setEnabled(False)
		self.b8_3.setEnabled(False)
		self.b8_4.setEnabled(False)
		self.b8_5.setEnabled(False)
		self.b8_6.setEnabled(False)
		self.b8_7.setEnabled(False)
		self.b8_8.setEnabled(False)
		self.b8_9.setEnabled(False)
		
	def disable_b9(self):
		self.b9_1.setEnabled(False)
		self.b9_2.setEnabled(False)
		self.b9_3.setEnabled(False)
		self.b9_4.setEnabled(False)
		self.b9_5.setEnabled(False)
		self.b9_6.setEnabled(False)
		self.b9_7.setEnabled(False)
		self.b9_8.setEnabled(False)
		self.b9_9.setEnabled(False)	
		
	def disable_all(self):
		self.disable_b1()
		self.disable_b2()
		self.disable_b3()
		self.disable_b4()
		self.disable_b5()
		self.disable_b6()
		self.disable_b7()
		self.disable_b8()
		self.disable_b9()
	
	#def bRestart_clicked(self):
		
		
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.showMaximized()
app.exec_()

