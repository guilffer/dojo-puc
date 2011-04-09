import unittest

from program import roman2Arabic

class testa_metodo(unittest.TestCase):
	def testeUmaLetra(self):
		self.assertEquals(roman2Arabic('I'),1)
		self.assertEquals(roman2Arabic('V'),5)
		self.assertEquals(roman2Arabic('X'),10)
		self.assertEquals(roman2Arabic('L'),50)
		self.assertEquals(roman2Arabic('C'),100)
		self.assertEquals(roman2Arabic('D'),500)
		self.assertEquals(roman2Arabic('M'),1000)

	def testeMais(self):
		self.assertEquals(roman2Arabic('III'), 3)
		self.assertEquals(roman2Arabic('XI'), 11)
		self.assertEquals(roman2Arabic('XX'), 20)
		self.assertEquals(roman2Arabic('VII'), 7)
		self.assertEquals(roman2Arabic('IV'),4)
		self.assertEquals(roman2Arabic('IX'),9)
		self.assertEquals(roman2Arabic('CXXXIV'),134)
		self.assertEquals(roman2Arabic('CM'),900)
		self.assertEquals(roman2Arabic('CMXCIX'),999)
		self.assertEquals(roman2Arabic('LXXX'),80)
		self.assertEquals(roman2Arabic('MMMCMXCIX'),3999)
unittest.main()