add_person_query = """
INSERT INTO %s (firstName, lastName, nationality) VALUES ('%s', '%s', '%s');
"""

get_person_id_query = """
select ID from %s where firstName='%s' and lastName='%s' order by ID limit 1;
"""

add_genre_query = """
INSERT INTO genre (genreName) VALUES ('%s');
"""

get_genre_id_query = """
SELECT ID FROM genre where genreName = '%s';
"""

add_film_row_query = """
INSERT INTO film (title, relYear, durationMins, rating, voters, ranking, directorID) VALUES
('%s', %s, %s, %s, %s, %s, %s);
"""

add_actor_in_film_row = """
INSERT INTO actor_in_film (filmID, actorID) VALUES (%s, %s);
"""

add_film_has_genre_row = """
INSERT INTO film_has_genre (filmID, genreID) VALUES (%s, %s);
"""