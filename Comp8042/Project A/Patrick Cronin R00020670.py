# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:48:51 2018

@author: R00020670
"""
import numpy as np

def main():
    print("Menu")
    print("1. Basic Statistics for Total Rainfall (Millimetres)")
    print("2. Basic Statistics for Most Rainfall in a Day (Millimetres)")
    print("3. Basic Statistics for Number of Rain days (0.2mm or More)")
    print("4. Wettest Location")
    print("5. Percentage of Rain Days")
    print("6. Exit")
    
    menuOptions = input("Please select one of the above options: ")
    if menuOptions.isdigit():
        menuOptions = int(menuOptions)
    else:
        print("\nPlease Enter a number between 1-6 \n")
        main()
    
    if (menuOptions==1):
        location, city = getLocation()
        totalRainfall(location, city)
    elif(menuOptions==2):
        location, city = getLocation()
        mostRainFallInADay(location, city)
    elif(menuOptions==3):
        location, city = getLocation()
        numberOfRainDays(location, city)
    elif(menuOptions==4):
        wettestLocation()
    elif(menuOptions==5):
        threshold = getThreshold()
        percentageOfRainDays(threshold)
    elif(menuOptions==6):
        print("Thank you for using this program")
    else:
        print("\nPlease Enter a number between 1-6 \n")
        main()
        
def getThreshold():
    threshold=""
    while not(threshold.isdigit()):
        threshold = input("Please enter maximum threshold value for number of rain days: ")
    threshold = int(threshold)
    return threshold

def getLocation():
    location =""
    city = ""
    while(location==""):
        location, city = selectLocation()
    return location, city

def selectLocation():
    print("1. Cork")
    print("2. Belfast")
    print("3. Dublin")
    print("4. Galway")
    print("5. Limerick")
    dataset =""
    city = ""
    
    menuOptions = input("Please select a location: ")
    if menuOptions.isdigit():
        menuOptions = int(menuOptions)
    else:
        print("\nRestarting Menu Please Enter a number between 1-5 next time \n")
        return dataset, city
    
    if (menuOptions==1):
        dataset = "CorkRainfall.txt"
        city = "Cork"
    elif(menuOptions==2):
        dataset = "BelfastRainfall.txt"
        city = "Belfast"
    elif(menuOptions==3):
        dataset = "DublinRainfall.txt"
        city = "Dublin"
    elif(menuOptions==4):
        dataset = "GalwayRainfall.txt"
        city = "Galway"
    elif(menuOptions==5):
        dataset = "LimerickRainfall.txt"
        city = "Limerick"
    else:
        print("\nRestarting Menu Please Enter a number between 1-5 next time \n")
        
    return dataset, city

def totalRainfall(location, city):
    data = np.genfromtxt(location)
    maxRainfall= np.amax(data[:,2])
    averageRainfall = np.mean(data[:,2])
    print("\n"+city + ": Max Total Rainfall =", maxRainfall)
    print(city + ": Average Total Rainfall =", averageRainfall)
        
def mostRainFallInADay(location, city):
    data = np.genfromtxt(location)
    maxRainfall= np.amax(data[:,3])
    averageRainfall = np.mean(data[:,3])
    print("\n"+city + ": Max Most Rainfall in a Day =", maxRainfall)
    print(city + ": Average Most Rainfall in a Day =", averageRainfall)
            
            
def numberOfRainDays(location, city):
    data = np.genfromtxt(location)
    maxDays= np.amax(data[:,4], dtype=int)
    averageDays = np.mean(data[:,4])
    print("\n"+city + ": Max Number of Rain days=", maxDays)
    print(city + ": Average Number of Rain days =", averageDays)
    
def wettestLocation():
    maxRainfall= 0
    maxCity = ""
    listOfDatasets = ["CorkRainfall.txt", "BelfastRainfall.txt", "DublinRainfall.txt", "GalwayRainfall.txt", "LimerickRainfall.txt"]
    for index, city in enumerate(listOfDatasets):
        data = np.genfromtxt(city)
        cityString = city[:-12]
        totalRainfall= np.sum(data[:,2])
        
        if(maxRainfall<totalRainfall):
            maxRainfall = totalRainfall
            maxCity = cityString
            
        totalRainfall = str(int(totalRainfall))
        indexString = str(index+1) +". "
        print(indexString +cityString, totalRainfall + "mm")
        
    maxRainfall = str(int(maxRainfall))
    print("The wettest location in Ireland is ", end="")
    print(maxCity + " with a rainfall figure of", maxRainfall + "mm")
    
def percentageOfRainDays(threshold):
    listOfDatasets = ["CorkRainfall.txt", "BelfastRainfall.txt", "DublinRainfall.txt", "GalwayRainfall.txt", "LimerickRainfall.txt"]
    for index, city in enumerate(listOfDatasets):
        data = np.genfromtxt(city)
        cityString = city[:-12]
        rainDaysColumn = data[:,4]
        countBelowThreshold = 0
        for rainDays in rainDaysColumn:
            if(rainDays<=threshold):
                countBelowThreshold+=1
        
        indexString = str(index+1) +". "
        percentage = countBelowThreshold/len(rainDaysColumn)
        percentageString = " "+"{0:.1f}%".format(percentage * 100)
        print(indexString + cityString + percentageString)
    
    
main()
