import tkinter

def Story1(win):
    def final(tl, name, sport, city, playername, drinkname, snacks):
        text = f'''
        One day me and my friend {name} decided to play a {sport} game in {city}.
        We wanted to watch {playername}.
        We drank {drinkname} and also ate some {snacks}.
        We really enjoyed it! We are looking forward to going again and enjoying it.
        '''
        tl.geometry('500x500')
        tkinter.Label(tl, text='Story:', wraplength=tl.winfo_width()).place(x=160, y=310)
        tkinter.Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)

    NewScreen = tkinter.Toplevel(win, bg='#818181')
    NewScreen.title("A memorable day")
    NewScreen.geometry('500x500')
    tkinter.Label(NewScreen, text='Memorable Day').place(x=100, y=0)
    tkinter.Label(NewScreen, text='Name:').place(x=0, y=35)
    tkinter.Label(NewScreen, text='Enter a game:').place(x=0, y=70)
    tkinter.Label(NewScreen, text='Enter a city:').place(x=0, y=110)
    tkinter.Label(NewScreen, text='Enter the name of a player:').place(x=0, y=150)
    tkinter.Label(NewScreen, text='Enter the name of a drink:').place(x=0, y=190)
    tkinter.Label(NewScreen, text='Enter the name of a snack:').place(x=0, y=230)
    Name = tkinter.Entry(NewScreen, width=17)
    Name.place(x=250, y=35)
    game = tkinter.Entry(NewScreen, width=17)
    game.place(x=250, y=70)
    city = tkinter.Entry(NewScreen, width=17)
    city.place(x=250, y=105)
    player = tkinter.Entry(NewScreen, width=17)
    player.place(x=250, y=150)
    drink = tkinter.Entry(NewScreen, width=17)
    drink.place(x=250, y=190)
    snack = tkinter.Entry(NewScreen, width=17)
    snack.place(x=250, y=220)
    SubmitButton = tkinter.Button(NewScreen, text="Submit", background="Blue", font=('Times', 12),
                                   command=lambda: final(NewScreen, Name.get(), game.get(), city.get(),
                                                         player.get(), drink.get(), snack.get()))
    SubmitButton.place(x=150, y=270)

def Story2(win):
    def final(tl, profession, noun, feeling, emotion, verb):
        text = f'''
        Me and my friend have a really good {profession}.
        We really liked to go to our job and use our {noun}. It is {feeling}.
        Our job always makes us {emotion}, and we hope to {verb} our job.
        We can't wait till tomorrow!
        '''
        tl.geometry('500x500')
        tkinter.Label(tl, text='Story:', wraplength=tl.winfo_width()).place(x=160, y=310)
        tkinter.Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)

    NewScreen = tkinter.Toplevel(win, bg='#818181')
    NewScreen.title("Ambitions")
    NewScreen.geometry('500x500')
    tkinter.Label(NewScreen, text='Ambitions').place(x=150, y=0)
    tkinter.Label(NewScreen, text='Enter a profession:').place(x=0, y=35)
    tkinter.Label(NewScreen, text='Enter a noun:').place(x=0, y=70)
    tkinter.Label(NewScreen, text='Enter a feeling:').place(x=0, y=110)
    tkinter.Label(NewScreen, text='Enter an emotion:').place(x=0, y=150)
    tkinter.Label(NewScreen, text='Enter a verb:').place(x=0, y=190)
    Profession = tkinter.Entry(NewScreen, width=17)
    Profession.place(x=250, y=35)
    Noun = tkinter.Entry(NewScreen, width=17)
    Noun.place(x=250, y=70)
    Feeling = tkinter.Entry(NewScreen, width=17)
    Feeling.place(x=250, y=105)
    Emotion = tkinter.Entry(NewScreen, width=17)
    Emotion.place(x=250, y=150)
    Verb = tkinter.Entry(NewScreen, width=17)
    Verb.place(x=250, y=190)
    SubmitButton = tkinter.Button(NewScreen, text="Submit", background="Blue", font=('Times', 12),
                                   command=lambda: final(NewScreen, Profession.get(), Noun.get(),
                                                         Feeling.get(), Emotion.get(), Verb.get()))
    SubmitButton.place(x=150, y=270)

Screen = tkinter.Tk()
Screen.title("Mad Libs Generator")
Screen.geometry('400x400')
Screen.config(bg="#818181")
tkinter.Label(Screen, text='Mad Libs Generator').place(x=100, y=20)
Story1Button = tkinter.Button(Screen, text='A memorable day', font=("Times New Roman", 13),
                               command=lambda: Story1(Screen), bg='Blue')
Story1Button.place(x=140, y=90)
Story2Button = tkinter.Button(Screen, text='Ambitions', font=("Times New Roman", 13),
                               command=lambda: Story2(Screen), bg='Blue')
Story2Button.place(x=150, y=150)
Screen.mainloop()