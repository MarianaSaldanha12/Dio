Projeto de banco de dados para E-commerce

Descriçào do projeto
Este projeto visa criar um banco de dados para um sistema de e-commerce. O objetivo é modelar as entidades e relacionamentos relevantes para suportar 
as operações de compra, venda e gerenciamento de produtos em uma plataforma de comércio eletrônico.

Esquema Lógico do Banco de Dados
O esquema lógico do banco de dados é composto por várias tabelas que representam entidades fundamentais do sistema de e-commerce. 
Aqui está uma visão geral das tabelas principais:

clients: Armazena informações sobre os clientes, como nome, CPF e endereço.
product: Contém informações sobre os produtos disponíveis para venda, incluindo nome, categoria, avaliação e tamanho.
payments: Registra os métodos de pagamento associados a cada cliente.
orders: Armazena detalhes sobre os pedidos feitos pelos clientes, como status, descrição e frete.
productsStorage: Mantém o controle do estoque de produtos em diferentes locais de armazenamento.
Supplier: Registra informações sobre os fornecedores de produtos.
Seller: Armazena dados sobre os vendedores que oferecem produtos na plataforma.
ProductSeller: Relaciona produtos a vendedores e inclui detalhes como quantidade disponível.
ProductOrder: Relaciona produtos a pedidos feitos pelos clientes e inclui detalhes como quantidade e status.
StorageLocation: Registra os locais de armazenamento dos produtos.
productSupplier: Estabelece a relação entre produtos e fornecedores, incluindo detalhes como quantidade disponível.

Scripts SQL
Os scripts SQL utilizados para criar o banco de dados, criar tabelas, inserir dados e realizar consultas estão disponíveis neste repositório. 
Aqui está uma breve descrição de cada script:

create_database.sql: Script fornecido para criar o banco de dados "ecommerce".
create_tables.sql: Script para criar todas as tabelas necessárias no banco de dados.
insert_data.sql: Script para inserir dados de exemplo nas tabelas para fins de teste.
queries.sql: Script contendo consultas SQL para recuperar informações específicas do banco de dados.

-- Criação do Banco de Dados para um cenário de E-commerce
create database ecommerce;
use ecommerce;
-- Criação de tabelas
-- tabela cliente
create table clients(
	idClient int auto_increment primary key,
    Fname varchar(10),
    Mname char(3),
    Lname varchar(20),
    CPF char(11) not null,
    Adress varchar(30),
    constraint unique_cpf_client unique (CPF)
);
desc clients;
alter table clients auto_increment=1;

-- tabela produto
-- size = dimensão do produto
create table product(
	idProduct int auto_increment primary key,
    Pname varchar(10) not null,
    Classification_kids bool default false,
    Category enum('Eletrônico','Vestuário','Brinquedos','Alimentos','Móveis') not null,
    Avaliation float default 0,
    Size varchar(10)
);
desc product;

-- tabela pedido
create table orders(
	idOrders int auto_increment primary key,
    idOrdersClient int,
    OrdersStatus enum('Cancelado','Confirmado','Em processamento') default 'Em processamento',
    OrdersDescription varchar(255),
    OrdersFreight float default 10,
    PaymentCash bool default false,
    constraint fk_orders_cliente foreign key(idOrdersClient) references clients(idClient)
);
desc orders;
-- tabela estoque
create table productsStorage(
	idProductsStorage int auto_increment primary key,
    StorageLocation varchar(255),
    Quantity int default 0
);
desc productsStorage;
-- tabela fornecedor
create table Supplier(
	idSupplier int auto_increment primary key,
    SocialNameSupplier varchar(255) not null,
    CNPJSupplier char(15) not null,
    ContactSupplier char(11) not null,
    constraint unique_supplier unique (CNPJSupplier)
);
desc Supplier;
-- tabela vendedor
create table Seller(
	idSeller int auto_increment primary key,
    SocialNameSeller varchar(255) not null,
    AbstName varchar(255),
    CNPJSeller char(15),
    CPFSeller char(9),
    Location varchar(255),
    ContactSeller char(11) not null,
    constraint unique_cnpj_seller unique (CNPJSeller),
    constraint unique_cpf_seller unique (CPFSeller)
);
desc Seller;
-- tabela produto vendedor
create table ProductSeller(
	idProductSeller int,
    idPproduct int,
    ProductQuantity int default 1,
    primary key(idProductSeller, idPproduct),
    constraint fk_product_seller foreign key(idProductSeller) references Seller(idSeller),
    constraint fk_product_product foreign key(idPproduct) references product(idProduct)
);
desc ProductSeller;
-- tabela produto pedido
create table ProductOrder(
	idProdOrder int,
    idProductOrder int,
    ProductOrderQuantity int default 1,
    ProductOrderStatus enum('Disponível','Sem estoque') default 'Disponível',
    primary key(idProdOrder, idProductOrder),
    constraint fk_productorder_seller foreign key (idProdOrder) references product(idProduct),
    constraint fk_productorder_product foreign key (idProductOrder) references orders(idOrders)
    );
    desc ProductOrder;
