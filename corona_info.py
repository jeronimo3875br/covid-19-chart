#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math as mt
import requests
import json

class CoronaInfo():
	
	def __init__(self, url):
		self.url = url
		pass
	
	def getAllData(self):
		
		req = requests.get(self.url).json()
		
		data = {
			"NewConfirmed": req["Global"]["NewConfirmed"],
			"TotalConfirmed": req["Global"]["TotalConfirmed"],
			"NewDeaths": req["Global"]["NewDeaths"],
			"NewRecovered": req["Global"]["NewRecovered"],
			"TotalRecovered": req["Global"]["TotalRecovered"],
		}
		
		self.createChart(data)
		
		pass
	
	def createChart(self, data):
		
		self.data = data;
		
		plt.plot(
		
			[
			 	"NewConfirmed ({})".format(self.data['NewConfirmed']),
			 	"TotalConfirmed ({})".format(self.data['TotalConfirmed']), 
			 	"NewDeaths ({})".format(self.data['NewDeaths']),
			 	"NewRecovered ({})".format(self.data['NewRecovered']), "TotalRecovered ({})".format(self.data['TotalRecovered'])
			],
			[
				self.data["NewConfirmed"],
				self.data["TotalConfirmed"],
				self.data["NewDeaths"],
				self.data["NewRecovered"],
				self.data["TotalRecovered"],
			],
			"-",
			label="Indice",
			color="green",
		)
		plt.style.use("ggplot")
		plt.title("Covid-19")
		plt.xlabel("Cases")
		plt.ylabel("Data")
		plt.legend()
		plt.show()
		
		pass

CVI = CoronaInfo("https://api.covid19api.com/summary")
CVI.getAllData()

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))