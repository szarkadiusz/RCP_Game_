import random

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,FadeTransition
from kivy.uix.image import Image
from random import randint as r
class RSP(MDApp):

    gameOption={1:'paper.png',
                2:'rock.png',
                3:'scissors.png'}

    randomNum=0
    def build(self):
        self.theme_cls.primary_palette = "Amber"


    def addImage(self):
        randomNum=r(1,3)



        self.root.ids.game_image.source=RSP.gameOption.get(randomNum)



if __name__ == '__main__':
    RSP().run()