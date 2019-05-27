# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:04:17 2019

@author: Olivor Holman

Simple tool that runs in the command line for easy calculation of volumes of
reagents required to create buffer solutions from protocols that specifiy
concentrations. Also includes a tool that allows calculation of mass
of chemicals required to create stock solutions of a desired concentration.
"""


def calcs(conc1, conc2, vol):
    return ((conc1/conc2)*vol)

arb_vols = []
stock_list = []
vol_list = []

v = input("Buffer solution calculator by Olivor Holman 2019. Press enter to begin \n")

stock = input("do you need to prepare stock solutions? y/n \n")

def stockCalc():
    nameChem = input("enter the name of the chemical you need a stock solution of \n")
    mr = float(input("enter the molecular mass of this chemical in grams \n"))
    stockConc = float(input("enter the desired concentration of the stock of this chemical in millimolar \n"))
    stockVol = float(input("enter the desired volume of stock solution in millilitres \n"))
    stock_list.append(nameChem)
    stock_list.append((stockVol/stockConc) * mr)

while stock == "y":
    stockCalc()
    stock = input("do you need to prepare another stock solution? y/n \n")


k = int(input("Enter desired volume of your buffer in ml \n"))

def ask():
    reagent = input("Enter the name of the reagent \n")
    concHave = float(input("Enter the concentration that you have in mM \n"))
    concWant = float(input("Enter the concentration you want in mM \n"))
    vol_list.append(reagent)
    vol_list.append(calcs(concWant, concHave, k))
    arb_vols.append(calcs(concWant, concHave, k))


while True:
    ask()
    t = input("calculate another reagent? y/n \n")
    if t == "n":
        break



print("Amounts of stock solution needed for your final buffer in ml:\n", vol_list)

if sum(arb_vols) > k:
    print("Warning: amount of each solution needed is in excess of your final concentration. Consider using more concentrated stock solutions.")

if len(stock_list) > 0:
    print("Mass of each chemical needed in grams to prepare your stock solutions:\n", stock_list)


while True:
    v = input("press enter to quit")
    if v == "fheupfheuwcxe":
        ask()
    else:
        break
