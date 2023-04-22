# Prompt
# In this challenge you must analyze demographic data using Pandas
# You are given a dataset of demographic data that was extracted from the 1994 Census database
# Here is a sample of what the data looks like:
# |    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
# |---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
# |  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
# |  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
# |  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
# |  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
# |  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |
# You must use Pandas to answer the following questions:
# How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
# What is the average age of men?
# What is the percentage of people who have a Bachelor's degree?
# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
# What percentage of people without advanced education make more than 50K?
# What is the minimum number of hours a person works per week?
# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
# What country has the highest percentage of people that earn >50K and what is that percentage?
# Identify the most popular occupation for those who earn >50K in India.
# Use the starter code in the file demographic_data_analyzer. Update the code so all variables set to "None" are set to the appropriate calculation or code. Round all decimals to the nearest tenth.


import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    # Filter data frame so that it only includes data for males and then select the age column from that resulting data frame and calculate the mean
    # Round answer to one decimal place
    average_age_men = df[df['sex'] == 'male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    # Count total bachelors and total people with any level of education
    total_bachelors = df[df['education'] == 'Bachelors']['education'].count()
    total_education = df['education'].count()
    percentage_bachelors = ((total_bachelors / total_education) * 100).round(1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_ed_over = len(higher_education[higher_education['salary'] == '>50K'])
    total_higher_ed = len(higher_education)
    percent_higher_ed_over = (higher_ed_over / total_higher_ed) * 100
    higher_education_rich = round(percent_higher_ed_over, 1)

    lower_ed_over = len(lower_education[lower_education['salary'] == '>50K'])
    total_lower_ed = len(lower_education)
    percent_lower_ed_over = (lower_ed_over / total_lower_ed) * 100

    lower_education_rich = round(percent_lower_ed_over, 1)
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = len(num_min_workers[(num_min_workers['salary'] == '>50K')])

    rich_percentage = round((rich_min_workers / len(num_min_workers) * 100), 1)

    # What country has the highest percentage of people that earn >50K?
    country_count = df['native-country'].value_counts()
    rich_country_count = df[df['salary'] == '>50K']['native-country'].value_counts()
    
    highest_earning_country = (rich_country_count / country_count * 100).idxmax()
    highest_earning_country_percentage = round((rich_country_count / country_count * 100), 1).max()
  
    # Identify the most popular occupation for those who earn >50K in India.
  
    rich_workers_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    occupation_count = rich_workers_india['occupation'].value_counts()
    
    # Need to use idxmax to find the idex of the occupation with the most workers that fit the criteria
    # Using just max only finds the maximumm number of occupation count for workers in India that make >50K
    top_IN_occupation = occupation_count.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

