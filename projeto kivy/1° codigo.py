from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
class Test(App):
    def build(self):
        box =  BoxLayout()
        button = Button(text = ' olá mundo')
        label = Label(text = 'texto 1')
        box.add_widget(button)
        box.add_widget(label)

        box2 =  BoxLayout(orientation = 'vertical')
        button2 = Button(text = ' Botao 2')
        label2 = Label(text = 'texto 2')
        box2.add_widget(button2)
        box2.add_widget(label2)
        
        box.add_widget(box2)
        return box
Test().run()
