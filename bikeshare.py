#Explore data regarding bike share systems for Chicago, New York City and Washington.

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print('Would you like to see data for Chicago (enter 1), New York City (enter 2) or Washington (enter 3)?')
    num_city = input('Enter number above for which city you would like information on? Invalid entries will be restarted.')
    while True:
        if num_city == '1':
            city = 'chicago'
            print('The second city')
            break
        elif num_city == '2':
            city = 'new york city'
            print('The city that never sleeps')
            break
        elif num_city == '3':
            city = 'washington'
            print('Nations capital')
            break
        else:
            print('That is not a valid entry.  We will have to start over.')
            return get_filters()

    # TO DO: get user input for month (all, january, february, ... , june)

    num_month = input('Which month would you like to see data on? Enter month as a number.  Type "all" if you want to see all six months available. ')
    while True:
        if num_month == '1':
            month = 'january'
            print('You picked to see data for the month of January')
            break
        elif num_month == '2':
            month = 'february'
            print('You picked to see data for the month of February')
            break
        elif num_month == '3':
            month = 'march'
            print('You picked to see data for the month of March')
            break
        elif num_month == '4':
            month = 'april'
            print('You picked to see data for the month of April')
            break
        elif num_month == '5':
            month = 'may'
            print('You picked to see data for the month of May')
            break
        elif num_month == '6':
            month = 'june'
            print('You picked to see data for the month of June')
            break
        elif num_month == 'all':
            month = 'all'
            df = pd.read_csv(CITY_DATA[city])
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            print('You want to see all months')
            break
        else:
            print('That is not a valid month.  We will have to start over.')
            return get_filters()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_week = input('What day of the week? Please spell out full day. Type "all" if you want to see all days.')
    while True:
        if day_week == 'monday':
            day = 'Monday'
            print('You want to see data on Monday.')
            break
        elif day_week == 'tuesday':
            day = 'Tuesday'
            print('You want to see data on Tuesday.')
            break
        elif day_week == 'wednesday':
            day = 'Wednesday'
            print('You want to see data on Wednesday.')
            break
        elif day_week == 'thursday':
            day = 'Thursday'
            print('You want to see data on Thursday.')
            break
        elif day_week == 'friday':
            day = 'Friday'
            print('You want to see data on Friday.')
            break
        elif day_week == 'saturday':
            day = 'Saturday'
            print('You want to see data on Saturday.')
            break
        elif day_week == 'sunday':
            day = 'Sunday'
            print('You want to see data on Sunday.')
            break
        elif day_week == 'all':
            day = 'all'
            df = pd.read_csv(CITY_DATA[city])
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            print('You want to see all days.')
            break
        else:
            print('That is not a vaid day.  We will have to start over.')
            return get_filters()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    all_months = ['january', 'february', 'march', 'april', 'may', 'june']

    if month != 'all':
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        month = all_months.index(month) + 1
        df= df[df['month'] == month]

    if day != 'all':
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['weekday'] = df['Start Time'].dt.weekday_name
        df = df[df['weekday'] == day.capitalize()]
    return df

def city_info(df):
    print(df)

def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    if month == 'all':
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        print('The most common month of travel is: ')
        print(df['month'].mode()[0])
        print()

    # TO DO: display the most common day of week
    if day == 'all':
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        day_week = df['day_of_week'].mode()[0]
        print('The most common day of week is:')
        print(day_week)
        print()

    # TO DO: display the most common start hour

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    com_st_hr = df['hour'].mode()[0]
    print('The most common start hour is:')
    print(com_st_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is:')
    print(common_start)
    print()

    # TO DO: display most commonly used end station

    end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:')
    print(end_station)
    print()

    # TO DO: display most frequent combination of start station and end station trip

    trip = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(5)
    print('The top five trips are:')
    print(trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_time = df['Trip Duration'].sum()
    print('The total travel time is:')
    print(total_time)
    print()

    # TO DO: display mean travel time

    mean_time = df['Trip Duration'].mean()
    print('The mean travel time is:')
    print(mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print(user_types)
    print()

    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth

    if city == 'washington':
        print('Gender and birth year information are not available for Washington.')
    else:
        gender = df['Gender'].value_counts()
        print(gender)
        print()
        earliest_year = df['Birth Year'].min()
        print('The earliest birth year is:')
        print(earliest_year)
        print()
        recent_year = df['Birth Year'].max()
        print('The most recent birth year is:')
        print(recent_year)
        print()
        common_year = df['Birth Year'].mode()
        print('The most common birth year is:')
        print(common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        city_info(df)
        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city, month, day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
