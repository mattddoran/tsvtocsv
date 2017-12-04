/*SET SQL_SAFE_UPDATES = 0;
delete  
from cast_has_person_with_profession;
SET SQL_SAFE_UPDATES = 1;*/

/*alter table keyword
	drop foreign key idKeyword;

SHOW CREATE TABLE cast_has_person_with_profession;

alter table keyword
	add constaint idKeyword
    foreign key; 

ALTER TABLE keyword
	drop primary key,
    add primary key(idKeyword);

ALTER TABLE keyword
	add column idKeyword2 varchar(120) 
    after idKeyword;

select *
from keyword
limit 10;*/

select Title_idTitle, gross, castTotalFBLikes,budget
from title cross join metadata
where startYear > 1950 and idTitle = Title_idTitle;


select * from metadata where Title_idTitle = 82216;

select * from person where idPerson = 525908 or idPerson = 525910;

select * from cast_has_person_with_profession 
where Cast_idCast = 7227772;
    
alter table metadata
	drop column imdbScore;
    
select * from metadata;

select * from title where idTitle = 38;

alter table cast_has_person_with_profession
	drop foreign key fk_Cast_has_Person_Person1;