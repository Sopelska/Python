-- inserção de dados e queries
use ecommerce;

show tables;
-- idClient, Fname, Minit, Lname, CPF, Address
insert into Clients (Fname, Minit, Lname, CPF, Address)
	values('Maria','M','Silva', 12346789,'rua silva de prata 29, Carangola - Cidade das flores'),
		  ('Mateus','O','Pimentel', 987654321,'rua alemeda 289, centro - Cidade das flores'),
		  ('Ricardo','F','Silva', 45678913,'rua alemeda vinha 1009, centro - Cidade das flores'),
          ('Julia','S','França', 789123456,'larejras 861, centro - Cidade das flores'),
          ('Roberta','G','Assis', 98745631, 'avenida koller 19, centro - Cidade das flores'),
          ('Isabela','M','Cruz', 654789123, 'rua alemeda das flores 28, centro - Cidade das flores');
          

-- idProduct, Pname, classification_kids boolean, category('Eletrônico','Vestimenta','Brinquedos','Alimentos','Móveis'), avaliação, size
insert into product (Pname, classification_kids, category, avaliação, size)
						  values('Fone de ouvido',false,'Eletrônico','4',null),
                                ('Barbie Elsa',true,'Brinquedos','3',null),
                                ('Body Carters',true,'Vestimenta','5',null),
                                ('Microfone Vedo - Youtuber',false,'Eletrônico','4',null),
                                ('Sofá retrátil',false,'Móveis','3','3x57x80'),
                                ('Farinha de arroz',false,'Alimento','2',null,
                                ('Fire Stick Amazon',false,'Eletrônico','3',null);
                                

-- idOrder, idOrderClient, orderStatus, orderDescription, sendValue, paymentCash
insert into orders (idOrderClient, orderStatus, orderDescription, sendValue, paymentCash) values
							(1, default,'compra via aplicativo',null,1),
                            (2,default,'compra via aplicativo',50,0),
                            (3,'confirmado',null,null,1),
                            (4,default,'compra via web site',150,0);
                            
-- idPOproduct, idOorder, poQuantity, poStatus
select * from orders;
insert into productOrder (idPOproduct, idPOorder, poQuantity, poStatus) values
						 (1,5,2,null),
                         (2,5,1,null),
                         (3,6,1,null);
                         
-- storageLocation,quantity
insert into productStorage (storageLocation,quantity) values
							('Rio de Janeiro',1000),
                            ('Rio de Janeiro',500),
                            ('São Paulo',10),
                            ('São Paulo',100),
                            ('São Paulo',10),
                            ('Brasília',60);
                            
-- idLproduct, idLstorage, location
insert into storageLocation (idLproduct, idLstorage, location) values
						(1,2,'RJ'),
                        (2,6,'GO');
                        
-- idSupplier, SocialName, CNPJ, contact
insert into supplier (SocialName, CNPJ, contact) values
							('Almeida e filhos', 123456789123456,'21985474'),
                            ('Elwtrônicos Silva', 854519649143457,'21985484'),
                            ('Eletrônicos Valma', 934567893934695,'21975474');
                            
select * from supplier;
-- idPsSupplier, idPsProduct, quantity
insert into productSupplier (idPsSupplier, idPsProduct, quantity) values
						(1,1,500),
                        (1,2,400),
                        (2,4,633),
                        (3,3,5),
                        (2,5,10);
                        
-- idSeller, SocialName, AbstName, CNPJ, CPF, location, contact
insert into seller (SocialName, AbsName, CNPJ, CPF, Location, contact) values
						('Tech eletronics',null, 123456789456321, null, 'Rio de Janeiro', 219946287),
                        ('Botique Burgas',null,null,123456783,'Rio de Janeiro', 219567895),
                        ('Kids World',null,456789123654485,null,'São Paulo', 1198657484);
                        
 select * from seller;
 -- idPseller, idPproduct, prodQunatity
 insert into productSeller (idPseller, idPproduct, prodQuantity) values
						  (1,6,80),
                          (2,7,10);
                          
select * from productSeller;