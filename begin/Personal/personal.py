## Functions
def GetInt(prompt):
	p = prompt + "? "
	while (True):
		try:
			i = int(input(p))
		except ValueError:
			print ("Eingabe ist ungültig, Bitte eine Ganzzahl eingeben!\n")
			continue
		break
	return i

def Menu(prompt, lowest, highest):
	print (prompt)
	while(True):
		result = GetInt("Ihre Auswahl")
		if result >= lowest and result <=highest:
			break
		print (f"bitte eine Zahl zwischen {lowest} und {highest} eingeben!\n\n")
	return result
		
def GetString(prompt):
	s = ""
	p = prompt + "? "
	while (True):
		s = input(p)
		if len(s) ==0:
			print ("Eingabe ist leer, bitte wiederholen!\n")
			continue
		break
	return s

def GetFloat(prompt):
	p = prompt + "? "
	while (True):
		try:
			f = float(input(p))
		except ValueError:
			print ("Eingabe ist ungültig, Bitte eine Gleitkommazahl eingeben!\n")
			continue
		break
	return f


def WaitForEnterKey():
	input("Mit Eingabe fortsetzen!")
	print ("\n")

def GetName(prompt):
	while (True):
			n = GetString(prompt)
			if len(n) >maxnamelength:
				print (F"Der {prompt} ist zu lang!")
				continue
			break
	return n

## Person
maxnamelength = 20

class Person:
	def __init__(self,number=0, nachname ="", vorname ="", income=0.0):
		self.number = number
		self.vorname = vorname
		self.nachname = nachname
		self.income = income
		self.marked = False
		
	def Input(self,number):
		self.number = number
		self.vorname = GetName("Vorname")
		self.nachname = GetName("Nachname")
		self.income = GetFloat("Einkommen")
		
	def Display(self):
		spaces1 = " "*(maxnamelength-len(self.vorname))
		spaces2 = " "*(maxnamelength-len(self.nachname))
		print (f"{self.number:3} {self.vorname}{spaces1} {self.nachname}{spaces2} {self.income:10.2f}")
		
	def Income(self):
		return self.income
		
	def Vorname(self):
		return self.vorname
		
	def Nachname(self):
		return self.nachname
		
	def Number(self):
		return self.number
		
	def IsMarked(self):
		return self.marked
		
	def Mark(self):
		self.marked = True
		
	def Unmark(self):
		self.marked = False
		
	def Is(self,nachname):
		return (self.nachname == nachname)
		
	def IsLike(self,match):
		return False
		
	def IsIncomeBetween(self,lowest, highest):
		high = highest
		low = lowest
		if high > low:
			high,low = lowest,highest
		return (self.income >= lowest and self.income <=highest)
		
	#string ToRecord();
	def __repr__(self):
		#return self.vorname +";"+self.nachname+";"+str(self.income)
		return f"{self.vorname};{self.nachname};{str(self.income)}"
		
	def __str__(self):
		return "Nummer: " + str(self.number) + "\n"\
			+ "Vorname: "+ self.vorname + "\n"\
			+ "Nachname: " + self.nachname +"\n"\
			+ "Gehalt: " + str(self.income) + " Euro\n";
		
		
	def FromStr(self,nummber, record):
		self.vorname,self.nachname,income = record.split(";")
		self.income = float(income)

	def __lt__(self,other):
		if not isinstance(other,Person):
			return False
		return (self.income < other.income)
	
## Staff Manager    

