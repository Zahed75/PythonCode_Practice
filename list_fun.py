#list iteam add

training=["WebDesign","Python","Django","Js"]
training.append(("MICROTIK"))
print(training)

#-------to check list iteam length---##
print(len(training))
#----add iteam in position--------###
training.insert(4,"CISCO")
print(training)

#--------#######remove iteams------#

training.remove("WebDesign")
print(training)

training.sort()
print(training)
#coto theke boro Sajano
num=[20,10,15,23,122,22]
num.sort()
print(num)

##-----------ulta theke suru korbe------##
num=[20,10,15,23,122,22]
num.reverse()
print(num)

#-----Remove list Iteam ----POP method

hate=["Zahed","Promi","Satyam","Tanuja","Rubel"]

hate.pop()
hate.pop()
print(hate)
hate.clear()
print(hate)

course=["Microtik","Cisco","Js","python","Ruby","django"]
newcourse=course.copy()
course.append("bootstrap5")
course.insert(2,"Ruby")
print(course)


