import pandas as pd

df_persons_data = pd.read_csv('person_data.csv')

print(df_persons_data.head())

distinct_cities = df_persons_data['location'].unique()

print("Distinct city names:")

print("--------------------------------------------------------------")

print(distinct_cities)

print("Top 5 oldest persons living in Washington:")

print("--------------------------------------------------------------")

washington_df = df_persons_data[df_persons_data['location'] == 'Washington'].sort_values(by='age', ascending=False)

print(washington_df.head())

print("Count of people living in each city:")
city_counts = df_persons_data['location'].value_counts()
print(city_counts)

person_sans_fransisco_count = df_persons_data[(df_persons_data['age'] >= 20) & (df_persons_data['age'] <= 30)
                                              & (df_persons_data['location'] == 'San Francisco')].shape[0]

print(f'Number of people with age 20-30 living in San Francisco {person_sans_fransisco_count}')

print("Count of senior citizens living in each city:")

senior_citizens_data = df_persons_data[(df_persons_data['age'] > 60)]

senior_citizens_count_per_city = senior_citizens_data['location'].value_counts()

print(senior_citizens_count_per_city)

print("Count of teenagers living in each city:")

teenagers_data = df_persons_data[(df_persons_data['age'] >= 13) & (df_persons_data['age'] <= 19)]

teenagers_count_per_city = teenagers_data['location'].value_counts()

print(teenagers_count_per_city)

# Teenagers living in LosAngles ordered by the age

teenagers_Los_Angeles = teenagers_data[teenagers_data['location'] == 'Los Angeles'].sort_values(by='age',
                                                                                                ascending=True)

print("Teenagers living in LosAngles:")

print(teenagers_Los_Angeles)

# Count the number of males and females
gender_counts = df_persons_data['gender'].value_counts()

print("Count the number of males and females")

print(gender_counts)

# find the female senior citizens living in boston

print("Female senior citizens in boston")

female_senior_citizens_data_boston = senior_citizens_data[
    (senior_citizens_data['location'] == 'Boston') &
    (senior_citizens_data['gender'] == 'Female')].sort_values(by='age', ascending=False)

print(female_senior_citizens_data_boston[['name', 'age']])


print("count the male and female teenagers in living New york")

teenagers_data_newyork = teenagers_data[teenagers_data['location'] == 'New York']

teenagers_data_newyork_gender = teenagers_data_newyork['gender'].value_counts()

print(teenagers_data_newyork_gender)

print("number of females living in each city")

city_female_counts = df_persons_data[df_persons_data['gender'] == 'Female'].groupby('location').size()

print(city_female_counts)

print("city with maximum of females")

city_with_max_females = city_female_counts.idxmax()

max_female_count = city_female_counts.max()


print(f'{city_with_max_females} with {max_female_count} females')


print("city with minimum of females")

city_with_min_females = city_female_counts.idxmin()

min_female_count = city_female_counts.min()


print(f'{city_with_min_females} with {min_female_count} females')






