import pandas as pd
import numpy as np
import requests

# Call the Detail and Subject Census APIs for North Carolina
nc_detailed = requests.get('https://api.census.gov/data/2018/acs/acs5/?get=B01003_001E,B02001_002E,B17017_001E,B17017_002E,B08201_002E&for=tract:*&in=state:37').json()
nc_subject = requests.get('https://api.census.gov/data/2018/acs/acs5/subject?get=S1701_C01_002E,S1701_C01_010E&for=tract:*&in=state:37').json()

# Create dataframes from the Census data
nc_df_det = pd.DataFrame(nc_detailed)
nc_df_sub = pd.DataFrame(nc_subject)

# Add values for column names for Detail table
header_det = ['total_pop',
              'white_only_pop',
              'total_hh',
              'hh_poverty',
              'hh_no_vehcile',
              'state',
              'county',
              'tract']
nc_df_det = nc_df_det[1:]
nc_df_det.columns = header_det

# Add values for column names for Subject table
header_sub = ['under18_pop',
              '65over_pop',
              'state',
              'county',
              'tract']
nc_df_sub = nc_df_sub[1:]
nc_df_sub.columns = header_sub

# Create new index by concatenating state, county and tract to give each record unique ID
nc_df_det['ID'] = nc_df_det['state'] + nc_df_det['county'] + nc_df_det['tract']
nc_df_det.set_index('ID', inplace=True)

nc_df_sub['ID'] = nc_df_sub['state'] + nc_df_sub['county'] + nc_df_sub['tract']
nc_df_sub.set_index('ID', inplace=True)

# Join the two data frames together
nc_census = nc_df_det.merge(nc_df_sub, how = 'outer', on = 'ID')


# Call the Detail and Subject Census APIs for Virginia
va_detailed = requests.get('https://api.census.gov/data/2018/acs/acs5/?get=B01003_001E,B02001_002E,B17017_001E,B17017_002E,B08201_002E&for=tract:*&in=state:51').json()
va_subject = requests.get('https://api.census.gov/data/2018/acs/acs5/subject?get=S1701_C01_002E,S1701_C01_010E&for=tract:*&in=state:51').json()

# Create dataframes from the Census data
va_df_det = pd.DataFrame(va_detailed)
va_df_sub = pd.DataFrame(va_subject)

# Add values for column names for Detail table
header_det = ['total_pop',
              'white_only_pop',
              'total_hh',
              'hh_poverty',
              'hh_no_vehcile',
              'state',
              'county',
              'tract']
va_df_det = va_df_det[1:]
va_df_det.columns = header_det

# Add values for column names for Subject table
header_sub = ['under18_pop',
              '65over_pop',
              'state',
              'county',
              'tract']
va_df_sub = va_df_sub[1:]
va_df_sub.columns = header_sub

# Create new index by concatenating state, county and tract to give each record unique ID
va_df_det['ID'] = va_df_det['state'] + va_df_det['county'] + va_df_det['tract']
va_df_det.set_index('ID', inplace=True)

va_df_sub['ID'] = va_df_sub['state'] + va_df_sub['county'] + va_df_sub['tract']
va_df_sub.set_index('ID', inplace=True)

# Join the two data frames together
va_census = va_df_det.merge(va_df_sub, how = 'outer', on = 'ID')


# Combine the North Carolina and Virginia dataframes
census = pd.concat([nc_census, va_census])

# Convert attributes to integers
census['total_pop'] = census['total_pop'].astype('int')
census['white_only_pop'] = census['white_only_pop'].astype('int')
census['hh_no_vehcile'] = census['hh_no_vehcile'].astype('int')
census['under18_pop'] = census['under18_pop'].astype('int')
census['65over_pop'] = census['65over_pop'].astype('int')
census['hh_poverty'] = census['hh_poverty'].astype('int')
census['total_hh'] = census['total_hh'].astype('int')

# Create the minority attribute
census['minority_pop'] = census['total_pop'] - census['white_only_pop']

census.drop(['state_x', 'state_y',
             'county_x', 'county_y',
             'tract_x', 'tract_y'], axis = 1, inplace = True)

# Write to an Excel file and save in Project folder
census.to_excel(r'D:\Project Data\System Analysis\Jan 2020\system_analysis_data_2020.xlsx')
