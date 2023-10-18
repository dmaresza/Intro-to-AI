import math
import random

def main():
    #Creates random 10-element list of numbers 1-99
    l = []
    for i in range(10):
        l.append(random.randrange(1, 100))
    
    print("Original list:\n", l)
    
    print("\nFunction #1 - Reverse list:\n", reverseList(l))
    
    print("\nFunction #2 - Index of max value in original list:\nMax Value: {}\tIndex: {}".format(max(l), findMaxValueIndex(l)))
    
    print("\nFunction #3 - Odd numbers from original list:\n", oddElementsList(l))
    
    #Creates two random points between [0,0] and [10,10]
    p1 = []
    p2 = []
    for i in range(2):
        p1.append(random.randrange(0, 11))
        p2.append(random.randrange(0, 11))
    
    print("\nFunction #4 - Distance between two points:")
    print("Point 1: {} \nPoint 2: {} \nDistance: {}".format(p1, p2, distanceBetweenTwoPoints(p1,p2)))
    
    l = readFile("StarWars.txt")
    print("\nFunction #5 - Read file:\nFilename = StarWars.txt\nFile Contents:\n", l)
    
    writeFile("function6.txt", l)
    print("\nFunction #6 - Write file:\nNew filename = function6.txt")
    
    print("\nBank Account Class:")
    
    account1 = BankAccount("Jane Doe", 100.00)
    account2 = BankAccount("John Smith", 36.55)
    
    print("\nAccount for {}:\nStarting Balance: ${:.2f}".format(account1.id, account1.balance))
    n = 50
    print("Depositing: ${:.2f}\nNew Balance: ${:.2f}".format(n,account1.deposit(n)))
    n = 100
    print("Withdrawing: ${:.2f}\nNew Balance: ${:.2f}".format(n,account1.withdraw(n)))
    print("\nAccount for {}:\nStarting Balance: ${:.2f}".format(account2.id, account2.balance))
    n = 0
    print("Depositing: ${:.2f}".format(n))
    print("Balance: ${:.2f}".format(account2.deposit(n)))
    n = 40
    print("Withdrawing: ${:.2f}".format(n))
    print("Balance: ${:.2f}".format(account2.withdraw(n)))

#Function 1: Take in list and return new list in reverse order
def reverseList(oldList):
    newList = []
    for e in oldList:
        newList.insert(0, e)
    return newList

#Function 2: Return index of maximum element in list
def findMaxValueIndex(oldList):
    return oldList.index(max(oldList))

#Function 3: Take in list and return new list with odd elements only
def oddElementsList(oldList):
    newList = [e for e in oldList if e % 2 == 1]
    return newList

#Function 4: Calculate Euclidean distance between two points
def distanceBetweenTwoPoints(point1, point2):
    return math.sqrt(math.pow(point2[0] - point1[0], 2) + math.pow(point2[1] - point1[1], 2))

#Function 5: Take in filename, open file, and return list with elements as lines from file
def readFile(filename):
    file = open(filename)
    newList = file.readlines()
    file.close()
    return newList

#Function 6: Take in filename and list, write contents of list to file with each element as new line
def writeFile(filename, linesList):
    file = open(filename, "w")
    file.writelines(linesList)
    file.close()

class BankAccount:
    def __init__(self, ID, initialDepositAmount):
        self.id = ID
        self.balance = initialDepositAmount
    
    def deposit(self, depositAmount):
        if depositAmount <= 0:
            print("Deposit amount must be greater than $0")
        else:
            self.balance += depositAmount
        return self.balance
    
    def withdraw(self, withdrawalAmount):
        if self.balance >= withdrawalAmount:
            self.balance -= withdrawalAmount
        else:
            print("Withdrawal amount too large. Insufficient funds.")
        return self.balance

if __name__ == '__main__':
    main()