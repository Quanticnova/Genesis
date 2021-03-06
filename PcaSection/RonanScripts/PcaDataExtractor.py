import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import os


####################################################
########Finds All Groups(Dictionary) START##################
#######################################################
##This function returns the number of individuals within a group as well as all the groups present within the phenotype file
def _checkIfUsedDic(data,Groups):
    hasBeenUsed = False
    
    if(len(Groups)>0):
        
        for x in range(len(Groups)):
            if(data in Groups):
                
                hasBeenUsed = True

    if(hasBeenUsed == False):
        Groups.update({data:1})
    if(hasBeenUsed == True):
        val = Groups.get(data)
        val+=1
        Groups.update({data:val})
        
    return Groups
###########################################
####Finds All Groups (Dictionary) END#################
########################################




###########################################
########Finds All Groups(Dictionary) START#################
########################################
##Creates a list of all the groups in the phenotype file
def _checkIfUsedList(data,Groups):
    hasBeenUsed = False
    
    if(len(Groups)>0):
        
        for x in range(len(Groups)):
            if(data ==Groups[x]):
                
                hasBeenUsed = True

    if(hasBeenUsed == False):
        Groups.append(data)
            
    return Groups
###########################################
########Finds All Groups (Dictionary) END#################
########################################




######################################################################################
#############GRABBING PHENOTYPE DATA (key and value) start############################
######################################################################################
def FindPhenData():
    ##creates string with path to phen file
    phenString = os.getcwd()
    phenString= phenString+'\..\Data\comm.phe'

    ## phenotypeData will grab the Group name from the coloumn specified
    ##(NOTE THIS IS WHERE THE COLOUMN REPRESENTING THE PHEN FILE IS CHANGED)
    phenotypeData = np.genfromtxt(phenString,unpack=True,usecols=2, dtype=str)
    ##key has the correspponding individial name for the phendata
    key = np.genfromtxt(phenString,unpack=True,usecols=0, dtype=str)

    ##dictPhen has individual name and group name
    dictPhen = {}
    ##Groups contains all the groups in the phenfile


    for i in range(len(phenotypeData)):
        dictPhen.update({key[i]:phenotypeData[i]})

    return dictPhen
    
######################################################################################
##############################GRABBING PHENOTYPE DATA (key and value) end#############
################################################################################


######################################################################################
#############GRABBING PHENOTYPE Groups start############################
######################################################################################
def FindPhenGroups():
    ##creates string with path to phen file
    phenString = os.getcwd()
    phenString= phenString+'\..\Data\comm.phe'

    ## phenotypeData will grab the Group name from the coloumn specified
    ##(NOTE THIS IS WHERE THE COLOUMN REPRESENTING THE PHEN FILE IS CHANGED)
    phenotypeData = np.genfromtxt(phenString,unpack=True,usecols=2, dtype=str)
    ##key has the correspponding individial name for the phendata
    key = np.genfromtxt(phenString,unpack=True,usecols=0, dtype=str)

   
    ##Groups contains all the groups in the phenfile
    Groups = []


    for i in range(len(phenotypeData)):
        Groups = _checkIfUsedList(phenotypeData[i], Groups)

    return Groups
######################################################################################
##############################GRABBING PHENOTYPE Groupsend#############
################################################################################




######################################################################################
############################## GETTING NAMES FROM THE EVEC DATA START#################
######################################################################################
def GetIndividuals(returnFirst):

    EvecString = os.getcwd()
    EvecString= EvecString+'\..\Data\comm-SYMCL.pca.evec'

    #A name in the evec file is formatted very specifically
    ## FirstCode:SecondCode

    ##NamesFirst contains the FirstCode half of the name
    NamesFirst=[]
    ##NamesSecond contains the SecondCode half of the name
    NamesSecond=[]
    ##contains all names from the evec file
    names = np.genfromtxt(EvecString,unpack=True, usecols = 0 ,skip_header=1, dtype=str)

    ##Name is split in half and the halves are placed in to their respective lists
    for i in range(len(names)):
        NamesTemp =names[i].split(':')
        NamesFirst.append(NamesTemp[0])
        NamesSecond.append(NamesTemp[1])

    if(returnFirst==True):
       return NamesFirst
    if(returnFirst == False):
        return NamesSecond
######################################################################################
############################## GETTING NAMES FROM THE EVEC DATA END###################
################################################################################




 ######################################################################################
############################## Return FilePath Start#############################
#################################################################################   

##Returns the path to the evec file
##comes from importer class
##needed for PcaGraph class
def FilePathEvec():
    pass






 ######################################################################################
############################## Return FilePath end#############################
#################################################################################
