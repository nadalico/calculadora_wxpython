# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 27 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class CalculadoraUI
###########################################################################

class CalculadoraUI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Calculadora", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.Colour( 208, 208, 208 ) )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.resultado = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,40 ), 0|wx.NO_BORDER )
		self.resultado.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.resultado.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer4.Add( self.resultado, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		bSizer6.Add( self.btn7, 0, wx.ALL, 5 )
		
		self.btn8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		bSizer6.Add( self.btn8, 0, wx.ALL, 5 )
		
		self.btn9 = wx.Button( self, wx.ID_ANY, u"9", wx.Point( -1,-1 ), wx.Size( 50,50 ), 0 )
		bSizer6.Add( self.btn9, 0, wx.ALL, 5 )
		
		self.btnMultiplicar = wx.Button( self, wx.ID_ANY, u"*", wx.Point( -1,-1 ), wx.Size( 50,50 ), 0 )
		bSizer6.Add( self.btnMultiplicar, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn4 = wx.Button( self, wx.ID_ANY, u"4", wx.Point( -1,-1 ), wx.Size( 50,50 ), 0 )
		bSizer7.Add( self.btn4, 0, wx.ALL, 5 )
		
		self.btn5 = wx.Button( self, wx.ID_ANY, u"5", wx.Point( -1,-1 ), wx.Size( 50,50 ), 0 )
		bSizer7.Add( self.btn5, 0, wx.ALL, 5 )
		
		self.btn6 = wx.Button( self, wx.ID_ANY, u"6", wx.Point( -1,-1 ), wx.Size( 50,50 ), 0 )
		bSizer7.Add( self.btn6, 0, wx.ALL, 5 )
		
		self.btnDividir = wx.Button( self, wx.ID_ANY, u"/", wx.Point( -1,-1 ), wx.Size( 50,50 ), 0 )
		bSizer7.Add( self.btnDividir, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		bSizer9.Add( self.btn1, 0, wx.ALL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"2", wx.Point( -1,-1 ), wx.Size( 50,50 ), 0 )
		bSizer9.Add( self.btn2, 0, wx.ALL, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u"3", wx.Point( -1,-1 ), wx.Size( 50,50 ), 0 )
		bSizer9.Add( self.btn3, 0, wx.ALL, 5 )
		
		self.btnRestar = wx.Button( self, wx.ID_ANY, u"-", wx.Point( -1,-1 ), wx.Size( 50,50 ), 0 )
		bSizer9.Add( self.btnRestar, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer9, 0, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn0 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		bSizer10.Add( self.btn0, 0, wx.ALL, 5 )
		
		self.btnDecimal = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		bSizer10.Add( self.btnDecimal, 0, wx.ALL, 5 )
		
		self.btnIgual = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		bSizer10.Add( self.btnIgual, 0, wx.ALL, 5 )
		
		self.btnSumar = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		bSizer10.Add( self.btnSumar, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"By: Javier Nadal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer5.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnAc = wx.Button( self, wx.ID_ANY, u"AC", wx.Point( -1,-1 ), wx.Size( 50,50 ), 0 )
		bSizer5.Add( self.btnAc, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		bSizer4.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn7.Bind( wx.EVT_BUTTON, self.onBtn7 )
		self.btn8.Bind( wx.EVT_BUTTON, self.onBtn8 )
		self.btn9.Bind( wx.EVT_BUTTON, self.onBtn9 )
		self.btnMultiplicar.Bind( wx.EVT_BUTTON, self.onBtnMultiplicar )
		self.btn4.Bind( wx.EVT_BUTTON, self.onBtn4 )
		self.btn5.Bind( wx.EVT_BUTTON, self.onBtn5 )
		self.btn6.Bind( wx.EVT_BUTTON, self.onBtn6 )
		self.btnDividir.Bind( wx.EVT_BUTTON, self.onBtnDividir )
		self.btn1.Bind( wx.EVT_BUTTON, self.onBtn1 )
		self.btn2.Bind( wx.EVT_BUTTON, self.onBtn2 )
		self.btn3.Bind( wx.EVT_BUTTON, self.onBtn3 )
		self.btnRestar.Bind( wx.EVT_BUTTON, self.onBtnRestar )
		self.btn0.Bind( wx.EVT_BUTTON, self.onBtn0 )
		self.btnDecimal.Bind( wx.EVT_BUTTON, self.onBtnDecimal )
		self.btnIgual.Bind( wx.EVT_BUTTON, self.onBtnTotal )
		self.btnSumar.Bind( wx.EVT_BUTTON, self.onBtnSumar )
		self.btnAc.Bind( wx.EVT_BUTTON, self.onBtnAc )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onBtn7( self, event ):
		event.Skip()
	
	def onBtn8( self, event ):
		event.Skip()
	
	def onBtn9( self, event ):
		event.Skip()
	
	def onBtnMultiplicar( self, event ):
		event.Skip()
	
	def onBtn4( self, event ):
		event.Skip()
	
	def onBtn5( self, event ):
		event.Skip()
	
	def onBtn6( self, event ):
		event.Skip()
	
	def onBtnDividir( self, event ):
		event.Skip()
	
	def onBtn1( self, event ):
		event.Skip()
	
	def onBtn2( self, event ):
		event.Skip()
	
	def onBtn3( self, event ):
		event.Skip()
	
	def onBtnRestar( self, event ):
		event.Skip()
	
	def onBtn0( self, event ):
		event.Skip()
	
	def onBtnDecimal( self, event ):
		event.Skip()
	
	def onBtnTotal( self, event ):
		event.Skip()
	
	def onBtnSumar( self, event ):
		event.Skip()
	
	def onBtnAc( self, event ):
		event.Skip()
	

