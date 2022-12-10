from kivy.app import App
from kivy.uix.image import Image, AsyncImage
from kivy.core.window import Window

Window.clearcolor=(0,0,0,1)

class my_image(App):
    def build(self):
        img=AsyncImage(source="Apple-iPhone-14-pro-max.jpg",size_hint=(None,None),width=400,height=400,pos_hint={"center_x":0.5,"center_y":0.5})
        return img
my_image().run()