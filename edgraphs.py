import matplotlib.pyplot as plt
import csv

#Choose database file - dindori.csv, bhopal.csv or chhatarpur.csv
database = "csv/chhatarpur.csv"

#Import content from database
content = []
with open(database) as myfile:
    csvreader = csv.reader(myfile)
    for row in csvreader:
        content.append(row)

classes = [content[i][0] for i in range(3, len(content))]
classes_for_dropouts = [content[i][0] for i in range(4, len(content))]


#Total Number of Students Enrolled
total_boys = [int(content[i][10]) for i in range(3, len(content))]
total_girls = [int(content[i][11]) for i in range(3, len(content))]
plt.plot(classes, total_boys, total_girls)
plt.title("Total Number of Students Enrolled")
plt.xlabel("Class")
plt.ylabel("Number of Students Enrolled")
plt.legend(["Boys", "Girls"])
plt.show()


#Total Number of Dropouts
boys_dropout = [total_boys[i]-total_boys[i+1] for i in range(len(total_boys)-1)]
girls_dropout = [total_girls[i]-total_girls[i+1] for i in range(len(total_girls)-1)]
plt.plot(classes_for_dropouts, boys_dropout, girls_dropout)
plt.title("Total Number of Dropouts")
plt.xlabel("Class")
plt.ylabel("Number of dropouts")
plt.legend(["Boys", "Girls"])
plt.show()


#Comparison across General vs ST vs SC vs OBC vs BPL
st_total = [int(content[i][2])+int(content[i][3]) for i in range(3, len(content))]
sc_total = [int(content[i][4])+int(content[i][5]) for i in range(3, len(content))]
obc_total = [int(content[i][6])+int(content[i][7]) for i in range(3, len(content))]
general_total = [int(content[i][8])+int(content[i][9]) for i in range(3, len(content))]
bpl_total = [int(content[i][12])+int(content[i][13]) for i in range(3, len(content))]
plt.plot(classes, st_total)
plt.plot(classes, sc_total)
plt.plot(classes, obc_total)
plt.plot(classes, general_total)
plt.plot(classes, bpl_total)
plt.title("Comparison Across Different Categories")
plt.xlabel("Class")
plt.ylabel("Number of Students Enrolled")
plt.legend(["Scheduled Tribe", "Scheduled Caste", "Other Backward Classes", "General", "Below Poverty Line"])
plt.show()


#Individual Graphs for Each Category

#Scheduled Tribes
st_boys = [int(content[i][2]) for i in range(3, len(content))]
st_girls = [int(content[i][3]) for i in range(3, len(content))]
plt.subplot(3, 2, 1)
plt.plot(classes, st_boys, st_girls)
plt.title("Scheduled Tribes")
plt.xlabel("Class")
plt.ylabel("Number of Students Enrolled")
plt.legend(["Boys", "Girls"])

#Scheduled Caste
sc_boys = [int(content[i][4]) for i in range(3, len(content))]
sc_girls = [int(content[i][5]) for i in range(3, len(content))]
plt.subplot(3, 2, 2)
plt.plot(classes, sc_boys, sc_girls)
plt.title("Scheduled Caste")
plt.xlabel("Class")
plt.ylabel("Number of Students Enrolled")
plt.legend(["Boys", "Girls"])

#Other Backward Classes
obc_boys = [int(content[i][6]) for i in range(3, len(content))]
obc_girls = [int(content[i][7]) for i in range(3, len(content))]
plt.subplot(3, 2, 3)
plt.plot(classes, obc_boys, obc_girls)
plt.title("Other Backward Classes")
plt.xlabel("Class")
plt.ylabel("Number of Students Enrolled")
plt.legend(["Boys", "Girls"])

#General
general_boys = [int(content[i][8]) for i in range(3, len(content))]
general_girls = [int(content[i][9]) for i in range(3, len(content))]
plt.subplot(3, 2, 4)
plt.plot(classes, general_boys, general_girls)
plt.title("General")
plt.xlabel("Class")
plt.ylabel("Number of Students Enrolled")
plt.legend(["Boys", "Girls"])

#Below Poverty Line
bpl_boys = [int(content[i][12]) for i in range(3, len(content))]
bpl_girls = [int(content[i][13]) for i in range(3, len(content))]
plt.subplot(3, 2, 5)
plt.plot(classes, obc_boys, general_boys)
plt.title("Below Poverty Line")
plt.xlabel("Class")
plt.ylabel("Number of Students Enrolled")
plt.legend(["OBC Boys", "General Boys"])

plt.show()