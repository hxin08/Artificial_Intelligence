# -*- coding: utf-8 -*-

"""
Created on Wed Oct 1 22:52:23 2014
@author: Hongsen
"""
# Import package

import random
import time

# Definiting arguments Class
class arguments():
    # Initialize the object. 
    def __init__(self, sizeCombi=4, sizePopulation=500):
        # List of available colors. 
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7','8','9']
        # Size of the combination at finding. 
        self.sizeCombi = sizeCombi
        # Size of the Population of part. 
        # * Must be pair * 
        self.sizePopulation = sizePopulation
        

#definiting Children Classes 

# Result of solution 
class result(arguments):
    # Initialize the object. 
    def __init__(self, sizeCombi=4, sizePopulation=500, rateOfMutation=9):
        print "[ STARTING... ]"
        arguments.__init__(self, sizeCombi, sizePopulation)

        self.rateOfMutation = rateOfMutation

        # Saves time part.
        self.startupTime = time.time()

        #creation and object initialization combination mystery. 
        self.c_unknown = inputcombination(self.sizeCombi)
        self.c_unknown.inputCombi()
        print "[ UNKNOWN DIGIT NUMBER:", self.c_unknown.combi, "]"

        # Iteration current.
        self.step = 1

        # List to store the current population. 
        self.population = []

    # Method to begin Result solution. 
    def start(self): # ---------------------------------------------------- #
        # Launch. 
        self.solve()

    # Rollover Result solution. 
    def solve(self): # ---------------------------------------------------- #
        print "\n[ --- BEGIN --- ]\n"
        
        # Generation 'sizePopulation' elements aleatoirs.
        for x in xrange(0,self.sizePopulation):
            self.population.append(0)           # # Incremention the size of 
                                                # List. 
            self.population[x] = combination()  # New instantiating a 
                                                # Object 'combination'. 
            self.population[x].generateCombi()  # of a new generation
                                                # combination for Random 
                                                # New object. 
        #print "[ POPULATION (", x+1, "):", self.population[x].combi, "]"
        #print "\n[ --- POPULATION INITIALIZED --- ]"
        print "\n[ STEP:\t 1 ]"
        
        # We loop until it has found the solution . 
        while True:
            # Selection of a couple of champions. 
            indexBest1, indexBest2 = self.selectBest()
            
            # If the best combination found e e is a combination mystery 
            # Then ends at the loop (and at the game). 
            if (self.population[indexBest1].combi == self.c_unknown.combi):
                break

            # If we have not yet found the right combination e e, it launches 
            # New reproduction. 
            self.reprodution(indexBest1, indexBest2)

            self.step += 1
            print "\n[ STEP:\t", self.step, "]"
        print "\n[ --- RESULT --- ]"                                       # #
        print "[ STEP:\t", self.step, "]"                                     # #
        print "[ UNKNOWN NUMBER:\t", self.c_unknown.combi, "]"                      # #
        print "[ ANSWER:\t", self.population[indexBest1].combi, "]"        # #
                                                                             # #
        # Calculation & Time display Result solution.                      # #
        self.finishTime = time.time()                                        # #
        print "[ SPEND TIME:", (self.finishTime - self.startupTime), "s ]"     # #




    # Method of comparison between the combination and the combination mystery 
    # proposal algorithm
    def comparer(self, proposition): # --------------------------------------- #
        # Creation variables 'pawns' which will store their numbers. 
        A = 0
        B  = 0

        # List index of right positions.
        list_b = []
        # List index of right color but wrong position.
        list_n = []

        # Compute the A. 
        for x in xrange(0,len(proposition)):
            if (proposition[x] == self.c_unknown.combi[x]):
                A += 1          # Add a A.
                list_b.append(x)    # It stores the index of the column. 

        # Compute the B. 
        for x in xrange(0,len(proposition)):
             # We value the proposed algorithm if it is not
             # Associate A. 
            if ((x in list_b) == False):
                for y in xrange(0,len(proposition)):
                    # value is the pawn of the mystery combination if not 
                    # teamed a white pawn or a black pawn at. 
                    if (((y in list_b) == False) and ((y in list_n) == False)):
                        if (proposition[x] == self.c_unknown.combi[y]):
                            B += 1            # Adding a black pawn. 
                            list_n.append(y)    # is stored in the column index
                            break               # not count a 
                                                # Second time. 

        # Returns the caller at the answering result of the comparison. 
        return A, B

    # Selection method of the nearest two proposals for the solution 
    # In the current population by successive comparison.
    def selectBest(self): 
        # 1 is chosen arbitrarily the first two e Le ments of the list 
        # As e as the two 'champions'. 
        best1 = 0
        best2 = 1

        # 2 We will look at all successively e Le ments of the list to 
        # Two best proposals to DA e pledge the two best. 
        for x in xrange(1, self.sizePopulation):
            # A. Score each proposal is calculated game to 
             # Each iterations. 

            # - Score the current champion. 
            ABest1, BBest1 = self.comparer(self.population[best1].combi)
            # - Score e me daille present money.
            ABest2, BBest2 = self.comparer(self.population[best2].combi) 
            # - Score of the current proposal. 
            AX, BX = self.comparer(self.population[x].combi)
            
            # B. We will now compare maniere ordained e e the score 
             # Current proposal to the two 'best'. 

            # - First, we compare the score 'white' Best ... 
            if (AX > ABest1):   # If the proposal is best 
                best2 = best1           # the first is Rela e e GUA second and 
                best1 = x               # proposal becomes premiere.
            # - ... Then the score 'black' best if there e e Galita 
             # White ... 
            elif ((AX == ABest1) and (BX > BBest1)):
                best2 = best1           # Same if e Gaux white but 
                best1 = x               # the proposal has more black. 
             # - ... Then the score 'white' of the second ... 
            elif (AX > ABest2): # If the proposal has more white than
                best2 = x               # the second it takes its place. 
             # - ... And finally the score 'black' second if there e ee Galita 
             # White. 
            elif ((AX == ABest2) and (BX > BBest2)):
                best2 = x                # Ditto if eGaux white but 
                                         # It has more blacks. 

        print "[SCORE: ",ABest1,"A, ",BBest1,"B ]"
        #print "[ BEST SCORE: ",self.comparer(self.A),"A, ",self.comparer(self.B),"B ]"
        #print "[SCORE: A",self.comparer(self.proposition[x]),"B ]"
        print "[", (float(ABest1)/float(self.sizeCombi))*100, "% ]"

        # Returns the index of the champions of the list. 
        return best1, best2

    # Playing cahmpions for a new population of 
     # TaillePopulation individuals. 
    def reprodution(self, best1, best2): # ----------------------------------- #
        # The quadruple population at every reproduction. 
        nouvelleTaillePopulation = (self.sizePopulation)*4
        self.population *= 4

        # We created new temporary objects to place on top of 
        # Tables two champions (at bubble sort). 
        temp1 = combination()
        temp1.combi = str(self.population[best1].combi)
        temp2 = combination()
        temp2.combi = str(self.population[best2].combi)

        self.population[best1].combi = self.population[0].combi
        self.population[best2].combi = self.population[1].combi

        self.population[0].combi = str(temp1.combi)
        self.population[1].combi = str(temp2.combi)

        # It is first "breed" the best with the rest of the table. 
        # We have up to loop through all the "basics" pre paths. 
        # This new population is placed "under" the precedente enlarger 
        # Ing the list. 
        for x in xrange (2*(self.sizePopulation), nouvelleTaillePopulation-1, 2):
            # On determine aleatoirement the rank to which we will cut proposed 
            # Sition (the "strand" of DNA). 
            coupure = random.randrange(1,self.sizeCombi)
            # It adds two new elements on the board. 
            # Self.population.append (0) 
            self.population[x] = combination()  # New instantiating a 
            # self.population.append (0)        # Object 'combination'. 
            self.population[x+1] = combination()# New instantiating a 
                                                # Object 'combination'. 
            
            # Temporary Chains that will store the pieces "DNA" that will 
            # Be recomposed thereafter is a full-proposal. 
            coupure1String = []
            coupure1Best   = []
            coupure2String = []
            coupure2Best   = []

            # Each "strand" is cut according to DA cut ended Alatoirement
            # previously. 
            for y in xrange(0,coupure):
                coupure1String.append(self.population[(x-2*self.sizePopulation)/2].combi[y])
            coupure1String = "".join(coupure1String)

            for y in xrange(0,coupure):
                coupure1Best.append(self.population[0].combi[y])
            coupure1Best = "".join(coupure1Best)

            for y in xrange(coupure,self.sizeCombi):
                coupure2String.append(self.population[(x-2*self.sizePopulation)/2].combi[y])
            coupure2String = "".join(coupure2String)

            for y in xrange(coupure,self.sizeCombi):
                coupure2Best.append(self.population[0].combi[y])
            coupure2Best = "".join(coupure2Best)

            # It joins the two new proposals. 
            self.population[x].combi   = (coupure1String+coupure2Best)
            self.population[x+1].combi = (coupure2String+coupure1Best)

            # Alegeatoirement we Nare mutations on the first of two 
             # Descendants. 
            if (random.randrange(self.rateOfMutation) == 1):
                # We stay selects a random color. 
                rand = random.randrange(len(self.numbers))
                couleur = self.numbers[rand]

                # We stay selects a location on the brain at random. 
                rand = random.randrange(self.sizeCombi)

                # It assembles a new strand. 
                newString = []
                for z in xrange(0,rand):
                    newString.append(self.population[x].combi[z])
                newString.append(couleur)       # We introduce the new "codon." 
                for z in xrange(rand+1, self.sizeCombi):
                    newString.append(self.population[x].combi[z])
                self.population[x].combi = "".join(newString)

             # We varified that no credit not identical descendants 
             # Champion. 
            identical1 = self.comparerDescendant(self.population[0].combi, self.population[x].combi)
            identical2 = self.comparerDescendant(self.population[0].combi, self.population[x+1].combi)

            # If they are identical descendants, they are recalculated. 
            if ((identical1 == self.sizeCombi) or (identical2 == self.sizeCombi)):
                x -= 2

         # Is then "reproduce" the second best with the rest of 
         # Table. We have up to loop through all the "basics" paths 
         # On the top part of the table e laughing. 
         # Result is on the old population. 
        for x in xrange(2,(self.sizePopulation)*2, 2):
            # Ends atoirement the rank to which we will cut proposed 
             # Sition (the "strand" of DNA). 
            coupure = random.randrange(1,self.sizeCombi)

            # Temporary Chains that will store the pieces "DNA" that will 
            # Be recomposed thereafter is a full-proposal. 
            coupure1String = []
            coupure1Best2  = []
            coupure2String = []
            coupure2Best2  = []

            # Each "strand" is cut according to cut ended 
            # Toirement previously. 
            for y in xrange(0,coupure):
                coupure1String.append(self.population[x/2+1].combi[y])
            coupure1String = "".join(coupure1String)

            for y in xrange(0,coupure):
                coupure1Best2.append(self.population[1].combi[y])
            coupure1Best2 = "".join(coupure1Best2)

            for y in xrange(coupure,self.sizeCombi):
                coupure2String.append(self.population[x/2+1].combi[y])
            coupure2String = "".join(coupure2String)

            for y in xrange(coupure,self.sizeCombi):
                coupure2Best2.append(self.population[1].combi[y])
            coupure2Best2 = "".join(coupure2Best2)

            self.population[x] = combination()
            self.population[x+1] = combination()

            # It joins the two new proposals. 
            self.population[x].combi   = (coupure1String+coupure2Best2)
            self.population[x+1].combi = (coupure2String+coupure1Best2)

            # verified that no credit not identical descendants 
             # Champion. 
            identical1 = self.comparerDescendant(self.population[1].combi, self.population[x].combi)
            identical2 = self.comparerDescendant(self.population[1].combi, self.population[x+1].combi)

            # If they are identical descendants, they are recalculated. 
            if (identical1 or identical2):
                x -= 2

        # Record the size of the new population. 
        self.sizePopulation = nouvelleTaillePopulation
        #print "[ NEW POPULATION SIZE:", self.sizePopulation, "]"


    # verified that spent two strings Parameter are not identical. 
    def comparerDescendant(self, best, proposition):
        identical = 0

        if (best == proposition):
            identical = 1

        # Returns the caller at the answering result of the comparison. 
        return identical



