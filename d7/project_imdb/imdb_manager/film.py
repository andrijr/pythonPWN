def zero_if_none(val):
    if val is None:
        return 0
    else:
        return val


def empty_list_if_none(val):
    if val is None:
        return []
    else:
        return val


class Person:
    """
    Holds data about person
    """
    def __init__(self, first_name, last_name, nationality=None):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality


class Genre:
    """
    Holds data about genre
    """
    def __init__(self, name):
        self.name = name


class Film:
    """
    Holds information about one film
    """

    def __init__(self,
                 title,
                 rel_year=None,
                 duration=None,
                 director=None,
                 rating=None,
                 voters=None,
                 ranking=None,
                 orig_title=None,
                 actors=None,
                 genres=None):
        """
        Film constructor
        :param title: film title string
        :param rel_year: release year - string  or int (converted to int)
        :param duration: string with duration
        :param actors: list of strings with actors names
        :param director: string with directors name
        :param rating: string with rating
        :param ranking: string with ranking
        :param voters: string with voters
        :
        :return:
        """

        self.title = title

        if type(rel_year) == 'int':
            self.rel_year = self.rel_year
        else:
            self.rel_year = int(rel_year)

        self.duration = zero_if_none(duration)
        self.director = director
        self.actors = empty_list_if_none(actors)
        self.rating = zero_if_none(rating)
        self.voters = zero_if_none(voters)
        self.ranking = zero_if_none(ranking)
        self.orig_title = orig_title
        self.genres = empty_list_if_none(genres)

#
# if __name__ == "__main__":
#     film = Film(title='Skazani na shawshank',
#                 rel_year='1994')