class StaffManager:
	staff = []

	def __init__(self):
		self.Load()


	def ShowStaffListHeading(self):
		print ("No. Vorname              Nachname             Einkommen")
		
	def Inputstaffmember(self):
		newnumber = len(self.staff)+1
		p = Person()
		p.Input(newnumber)
		self.staff.append(p)
		self.staff.sort()
		self.ShowStaffListHeading()
		p.Display()

	def Showstafflist(self):
		lowest = Person(0,"","",4000000)
		highest = Person()
		for member in self.staff:
			if member.income < lowest.income:
				lowest = member
			elif member.income > highest.income:
				highest = member
		self.ShowStaffListHeading()
		for member in self.staff:
			member.Display()
		print ("\n")
		self.ShowStaffListHeading()
		lowest.Display()
		highest.Display()

	def StorePerson(self, Person):
		self.staff.append(Person)
		self.staff.sort()

	def LoadDefaults(self):
		self.StorePerson(Person(1, "Berger", "Joachim", 3000))
		self.StorePerson(Person(2, "Schutz", "Adelinde", 1000))
		self.StorePerson(Person(3, "Jurk", "Merlin", 5000))
		self.StorePerson(Person(4, "Wilke", "Stefan", 4000))
		self.StorePerson(Person(5, "Brecht", "Dieter", 2000))
		self.StorePerson(Person(6, "Brecht", "Tina", 2500))
		self.StorePerson(Person(7, "Springer", "Axel", 2900))
		self.StorePerson(Person(8, "Radebrecher", "Albrecht", 7900))
		self.StorePerson(Person(9, "Meier", "Ingolf", 4800))
		self.StorePerson(Person(10, "Maier", "Jost", 4000))
		self.StorePerson(Person(11, "Mayer", "Annette", 4000))
		self.StorePerson(Person(12, "Meyer", "Miriam", 4000))


	def Save(self):
		with open("personal.txt","w") as f:
			for member in self.staff:
				s = reper(member)+"\n"
				f.write(s)

	def Load(self):
		print ("Lade Personaldaten!")
		self.staff.clear()
		try:
			f = open("personal.txt","r")
			all = f.read().split()
			print (all)
			for s in all:
				if len(s) >0:
					p = Person()
					p.FromStr(len(self.staff)+1,s)
				self.StorePerson(p)
				f.close()
		except IOError as e:
				pass
		if len(self.staff) == 0:
			print ("Keine Daten geladen. Lade aus Programm.")
			self.LoadDefaults()
		print (f"{len(self.staff)} Personen geladen.")


	def ClearMarks(self):
		for member in self.staff:
			member.Unmark()

	def DisplayAllMarkedPersons(self, errormessage):
		marked = self.GettAlMarkedPersons()
		if len(marked):
			[member.display() for member in marked]
		else:
			print (errormessage)
		

	def GetAllMarkedPersons(self):
		marked = []
		[marked.append(member) for member in self.staff if member.IsMarked()]
		return marked

	def FindPerson(self):
		nachname = GetName("Nachname")
		return [member for member in self.staff if member.Is(nachname)]

	def FindIncome(self):
		lowest = GetFloat("Minimaleinkommen")
		highest = GetFloat("Maximaleinkommen")
		self.ClearAllMarks()
		[member.mark() for member in self.staff if member.IncomeBetween(lowest,highest)]
		self.displayAllMarkedPersons("Keine Persone(n) im gesuchten Einkommensbereich gefunden!")
		

	def FindExtended(self):
		pass
## Main

menuprompt = """
	Willkommen bei Faktus pro, Version 2021.40.44.48
	Auswahl der Hauptfunktion:
	1 = Personaldaten eingeben.
	2 = Personaldaten auflisten.
	3 = Mitarbeiter mit Namen Suchen.
	4 = Suche nach Mitarbeitern zwischen einem bestimmten Einkommen.
	5 = erweiterte Namenssuche.
	
	
	8 = Laden.
	9 = Speichern.
	0 = Programmende.
	"""
	


def main():
	SM = StaffManager()
	#SM.Load()
	result = 1
	while (result):
		result = Menu(menuprompt, 0, 9)
		# ausführen der gewählten Menüfunktion
		if result == 1:
			SM.Inputstaffmember()
		elif result == 2:
			SM.Showstafflist()
		elif result == 3:
			SM.FindPerson()
		elif result == 4:
			SM.FindIncome()
		elif result == 5:
			SM.FindExtended()
		elif result in [6,7]:
			print ("Diese Funktion ist noch nicht unterstützt!\n")
		elif result == 8:
			SM.Load()
		elif result == 9:
			SM.Save()
		else:
			print ("Das Programm wird beendet!\n")

	
if __name__ == "__main__":
	main()
