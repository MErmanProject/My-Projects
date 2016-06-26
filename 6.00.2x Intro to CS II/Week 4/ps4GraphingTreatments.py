# 6.00.2x Problem Set 4
from ps3b import *
import numpy
import random
import pylab

class ResistantVirus(SimpleVirus):  
 
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.mutProb = mutProb
        self.resistances = resistances
 
    def isResistantTo(self, drug):
        return self.resistances.get(drug, False)
 
    def reproduce(self, popDensity, activeDrugs):
        if (all(self.isResistantTo(d) for d in activeDrugs) and
            random.random() <= self.getMaxBirthProb() * (1 - popDensity)):
            resistances = {k:v if random.random() > self.mutProb else not v
                           for k, v in self.resistances.items()}
            return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(), 
                                  resistances, self.mutProb)
        raise NoChildException


class TreatedPatient(Patient):
    
    def __init__(self, viruses, maxPop):
        Patient.__init__(self, viruses, maxPop)
        self.drugs =[]
 
    def addPrescription(self, newDrug):
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)
 
    def getPrescriptions(self):
        return self.drugs
 
    def getResistPop(self, drugResist):
        return len([v for v in self.viruses if all(v.isResistantTo(d) 
                                                   for d in drugResist)])
 
    def update(self):
        self.viruses = [v for v in self.viruses if not v.doesClear()]
        popDensity = len(self.viruses) / float(self.maxPop)
        for v in self.viruses[:]:
            try:
                self.viruses.append(v.reproduce(popDensity,
                                                self.getPrescriptions()))
            except NoChildException:
                pass
        return len(self.viruses)

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    preCount = 150
    totCount = preCount + 150
    numViruses = 100
    finalResultsTot = []
    timeSteps = range(totCount)
    for i in range(numTrials):
        virusList = []
        for v in range(numViruses):
            virusList.append(ResistantVirus(0.1, 0.05, {'guttagonol': True}, 0.005))
        newPatient = TreatedPatient(virusList, 1000)
        for timeCount in timeSteps:
            if timeCount == preCount:
                newPatient.addPrescription('guttagonol')
            newPatient.update()
        finalResultsTot.append(newPatient.getTotalPop())
        print 'Trial#: ' + str(i)
      
    pylab.hist(finalResultsTot, bins=11)
    hTitle = 'Delay = ' + str(preCount) 
    pylab.title(hTitle) 
    pylab.xlabel('Virus Pop') 
    pylab.ylabel('NumTrials') 
    pylab.show()

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    preCount = 150
    varCount = 0
    totCount = preCount + varCount + 150
    numViruses = 100
    finalResultsTot = []
    timeSteps = range(totCount)
    for i in range(numTrials):
        virusList = []
        for v in range(numViruses):
            virusList.append(ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005))
        newPatient = TreatedPatient(virusList, 1000)
        for timeCount in timeSteps:
            if timeCount == preCount:
                newPatient.addPrescription('guttagonol')
            if timeCount == preCount + varCount:
                newPatient.addPrescription('grimpex')
            newPatient.update()
        finalResultsTot.append(newPatient.getTotalPop())
        print 'Trial#: ' + str(i)
    
    mean = 0.0
    meanTot = 0
    for i in finalResultsTot:
        meanTot += i
    mean = meanTot / float(len(finalResultsTot))
    print 'Mean = ' + str(mean)
    
    varList = []
    for i in finalResultsTot:
        varList.append((i-mean)**2)
    
    vari = 0.0
    variTot = 0
    for i in varList:
        variTot += i
    vari = variTot / float(len(varList))
    print 'Variance = ' + str(vari)
    
    pylab.hist(finalResultsTot, bins=11)
    hTitle = '2 Drugs (Delay = ' + str(varCount) + ')' 
    pylab.title(hTitle) 
    pylab.xlabel('Virus Pop') 
    pylab.ylabel('NumTrials') 
    pylab.show()

simulationTwoDrugsDelayedTreatment(100)