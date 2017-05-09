#indices
GRAIN_INDEX = 0
FLOUR_INDEX = 1
BEER_INDEX  = 2
BREAD_INDEX = 3
MEAT_INDEX  = 4
FRUIT_INDEX = 5
WOOD_INDEX  = 6
CHAIR_INDEX = 7
TABLE_INDEX = 8 

#profile indices
MANU_INDEX = 0
STORE_INDEX = 1
HOME_INDEX = 2
CHURCH_INDEX = 3

#required stock
#each tuple contains indexes of required inputs and the ratio of input to output. eg 1 flour needs only 2 grain.
#harvest inputs are currently placeholders
grain   = [(GRAIN_INDEX, .04)]
flour   = [(GRAIN_INDEX, 2)]
beer    = [(GRAIN_INDEX, 0)]
bread   = [(FLOUR_INDEX, 4)]
meat    = []
fruit   = [(FRUIT_INDEX, .04)]
wood    = [(WOOD_INDEX, .04)]
chair   = [(WOOD_INDEX, 35)]
table   = [(WOOD_INDEX, 100)]

components = [grain, flour, beer, bread, meat, fruit, wood, chair, table]

#name lists
maleNameList = ['John','Jake','Joseph']
femaleNameList = ['Jane','Joan','Jeanne']
lastNameList = ['Johnson','Jacobson','Josephson']

#these are identified by these same indices throughout the program.
equipmentList = ["millstone"]
materialsList = ["wheat", "flour", "beer", "bread", "meat", "fruit", "wood", "chair", "table"]
unitMissions = ["manu", "store", "house", "church"]

#game objects
localityList = []
businessList = []
religionList = []
unitList = []
churchList = []
# jobList = []
peopleList = []
bossList = []

#utility
#people will buy up to the number below INCLUSIVE.
utilityLimitList = [0,2,6,3, 2, 2, 0,2, 1]
utilityScaleList = [0,2,6,10,20,15,0,50,75]
happinessMax = 80.8626720903

def addBusiness(business):
    businessList.append(business)

def addLocality(locality):
    localityList.append(locality)

def addPeople(person):
    peopleList.append(person)

def addUnit(unit):
    unitList.append(unit)

def addReligion(religion):
    religionList.append(religion)

def addChurch(church):
    addUnit(church)
    churchList.append(church)

def getReligions():
    return religionList

def getBosses():
    return bossList

def getChurches():
    return churchList

def getBusinesses():
    return businessList

def getEquipment():
    return equipmentList

def getFirstNameList(gender):
    if gender == 0:
        nameList = maleNameList
    else:
        nameList = femaleNameList
    return nameList

# def getJob():
#     return jobList

def getLastNameList():
    return lastNameList

def getLocality():
    return localityList

def getMaxHappiness():
    return happinessMax

def getMaterials():
    return materialsList

def getComponents(materialIndex):
    return components[materialIndex]

def getAllComponents():
    return components

def getPeople():
    return peopleList

def getUnit():
    return unitList

def getUnitMissions():
    return unitMissions

def getUtilityLimit():
    return utilityLimitList

def getUtilityScale():
    return utilityScaleList