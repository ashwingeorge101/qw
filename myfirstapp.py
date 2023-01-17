
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image



image = Image.open("Logo.jpg")
st.image(image)

st.write("""
# North Financial Group
Investment Calculator
""")



pv = st.number_input('Initial Investment')
interest = st.slider('Interest Rate PJ %',min_value=1,max_value=20)
period =st.number_input('Number Of Months')
payments = st.number_input('Monthly Investment')
calc = (1 +(int(interest)/1200))

for i in range(1):
 i= payments
 count  = 1
fv = 0
list = []
list_plus2 = []
list_minus2 = []
pv2 = pv
pv3 = pv


for fv in range(int(period)):
    fv = i + pv * calc
    fv2 = i + pv2 * (1 +(int(interest + 2 )/1200))
    fv3 = i + pv3 * (1 +(int(interest - 2 )/1200))
    pv = fv
    pv2 = fv2
    pv3 = fv3
    list.append(fv)
    list_plus2.append(fv2)
    list_minus2.append(fv3)


df = pd.DataFrame(list)
per = int(period)


total_payments =" Total Payments made: **_R {:.2f}_**".format(i * period)
interest_tot = fv - (i * period)
total_intr =" Total Interest Received: **_R {:.2f}_**".format(interest_tot)
st.markdown("You will have **_R {0:.2f}_** after **_{1}_** months of investing with **_North Financial Group_**".format(fv,per))
total_payments
total_intr
interest_2 = interest + 2
interest_3 = interest - 2

fig = plt.figure(figsize=(12,6))
plt.xlim(0,period)
plt.plot(list,'b')
plt.plot(list_plus2,'g')
plt.plot(list_minus2,'r')
plt.legend([str(interest) +" %",str(interest_2) + " %" ,str(interest_3) +" %"],title = "Interest Rate")

st.pyplot(fig)




