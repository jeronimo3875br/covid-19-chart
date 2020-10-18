#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math as mt
import requests as req
import json

class Criptomoedas():
	
	def __init__(self, url):
		self.url = url
	
	def getValues(self):
		
		data = {
			"BTC": req.get(self.url.format("BTC")).json(),
			"ETH": req.get(self.url.format("ETH")).json(),
			"LTC":  req.get(self.url.format("LTC")).json(),
			"XRP": req.get(self.url.format("XRP")).json()
		}
		
		self.createChart(data)
		
	def createChart(self, data):
		
		self.data = data;
		
		plt.barh(
			["Bitcoin", "Ethereun", "Litecoin", "Ripple"],
			[
				self.data["BTC"]["ticker"]["last"],
				self.data["ETH"]["ticker"]["last"],
				self.data["LTC"]["ticker"]["last"],
				self.data["XRP"]["ticker"]["last"],
			],
			0.4,
			align="center",
			alpha=0.7,
			label="growth by price",
			color="purple"
		)
		plt.style.use("ggplot")
		plt.title("Criptomoedas")
		plt.ylabel("Price")
		plt.xlabel("Criptomoeda")
		plt.legend()
		plt.show()
		
generateChart = Criptomoedas("https://www.mercadobitcoin.net/api/{}/ticker")
generateChart.getValues()
