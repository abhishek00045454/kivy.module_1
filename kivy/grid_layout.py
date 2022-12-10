from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class myGridLayoutApp(App):
    def build(self):
        layout=GridLayout(rows=2,spacing=10,padding=100)

        btn_1 =Button(text="button_1")
        btn_2 =Button(text="button_2")
        btn_3 =Button(text="button_3")
        btn_4 =Button(text="button_4")
        layout.add_widget(btn_1)
        layout.add_widget(btn_2)
        layout.add_widget(btn_3)
        layout.add_widget(btn_4)
        return layout
myGridLayoutApp().run()

