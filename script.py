highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# Splitting poems by commas (.split() method) -> this creates a list
highlighted_poems_list = highlighted_poems.split(",")

# Whitespace removal (.strip() method + for loop)
highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
# print(highlighted_poems_stripped)

# Break up the list into lists
highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(":"))
# print(highlighted_poems_details)

# Separating the titles, poets and dates
titles = []
poets = []
dates = []

for detail in highlighted_poems_details:
  titles.append(detail[0])
  poets.append(detail[1])
  dates.append(detail[2])

# Printing out the details for each poems (using .format())
for i in range(len(highlighted_poems_details)):
  print("The poem {} was published by {} in {}".format(titles[i], poets[i], dates[i]))
