
#define process class that requires no decisions

class process:
	def __init__(self, text, asignee, output = None):
		self.text = text                #the text/instructions as written on the flowchart
		self.asignee = asignee          #who is supposed to do this task
		self.output = output            #the next step or question
	def go(self):      #makes the step go
		print(self.asignee + ': ' + self.text + '\n')
		ap = open('fullprocess.txt', 'a')
		ap.write(self.asignee + ': ' + self.text + '\n')
		ap.close()
			

#define decision class that requires a yes/no answer
class decision:
	def __init__(self, text, asignee, yes = None, no = None, output = None):
		self.text = text          #the question as written on the flowchart
		self.asignee = asignee    #who needs to answer the question
		self.yes = yes            #the next step if the answer is yes
		self.no = no              #the next step if the answer is no
		self.output = output
	def go(self):       #makes this question go
		print(self.asignee +': ' + self.text + '\n')
		ans = input('Y or N?\n>>')
		if "y" in ans or "Y" in ans:
			self.output = self.yes
		elif "n" in ans or "N" in ans:
			self.output = self.no
		else:
			print('please answer yes or no.\n')
			self.go()

#define a multiple choice class with three choices

class special:
	def __init__(self, text, asignee, a = None, b = None, c = None, output = None):
		self.text = text          
		self.asignee = asignee    
		self.a = a
		self.b = b
		self.c = c
	def go(self):
		print(self.asignee + ': ' + self.text)
		ans = input('a, b, or c?\n>>')
		if 'a' in ans or 'A' in ans:
			self.output = self.a
		elif 'b' in ans or 'B' in ans:
			self.output = self.b
		elif 'c' in ans or 'C' in ans:
			self.output = self.c
		else:
			print('please answer a, b, or c.\n')
			self.go()

#define the function that lets the whole thing run
def run(x):
	while x != None:
		if type(x) != list:   #if current step has multiple outputs
			x.go()
		else:
			y = x[1]
			x = x[0]
			x.go()
			run(y)
		if x == end:      #if this is the last step
			print('\nwould you like to view the whole process?\n')
			printall = input('Y or N?\n>>')
			if 'y' in printall or 'Y' in printall:
				print('Click on the file "fullprocess.text" to view the whole process.')
			elif 'n' in printall or 'No' in printall:
				print('end of process.')
		x = x.output

	
#here is an example of a quiz. the first step should be start and the last step should be end. you can have more than one output in the form of a list, but if you do that, DO NOT have the branches rejoin with each other. one of the branches should be a dead end.
#once you understand how this works, you can delete it all and make your own.


#initialize all classes with text and asignee but NOT OUTPUT

start = process('start', 'Varrick')

exampleprocess = process('do the thing', 'Zhu Lee')

examplespecial = special('PLEASE ANSWER: did you do the thing?\na. yes\nb. no\nc. in progress', 'Zhu Lee')

examplequestion = decision('Do we need help', 'manager, employee')

ex2 = process('call team avatar', 'everyone')

ex3 = process('glare at Varrick', 'Zhu Lee')

end = process('end of process', 'manager')



#add outputs

start.output = exampleprocess

exampleprocess.output = examplespecial

examplespecial.a = examplequestion
examplespecial.b = examplequestion
examplespecial.c = examplequestion

examplequestion.yes = [ex2, ex3]
examplequestion.no = end

ex3.output = end
