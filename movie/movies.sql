create user dbadmin identified WITH ‘administrator’;
grant all on djangodatabase.* to ‘dbadmin@localhost;
flush privileges;