-- tabela local estoque
create table StorageLocation(
	idLproduct int,
    idLStorage int,
    location varchar(255) not null,
    primary key(idLproduct, idLStorage),
    constraint fk_productstorage_seller foreign key(idLproduct) references product(idProduct),
    constraint fk_productstorage_product foreign key(idLStorage) references productsStorage(idProductsStorage)
);
-- tabela produto fornecedor
create table productSupplier(
	idPsSupplier int,
    idPsProduct int,
    ProductSupplierQuantity int not null,
    primary key(idPsSupplier, idPsProduct),
    constraint fk_product_supplier_supplier foreign key(idPsSupplier) references Supplier(idSupplier),
    constraint fk_product_supplier_product foreign key(idPsProduct) references product(idProduct)
);

Populaçào de dados no bando de dados:

-- Inserção de dados na tabela clients
INSERT INTO clients (Fname, Mname, Lname, CPF, Adress) VALUES
('Ana', NULL, 'Pereira', '45678901234', 'Rua B, 456'),
('Carlos', 'C', 'Ferreira', '56789012345', 'Av. Secundária, 789'),
('Luisa', 'D', 'Costa', '67890123456', 'Rua C, 789'),
('João', 'A', 'Silva', '12345678901', 'Rua A, 123'),
('Maria', 'B', 'Santos', '23456789012', 'Av. Principal, 456'),
('Pedro', NULL, 'Oliveira', '34567890123', 'Praça Central, 789');

-- Inserção de dados na tabela product
INSERT INTO product (Pname, Classification_kids, Category, Avaliation, Size) VALUES
('Notebook', false, 'Eletrônico', 4.7, '15x10x1'),
('Jeans', false, 'Vestuário', 4.1, 'G'),
('QCabeça', true, 'Brinquedos', 4.5, 'Grande'),
('Celular', false, 'Eletrônico', 4.5, '10x5x1'),
('Camiseta', true, 'Vestuário', 4.2, 'M'),
('Bola', true, 'Brinquedos', 4.8, 'Único');

-- Inserção de dados na tabela orders
INSERT INTO orders (idOrdersClient, OrdersDescription) VALUES
(1, 'Pedido 1: Notebook e Calça Jeans'),
(2, 'Pedido 2: Quebra-Cabeça'),
(3, 'Pedido 3: Notebook e Quebra-Cabeça'),
(4, 'Pedido 1: Celular e Camiseta'),
(5, 'Pedido 2: Bola'),
(6, 'Pedido 3: Celular e Bola');

-- Inserção de dados na tabela productsStorage
INSERT INTO productsStorage (StorageLocation, Quantity) VALUES
('Depósito D', 20),
('Depósito E', 40),
('Depósito F', 10),
('Depósito A', 50),
('Depósito B', 20),
('Depósito C', 0);

-- Inserção de dados na tabela Supplier
INSERT INTO Supplier (SocialNameSupplier, CNPJSupplier, ContactSupplier) VALUES
('Fornecedor A', '12345678901234', '123456789'),
('Fornecedor B', '23456789012345', '234567890');

-- Inserção de dados na tabela Seller
INSERT INTO Seller (SocialNameSeller, AbstName, CNPJSeller, CPFSeller, Location, ContactSeller) VALUES
('Vendedor X', NULL, '34567890123456', '345678901', 'Loja 1', '345678901'),
('Vendedor Y', NULL, '45678901234567', '456789012', 'Loja 2', '456789012');


-- Inserção de dados na tabela ProductSeller
INSERT INTO ProductSeller (idProductSeller, idPproduct, ProductQuantity) VALUES
(1, 1, 30),  
(1, 3, 20),  
(2, 2, 25),  
(3, 1, 10),
(3, 3, 15), 
(4, 4, 20),
(5, 6, 10),
(5, 5, 30);


-- Inserção de dados na tabela ProductOrder
INSERT INTO ProductOrder (idProdOrder, idProductOrder, ProductOrderQuantity, ProductOrderStatus) VALUES
(1, 1, 1, 'Disponível'),
(1, 2, 2, 'Disponível'),
(2, 3, 1, 'Disponível'),
(3, 1, 1, 'Disponível'),
(3, 3, 1, 'Disponível'),
(4, 4, 1, 'Disponível'),
(4, 5, 2, 'Sem estoque'),
(5, 6, 1, 'Disponível'),
(6, 4, 1, 'Disponível'),
(6, 6, 1, 'Sem estoque');

-- Inserção de dados na tabela StorageLocation
INSERT INTO StorageLocation (idLproduct, idLStorage, location) VALUES
(1, 1, 'Depósito D'),
(2, 2, 'Depósito E'),
(3, 3, 'Depósito F'),
(4, 4, 'Depósito A'),
(5, 5, 'Depósito B'),
(6, 6, 'Depósito C');

