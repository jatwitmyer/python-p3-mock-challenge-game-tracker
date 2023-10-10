class Game:
    def __init__(self, title):
        self.title = title

        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, "title"):
            self._title = title
        else:
            raise Exception("Title must be a string, cannot be empty, and cannot be changed after being defined.")

    def results(self):
        return self._results

    def players(self):
        return list(set(self._players))

    def average_score(self, player):
        all_scores = [result.score for result in self._results if result.player == player]
        return sum(all_scores)/len(all_scores)

class Player:
    def __init__(self, username):
        self.username = username

        self._results = []
        self._games = []
    
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Username must be a string between 2 and 16 characters.")

    def results(self):
        return self._results

    def games_played(self):
        return list(set(self._games))

    def played_game(self, game):
        if game in self._games:
            return True
        else:
            return False

    def num_times_played(self, game):
        count = 0
        for _game in self._games:
            if game == _game:
                count = count + 1
        return count

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        Result.all.append(self)

        self.player._results.append(self)
        self.player._games.append(self.game)

        self.game._results.append(self)
        self.game._players.append(self.player)

    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        if isinstance(player, Player) and player not in Result.all:
            self._player = player
        else:
            raise Exception("Player must be an instance of the class Player.")
    
    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception("Game must be an instance of the class Game.")   

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, "score"):
            self._score = score
        else:
            raise Exception("Score must be an integer between 1 and 5000 and cannot be changed after being declared.")