import pyttsx3
import tkinter as tk

class txt2speech():
	def __init__(self, driverName=None, rate=180, volume=1.00, voice_id=2):
		self.engine = pyttsx3.init(driverName=driverName)
		self.engine.setProperty('rate', 180)
		self.engine.setProperty('volumne', 1.00)
		self.voices = self.engine.getProperty('voices')
		self.engine.setProperty('voice', self.voices[voice_id].id)
		self.token_words = {r' \n': '', r' \r': '', r'elling, general and administrative': r'elling general and administrative'}
		self.txt = ''
		self.root = tk.Tk()
		self.frame = tk.Frame(self.root)
		self.quit_button = tk.Button(self.frame, text='Quit', fg='red', command=self.frame.quit)
		self.say_button = tk.Button(self.frame, text='Say', command=self.speak)

	@property
	def txt(self):
		return self.__txt

	@txt.setter
	def txt(self, new_txt):
		self.__txt = new_txt

	def get_txt(self):
		self.txt = self.root.clipboard_get()

	@property
	def token_words(self):
		return self.__token_words

	@token_words.setter
	def token_words(self, d:{}):
		self.__token_words = d
	
	def add_tokens(self, new_tokens={}):
		if new_tokens:
			for key, value in new_tokens.items():
				self.token_words[key] = value
	
	def clean_txt(self):
		for key, value in self.token_words.items():
			self.txt = self.txt.replace(key, value)

	def speak(self):
		self.get_txt()
		self.engine.say(self.txt)
		self.engine.runAndWait()

	def draw_gui(self):
		self.quit_button.pack(side=tk.LEFT)
		self.say_button.pack(side=tk.LEFT)
		self.frame.pack()
		
	def gui(self):
		self.root.mainloop()

if __name__ == '__main__':
	engine = txt2speech()
	engine.draw_gui()
	engine.gui()