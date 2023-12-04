# -*- coding: utf-8 -*-
"""
Example for Windsor Workshop Tue Dec  5 2023

Take Durham weather data in file DurhamWeather1850_2022.xlsx which is in the format:
year, month, day, max temp, min temp, rainfall

and output a subset of the data from 1961-1990 in the format
year, mean temperature, annual rainfall

Checks that the data file exists in the current working directory before doing anything
and tell the user how many days of data have been read in / written out

@author: John Wainwright
"""
#set up variables with input and output filenames
in_file = "DurhamWeather1850_2022.xlsx"
results_file = "DurhamAnnualData1961_1990.csv"

#Check if the input file exists before doing anything else
import os      #the os library has utilities relating to the operating system
import pandas as pd     #the pandas library allows data-frame based analysis


#check whether the input file exists and continue execution if so
fileExists = os.path.isfile (in_file)
if fileExists:
    print ("Reading data from: " + in_file)

#open the output file
#"with open" is a safer way of opening files for reading/writing
#it has built-in error checking and automatically closes the file if there's an
#issue during the process so you can read it in other programs
#it replaces outFile = open (results_file, 'w') which would do the same
#thing without the error checking
    with open (results_file, 'w') as outFile:   
        #use the Pandas function to get the data into a data frame 
        durhamData = pd.read_excel (in_file, 
                                    sheet_name = "data")
        #check what the data look like
        print (durhamData.head ())
        #produce some basic descriptive statistics
        print (durhamData [["Tmax", "Tmin", "rainfall"]].describe ())
        #create a new column with mean temperature
        durhamData ["Tmean"] = (durhamData ["Tmax"] + durhamData ["Tmin"])  / 2.
        #produce shorter data frame with values from 1961-1990
        durhamDataShort =  durhamData [durhamData ["year"].isin (range (1961, 1991))]
        print (durhamDataShort [["Tmax", "Tmin", "rainfall"]].describe ())
        #create a new data frame with annual mean temperature
        annualMeanTemp = durhamDataShort [["year", "Tmean"]].groupby ("year").mean ()
        #create a new data frame with annual total rainfall
        annualRainfall = durhamDataShort [["year", "rainfall"]].groupby ("year").sum ()
        #merge the two data frames together using pd.merge (so we have just one year value)
        outputData = pd.merge (annualMeanTemp, annualRainfall, how = "left", on = "year")
        #use .to_csv to output the data frame in one go
        #need to specify line terminator to ensure no blank lines
        outputData.to_csv (outFile, lineterminator = '\n')
        #end of main loop (based on indentation)
#if the input file doesn't exist, tell the user
else:
    print ("Input file: " + in_file + " does not exist, done nothing")


#tell the user something useful to let them know what's happened
print ("End of run")
#=======================================================================================================================
#That's it
