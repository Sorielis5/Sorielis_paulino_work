#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 11:10:58 2025

@author: sorielispaulinopolanco
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy.stats import pearsonr



data2 = pd.read_csv('/Volumes/qac201/Studies and Codebooks/AddHealth/Data/Wave 1/addhealth_pds.csv')
data3 = pd.read_csv('/Volumes/qac201/Studies and Codebooks/AddHealth/Data/Wave 5/addhealth_multiwave.csv')

data2.head()
data2.info()
data3.head()
data3.info()

#------Variables 
# Dyslexia indicator

data2['PC38'].value_counts() 
data2['dyslexia'] = data2['PC38']
data2['dyslexia'] = data2['dyslexia'].replace(6, np.nan)
data2['dyslexia'] = data2['dyslexia'].replace(8, np.nan)
data2['dyslexia'] = data2['dyslexia'].replace(9, np.nan)

print(data2['dyslexia'].value_counts(dropna=False))

# Math grade
data2['H1ED12'].value_counts()
data2['math'] = data2['H1ED12']
data2['math'] = data2['math'].replace(5, np.nan)
data2['math'] = data2['math'].replace(6, np.nan)
data2['math'] = data2['math'].replace(96, np.nan)
data2['math'] = data2['math'].replace(97, np.nan)
data2['math'] = data2['math'].replace(98, np.nan)
print(data2['math'].value_counts(dropna=False))

# English grade
data2['H1ED11'].value_counts()
data2['english'] = data2['H1ED11']
data2['english'] = data2['english'].replace(5, np.nan)
data2['english'] = data2['english'].replace(6, np.nan)
data2['english'] = data2['english'].replace(96, np.nan)
data2['english'] = data2['english'].replace(97, np.nan)
data2['english'] = data2['english'].replace(98, np.nan)
print(data2['english'].value_counts(dropna=False))


# School grade
data2['H1GI20'].value_counts()
data2['school_grade']=data2['H1GI20']
data2['school_grade'] = data2['school_grade'].replace(96, np.nan)
data2['school_grade'] = data2['school_grade'].replace(97, np.nan)
data2['school_grade'] = data2['school_grade'].replace(98, np.nan)
data2['school_grade'] = data2['school_grade'].replace(99, np.nan)
print(data2['school_grade'].value_counts(dropna=False))


# Gender
data2['BIO_SEX'].value_counts()
data2['gender']= data2['BIO_SEX']
data2['gender'] = data2['gender'].replace(6, np.nan)
print(data2['gender'].value_counts(dropna=False))

#Which one of the following best describes your chief job activity or
#business this week?

data3['H5LM9'].value_counts()
data3['job'] = data3['H5LM9']
data3['job'] = data3['job'].replace(97, np.nan)
print(data3['job'].value_counts())


#Income 
data3['H5EC1'].value_counts()
data3['income'] = data3['H5EC1']
data3['income'] = data3['income'].replace(96, np.nan)
data3['income'] = data3['income'].replace(97, np.nan)
data3['income'] = data3['income'].replace(98, np.nan)
data3['income'] = data3['income'].replace(99, np.nan)
print(data3['income'].value_counts())

# Highest education
data3['H5OD11'].value_counts()
data3['education'] = data3['H5OD11']
data3['education'] = data3['education'].replace(96, np.nan)
data3['education'] = data3['education'].replace(97, np.nan)
data3['education'] = data3['education'].replace(98, np.nan)
data3['education'] = data3['education'].replace(99, np.nan)
print(data3['education'].value_counts())

# Race dummy variables
data3['white']= data3['H5OD4A']
data3['black']= data3['H5OD4B']
data3['hispanic'] = data3['H5OD4C']
data3['asian'] = data3['H5OD4D']

def races(row):
    if row['white'] == 1: return 'White'
    if row['black'] == 1: return 'Black'
    if row['hispanic'] == 1: return 'Hispanic'
    if row['asian'] == 1: return 'Asian'
    return 'Other'

data3['race'] = data3.apply(races, axis=1)

#merge
data2_subset = data2[['AID', 'dyslexia', 'math', 'english', 'gender', 'age', 'school_grade']]
data3_subset = data3[['AID', 'income', 'education', 'race','job']]

merged_data = pd.merge(data2_subset, data3_subset, on="AID").dropna()


#-----Plots
#dyslexia vs education and dyslexia

