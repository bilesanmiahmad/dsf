import csv
import numpy as np
import pandas as pd

# plans = pd.read_csv('plans.csv', delimiter=',')
# # print(plans)
# print(plans.sample(5))

def get_silver_metals():
    plans = pd.read_csv('plans.csv', delimiter=',')
    silver_metals = plans[plans.metal_level == 'Silver']
    return silver_metals

silver = get_silver_metals()

def get_states(df):
    states = df['state'].unique()
    return set(states)


def state_plans_by_state(state, df):
    state_plans = df[df.state == state]
    return state_plans

def get_state_rate_number_set(state):
    number_set = state_plans_by_state(state, silver)['rate_area'].unique()
    return set(number_set)

def get_state_rate_area(state_plan, number):
    rate_area = state_plan[state_plan.rate_area == number]
    return rate_area

def get_data_by_rate_area(rate_area, frame):
    full_rate_area_frame = frame[frame.full_rate_area == rate_area]
    return full_rate_area_frame


def get_slcsp_for_rate_area(rate_area):
    rates = rate_area.rate.nsmallest(2).iloc[-1]
    return rates

def create_full_rate_area_column(dataframe):
    dataframe['full_rate_area'] = dataframe['state'] + dataframe['rate_area'].map(str)
    return dataframe

# Step 1: Add column full_rate_area
zips = pd.read_csv('zips.csv')
rate_areas = create_full_rate_area_column(zips)['full_rate_area']
unique_rate_areas = rate_areas.unique()

# Step 2: Get rates for a rate area
silver_with_full_rate_areas = create_full_rate_area_column(silver)
rate_areas_data = get_data_by_rate_area('AZ4', silver_with_full_rate_areas)
rate_areas_data['rate']

# Step 3: Get SLCSP for rate area
rate_area_slcsp = get_slcsp_for_rate_area(rate_areas_data)

#Step 4: Get zips for a rate area
zips = pd.read_csv('zips.csv')
full_rate_area_zips = create_full_rate_area_column(zips)
rate_areas_data = get_data_by_rate_area('AZ4', full_rate_area_zips)
rate_areas_data['zipcodes']



# print(get_states(silver))
# az_plans = state_plans_by_state('AZ', silver)
# az_rate_area = get_state_rate_area(az_plans, 1)
# print(get_state_rate_number_set('AZ'))
# print(get_state_rate_area(az_plans, 1))
# az1_slcsp = get_slcsp_for_rate_area(az_rate_area)
# print(az1_slcsp)
# zips = pd.read_csv('zips.csv')
#print(create_full_rate_area_column(zips).head(5))
# rate_areas = create_full_rate_area_column(zips)['full_rate_area'].unique()
rate_areas_rates = get_data_by_rate_area('AZ4', silver_with_full_rate_areas)
# full_silver = silver_with_full_rate_areas[silver_with_full_rate_areas.full_rate_area == 'AZ1']
print(rate_areas_rates['rate'])

az1_slcsp = get_slcsp_for_rate_area(rate_areas_rates)
print(az1_slcsp)