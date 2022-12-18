# Create a dictionary with the countries as keys and the years they won as values
countries_and_years = {
  'Argentina': [1978, 1986],  
  'Brazil': [1958, 1962, 1970, 1994, 2002],
  'England': [1966],
  'France': [1998, 2018],
  'Germany': [1954, 1974, 1990, 2014],
  'Italy': [1934, 1938, 1982, 2006],
  'Spain': [2010],
  'Uruguay': [1930, 1950]
}

# Sort the dictionary by the number of trophies won (in descending order)
sorted_countries = sorted(countries_and_years.items(), key=lambda x: len(x[1]), reverse=True)

# Print the sorted list of countries and their winning years
for country, years in sorted_countries:
    print(f'{country}: {years}')