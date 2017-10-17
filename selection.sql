/*select *
from (
select genres.genre, title.idTitle, rating.numVotes, rating.averageRating
from mydb2.genres cross join  mydb2.titlegenres cross join mydb2.title cross join mydb2.rating
where genres.idGenre = titlegenres.Genres_idGenre and title.idTitle = titlegenres.Title_idTitle and rating.Title_idTitle = title.idTitle and title.isAdult = 1 and rating.averageRating > 8 and rating.numVotes > 10 and genres.genre != 'Adult'
) A 
order by numVotes ASC;
-- good to go*/

/*select genres.genre, count(*) as 'Number of Titles', sum(rating.numVotes) as 'Sum of votes for all Titles in this Genre' -- distinct genres.genre
from mydb2.genres cross join  mydb2.titlegenres cross join mydb2.title cross join mydb2.rating
where genres.idGenre = titlegenres.Genres_idGenre and title.idTitle = titlegenres.Title_idTitle and rating.Title_idTitle = title.idTitle and title.isAdult = 1 and rating.averageRating > 8 and rating.numVotes > 10 and genres.genre != 'Adult'
group by genres.idGenre
order by sum(rating.numVotes) Desc;*/
-- order by numVotes ASC;

select count(*) as 'Number of Titles'
from mydb2.titlegenres
group by mydb2.titlegenres.Title_idTitle
order by count(*) desc;

select episode.idParent, rating.averageRating
from rating cross join title cross join episode
where rating.Title_idTitle = title.idTitle and title.idTitle = episode.idParent and rating.averageRating > 9;

-- set @@NET_READ_TIMEOUT=100;
