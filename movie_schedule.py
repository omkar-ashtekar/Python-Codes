movies = {"IronMan": "10:00AM",
          "Thor": "12:00PM",
          "Captain America": "2:00PM",
          "Spiderman": "4:00PM"}

print("Following are the Movies showing in Theatre")
for key in movies:
    print(key)

movieName = input("What movie would you like the Showtime for?\n")
showTime = movies.get(movieName)

if showTime:
    print("Showtime of", movieName, "is", showTime)
else:
    print("No Screening for", movieName)
