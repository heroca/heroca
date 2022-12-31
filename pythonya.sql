CREATE TABLE `articulos` (
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) DEFAULT NULL,
  `precio` float DEFAULT NULL,
  PRIMARY KEY (`codigo`)
);

insert into `articulos` values (1,'papas',15);
insert into `articulos` values (2,'manzanas',24);
insert into `articulos` values (3,'peras',45.3);
insert into `articulos` values (4,'naranjas',22);
insert into `articulos` values (5,'pomelos',29);
insert into `articulos` values (6,'frutillas',130);
insert into `articulos` values (7,'anana',75);