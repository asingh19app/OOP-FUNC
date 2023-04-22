# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

# Remember, when writing in a functional style:
# Keep variables immutable
# Write only pure functions
# Remember, functions may be higher order

def flatten_list():
    #test case 
    lst = [[70,20,30], [90,100,30], [90,70,60]]
    empty_list = [ ]

    for i in range(len(lst)):
        empty_list.extend(lst[i])
        empty_list.sort()

    return empty_list

print(flatten_list())


#How does this solution ensure data immutability?
## This solution ensures data immutability as it only affects the variables within the function, and nothing outside of it.

# Is this solution a pure function? Why or why not?
## Yes this solution is a pure function as the output depends on the input and does not affect any outside variables

# Is this solution a higher order function? Why or why not?
##No this solution is not a high order function as it does not return or take any functions as arguments

# Would it have been easier to solve this problem using a different programming style?
## For a real world case, I would of passed an argument of lst to the function and let the user assign a variable to a list and test that list as the argument when calling the function to allow for more usage of the function

# Why in particular is functional programming a helpful paradigm when solving this problem?
##Its helpful when testing certain functions, ensures less bugs and can be reused for other problems


# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
# Define a repair() method that will update the condition of the podracer to "repaired".
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

class Podracer:
    def __init__(self,max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        if self.condition == 'perfect':
            print('No repair needed')
        elif self.condition == 'trashed':
            print('Repair needed')
            self.condition = 'repaired'
            print('Repair complete')
            self.price+=1
        elif self.condition == 'repaired':
            print('Repaired already')

class AnakinsPod(Podracer):
    def __init__(self,max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def boost(self):
        print(self.max_speed*2)
    
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self):
        if self.condition == 'perfect':
            self.condition = 'trashed'
        elif self.condition == 'repaired':
            self.conditon ='trashed'
        return self.condition
#     The line self.condition = 'trashed' updates the value of self.condition to 'trashed'. The following line return self.condition == 'trashed' returns True if self.condition is 'trashed' and False otherwise.

# So the first line sets the value of self.condition and the second line returns a Boolean value indicating whether self.condition was successfully updated to 'trashed'.

pod = Podracer(50, 'trashed', 0)
pod.repair()
print(pod.condition)

pod2 = AnakinsPod(2, 'perfect', 0)
pod2.boost()

pod3 = SebulbasPod(2,'perfect', 0)
pod3.flame_jet()
print(pod3.condition)
# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism
## This code includes encapsulation as it prompts the user if the car is trashed, perfect or repaired, it then adds on the cost and and "repairs" the car if trashed. The user does not see this and just has to enter the state of the car and the program handles the rest. As well with abstarction, the program returns the desired outcone for the input. If the car is perfect, it does not return it needs to be repaired and the cost increase. The program includes inheritance as it passes the superclass as an arg in the subclasses and uses the passed in args in the superclass in their own methods and modify it to the desired outcome such as multiplying the spped by 2. The program does have polymorhpism as this classes can be reused and modified for other purposes.

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
## I would say no because the program builds off a certain set of data and args that are used in other subclasses and for future ones as well which eliminates the need to declare a new func with new args and data

# How in particular did Object Oriented Programming assist in the solving of this problem?
## OOP solved this problem by having a superclass with args/data that will be utitlized in subclasses. Those data/args can be modified and used in the subclasses by calling the parent class. It in a sense kills two birds with one stone, as the classes perform different operations wiht the same data w/o the need to reassign those variables/data/args.


# Is one of these coding paradigms "better" than the other? Why or why not?
## I would say each coding paradigm has its pros and cons. The functional way allows for a more clear cut answer w/o complicated varaibles/args whereas the OOP method allows for the utilizations of data in multiple ways.

# Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
##I prefer the functional method as its more clear and cut and sinec I worked with it longer than OOP

# Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming?
##Problems such as calculations would be best for fucntional programming and problems that have to do with data handling and user input would be best for OOP as that data can be manipulated via OOP methods.

# Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?
## I would say OOP, undertanding how to assign variables, the amount of args and the conditions can get tricky but to deepen understanding just comes with practice.