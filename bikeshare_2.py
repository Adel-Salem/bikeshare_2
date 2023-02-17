import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

def get_month():
    while True:
        print('Which month? ', MONTHS, '? or type "all"\n')
        r = input().lower()
        if r == 'all' or r == 'january' or r == 'february' or r == 'march' or r == 'april' or r == 'may' or r == 'june':
            break
    return r

def get_day():
    while True:
        print('Which day? Please tyoe your response as an integer (e.g., 1=Sunday) or "all".\n')
        r = input().lower()
        if r == 'all':
            break
        elif r.isdigit():
            r = int(r)
            if r>=1 and r <=7:
                break
    return r

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print('Would you like to see data for Chicago, New York, or Washington?\n')
        city = input().lower()
        if(city == 'chicago' or city == 'new york' or city == 'washington'):
            break
    
    # get user input for month (all, january, february, ... , june)
    while True:
        print('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n')
        res = input()
        if(res == 'month' or res == 'day' or res == 'both' or res == 'none'):
            break
    
    if res == 'both':
        month = get_month()
        day = get_day()
    elif res == 'day':
        day = get_day()
        month = 'all'
    elif res == 'month':
        month = get_month()
        day = 'all'
    else:
        day = ''
        month = ''
        
        
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    

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
    
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day Of Week'] = df['Start Time'].dt.weekday
    df['Hour'] = df['Start Time'].dt.hour
    
    if month != 'all' and month != '':
        month = MONTHS.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all' and day != '':
        df = df[df['Day Of Week'] == int(day)]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print()
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    com_month = df['Month'].mode()[0]
    print("Most Populer Month: ", com_month, )
    
    # display the most common day of week
    com_week = df['Day Of Week'].mode()[0]
    print("Most Populer Day of Week: ", com_week)

    # display the most common start hour
    com_hour = df['Hour'].mode()[0]
    print("Most Populer Hour: ", com_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print()
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    com_start_station = df['Start Station'].mode()[0]
    print('Most commolny used start station is: ', com_start_station)

    # display most commonly used end station
    com_end_station = df['End Station'].mode()[0]
    print('Most commolny used end station is: ', com_end_station)

    # display most frequent combination of start station and end station trip
    
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print()
    start_time = time.time()
    
    print('\nCalculating Trip Duration...\n')
    total_duration = df['Trip Duration'].sum()
    count = df['Trip Duration'].count()

    # display total travel time
    # display mean travel time
    avg = df['Trip Duration'].mode()[0]
    print('Total Duration: ', total_duration, ', Count: ', count, ', Avg Duration: ', avg)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print()
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    print(df.groupby(['User Type'])['User Type'].count())

    # Display counts of gender
    if city.lower() != 'washington':
        print(df.groupby(['Gender'])['Gender'].count())

    # Display earliest, most recent, and most common year of birth
    
    if city.lower() != 'washington':
        earliest_year = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        com_year = df['Birth Year'].mode()[0]
        print('Earliest: ', earliest_year, ', Most Recent: ', most_recent, ', Common Year: ', com_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    indx = 0
    while True:
        print(df.iloc[indx:indx+5])
        
        res = input('Would you like to show individual data (yes or no)?')
        if res == 'no':
            break
        indx += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
