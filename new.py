from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
import random

countries = ["Russia","USA","Canada","France","China","Japan","Germany","Great Britain"]
numbears = ["784336473","343432342365675","13245633445544","68689402049","448575692294","8384858494949","473839399393"]
ages = [ "18", "25", "30", "45", "50", "60", "70", "80", "90", "100"]
namesm = ["Ivan", "Alexey","Dmitry","Sergey", "Michael","Stepan"]
namesf = ["Elizabeth","Maria","Anastasia","Anna","Irina","Christina"]
names = []
gender = ["Male","Female"]
cities = ["Moscow", "New York", "Paris", "Berlin", "Tokyo","London", "Rome", "Madrid", "Sydney", "Toronto", "Dubai", "Seoul", "Mexico City", "Cairo", "Cape Town","Vladivostok","Cleveland"]
Country_user = None
City_user = None
Window.size = (600,600)
Window.clearcolor = (0.05, 0.05, 0.2, 1); TextInput.background_color = (0.1, 0.1, 0.3, 1); TextInput.foreground_color = (1, 1, 1, 1); Button.background_color = (0.2, 0.3, 0.6, 1); Button.color = (1, 1, 1, 1)
Window.title = "Chat Roulette"

class Human:
    def __init__(self,number = 0,name = "",age = 0,country = "",city = "",gender = ""):
        self.number = number
        self.name = name
        self.age = age
        self.country = country
        self.city = city
        self.gender = gender
    def input(self):
        try:
            self.country = input("Enter your country: ")
            self.city  = input("Enter your city: ")
            self.age = int(input("Enter your age: "))
            self.gender = input("Enter your gender: ")
            self.name = input("Enter your name: ")
            self.number = int(input("Enter your mobile phone number: "))
        except BaseException:
            print("Input error. Please try again:")
            self.input()
        if self.country not in countries or self.city not in cities or self.gender not in gender:
            print("Input error. You entered country or city incorrectly (should start with capital letter). Please try again:")
            self.input() 
        if self.gender == "Male" and self.name not in namesm:
            print("You can only have a male name. Please try again")
            self.input()
        if self.gender == "Female" and self.name not in namesf:
            print("You can only have a female name. Please try again")
            self.input()                    
    def __str__(self):
        all = "Number: " + str(self.number) + "\n" + "Name: " + str(self.name) + "\n" + "Age: " + str(self.age) + "\n" + "Country: " + str(self.country) + "\n" + "City: " + str(self.city) + "\n"  + "Gender: " + str(self.gender) + "\n"
        return all
    def check(self,hum2,quest1,quest2,btn1,btn2):
        if self.country == hum2.country or not quest1:
            if self.city == hum2.city or not quest2:
                if abs(self.age - hum2.age) <= 10:
                    if  btn1  == "down" and hum2.gender == "Female":
                        return True
                    elif  btn2 == "down" and hum2.gender == "Male":
                        return True    
                    
        return False
    def DATA(self,file_name):
        DATABASE = open(file_name,'a')         
        man = '\n' + self.name + ' ' + self.country + ' ' + self.city + ' ' +  self.gender + ' ' + str(self.age) + ' ' +  str(self.number)    
        DATABASE.write(man)   
        DATABASE.close()
    def random_human(self):
       self.country = random.choice(countries)
       self.number = random.choice(numbears)
       self.age = random.choice(ages)
       self.gender = random.choice(gender)
       if self.gender == "Male":
           self.name = random.choice(namesm)
       elif self.gender == "Female":
           self.name = random.choice(namesf)
       self.city = random.choice(cities)     
    def __lt__(self,other):
        counts = 0
        countot = 0
        if self.city == City_user:
            counts += 2
        if self.country == Country_user:
            counts += 1
        if other.city == City_user:
            countot += 2
        if other.country == Country_user:
            countot += 1
        return counts > countot   
