-- Highest Rated T.V. series
select distinct (title.primaryTitle), rating.averageRating
from rating cross join title cross join episode
where rating.averageRating = 10 and rating.Title_idTitle = title.idTitle and title.idTitle = episode.idParent;

-- After 2000 popular
select genres.genre, count(*) as 'Number of Titles', sum(rating.numVotes) as 'Sum of votes for all Titles in this Genre' -- distinct genres.genre
from mydb2.genres cross join  mydb2.titlegenres cross join mydb2.title cross join mydb2.rating
where genres.idGenre = titlegenres.Genres_idGenre and title.idTitle = titlegenres.Title_idTitle and title.startYear > 2000 and rating.Title_idTitle = title.idTitle and rating.averageRating > 6 and rating.numVotes > 10 
group by genres.idGenre
order by count(*) Desc;

-- Highest Seasons
select rating.averageRating, title.primaryTitle, episode.season
from rating cross join title cross join episode
where rating.Title_idTitle = title.idTitle and title.idTitle = episode.idParent and episode.season > 6 and episode.season < 2000
group by episode.idParent
order by episode.season desc;

-- Adult
select genres.genre, count(*) as 'Number of Titles', sum(rating.numVotes) as 'Sum of votes for all Titles in this Genre'
from mydb2.genres cross join  mydb2.titlegenres cross join mydb2.title cross join mydb2.rating
where genres.idGenre = titlegenres.Genres_idGenre and title.idTitle = titlegenres.Title_idTitle and rating.Title_idTitle = title.idTitle and title.isAdult = 1 and rating.averageRating > 8 and rating.numVotes > 10 and genres.genre != 'Adult'
group by genres.idGenre
order by sum(rating.numVotes) Desc;
-- order by numVotes ASC;

-- Negative Rating Genre
select genres.genre, count(*) as 'Number of Titles', sum(rating.numVotes) as 'Sum of votes for all Titles in this Genre'
from mydb2.genres cross join  mydb2.titlegenres cross join mydb2.title cross join mydb2.rating
where genres.idGenre = titlegenres.Genres_idGenre and title.idTitle = titlegenres.Title_idTitle and rating.Title_idTitle = title.idTitle and rating.averageRating < 2 and rating.numVotes > 10 
group by genres.idGenre
order by sum(rating.numVotes) Desc;




/*select genres.genre, count(*) as 'Number of Titles', sum(rating.numVotes) as 'Sum of votes for all Titles in this Genre' -- distinct genres.genre
from mydb2.genres cross join  mydb2.titlegenres cross join mydb2.title cross join mydb2.rating
where genres.idGenre = titlegenres.Genres_idGenre and title.idTitle = titlegenres.Title_idTitle and rating.Title_idTitle = title.idTitle and rating.averageRating < 2 and rating.numVotes > 10 
group by genres.idGenre
order by sum(rating.numVotes) Desc;

select genres.genre, count(*) as 'Number of Titles', sum(rating.numVotes) as 'Sum of votes for all Titles in this Genre' -- distinct genres.genre
from mydb2.genres cross join  mydb2.titlegenres cross join mydb2.title cross join mydb2.rating
where genres.idGenre = titlegenres.Genres_idGenre and title.idTitle = titlegenres.Title_idTitle and title.startYear > 2000 and rating.Title_idTitle = title.idTitle and rating.averageRating > 6 and rating.numVotes > 10 
group by genres.idGenre
order by count(*) Desc;*/


/*select genres.genre, count(*) as 'num of that genre'
from genres cross join titlegenres cross join (
select distinct title.idTitle as 'idTitle'
from title cross join episode
where idTitle = episode.idParent
) A 
where genres.idGenre = titlegenres.Genres_idGenre and A.idTitle = titlegenres.Title_idTitle
group by titlegenres.Genres_idGenre
order by count(*) desc;*/
-- order by rating.averageRating desc;

/*select count(*) as 'Number of Titles'
from mydb2.titlegenres
group by mydb2.titlegenres.Title_idTitle
order by count(*) desc;*/

/*select *
from (
select genres.genre, title.idTitle, rating.numVotes, rating.averageRating
from mydb2.genres cross join  mydb2.titlegenres cross join mydb2.title cross join mydb2.rating
where genres.idGenre = titlegenres.Genres_idGenre and title.idTitle = titlegenres.Title_idTitle and rating.Title_idTitle = title.idTitle and title.isAdult = 1 and rating.averageRating > 8 and rating.numVotes > 10 and genres.genre != 'Adult'
) A 
order by numVotes ASC;
-- good to go*/

/*select episode.idParent, rating.averageRating, title.primaryTitle, sum(title.runtime) as 'combined runtime of all episodes in a series'
from rating cross join title cross join episode
where rating.averageRating = 10 and rating.Title_idTitle = title.idTitle and title.idTitle = episode.idParent
group by episode.idParent
order by sum(title.runtime) desc;*/
/*select episode.idParent, rating.averageRating, title.primaryTitle, sum(title.runtime) as 'combined runtime of all episodes in a series'
from rating cross join title cross join episode
where rating.averageRating = 10 and rating.Title_idTitle = title.idTitle and title.idTitle = episode.idParent
group by episode.idParent
order by sum(title.runtime) desc;
SELECT SLEEP(5);*/

-- set @@NET_READ_TIMEOUT=100;
