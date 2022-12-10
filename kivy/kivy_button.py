from kivy.app import App
from kivy.uix.button import Button



class button_app(App):
    def build(self):
        btn= Button(text="click me",size_hint={0.3,0.4},pos_hint={"center_x":0.5,"center_y":0.5},font_size="44sp",color=(0,0,1,1),on_press=self.btn_click,on_realse=self.btn_release)
        return btn
    def btn_click(self,btn):
        print("button Clicked")
    def btn_release(self,btn):
        print("button Release")
button_app().run()




"""
button import is the when you a hve need a button
size_hint-> when you need a button size
pos_hint-> its the button in the goes in the center
on_press-> its function came on the button press
on_release-> its function come when you have the hold the button until you release the button
"""