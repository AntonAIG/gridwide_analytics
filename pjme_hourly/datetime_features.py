# this is a function for extracting hour, hourofweek, dayofweek, holidays, etc.,
# from an array of datetime objects in a dataframe

def date_time_features(dataframe, date_column):
  date_list = dataframe[date_column]

  dataframe['hour'] = np.int8(date_list.dt.hour)
  dataframe['hourofweek'] = np.int16(((date_list.dt.dayofweek) * 24 + 24) - (24 - date_list.dt.hour) + 1)
  dataframe['dayofweek'] = np.int8(date_list.dt.dayofweek)
  dataframe['month'] = np.int8(date_list.dt.month)
  dataframe['year'] = np.int16(date_list.dt.year)

  # extracting holidays with the 'holiday' package
  us_holidays = []
  years = list(range(2002, 2019, 1))

  for year in years:
    for date in holidays.UnitedStates(years=year).items():
      us_holidays.append(str(date[0]))
  
  #make a list of all the holidays in a given year
  holiday = []
  for item in range(len(date_list)):
    date = date_list.iloc[item]
    date_item = date.strftime('%Y-%m-%d')
    if date_item in us_holidays:
      holiday.append(int(1))
    else:
      holiday.append(int(0))
    item+=1
  
  #make a 'holiday' column in the dataframe
  dataframe['holiday'] = holiday

  # search for seasons in the given months of the datetime object
  seasons = []
  for month in date_list.dt.month:
    if month in range(3,6):
      seasons.append('spring')
    elif month in range(6,9):
      seasons.append('summer')
    elif month in range(9,11):
      seasons.append('autumn')
    else:
      seasons.append('winter')

  #make a 'seasons' column in the dataframe
  dataframe['season'] = seasons

  return dataframe