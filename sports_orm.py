1...all baseball leagues
"leagues": League.objects.filter(sport="Baseball"),
2...all womens' leagues
"leagues": League.objects.filter(name__contains="Womens'"),
3...all leagues where sport is any type of hockey
"leagues": League.objects.filter(sport__contains="Hockey"),
4...all leagues where sport is something OTHER THAN football
"leagues": League.objects.exclude(sport="Football"),
5...all leagues that call themselves "conferences"
"leagues": League.objects.filter(name__contains="Conference"),
6...all leagues in the Atlantic region
"leagues": League.objects.filter(name__contains="Atlantic"),
7...all teams based in Dallas
"teams": Team.objects.filter(location="Dallas"),
8...all teams named the Raptors
"teams": Team.objects.filter(team_name="Raptors"),
9...all teams whose location includes "City"
"teams": Team.objects.filter(location__contains="City"),
10...all teams whose names begin with "T"
"teams": Team.objects.filter(team_name__startswith="T"),
11...all teams, ordered alphabetically by location
"teams": Team.objects.order_by("team_name"),
12...all teams, ordered by team name in reverse alphabetical order
"teams": Team.objects.order_by("-team_name"),
13...every player with last name "Cooper"
"players": Player.objects.filter(last_name="Cooper"),
14...every player with first name "Joshua"
"players": Player.objects.filter(first_name="Joshua"),
15...every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
"players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
16...all players with first name "Alexander" OR first name "Wyatt"
"players": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt"),