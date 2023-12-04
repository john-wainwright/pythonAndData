# -*- coding: utf-8 -*-
"""
Example for Windsor Workshop Tue Dec  5 2023

Take Durham weather data in file DurhamWeather1850_2022.csv which is in the format:
year, month, day, max temp, min temp, rainfall

and output in the format
day, month, year, rainfall


@author: John Wainwright
"""
#set up variables with input and output filenames
in_file = "DurhamWeather1850_2022.csv"
out_file = "DurhamDailyRainfall.csv"

#open the input and output files so the script can read them
inputFile = open (in_file, "r")
outputFile = open (out_file, "w")

#main loop
for in_data in inputFile:
    in_data = in_data.strip ()            # remove leading and trailing whitespace
    
    data_list = in_data.split (",")       # make a list (called data_list) from the comma-separated data items in in_data
    # write out only the day, month and year (third, second, first items in the list 
    #   (which starts with item zero))), and the rainfall (sixth item in the list)
    outputFile.write (data_list [2] + "," + 
                      data_list [1] + "," + 
                      data_list [0] + "," + 
                      data_list [5])      
    outputFile.write ("\n")               # write a newline character to the output (otherwise all values will be on one line next to each other)
#end of main loop (based on indentation)

#close files so other programs can access them
inputFile.close ()
outputFile.close ()

#tell the user something useful to let them know what's happened
print ("File " + out_file + " created, end of run")
#=======================================================================================================================
#That's it
