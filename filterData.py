############################################################################
###### filterData.py serves as a method of extracting abstracts from #######
###### given text (.txt) files. Program will ask for input, insert #########
###### name of file with the .txt entension ################################
############################################################################

import xml.etree.ElementTree as ET
import os

# Greet the user and ask them which file they want to filter.
print ("Welcome to the UWECLK Data Extractor")
MJA = input("Please enter the name of the file to be read (ensure to use .txt):")

print('Parsing xml...')
root = ET.parse(MJA).getroot()

with open("filtered_data/filtered.txt", "w+", encoding="utf8") as newdata:
    abstracts = root.findall('.//AbstractText')
    abLength = len(abstracts)
    i = 0

    for abstract in abstracts:
        os.system('cls')
        print("Extraction is " + str(int((i * 100)/abLength)) + "% complete")

        newdata.write(abstract.text)
        i = i + 1

# Print completion message.
os.system('cls')
print("Extraction is 100% complete")
print("Extraction Complete")
print("Thank you for using the UWECLK Data Extractor")

# A command line to not close the program.
end = input()
