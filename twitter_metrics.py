import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from connection import conn
import streamlit as st


@st.cache(allow_output_mutation=True)
def over_all_twitter_metrics():
    con=conn()
    over_all_twitter_metrics = pd.read_sql_table('leaders_ul_data', con)
    return over_all_twitter_metrics

def year_wise_twitter_metrics(data):
    year_data=data.groupby(['year', 'username']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    year_data=year_data.reset_index()
    year_data=year_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    year_data=year_data.sort_values(by=['year'])
    return year_data
    


def month_year_wise_twitter_metrics(data):
    month_data=data.groupby(['month_year', 'username']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    month_data=month_data.reset_index()
    month_data=month_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    month_data=month_data.sort_values(by=['month_year'])
    return month_data

def week_wise_twitter_metrics(data):
    week_data=data.groupby(['week', 'username']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    week_data=week_data.reset_index()
    week_data=week_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    week_data=week_data.sort_values(by=['week'])
    return week_data




def day_wise_twitter_metrics(data):
    day_data=data.groupby(['date', 'username']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    day_data=day_data.reset_index()
    day_data=day_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    day_data=day_data.sort_values(by=['date'])
    return day_data
    

def hour_wise_twitter_metrics(data):
    hour_data=data.groupby(['hour', 'username']).agg({'id':'count','likecount':'sum','replycount':'sum','retweetcount':'sum','quotecount':'sum'})
    hour_data=hour_data.reset_index()
    hour_data=hour_data.rename(columns={'id':'total_tweets','likecount':'total_likes','replycount':'total_replies','retweetcount':'total_retweets','quotecount':'total_quotes'})
    hour_data=hour_data.sort_values(by=['hour'])
    return hour_data
    


