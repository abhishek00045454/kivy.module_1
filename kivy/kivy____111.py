from kivy.app import App
from kivy.uix.label import Label
class Myapp(App):
    def build(self):
        label = Label(text='hello world',font_size="120",bold=True,italic=True,color=(0,0,1,1))
        return label

Myapp().run()