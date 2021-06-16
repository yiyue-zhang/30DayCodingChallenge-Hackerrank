# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:16:45 2021

@author: Yi
"""

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
        
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):    
        Person.__init__(self, firstName, lastName, idNumber)
        self.Scores = []
        for i in Scores:
            self.score.append(int(i))
   	def calgrade(self):
		a = float(sum(self.scores)) / len(self.scores)
		if a < 40:
			return 'T'
		elif a < 55:
			return 'D'
		elif a < 70:
			return 'P'
		elif a < 80:
			return 'A'
		elif a < 90:
			return 'E'
		else:
			return 'O'

a = Student(Heraldo, Memelli, 8135627, [100, 80])
calgrade(a)