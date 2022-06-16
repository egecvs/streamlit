# -*- coding: utf-8 -*-

# -- Sheet --

import streamlit as st 
import pandas as pd 
import numpy as np 

core_hardcap = st.sidebar.number_input("CORE hardcap", 10000000)
input = 1 
supply = 0 
_price = []
_pricelog = []
_supply = []
_corepereth = []

for i in range(int(core_hardcap)):
    if core_hardcap - supply > 0:
        _price.insert(i,(input * core_hardcap / (core_hardcap - supply)))
        _pricelog.insert(i, np.log(input * core_hardcap / (core_hardcap - supply)))
        _corepereth.insert(i, (1/(input * core_hardcap / (core_hardcap - supply))))
        supply += core_hardcap / (core_hardcap - supply)
        _supply.insert(i, supply)

st.title("price chart")
st.bar_chart(pd.DataFrame(_price))
st.title("Price Chart (log)")
st.bar_chart(pd.DataFrame(_pricelog))
st.title("CORE per ETH")
st.bar_chart(pd.DataFrame(_corepereth))



