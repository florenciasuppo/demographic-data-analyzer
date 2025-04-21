import pandas as pd

def calculate_demographic_data():

    # Load the dataset
    df = pd.read_csv("adult.data.csv")

    # Remove leading/trailing spaces from column names
    df.columns = df.columns.str.strip()

    # 1. Count the number of people by race
    race_count = df['race'].value_counts()

    # 2. Calculate the average age of men
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. Percentage of people with a Bachelor's degree
    total_personas = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = (bachelors_count / total_personas) * 100

    # 4. Percentage of people with advanced education earning >50K
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu_df = df[df['education'].isin(advanced_education)]
    higher_edu_rich = higher_edu_df[higher_edu_df['salary'] == '>50K']
    percentage_higher_edu_rich = (len(higher_edu_rich) / len(higher_edu_df)) * 100

    # 5. Percentage of people without advanced education earning >50K
    lower_edu_df = df[~df['education'].isin(advanced_education)]
    lower_edu_rich = lower_edu_df[lower_edu_df['salary'] == '>50K']
    percentage_lower_edu_rich = (len(lower_edu_rich) / len(lower_edu_df)) * 100

    # 6. Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of people who work the minimum hours and earn >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage = (len(rich_min_workers) / len(min_workers)) * 100

    # 8. Country with the highest percentage of people earning >50K
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_country_percentages = (rich_country_counts / country_counts) * 100
    highest_earning_country = rich_country_percentages.idxmax()
    highest_earning_country_percentage = rich_country_percentages.max()

    # 9. Most common occupation among those who earn >50K in India
    rich_indians = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = rich_indians['occupation'].value_counts().idxmax()

    return {
            'race_count': race_count,
            'average_age_men': average_age_men,
            'percentage_bachelors': percentage_bachelors,
            'percentage_higher_edu_rich': percentage_higher_edu_rich,
            'percentage_lower_edu_rich': percentage_lower_edu_rich,
            'min_work_hours': min_work_hours,
            'rich_percentage': rich_percentage,
            'highest_earning_country': highest_earning_country,
            'highest_earning_country_percentage': highest_earning_country_percentage,
            'top_IN_occupation': top_IN_occupation
        }