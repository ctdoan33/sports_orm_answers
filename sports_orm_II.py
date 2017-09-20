1...all teams in the Atlantic Soccer Conference
"teams": Team.objects.filter(league__name="Atlantic Soccer Conference"),
2...all (current) players on the Boston Penguins
"players": Player.objects.filter(curr_team__location="Boston", curr_team__team_name="Penguins"),
3...all (current) players in the International Collegiate Baseball Conference
"players": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
4...all (current) players in the American Conference of Amateur Football with last name "Lopez"
"players": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football").filter(last_name="Lopez"),
5...all football players
"players": Player.objects.filter(curr_team__league__sport="Football"),
6...all teams with a (current) player named "Sophia"
"teams": Team.objects.filter(curr_players__first_name="Sophia"),
7...all leagues with a (current) player named "Sophia"
"leagues": League.objects.filter(teams__curr_players__first_name="Sophia"),
8...everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
"players": Player.objects.filter(last_name="Flores").exclude(curr_team__location="Washington", curr_team__team_name="Roughriders"),
9...all teams, past and present, that Samuel Evans has played with
"teams": Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
10...all players, past and present, with the Manitoba Tiger-Cats
"players": Player.objects.filter(all_teams__location="Manitoba", all_teams__team_name="Tiger-Cats"),
11...all players who were formerly (but aren't currently) with the Wichita Vikings
"players": Player.objects.filter(all_teams__location="Wichita", all_teams__team_name="Vikings").exclude(curr_team__location="Wichita", curr_team__team_name="Vikings"),
12...every team that Jacob Gray played for before he joined the Oregon Colts
"teams": Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(location="Oregon", team_name="Colts"),
13...everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
"players": Player.objects.filter(first_name="Joshua").filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players"),
14...all teams that have had 12 or more players, past and present. (HINT: Look up the Django annotate function.)
from django.db.models import Count
"teams": Team.objects.annotate(total_players=Count("all_players")).filter(total_players__gte=12),
15...all players and count of teams played for, sorted by the number of teams they've played for
"players": Player.objects.annotate(total_teams=Count("all_teams")).order_by("total_teams")
{{player.total_teams}} in for loop of html