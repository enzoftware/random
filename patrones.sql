use patrones_pc2;

create table cuenta (id int primary key not null,nombre varchar(45), saldo  double(10,2) not null check(saldo>=0)  , agencia varchar(45), operacion varchar(45));

insert into cuenta values(1,'luis',300,'la molina','abono');
insert into cuenta values(2,'nadia',500,'san isidro','abono');
insert into cuenta values(3,'janett',240,'san isidro','abono');
insert into cuenta values(4,'pedro',600,'la molina','abono');
insert into cuenta values(5,'fabricio',400,'san borja','abono');
insert into cuenta values(6,'carlos',900,'san borja','abono');
insert into cuenta values(7,'marian',350,'la molina','abono');
insert into cuenta values(8,'alberto',600,'san isidro','abono');
insert into cuenta values(9,'juan',450,'la molina','abono');
insert into cuenta values(10,'javier',700,'san borja','abono');
insert into cuenta values(11,'mary',650,'la molina','abono');
insert into cuenta values(12,'cris',300,'san borja','abono');	


delete from cuenta;

select * from cuenta;

alter table cuenta drop column id;

alter table cuenta add column id int not null;

insert into cuenta values('alberto',500,'','abono');
insert into cuenta values('marian',200,'','retiro');
insert into cuenta values('mary',200,'','abono');
insert into cuenta values('carlos',300,'','retiro');

/* Agregar datos */

insert into cuenta values('fabricio',400,'san borja','abono',1);
insert into cuenta values('carlos',900,'san borja','abono',2);
insert into cuenta values('marian',350,'la molina','abono',3);
insert into cuenta values('alberto',600,'san isidro','abono',4);
insert into cuenta values('juan',450,'la molina','abono',5);
insert into cuenta values('javier',700,'san borja','abono',6);
insert into cuenta values('mary',650,'la molina','abono',7);
insert into cuenta values('cris',300,'san borja','abono',8);	
insert into cuenta values('cristiano',-300,'san borja','abono',9);	


select * from cuenta where id % 2 != 0 and agencia = 'la molina' and saldo >= 300;

select (cuenta.agencia) as agen, ( select count(*) from cuenta where cuenta.agencia=agen) as clientes, 
(select SUM(cuenta.saldo) from cuenta where cuenta.agencia=agen) as saldo
 from cuenta
 group by cuenta.agencia;
 
 
