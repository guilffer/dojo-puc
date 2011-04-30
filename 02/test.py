import unittest

from program import caixaEletronico

class testa_metodo(unittest.TestCase):

    def testeNotasSimples(self):
        self.assertEqual(caixaEletronico(2), {"notas": {2: 1}, "moedas":{}})
        
                                              
        self.assertEqual(caixaEletronico(5), {"notas": {5: 1},"moedas":{}})
                                              
        self.assertEqual(caixaEletronico(10), {"notas": {10: 1},"moedas":{}})
                                               
        self.assertEqual(caixaEletronico(20), {"notas": {20: 1},"moedas":{}})
                                               
        self.assertEqual(caixaEletronico(50), {"notas": {50: 1},"moedas":{}})
                                               
        self.assertEqual(caixaEletronico(100), {"notas": {100: 1},"moedas":{}})
        
    def testeMoedaSimples(self):
        self.assertEqual(caixaEletronico(0.01), {"notas": {}, "moedas":{0.01:1}})
                                              
        self.assertEqual(caixaEletronico(0.05), {"notas": {},"moedas":{0.05:1}})
                                              
        self.assertEqual(caixaEletronico(0.10), {"notas": {},"moedas":{0.10:1}})
                                               
        self.assertEqual(caixaEletronico(0.25), {"notas": {},"moedas":{0.25:1}})
                                               
        self.assertEqual(caixaEletronico(0.50), {"notas": {},"moedas":{0.50:1}})
        
        self.assertEqual(caixaEletronico(1), {"notas": {},"moedas":{1:1}})
    
    def testeNotasEMoedas(self):
        self.assertEqual(caixaEletronico(10.50), {"notas": {10:1},"moedas":{0.50:1}})
        self.assertEqual(caixaEletronico(10.75), {"notas": {10:1},"moedas":{0.50:1, 0.25:1}})
        
        
        
        
    
        

unittest.main()