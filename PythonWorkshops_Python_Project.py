
# coding: utf-8

# There are 2 projects in this Notebook, your python guide will assign a Project, Please complete that Project. 
# 
# <a href="#Project-01---Find-nearest-Govt-Health-Center">Project 01 - Find nearest Govt Health Center </a><br />
# <a href="#Project-02---Allocate-Lab-System-to-Students">Project 02 - Lab system allocation tool</a><br />
# 
# <br />If you have any questions please write an email to learn@pythonworkshops.com

# ## Project 01 - Find nearest Govt Health Center
# 
# You have been given with a csv file with all the health center details with latitiude and longitude in India. <br>
# 
# Funny side, Somu after paying so many bills is feelign sick and wants to find the nearest hospital and meet the doctor. <br>
# 
# below project should be able to take input of Latitiude and Longitude from the user and provide the nearest government health center details. <br>
# 
# [the csv file link](https://data.gov.in/catalog/all-india-health-centres-directory)<br>
# or <br>
# [Direct Link](https://github.com/rajasekharsl/myrepo/blob/master/geocode_health_centre.csv) Click on Download button<br>
# 
# File has data in below format, 
# 
# State Name,	District Name,	Subdistrict Name,	Facility Type,	Facility Name,	Facility Address,	Latitude,	Longitude,	ActiveFlag_C,	NOTIONAL_PHYSICAL,	Location Type,	Type Of Facility,	Nin_N
# 
# Andhra Pradesh,	Vishakapatnam,	CHC Bheemilipatnam,	chc	Bheemilipatnam,	NA,	17.887517,	83.44568,	Y,	Physical,	Urban,	Public,	1111658272
# 
# [Code to get Nearest LatLong](#NearestLatlong)

# #### NearestLatlong
# <br>
# <pre>
# from math import radians, sin, cos, acos
# 
# 
# def nearest_two_latlongs(slatlon,dlatlon1,dlatlon2):
#   dist1 = 6371.01 * acos(sin(slatlon[0])*sin(dlatlon1[0]) + cos(slatlon[0])*cos(dlatlon1[0])*cos(slatlon[1] - dlatlon1[1]))<br>
#   dist2 = 6371.01 * acos(sin(slatlon[0])*sin(dlatlon2[0]) + cos(slatlon[0])*cos(dlatlon2[0])*cos(slatlon[1] - dlatlon2[1]))<br>
#   
#   if(dist1 &lt;= dist2):
#     return dlatlon1
#   else:
#     return dlatlon2
#     
#   return "Sorry, Couldn't find the nearest, Check the latlongs."
#   
# </pre>  
# 
# copy the above method into your project<br>
# call method nearest_two_latlongs(source_latlong_list,first_scenter_latlong_list,second_hcenter_latlong_list) as below <br>
# print("Nearest Health Center is " ,nearest_two_latlongs([17.731277,	83.315387], [17.720752, 83.284715], [17.765157, 83.356231]))<br>

# In[1]:


#Write your project code here 





# ## Project 02 - Lab system allocation tool
# <pre>
# There are list of students who need to either practice programming or need to give a test and you need allocate lab systems in your college to these students. 
# 
# Below is the list of students and their roll numbers, 
# Student_list = {'Raja':701,'Teja':702,'Suraj':770...}
# Name - Raja , Roll Number - 701
# 
# List of Labs and their system allocation status is as given below
# 
# {'MCA Lab':{'1':['Free','Good'],'2':['Allocated','Repair'],'3':['Free','Good'] ....}, 'Cisco Lab':{'1':['Free','Good'],'2':['Allocated','Repair'],'3':['Free','Good'] ....}}
# 
# Main dictonary - Lab Name : dicitonary of System ID's
# Second Dictionary(values) - System ID : [Allocation status , Repair status]
# 
# Allocate the system to students in order of the ID's and Labs as below
# 
# Raja - 701 - MCA Lab - 1
# Teja - 701 - MCA Lab - 3
# Suraj - 770 - Cisco Lab - 1
# 
# </pre>

# In[3]:


#Write your project code here
#lab_system_details = {'C Lab':{'1':['Free','Good'],'2':['Allocated','Repair'],'3':['Free','Good'] }, 'Cisco Lab':{'1':['Free','Good'],'2':['Free','Good'],'3':['Allocated','Repair']}}

#Name of students:
names=['Raja','Teja','Suraj']

#Roll no list:
roll=[701,702,770]

#Creating a dictionary combining the above two lists:

stu_data = dict(zip(names,roll))

print(stu_data)
#Creating a lab dictionary:
Lab_dict={'MCA Lab':{'1': ['Free', 'Good'], '2': ['Allocated', 'Repair'], '3': ['Free', 'Good']},'Cisco Lab':{'1': ['Free', 'Good'], '2': ['Allocated', 'Repair'], '3': ['Free', 'Good']}}
print(Lab_dict)
#Assigning the values of the list names as per the allocation
Raja=Lab_dict['MCA Lab']['1']
Teja=Lab_dict['MCA Lab']['3']
Suraj=Lab_dict['Cisco Lab']['1']

#printing final output
print('Raja would be alloted MCA Lab 1 which is',Raja)
print('Teja would be alloted MCA Lab 2 which is',Teja)
print('Suraj would be alloted Cisco Lab 1 which is',Suraj)


# How to submit project work, <br />
# 
# Go to File --> Download as --> Python (.py)<br />
# 
