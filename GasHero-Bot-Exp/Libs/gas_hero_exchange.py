import streamlit as st
from const_gas_hero_exchange import *
from func_gas_hero_exchange import *

st.set_page_config(
    page_title="Gas Hero Beta Exchange",
    page_icon="https://framerusercontent.com/images/wMXHA9cBuudtI8kf36EHXH329rA.svg",
)

st.header('Gas Hero Beta Exchange :sunglasses:', divider='rainbow')
st.markdown(f'**Doc Shoshu**: &nbsp;&nbsp;&nbsp;{twitter_icon}')


tab1, tab2 = st.tabs(["Find Order", "Create Order", ])

with tab1:
    find_order()
with tab2:
    create_order()