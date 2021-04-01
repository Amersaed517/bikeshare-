import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def check_the_input(input_str, input_type):
    while True:
        read_theinput = input(input_str).lower()
        try:
            if read_theinput in ['new york city', 'washington' , 'chicago'] and input_type == 0:
                break
            elif read_theinput in ['january', 'february', 'march', 'april', 'may', 'june', 'all'] and input_type == 1:
                break
            elif read_theinput in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all'] and input_type == 2:
                break
            else:
                if input_type == 0:
                    print(" Sorry, your input should be ( new york city or washington or chicago ) ,Try again ")
                if input_type == 1:
                    print(" Sorry, your input should be ( january, february, march, april, may, june or all ) ,Try again")
                if input_type == 2:
                    print(" Sorry, your input should be  ( sunday,monday,tuesday,wednesday,thursday,friday,saturday or all) ,Try again")
        except ValueError:
            print("Sorry,but your input is wrong,Try again ")
    return read_theinput

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = check_the_input("Would you like to see the data for chicago, new york city or washington?", 0)
    # get user input for month (all, january, february, ... , june)
    month = check_the_input("Which Month ?", 1)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_the_input("Which day of week ? ", 2)

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Day Of Week:', popular_day_of_week)

    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print('Most Start Station:', popular_startstation)

    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print('Most End Station:', popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end = df.groupby(['Start Station', 'End Station']).count().idxmax()[0]
    print('Most Frequent Combination of Start and End Stations:', combination_start_end)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time/86400, " Days")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # TO DO: Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:', common_year)
        recent_year = df['Birth Year'].max()
        print('Most Recent Year:', recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:', earliest_year)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def raw_data(df):
    raw = input('Would you like to read the raw data? Yes/No ').lower()
    print()
    if raw=='yes' :
        raw=True
    elif raw=='no' :
        raw=False
    else:
        print('You did not enter a valid choice. try again. ')
        raw_data(df)
        return

    if raw:
        k=0
        while 1:

            for i in range(5):
                print(df.iloc[i+k])
                print()
            raw = input('Another five? Yes/No ').lower()
            if raw=='yes' :
                k=k+5
                continue
            elif raw=='no' :
                break
            else:
                print('try again.')
                return
  

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
          break


if __name__ == "__main__":
    main()
