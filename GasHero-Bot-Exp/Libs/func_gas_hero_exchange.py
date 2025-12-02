import streamlit as st
import pymongo
from pandas import DataFrame
from const_gas_hero_exchange import *
from time import sleep

def find_order():
    order_type = st.selectbox(
        'Asset type you want to exchange',
        ('hero', 'weapon', 'pet')
    )
    st.divider()
    if order_type == 'hero':
        provide_keyword = st.selectbox(
            'The hero you can offer',
            HEROS,    
        )
        want_keyword = st.selectbox(
            'The hero you want',
            HEROS,    
        )
    if order_type == 'weapon':
        provide_keyword = st.selectbox(
            'The weapon you can offer',
            WEAPONS,
        )
        want_keyword = st.selectbox(
            'The weapon you want',
            WEAPONS,
        )
    if order_type == 'pet':
        provide_keyword = st.selectbox(
            'The pet you can offer',
            PETS,
        )
        want_keyword = st.selectbox(
            'The pet you want',
            PETS,
        )
    st.button('Refresh Data', use_container_width=True)
    show_orders(order_type, provide_keyword, want_keyword)

def show_orders(order_type, provide_keyword, want_keyword):
    client = pymongo.MongoClient(mongo_srv_url)
    gashero_db = client['gashero']
    order_collection = gashero_db[f'{order_type}_order']

    query_filter = {}
    if provide_keyword:
        query_filter['want_asset'] = provide_keyword
    if want_keyword:
        query_filter['provide_asset'] = want_keyword
    query_result = list(order_collection.find(query_filter, projection={'_id': False}))
    df = DataFrame(query_result)
    df = rename_query_result_columns(df)

    st.dataframe(df, hide_index=True, use_container_width=True)

def rename_query_result_columns(df):
    rename_rule = {
        'want_asset': 'The hero he wants',
        'provide_asset': 'The hero he offers',
        'discord_name': "offerer's discord"
    }
    df = df.rename(columns=rename_rule)
    return df

def create_order():
    order_type = st.selectbox(
        'Asset Order type you want to create',
        ('hero', 'weapon', 'pet')
    )
    st.divider()

    success = False
    with st.form("my_form", clear_on_submit=True):
        if order_type == 'hero':
            provide_keyword = st.selectbox(
                'The hero you can offer',
                HEROS,    
            )
            want_keyword = st.selectbox(
                'The hero you want',
                HEROS,    
            )
        if order_type == 'weapon':
            provide_keyword = st.selectbox(
                'The weapon you can offer',
                WEAPONS,    
            )
            want_keyword = st.selectbox(
                'The weapon you want',
                WEAPONS,
            )
        if order_type == 'pet':
            provide_keyword = st.selectbox(
                'The pet you can offer',
                PETS,
            )
            want_keyword = st.selectbox(
                'The pet you want',
                PETS,
            )
        discord_name = st.text_input('You discord name.', key='7')

        submitted = st.form_submit_button('Submit Order')
        if submitted:
            success = submit_order(order_type, provide_keyword, want_keyword, discord_name)
    if success:
        success_msg = st.success('You order is submitted!', icon="✅")
        sleep(3)
        success_msg.empty()


def submit_order(order_type, provide_keyword, want_keyword, discord_name):
    client = pymongo.MongoClient(mongo_srv_url)
    gashero_db = client['gashero']

    order_collection = gashero_db[f'{order_type}_order']

    insert_data = {
        "provide_asset": provide_keyword,
        "want_asset": want_keyword, 
        "discord_name": discord_name,
    }
    insert_result = order_collection.insert_one(insert_data)
    
    return insert_result.inserted_id
