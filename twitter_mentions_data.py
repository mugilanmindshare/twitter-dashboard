import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from connection import conn
import streamlit as st
from sqlalchemy import text





@st.cache(allow_output_mutation=True)
def get_username_for_search():
    con=conn()
    mapping_query = "SELECT distinct mentioned_user FROM twitter_leaders_mentions_view"
    t = text(mapping_query)
    data = pd.read_sql_query(t, con)
    data_list = data['mentioned_user'].tolist()
    return data_list



@st.cache(allow_output_mutation=True)
def over_all_twitter_mentions_data(username, fromm, to):
    con=conn()
    username = tuple(username)
    selected_users_query = "select * from twitter_leaders_mentions_view where mentioned_user in :username and date >= :fromm and date <= :to"
    params = {"username" : username, 'fromm': fromm, 'to':to }
    t = text(selected_users_query)
    selected_users_info = pd.read_sql(t, con, params=params)
    return selected_users_info













def year_wise_twitter_mentions(data):
    year_data=data.groupby(['year', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    year_data=year_data.reset_index()
    year_data=year_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    year_data=year_data.sort_values(by=['year'])
    return year_data
    


def month_year_wise_twitter_mentions(data):
    month_data=data.groupby(['month_year', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    month_data=month_data.reset_index()
    month_data=month_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    month_data=month_data.sort_values(by=['month_year'])
    return month_data

def week_wise_twitter_mentions(data):
    week_data=data.groupby(['week', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    week_data=week_data.reset_index()
    week_data=week_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    week_data=week_data.sort_values(by=['week'])
    return week_data




def day_wise_twitter_mentions(data):
    day_data=data.groupby(['date', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    day_data=day_data.reset_index()
    day_data=day_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    day_data=day_data.sort_values(by=['date'])
    return day_data
    

def hour_wise_twitter_mentions(data):
    hour_data=data.groupby(['hour', 'mentioned_user']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    hour_data=hour_data.reset_index()
    hour_data=hour_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    hour_data=hour_data.sort_values(by=['hour'])
    return hour_data
    



