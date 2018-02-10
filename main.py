import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '350')

class mylayout(GridLayout):
	def backspace(self): 
		self.ids.egg.text = self.ids.egg.text[:-1]
	
	def lemon(self):
		s = self.ids.egg.text
		if s:
			if s.find("+") or s.find("-") or s.find("/") or s.find("*") or s.find("1") or s.find("2") or s.find("3") or s.find("4") or s.find("5") or s.find("6") or s.find("7") or s.find("8") or s.find("9") or s.find("0"):
				#self.ids.egg.text = str(eval(s))
				try:
					self.ids.egg.text = str(eval(s))
				except SyntaxError:
					self.ids.egg.text = 'Error!'
			else:
				self.ids.egg.text = 'NO!'		
		else:
			self.ids.egg.text = 'Empty!'

class calculatorApp(App):
	def build(self):
		self.title = 'Calculator'
		return mylayout()

if __name__ == '__main__':
	calculatorApp().run()
