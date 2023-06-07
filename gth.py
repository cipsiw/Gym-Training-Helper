import sys, os
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from pokamain_ui import Ui_MainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.icons_only.hide()
		self.ui.stackedWidget.setCurrentIndex(0)
		self.ui.pushButton.setChecked(True)
		self.ui.search3.clicked.connect(self.searchgroup)
		self.ui.pushButton_3.clicked.connect(self.backtosearch)
		self.ui.pushButton_4.clicked.connect(self.backtosearch)
		self.ui.pushButton_5.clicked.connect(self.backtosearch)
		self.ui.pushButton_6.clicked.connect(self.backtosearch)
		self.ui.pushButton_7.clicked.connect(self.backtosearch)
		self.ui.pushButton_8.clicked.connect(self.backtosearch)
		self.ui.pushButton_10.clicked.connect(self.backtosearch)
		self.ui.unmute.clicked.connect(self.playsound)
		self.ui.mute.clicked.connect(self.mutesound)
		self.ui.volumeup.clicked.connect(self.volumeup)
		self.ui.volumedown.clicked.connect(self.volumedown)
		self.player = QMediaPlayer()




	def on_pushButton_toggled(self):
		self.ui.stackedWidget.setCurrentIndex(0)
	def on_pushButton_2_toggled(self):
		self.ui.stackedWidget.setCurrentIndex(0)
	def on_warmup_toggled(self):
		self.ui.stackedWidget.setCurrentIndex(1)
	def on_warmup2_toggled(self):
		self.ui.stackedWidget.setCurrentIndex(1)
	def on_fullbody1_toggled(self):
		self.ui.stackedWidget.setCurrentIndex(2)
	def on_fullbody2_toggled(self):
		self.ui.stackedWidget.setCurrentIndex(2)
	def on_split1_toggled(self):
		self.ui.stackedWidget.setCurrentIndex(3)
	def on_split2_toggled(self):
		self.ui.stackedWidget.setCurrentIndex(3)
	def on_search1_toggled(self):
		self.ui.stackedWidget.setCurrentIndex(4)
	def on_search2_toggled(self):
		self.ui.stackedWidget.setCurrentIndex(4)

	def searchgroup(self):
		if self.ui.searchinput.text() == "Руки":
			self.ui.stackedWidget.setCurrentIndex(5)
		elif self.ui.searchinput.text() == "Ноги":
			self.ui.stackedWidget.setCurrentIndex(6)
		elif self.ui.searchinput.text() == "Спина":
			self.ui.stackedWidget.setCurrentIndex(7)
		elif self.ui.searchinput.text() == "Плечи":
			self.ui.stackedWidget.setCurrentIndex(8)
		elif self.ui.searchinput.text() == "Грудь":
			self.ui.stackedWidget.setCurrentIndex(9)
		elif self.ui.searchinput.text() == "Трапеции":
			self.ui.stackedWidget.setCurrentIndex(10)
		elif self.ui.searchinput.text() == "Пресс":
			self.ui.stackedWidget.setCurrentIndex(11)
		else:
			msgBox = QMessageBox().warning(window, "Предупреждение", "Введенный текст не соответствует ожидаемому")


	def backtosearch(self):
		self.ui.stackedWidget.setCurrentIndex(4)


	def playsound(self):
		soundt = os.path.join(os.getcwd(), "D:\учеба\Шарашка ВятГУ\PythonProjects\Тренировки на pyqt5\gosling.mp3")
		url = QUrl.fromLocalFile(soundt)
		content = QMediaContent(url)
		self.player.setMedia(content)
		self.player.play()


	def mutesound(self):
		self.player.setMuted(not self.player.isMuted())

	def volumeup(self):
		curvolume = self.player.volume()
		print(curvolume)
		self.player.setVolume(curvolume +5)

	def volumedown(self):
		curvolume = self.player.volume()
		print(curvolume)
		self.player.setVolume(curvolume - 5)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()

	sys.exit(app.exec_())