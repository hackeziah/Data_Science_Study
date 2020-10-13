import pandas as pd
import matplotlib.pyplot as plt
# data_frame = df
# sep => Separator

df = pd.read_csv('sample.csv', sep=',', header=0)


def cleanup_salary(row):
    # this is use to replace the string to float()
    salary = row['Salary'].replace('$', '')
    salary = float(salary)
    return salary


df['clean_salary'] = df.apply(cleanup_salary, axis=1)

df['rank'] = df['clean_salary'].rank(ascending=False)

# print(df.sort_values('rank'))


# asign the function to the dataframe
# axis 1 use to access every single row in data frame


# print('AVERAGE SALARY PER GENDER')
# print(df.groupby('gender')['clean_salary'].mean())

# df['gender'] = df['gender'].str.lower() #lower case


# def female_salary(row):
#     if row['gender'] == 'female':
#         return row['clean_salary']


# def male_salary(row):
#     if row['gender'] == 'male':
#         return row['clean_salary']


# df['female_salary_avg'] = df.apply(female_salary, axis=1)
# df['male_salary_avg'] = df.apply(male_salary, axis=1)

# use to organize the view of the data frame
# pd.set_option('display.max_column', None)
# print(df.groupby(['Job Title', 'City'])['clean_salary',
# 'male_salary_avg', 'female_salary_avg'].mean())


# dataFrame1 = pd.DataFrame(myjson, index=[1])

# print(df.head(5)) start first five data in tablle
# print(df.teil(5)) endlast five data in tablle
# print(df.describe())  # describe  data in table
# print(df.info())  # describe  data in table inforamtion
# df.plot.box()
# print(df.shape) #will count row and column
# print(df.describe())  # the summary statistics

# df['City'].fillna('London', inplace=True)  # fixing the blank
# median = df['Latitude'].median()  # using of median function
# df['Latitude'].fillna(median, inplace=True)  # fixing the blank
# dframe = df.dropna()
# print(df.shape)  # i shape it to know count data changes
# dframe = df.duplicated() # will determine the duplicated index by (Bool)
# print(dframe.head(20))
# dframe1 = df.drop_duplicates()  # droping duplicated data
# print(dframe1.shape)
# dframe2 = df.drop_duplicates(['first_name'], keep='last')
# print(dframe2.shape)

# dftest = df.duplicated(subset=['first_name'])
# print(dftest.head(30))


# print(df.loc[(df['clean_salary'] > 50000) & (df['clean_salary'] > 70000)])
# using of where location - loc
# print(df.sort_values('clean_salary', ascending=False))
# dfreplace = df.replace(['male', 'female'], ['M', 'F'])
# print(dfreplace[['first_name', 'gender']])
# goupby