# Definiting the subject combination 
class inputcombination(arguments):
    # Initialize the object. 
    def __init__(self, sizeCombi=4): 
        arguments.__init__(self)
        # Value of the combination. 
        self.combi = []
        self.unknown = []
        for x in xrange(0, self.sizeCombi):
            digit = input("Enter a digit: ")
            self.unknown.append(digit)
        

    def inputCombi(self): 
        # Generation combination
        # Initialize unknown combination
            
        #Generates the random numbers.
        #for x in xrange(0, self.sizeCombi):
            #self.unknown.append(random.randrange(9))
            
        #if (self.unknown[0]!=self.unknown[1])and(self.unknown[0]!=self.unknown[2])and(self.unknown[1]!=self.unknown[2])and(self.unknown[0]!=self.unknown[3])and(self.unknown[1]!=self.unknown[3])and(self.unknown[2]!=self.unknown[3]):

        # Make the code number a digit number
        for x in self.unknown:
            self.combi.append(self.numbers[x])
        # Make the list a string
        self.combi = "".join(self.combi)


# Definiting the subject combination 
class combination(arguments):
    # Initialize the object. 
    def __init__(self, sizeCombi=4): 
        arguments.__init__(self)
        # Value of the combination. 
        self.combi = []
        

    def generateCombi(self): 
        # Generation combination
        #Generates the random numbers.
        self.unknown = []
        for x in xrange(0, self.sizeCombi):
            self.unknown.append(random.randrange(9))
            
        #if (self.unknown[0]!=self.unknown[1])and(self.unknown[0]!=self.unknown[2])and(self.unknown[1]!=self.unknown[2])and(self.unknown[0]!=self.unknown[3])and(self.unknown[1]!=self.unknown[3])and(self.unknown[2]!=self.unknown[3]):

        # Make the code number a digit number
        for x in self.unknown:
            self.combi.append(self.numbers[x])
        # Make the list a string
        self.combi = "".join(self.combi)



# Launching the program 

# Creation of a new Result solution. 
# SizeCombi = 8 sizePopulation = 100 = 9 rateOfMutation 
newResult = result()
# Launch Result solution.
newResult.start()#START 

# ################################# END ###################################### #