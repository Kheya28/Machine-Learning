
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Load the data
from google.colab import files
uploaded = files.upload()
# Get the data
log = pd.read_csv("Login.csv")

