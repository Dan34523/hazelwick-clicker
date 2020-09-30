from tkinter import *

root = Tk()
root.title("Hazelwick Clicker! Gotta catch em all!")
root["bg"] = "light blue"
root.resizable(0, 0)

mrsFearonPic = PhotoImage(file="Mrs Fearon.png")
mrPalmerPic = PhotoImage(file="Mr Palmer.png")
hazelwickPic = PhotoImage(file="Hazelwick Logo.png")
gypsiePic = PhotoImage(file="Gypsies.png")

x = 0
click_multiplier = 1
autoclickredeem = 0
gypsieredeem = 0
mr_palmer_redeem = 0

gypsie_price = 2000
fearon_price = 100
palmer_price = 300

status_bar = "Every click earns you {} point(s). You have {} auto-clicker(s). You have {} gypsie invasion(s)".format(click_multiplier, autoclickredeem, gypsieredeem)
score = Label(root, text=(str(x) + " points"), font="Helvetica 16 bold", bg="light blue")
score.grid(row=0, columnspan=4, pady=20)
statusBar = Label(root, text=status_bar, bd=1, relief=SUNKEN, anchor=W)
statusBar.grid(row=3, columnspan=4, sticky=N + E + S + W)


def click():
    global x
    x += click_multiplier
    score.config(text=(str(x) + " points"))


def autoclickpurchase():
    global autoclickredeem
    global x
    global status_bar
    global fearon_price
    if autoclickredeem != 5 and x >= fearon_price:
        autoclickredeem += 1
        x -= fearon_price
        fearon_price *= 2
        mrsfearonlabel.config(text="Auto Click.\nCan only be redeemed 5 times.\n Costs {} points".format(fearon_price))
        status_bar = "Every click earns you {} point(s). You have {} auto-clicker(s). You have {} gypsie invasion(s)".format(
            click_multiplier, autoclickredeem, gypsieredeem)
        statusBar.config(text=status_bar)
        score.config(text=(str(x) + " points"))
        autoclicker()


def autoclicker():
    global root
    global x
    x = x + click_multiplier
    score.config(text=(str(x) + " points"))
    root.after(300, autoclicker)


def click_multiplier_increase():
    global click_multiplier
    global x
    global status_bar
    global palmer_price
    if x >= palmer_price:
        x -= palmer_price
        palmer_price *= 2
        mrpalmerlabel.config(text="More points per click.\nCan be bought unlimited times\nCosts {} points".format(palmer_price))
        click_multiplier = click_multiplier + 1
        status_bar = "Every click earns you {} point(s). You have {} auto-clicker(s). You have {} gypsie invasion(s)".format(
            click_multiplier, autoclickredeem, gypsieredeem)
        statusBar.config(text=status_bar)
        score.config(text=(str(x) + " points"))


def gyspies_purchase():
    global x
    global gypsieredeem
    global status_bar
    global gypsie_price
    if x >= gypsie_price and gypsieredeem != 2:
        gypsieredeem += 1
        x -= gypsie_price
        gypsie_price *= 10
        gypsie_label.config(text="Rapid Auto Click.\nOnly redeemable twice.\nCosts {} points".format(gypsie_price))
        status_bar = "Every click earns you {} point(s). You have {} auto-clicker(s). You have {} gypsie invasion(s)".format(
            click_multiplier, autoclickredeem, gypsieredeem)
        statusBar.config(text=status_bar)
        score.config(text=(str(x) + " points"))
        gypsie()


def gypsie():
    global root
    global x
    x = x + click_multiplier
    score.config(text=(str(x) + " points"))
    root.after(50, gypsie)


hazelwick = Button(root, image=hazelwickPic, command=click)
hazelwick.image = hazelwickPic
hazelwick.grid(row=1, column=0, padx=20)
hazelwicklabel = Label(root, text="Click me", bg="light blue").grid(row=2, column=0, padx=20)

mrsfearon = Button(root, image=mrsFearonPic, command=autoclickpurchase)
mrsfearon.image = mrsFearonPic
mrsfearon.grid(row=1, column=1, padx=20)
mrsfearonlabel = Label(root, text="Auto Click.\nCan only be redeemed 5 times.\n Costs 100 points", bg="light blue").grid(row=2, column=1, padx=20)

mrpalmer = Button(root, image=mrPalmerPic, command=click_multiplier_increase)
mrpalmer.image = mrPalmerPic
mrpalmer.grid(row=1, column=2, padx=20)
mrpalmerlabel = Label(root, text="More points per click.\nCan be bought unlimited times\nCosts 300 points", bg="light blue").grid(row=2, column=2, padx=20)

gypsie_button = Button(root, image=gypsiePic, command=gyspies_purchase)
gypsie_button.image = gypsiePic
gypsie_button.grid(row=1, column=3, padx=20)
gypsie_label = Label(root, text="Rapid Auto Click.\nOnly redeemable twice.\nCosts 2000 points", bg="light blue").grid(row=2, column=3, padx=20)

root.mainloop()
