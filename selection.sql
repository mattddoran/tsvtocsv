select * 
from mydb2.genres cross join  mydb2.titlegenres cross join mydb2.title
where genres.idGenre = 5 and genres.idGenre = titlegenres.Genres_idGenre and title.idTitle = titlegenres.Title_idTitle and title.idTitle > 3000000;
-- good to go

