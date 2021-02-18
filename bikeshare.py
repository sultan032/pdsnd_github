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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nWhich city would you like to see its data (chicago, new york city, washington)? ').lower().strip()
    #this loop handles the the wrong inputs
    while (city not in CITY_DATA.keys()):
        print("\Invalid input!")
        city = input('\ntry again (chicago, new york city, washington): ').lower().strip()

    # get user input for month (all, january, february, ... , june)
    month = input('\nWhich month would you like to filter by(all, january, february, ... , june)? ').title().strip()
    #this loop handles the the wrong inputs
    while (month not in ['All', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']):
        print("Invalid input!")
        month = input('\ntry again (all, january, february, ... , june): ').title().strip()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWhich day would you like to filter by (all, monday, tuesday, ... sunday)? ').title().strip()
    #this loop handles the the wrong inputs
    while (day not in ['All', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']):
        print("Invalid input!")
        day = input('\ntry again (all, monday, tuesday, ... sunday): ').title().strip()

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
    df['Start Time'] =  pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day of week'] = df['Start Time'].dt.day_name()


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('\nThe most common month is ({})'.format(df['month'].mode()[0]))

    # display the most common day of week
    print('\nThe most common day of week is ({})'.format(df['day of week'].mode()[0]))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('\nThe most common start hour is ({})'.format(df['hour'].mode()[0]))

    print("\nThis took {}s .".format(time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\nThe most commonly used start station is ({}) '.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('\nThe most commonly used end station is ({})'.format( df['End Station'].mode()[0]))
    # display most frequent combination of start station and end station trip
    df['route'] = 'From: ' + df['Start Station'] + ' To: ' + df['End Station']
    print('\nThe most frequent route is ({})'.format(df['route'].mode()[0]))

    print("\nThis took {}s .".format(time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nThe total travel time: {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('\nThe average travel time: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took {}s .".format(time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nThe counts of user types: \n{}'.format(df['User Type'].value_counts()))

    # Display counts of gender
    print('\nThe counts of gender: \n{}'.format(df['Gender'].value_counts()))

    # Display earliest, most recent, and most common year of birth
    print('\nThe earliest year of birth is ({})'.format(df['Birth Year'].min()))
    print('\nThe most recent year of birth is ({})'.format(df['Birth Year'].max()))
    print('\nThe most commen year of birth is ({})'.format(df['Birth Year'].mode()[0]))

    print("\nThis took {}s .".format(time.time() - start_time))
    print('-'*40)


def main():

    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)

        user_raw_data = input('\nWould you like to see the row data? Enter (yes or no): ').lower().strip()
        start = 0
        end = 5
        #this loop handles the the wrong inputs
        while (user_raw_data not in ['yes', 'no'] ):
            print("\nInvalid input!")
            user_raw_data = input('\nTry again (yes or no): ').lower().strip()
        while (user_raw_data == 'yes'):
            print(df.iloc[start:end])
            start += 5
            end += 5
            user_raw_data = input('Would you like to see more data? Enter (yes or no): ').lower().strip()
            while (user_raw_data not in ['yes', 'no'] ):
                print("\nInvalid input!")
                user_raw_data = input('\nTry again (yes or no): ').lower().strip()

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no. ').lower().strip()
        #this loop handles the the wrong inputs
        while (restart not in ['yes', 'no'] ):
            print("\nInvalid input!")
            restart = input('\nTry again (yes or no): ')
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
