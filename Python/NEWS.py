import numpy as np 
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
df=pd.read_csv('/Users/praveensingampalli/Documents/BOOTCAMP2_FINAL/Python/news.csv')
df.shape
cat = df.head()
print(cat)