-- Inserção de dados na tabela productSupplier
INSERT INTO productSupplier (idPsSupplier, idPsProduct, ProductSupplierQuantity) VALUES
(1, 1, 40),
(2, 3, 30),
(3, 1, 100),
(4, 6, 50);


Perguntas de Negócio e Consultas SQL

Perguntas de Negócio:
Quais são os produtos mais vendidos no último mês?

SELECT p.Pname, SUM(po.ProductOrderQuantity) AS TotalVendas
FROM product p
JOIN ProductOrder po ON p.idProduct = po.idProdOrder
WHERE MONTH(po.Date) = MONTH(CURRENT_DATE()) AND YEAR(po.Date) = YEAR(CURRENT_DATE())
GROUP BY p.idProduct
ORDER BY TotalVendas DESC;

Qual é o total de vendas por categoria de produto?

SELECT p.Category, SUM(po.ProductOrderQuantity) AS TotalVendas
FROM product p
JOIN ProductOrder po ON p.idProduct = po.idProdOrder
GROUP BY p.Category;

Quais clientes têm o maior histórico de compras?

SELECT c.idClient, CONCAT(c.Fname, ' ', c.Lname) AS NomeCliente, COUNT(*) AS TotalCompras
FROM clients c
JOIN orders o ON c.idClient = o.idOrdersClient
GROUP BY c.idClient
ORDER BY TotalCompras DESC;

Quais são os fornecedores mais importantes em termos de quantidade de produtos fornecidos?

SELECT s.SocialNameSupplier, COUNT(*) AS TotalProdutosFornecidos
FROM Supplier s
JOIN productSupplier ps ON s.idSupplier = ps.idPsSupplier
GROUP BY s.idSupplier
ORDER BY TotalProdutosFornecidos DESC;

Qual é o total de vendas por vendedor?

SELECT s.idSeller, CONCAT(s.SocialNameSeller, ' - ', s.Location) AS NomeVendedor, SUM(po.ProductOrderQuantity) AS TotalVendas
FROM Seller s
JOIN ProductSeller ps ON s.idSeller = ps.idProductSeller
JOIN ProductOrder po ON ps.idPproduct = po.idProductOrder
GROUP BY s.idSeller
ORDER BY TotalVendas DESC;

Consultas SQL:
Recuperação simples de todos os clientes:

SELECT * FROM clients;

Recuperação de produtos eletrônicos com avaliação maior que 4:

SELECT * FROM product WHERE Category = 'Eletrônico' AND Avaliation > 4;

Recuperação dos pedidos confirmados, ordenados pelo valor do frete de forma decrescente:

SELECT * FROM orders WHERE OrdersStatus = 'Confirmado' ORDER BY OrdersFreight DESC;

Recuperação dos produtos que têm estoque inferior a 10 unidades:

SELECT * FROM productsStorage WHERE Quantity < 10;

Recuperação dos clientes que fizeram pedidos com frete acima de 20 reais, mostrando também o total gasto por cada cliente:

SELECT c.*, SUM(o.OrdersFreight) AS TotalFrete 
FROM clients c
JOIN orders o ON c.idClient = o.idOrdersClient
WHERE o.OrdersFreight > 20
GROUP BY c.idClient;

Recuperação dos produtos vendidos por um determinado vendedor, mostrando o total de vendas de cada produto e o total de vendas por vendedor:

SELECT s.SocialNameSeller, p.Pname, SUM(po.ProductOrderQuantity) AS TotalVendasProduto, 
       SUM(po.ProductOrderQuantity) AS TotalVendasVendedor
FROM Seller s
JOIN ProductSeller ps ON s.idSeller = ps.idProductSeller
JOIN product p ON ps.idPproduct = p.idProduct
JOIN ProductOrder po ON p.idProduct = po.idProdOrder
GROUP BY s.idSeller, p.idProduct;

Recuperação dos produtos que não têm estoque disponível e estão na categoria de eletrônicos, mostrando também o fornecedor de cada produto:

SELECT p.*, s.SocialNameSupplier
FROM product p
JOIN productSupplier ps ON p.idProduct = ps.idPsProduct
JOIN Supplier s ON ps.idPsSupplier = s.idSupplier
JOIN ProductOrder po ON p.idProduct = po.idProdOrder
WHERE po.ProductOrderStatus = 'Sem estoque' AND p.Category = 'Eletrônico';

Recuperação dos produtos que tiveram mais de 50 unidades vendidas, ordenados pelo total de vendas de forma decrescente:

SELECT p.*, SUM(po.ProductOrderQuantity) AS TotalVendas
FROM product p
JOIN ProductOrder po ON p.idProduct = po.idProdOrder
GROUP BY p.idProduct
HAVING TotalVendas > 50
ORDER BY TotalVendas DESC;
