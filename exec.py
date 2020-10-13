import pandas as pd

df = pd.read_csv('exercise_course.csv', sep=',', header=0)

# a = df.groupby('url')['bytes'].sum()
# b = df.groupby('gender')['bytes'].sum()
# c = df.groupby(['country', 'gender'])['bytes'].sum()


def male_bytes(row):
    if row['gender'] == 'Male':
        return row['bytes']


def female_bytes(row):
    if row['gender'] == 'Female':
        return row['bytes']


df['male_bytes'] = df.apply(male_bytes, axis=1)
df['female_bytes'] = df.apply(female_bytes, axis=1)

c = df.groupby(['country', 'url'])['male_bytes', 'female_bytes'].sum()

# print(a)
# print(b)
print(c)


# def data(row):
#     if row['gender'] == 'male':
#         return row['bytes'].sum()


# df['male_data_avg'] = df.apply(data, axis=1)
