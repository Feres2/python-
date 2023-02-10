SELECT * FROM useres_schema.useres;
INSERT INTO `useres_schema`.`useres` (`first_name`, `last_name`, `email`)
 VALUES ('ousema', 'joe', 'ousemma@gmail.com'),
 ('julia', 'joe', 'juliaa@gmail.com');
 select first_name,last_name FROM useres_schema.useres;
 select * from useres_schema.useres where email='feres@gmail.com';
select * from useres_schema.useres where id=3;
UPDATE useres_schema.useres
SET last_name='panckaces'
WHERE id=3;
DELETE FROM useres_schema.useres WHERE id=2;
select first_name FROM useres_schema.useres;