sns.boxplot(x='education', y='income', hue='dyslexia', data=merged_data)
plt.ylabel('Income')
plt.title('Income Distribution by Education Level and Dyslexia Status')


#income vs dyslexia 
sns.kdeplot(data=merged_data, x='income', hue='dyslexia')
plt.title("Income Distribution by Dyslexia Status")


#--dyslexia-- Univariate 
sns.countplot(data=merged_data, x='dyslexia')
plt.title("Number of Students by Dyslexia Status")
plt.xlabel("Dyslexia Status (0 = No, 1 = Yes)")


# ---- Dyslexia vs Grades ----
sns.boxplot(x='dyslexia', y='english', data=data2)
plt.title("Reading Grades by Dyslexia Status")

sns.boxplot(x='dyslexia', y='math', data=data2)
plt.title("Math Grades by Dyslexia Status")


#--income vs dyselxia
sns.boxplot(data=merged_data, x='dyslexia', y='income', hue='dyslexia')
plt.ylabel("Income")
plt.title("Income Distribution by Dyselxia Status")



# ---- Math and Reading by School Grade ----
sns.boxplot(x='school_grade', y='english', data=data2)
plt.title("Reading Grades Across School Grades")


sns.barplot(x='school_grade', y='math', data=data2, estimator='mean')
plt.title("Mean Math Grade by School Grade")


# ---- Income vs. Grades ----
sns.boxplot(x='math', y='income', hue='dyslexia', data=merged_data)
plt.title("Income Distribution by Math Grade and Dyslexia")


sns.boxplot(x='english', y='income', hue='dyslexia', data=merged_data)
plt.title("Income Distribution by Reading Grade and Dyslexia")


#-----dyslexia and job

sns.barplot(data=merged_data, x='dyslexia', y='job', estimator='mean') 
plt.ylabel("Mean of Job") 
plt.title("Mean of Job by Dyslexia") 

#income vs education
sns.barplot(data=merged_data, x='income', y='education', estimator='mean') 
plt.ylabel("Mean of Income") 
plt.title("Mean of Income by Education") 



# ---- Analyses 

# ---- ANOVA
#anova significant job -dyslexia 
model1= smf.ols(formula='job~ C(dyslexia)', data=merged_data)
results1=model1.fit()
print (results1.summary())


model1= smf.ols(formula='income~ C(dyslexia)', data=merged_data)
results1=model1.fit()
print (results1.summary())




# ---- Correlation: Grades and Income 
corr_math = pearsonr(merged_data['math'], merged_data['income'])
print("Math-Income correlation:", corr_math)

corr_eng  = pearsonr(merged_data['english'], merged_data['income'])
print("Reading-Income correlation:", corr_eng)

import scipy  #not significant 
sub1=merged_data[['math', 'job']].dropna()
print ('Math and Job correlation')
print(scipy.stats.pearsonr(sub1['math'],sub1['job']))


# ---- Logistic Regression 
my_logreg = smf.logit('dyslexia ~ income', data=merged_data).fit()
print(my_logreg.summary())
print("Odds ratios:\n", np.exp(my_logreg.params))

sns.barplot(data=merged_data, x='dyslexia', y='income', estimator='mean') 
plt.ylabel("Mean of Income") 
plt.title("Mean of Income by Dyslexia") 

my_logreg = smf.logit('dyslexia ~ C(job)', data=merged_data).fit()
print(my_logreg.summary())
print("Odds ratios:\n", np.exp(my_logreg.params))

sns.barplot(data=merged_data, x = 'dyslexia', y='job', estimator = 'mean')
plt.ylabel("mean of Job ")
plt.title("")


# ---- Multiple Regression
model_multiple = smf.ols(
    'income ~ dyslexia + C(gender) + education + C(race)  + school_grade + C(job) + english + math',
    data=merged_data).fit()
print(model_multiple.summary())

# multple linear regression 
model = smf.ols('income ~ C(math) + C(dyslexia)', data=merged_data).fit()
print(model.summary()) 

model= smf.ols(
    'job ~ C(dyslexia) + math + english + C(gender) + C(race)',
    data=merged_data).fit()
print(model.summary())

model = smf.ols('income ~ C(english) + C(dyslexia)', data=merged_data).fit()
print(model.summary())

model = smf.ols('dyslexia ~ C(job) + income', data=merged_data).fit()
print(model.summary())


