# Simple finds

1. Find all baseball leagues
def index(request):
	context = {
		"leagues": League.objects.filter(sport="Baseball"),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}

2. Find all womens' leagues
def index(request):
	context = {
		"leagues": League.objects.raw('SELECT * FROM leagues_League WHERE name like "%women%"'),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}

3. Find all leagues where sport is any type of hockey
def index(request):
	context = {
		"leagues": League.objects.raw('SELECT * FROM leagues_League WHERE sport like "%hockey%"'),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}

4. Find all leagues where sport is something OTHER THAN football
def index(request):
	context = {
		"leagues": League.objects.raw('SELECT * FROM leagues_League WHERE sport NOT like "%football%"'),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}

5. Find all leagues that call themselves "conferences"
def index(request):
	context = {
		"leagues": League.objects.raw('SELECT * FROM leagues_League WHERE name like "%conference%"'),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}

6. Find all leagues in the Atlantic region
def index(request):
	context = {
		"leagues": League.objects.raw('SELECT * FROM leagues_League WHERE name like "%atlantic%"'),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}

7. Find all teams based in Dallas
def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.filter(location="Dallas"),
		"players": Player.objects.all(),
	}

8. Find all teams named the Raptors
def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.filter(team_name="Raptors"),
		"players": Player.objects.all(),
	}

9. Find all teams whose location includes "City"
def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.raw('SELECT * FROM leagues_team WHERE location LIKE "%city%"'),
		"players": Player.objects.all(),
	}

10. Find all teams whose names begin with "T"
def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.filter(location__startswith="T"),
		"players": Player.objects.all(),
	}

11. Return all teams, ordered alphabetically by location
def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.order_by('location'),
		"players": Player.objects.all(),
	}

12. Return all teams, ordered by team name in reverse alphabetical order
def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.order_by('-team_name'),
		"players": Player.objects.all(),
	}

13. Find every player with last name "Cooper"
def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.filter(last_name='Cooper'),
	}

14. Find every player with first name "Joshua"
def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.filter(first_name='Joshua'),
	}

15. Find every player with last name "Cooper" EXCEPT FOR Joshua
def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua'),
	}

16. Find all players with first name "Alexander" OR first name "Wyatt"
def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.raw('SELECT * from leagues_Player WHERE first_name="Alexander" OR first_name="Wyatt"'),
	}