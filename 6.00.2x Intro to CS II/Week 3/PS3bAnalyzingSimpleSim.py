def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """ 
    steps = 300
    trialResults = [[] for s in range(steps)]
    for __ in range(numTrials):
        viruses = [SimpleVirus(maxBirthProb, clearProb) for v in range(numViruses)]
        patient = Patient(viruses, maxPop)
        for eachstep in range(steps):
            trialResults[eachstep].append(patient.update())
    resultsSummary = [sum(l) / float(numTrials) for l in trialResults]
    pylab.plot(resultsSummary, label="Total Virus Population")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend()
    pylab.show()
