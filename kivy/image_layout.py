from kivy.app import App
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import  BoxLayout

class my_image(App):
    def build(self):
        layput=BoxLayout(orientation="vertical")
        img_1=AsyncImage(source="Apple-iPhone-14-pro-max.jpg",size_hint=(None,None),width=300,height=300,pos_hint={"center_x":0.5,"center_y":0.5})
        img_2=AsyncImage(source="google.png",size_hint=(None,None),width=400,height=400,pos_hint={"center_x":0.5,"center_y":0.5})
        layput.add_widget(img_1)
        layput.add_widget(img_2)
        return layput
my_image().run()