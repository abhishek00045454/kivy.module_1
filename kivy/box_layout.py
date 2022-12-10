from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.clearcolor=(1,1,1,1)
Window.size=(800,720)


class my_button_app(App):
    def build(self):
        layout=BoxLayout(orientation="vertical",spacing=10,pos_hint={"center_x":0.5,"center_y":0.5},padding=100)
        btn_1=Button(text="Button_1",size_hint={0.3,0.4},pos_hint={"center_x":0.5,"center_y":0.5},font_size="44sp",color=(0,0,1,1))
        btn_2=Button(text="Button_2",size_hint={0.3,0.4},pos_hint={"center_x":0.5,"center_y":0.5},font_size="44sp",color=(0,1,1,1))
        btn_3=Button(text="Button_3",size_hint={0.3,0.4},pos_hint={"center_x":0.5,"center_y":0.5},font_size="44sp",color=(0,0,1,1))
        btn_4=Button(text="Button_4",size_hint={0.3,0.4},pos_hint={"center_x":0.5,"center_y":0.5},font_size="44sp",color=(0,0,1,1))
        layout.add_widget(btn_1)
        layout.add_widget(btn_2)
        layout.add_widget(btn_3)
        layout.add_widget(btn_4)
        return layout


my_button_app().run()
"""
this is the button layout means is that the define the layout is the help of wrap the items what have you need
that means layout you need insert a four button in one image and what you can do you import layout option modulue
puding-> that shift the button the outside from screen
spacing-> that shift the button the gaping b\w each other
"""