##################################################################     
##################################################################  
##################################################################    
class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button = Button(text="Find", on_press=self.on_button_press,size_hint_x=1)
        self.text_inputs = []
        self.count = TextInput(hint_text="Country", multiline=False, size_hint_x=1)
        self.cit = TextInput(hint_text="City", multiline=False, size_hint_x=1)
        self.ag = TextInput(hint_text="Age", multiline=False, size_hint_x=1)
        self.btn1 = ToggleButton(text='Male', group='sex',state='down',allow_no_selection=False, size_hint_x=0.5)
        self.btn2 = ToggleButton(text='Female', group='sex',allow_no_selection=False,size_hint_x=0.5)
        self.na = TextInput(hint_text="Name", multiline=False, size_hint_x=1)
        self.output = TextInput()
        self.num = TextInput(hint_text="Phone number", multiline=False, size_hint_x=1)
        self.question1 = CheckBox(active = True, color = [100, 100, 100, 5], size_hint_x=0.1)
        self.question2 = CheckBox(active = True, color = [100, 100, 100, 5], size_hint_x=0.1)
        self.user = Human()
        self.out = TextInput(multiline=True, size_hint_x=1, size_hint_y=1)
        
    def build(self):
        title_label = Label(text="Chat Roulette", font_size=24, size_hint_y=0.1)
        app_box = BoxLayout(orientation='vertical', size_hint_x = 1)
        app_box.add_widget(title_label)
        main_box = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_x=1)
        outbox = BoxLayout(orientation='vertical', size_hint_x = 1, padding=10, spacing=10)
        all_box = BoxLayout(orientation = 'horizontal', size_hint_x = 1)
        min_box4 =  BoxLayout(orientation='horizontal', size_hint_y=0.5)
        min_box5 =  BoxLayout(orientation='horizontal', size_hint_y=0.5)
        btn_box = BoxLayout(orientation='horizontal', size_hint_y=1,size_hint_x = 1)
        label1  = Label(text = "Search for people in your country?", size_hint_x=0.6)
        all_box.add_widget(main_box)
        outbox.add_widget(self.out)
        all_box.add_widget(outbox)

        label2 = Label(text = "Search for people in your city?", size_hint_x=0.6)

        mini_box1 = BoxLayout(orientation='vertical', size_hint_y=1.5,size_hint_x = 1)
        mini_box2 = BoxLayout(orientation='vertical', size_hint_y=1.5,size_hint_x = 1)
        mini_box1.add_widget(self.count)
        mini_box2.add_widget(self.cit)
        min_box4.add_widget(label1)
        min_box5.add_widget(label2)
        min_box4.add_widget(self.question1)
        min_box5.add_widget(self.question2)
        mini_box1.add_widget(min_box4)
        mini_box2.add_widget(min_box5)

        btn_box.add_widget(self.btn1)
        btn_box.add_widget(self.btn2)
        main_box.add_widget(self.na)
        main_box.add_widget(btn_box)
        main_box.add_widget(self.num)
        main_box.add_widget(self.ag)
        main_box.add_widget(mini_box1)
        main_box.add_widget(mini_box2)
        button = Button(text="Find", on_press=self.on_button_press, size_hint_y=0.1)
        app_box.add_widget(all_box)
        app_box.add_widget(button)

        return app_box

    def on_button_press(self,instance): 
        a = False
        if self.count.text == '':
            print('1')
            a = True
            self.count.hint_text = "ERROR\nENTER YOUR NATIONALITY"
        if self.cit.text == '':
            print('2')
            a = True
            self.cit.hint_text = "ERROR\nENTER YOUR CITY"  
        if  not str(self.ag.text).isdigit() or self.ag.text == '':
            print('3')
            a = True
            self.ag.hint_text = "ERROR\nENTER YOUR AGE"        
        if self.na.text == '':
            print('4')
            a = True
            self.na.hint_text = "ERROR\nENTER YOUR NAME"          
        if self.num.text == '' or not (str(self.num.text).isdigit() or self.num.text[0] == '+' and str(self.num.text)[1:].isdigit()):
            print('5')
            a = True
            self.num.hint_text  = "ERROR\nENTER YOUR PHONE NUMBER"

        if a:
            self.out.text = ''

        if not a:
            DATABASE = open('111.txt','r')
            peoples = []
            self.user.country = self.count.text
            self.user.city = self.cit.text
            self.user.age = int(self.ag.text)
            self.user.name = self.na.text
            self.user.number = int(self.num.text)
            if self.btn1.state == "down":
                self.user.gender = self.btn1.text
            else:
                self.user.gender = self.btn2.text    
        
            for i in DATABASE:
                people = i.split()
                if len(people) == 6:
                    people[4] = int(people[4])
                    people[5] = int(people[5])
                    people = Human(people[5],people[0],people[4],people[1],people[2],people[3])
                    peoples.append(people)
            guys = [] 
            for i in peoples:
                if self.user.check(i,self.question1.active,self.question2.active,self.btn1.state,self.btn2.state):
                    guys.append(i)
            guys.sort()   
            all_g = ""     
            for j in guys:
                all_g += str(j) + '\n\n'
            self.out.text = all_g    
                    
            DATABASE.close()       

if __name__ == "__main__":
    MyApp().run()
    #soon i will add a profile photo
    
