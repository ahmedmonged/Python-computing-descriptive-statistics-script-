import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    #  get user input for city (chicago, new york city, washington).
    city = ''
    while True:
        city = input('please insert the city name between "chicago", "new york city" and "washington": ').lower()
        if city == ("chicago") or city == ("new york city") or city == ("washington"):
                break
        else:
                print('your input has a misktake make sure to choose from "chicago" or "new york city" or "washington"')
        
    #  get user input for month (all, january, february, ... , june)
    month = ''
    while True:
        month = input('type "all" if you want all months or choose from "january", "february", "march", "april", "may" and "june" if you want a specific month ').lower()
        if month == ("all") or month == ( "january") or month == ("february") or month == ("march") or month == ("april") or month == ("may") or month == ("june"):
            break
        else:
            print('your input has a misktake make sure to choose from the first six months or "all". ')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while True:
        day = input('please insert "all" if you want all days or a specific day of the week ').lower()
        if day == ('all') or day == ('sunday') or day == ('monday') or day == ('friday') or day == ('wednesday') or day == ('tuesday') or day ==('saturday') or day == ('thursday'):
            break
        else:
            print('your input has a misktake make sure to type the day correctly.')
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['combination of start and end'] = 'START STATION:   '+ df['Start Station'] +'   END STATION:   '+ df['End Station']
    month_order = ["january", "february", "march", "april", "may", "june"]
    if month != 'all':
        df = df[df['month']== month_order.index(month) + 1]
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('the most common month is:\n' + str(df['month'].mode()[0]))

    # display the most common day of week
    print('the most common day of week is:\n' + str(df['day'].mode()[0]))

    # display the most common start hour
    print('the most common hour is:\n' + str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('the most commonly used start station is: \n' + df['Start Station'].mode()[0])

    # display most commonly used end station
    print('the most commonly used end station is: \n' + df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('the most frequent combination of start station and end station trip is: \n' +  str(df['combination of start and end'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total travel time is:\n' + str(df['Trip Duration'].sum()))

    # display mean travel time
    print('mean travel time is:\n' + str(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('counts of user types is:\n' + str(df['User Type'].value_counts()))

    # Display counts of gender
    print('counts of gender is:\n' + str(df['Gender'].value_counts()))

    # Display earliest, most recent, and most common year of birth
    print('most common year of birth is:\n' + str(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(df):
    i = 5
    while True:
        while True:
            response = input('would you like to see 5 raws of data (or another 5 raws) types "yes" or "no" ').lower()
            if response == "yes" or response == "no":
                break
            else:
                print('your input has a mistake make sure to type yes or no')
        if response == 'no':
            break
        else:
            print(df.head(i))
            i+=5
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()