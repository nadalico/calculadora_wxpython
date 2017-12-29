# -*- coding: utf-8 -*-

import wx
from calculadoraVista import CalculadoraUI

class Calculadora(CalculadoraUI):
  	def __init__(self, *args, **kargs):
  		CalculadoraUI.__init__(self, *args, **kargs)

  		self.resultado.SetValue("0") # establecemos el primer valor a 0
  		self.total = 0
  		self.string =""

  	def onBtn1( self, event ):
  		num = self.btn1.GetLabel() # cogemos el numero de la interfaz gráfica
	  	self.string += num
	  	self.resultado.SetValue(self.string) # lo añadimos en el campo de texto

	def onBtn2( self, event ):
  		num = self.btn2.GetLabel()
	  	self.string += num
	  	self.resultado.SetValue(self.string)

	def onBtn3( self, event ):
  		num = self.btn3.GetLabel()
	  	self.string += num
	  	self.resultado.SetValue(self.string)

	def onBtn4( self, event ):
  		num = self.btn4.GetLabel()
	  	self.string += num
	  	self.resultado.SetValue(self.string)

	def onBtn5( self, event ):
  		num = self.btn5.GetLabel()
	  	self.string += num
	  	self.resultado.SetValue(self.string)

	def onBtn6( self, event ):
  		num = self.btn6.GetLabel()
	  	self.string += num
	  	self.resultado.SetValue(self.string)

	def onBtn7( self, event ):
  		num = self.btn7.GetLabel()
	  	self.string += num
	  	self.resultado.SetValue(self.string)

	def onBtn8( self, event ):
  		num = self.btn8.GetLabel()
	  	self.string += num
	  	self.resultado.SetValue(self.string)

	def onBtn9( self, event ):
  		num = self.btn9.GetLabel()
	  	self.string += num
	  	self.resultado.SetValue(self.string)

  	def onBtnSumar( self, event ):
  		operador = self.btnSumar.GetLabel()
  		self.string += operador
	  	self.resultado.SetValue(self.string)

	def onBtnRestar( self, event ):
  		operador = self.btnRestar.GetLabel()
  		self.string += operador
	  	self.resultado.SetValue(self.string)

	def onBtnMultiplicar( self, event ):
  		operador = self.btnMultiplicar.GetLabel()
  		self.string += operador
	  	self.resultado.SetValue(self.string)

	def onBtnDividir( self, event ):
  		operador = self.btnDividir.GetLabel()
  		self.string += operador
	  	self.resultado.SetValue(self.string)

  	def onBtnAc( self, event ):
  		self.string = "";
  		self.resultado.SetValue("0")
  		

  	def onBtnTotal( self, event ):
  		self.total = eval(self.string) #eval hace la suma
  		self.resultado.SetValue("")
  		self.resultado.SetValue(str(self.total))
  		self.string = ""

if __name__ == '__main__':

    app = wx.PySimpleApp()
    frame = Calculadora(None)
    frame.Show()
    app.MainLoop()  