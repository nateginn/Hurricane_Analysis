# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def format_large_number(number):
    suffixes = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion']
    suffix_index = 0

    if number < 0:
        sign = '-'
        number = abs(number)
    else:
        sign = ''

    while number >= 1000 and suffix_index < len(suffixes) - 1:
        number /= 1000
        suffix_index += 1

    if suffix_index == 0:
        formatted_number = f"{sign}{int(number)}"
    else:
        formatted_number = f"{sign}{number:,.0f} {suffixes[suffix_index]}"

    return formatted_number

# Initialize an empty list to store the converted values
converted_damages = []

def is_num(item):
    # Check if the item ends with 'M' or 'B' and the preceding characters are numeric
    return item[:-1].replace('.', '', 1).isdigit() and item[-1] in conversion

def convert_damages(damages, conversion):
    for item in damages:
        if is_num(item):
            numeric_value = float(item[:-1])
            suffix = item[-1]
            converted_value = numeric_value * conversion[suffix]
            converted_damages.append(converted_value)
        else:
            # If the item is not a numeric damage value, append it as is
            converted_damages.append(item)
    return converted_damages

# Test function by updating damages
adjusted_damages = convert_damages(damages, conversion)
print(adjusted_damages)
print('---------------------')

# 2 
# Create a Table
def combined_data(names, months, years, max_sustained_winds, areas_affected, deaths):
  hurricane_data = {}
  for i in range(len(names)):
    hurricane_data[names[i]] = {
      "Name": names[i],
      "Month": months[i],
      "Year": years[i],
      "Max Sustained Wind": max_sustained_winds[i],
      "Areas Affected": areas_affected[i],
      "Damage": converted_damages[i],
      "Deaths": deaths[i]
    }
  return hurricane_data

# Create and view the hurricanes dictionary
result = combined_data(names, months, years, max_sustained_winds, areas_affected, deaths)
print(result)
print('---------------------')
# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key
def hurricane_by_year(hurricane_data):
    yearly_data = {}
    for hurricane in hurricane_data.values():
        year = hurricane["Year"]
        if year not in yearly_data:
            yearly_data[year] = []
        yearly_data[year].append(hurricane)
    return yearly_data
  
org_by_year = hurricane_by_year(result)
print(org_by_year)
print('---------------------')

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def location_frequency(hurricane_data):
    frequency = {}
    for hurricane in hurricane_data.values():
        areas = hurricane["Areas Affected"]
        for area in areas:
            if area not in frequency:
                frequency[area] = 0
            frequency[area] += 1
    return frequency

frequency_by_area = location_frequency(result)
print(frequency_by_area)
print('---------------------')
      

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_affected_area(hurricane_data):
    frequency = {}
    total_deaths = {}
    
    # Count the frequency of affected areas
    for hurricane in hurricane_data.values():
        areas = hurricane["Areas Affected"]
        deaths = hurricane["Deaths"]
        for area in areas:
            if area not in frequency:
                frequency[area] = 0
                total_deaths[area] = 0
            frequency[area] += 1
            total_deaths[area] += deaths
    
    # Find the area with the highest frequency
    max_area = max(frequency, key=frequency.get)
    max_frequency = frequency[max_area]
    max_deaths = total_deaths[max_area]
    
    return max_area, max_frequency, max_deaths

# Call the function and print the result
result = combined_data(names, months, years, max_sustained_winds, areas_affected, deaths)
most_affected, frequency, total_deaths = most_affected_area(result)
print(f"The area affected by the most hurricanes is {most_affected}, which was hit {frequency} times, with a total of {total_deaths} deaths.")
print('---------------------')
# 6
# Calculating the Deadliest Hurricane
def death_toll(hurricane_data):
    area_deaths = {}
    for hurricane in hurricane_data.values():
        areas = hurricane["Areas Affected"]
        deaths = hurricane["Deaths"]
        for area in areas:
            if area not in area_deaths:
                area_deaths[area] = 0
            area_deaths[area] += deaths

    # Find the highest mortality hurricane and the number of deaths
    max_deaths = max(area_deaths.values())

    return area_deaths,  max_deaths

# Call the function and print the result
area_mortality_totals, max_deaths = death_toll(result)
# find highest mortality hurricane and the number of deaths
highest_mortality_hurricane = max(area_mortality_totals, key=area_mortality_totals.get)

print(f'Mortality numbers: {area_mortality_totals}')
print('---------------------')
print(f'The hurricane with the highest mortality was {highest_mortality_hurricane}, with {max_deaths} deaths.')
print('---------------------')

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                1: 100,
                2: 500,
                3: 1000,
                4: 10000}

# categorize hurricanes in new dictionary with mortality severity as key
def mortality_rating(hurricane_data):
  mortality_rating = {i:[] for i in range(6)}
  for hurricane in hurricane_data.values():
    name = hurricane["Name"]
    deaths = hurricane["Deaths"]
    if deaths == 0:
      mortality_rating[0].append(name)
    elif 0 < deaths <= 100:
      mortality_rating[1].append(name)
    elif 100 < deaths <=500:
      mortality_rating[2].append(name)
    elif 500 < deaths <=1000:
      mortality_rating[3].append(name)
    elif 1000 < deaths <=10000:
      mortality_rating[4].append(name)
    else:
      mortality_rating[5].append(name)

  return mortality_rating

print("Mortality/deaths rating (0-5):")
print(mortality_rating(result))
print("--------------")
      

# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def most_damage(hurricane_data):
    damage_amount = 0
    hurricane_name = None
    for hurricane in hurricane_data.values():
        damage = hurricane["Damage"]
        name = hurricane["Name"]
        if isinstance(damage, str):
          damage = 0
        if damage > damage_amount:
          damage_amount = damage
          hurricane_name = name
    return hurricane_name, damage_amount

hurricane_most_destructive, damage_amount = most_damage(result)
formatted_damages = format_large_number(damage_amount)
print(f'The hurricane which caused the most damage was: {hurricane_most_destructive} with ${damage_amount:,.0f} or ${formatted_damages} in damages.')
print('---------------------')

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def destruction_rating(hurricane_data):
  destruction_rating = {i:[] for i in range(6)}
  destruction_rating['Damages not recorded'] =[]

  for hurricane in hurricane_data.values():
    name = hurricane["Name"]
    damage = hurricane["Damage"]
    
    if damage == 'Damages not recorded':
          destruction_rating['Damages not recorded'].append(name)
    else:
      try:
        damage = float(damage)  
        if damage == 0:
          destruction_rating[0].append(name)
        elif 0 < damage <= 10000000:
          destruction_rating[1].append(name)
        elif 10000000 < damage <=1000000000:
          destruction_rating[2].append(name)
        elif 1000000000 < damage <=10000000000:
          destruction_rating[3].append(name)
        elif 10000000000 < damage <=50000000000:
          destruction_rating[4].append(name)
        else:
          destruction_rating[5].append(name)
      except ValueError:
        destruction_rating[5].append(name)

  return destruction_rating

print("Damages rating (0-5):")
print(destruction_rating(result))
print("--------------")

