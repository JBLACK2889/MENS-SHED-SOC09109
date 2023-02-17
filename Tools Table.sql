CREATE TABLE Tools (
itemID INTEGER NOT NULL,
item VARCHAR2(100) NOT NULL,
catagory VARCHAR2(20), 
vis_test VARCHAR2(50),
pat_test VARCHAR2(50),
donated_by VARCHAR2(20),
date_listed DATE NOT NULL,
picture IMAGE,
ppe_needed BOOLEAN,
Restriced_item BOOLEAN,
training_needed BOOLEAN,
CONSTRAINT PK_ItemID PRIMARY KEY (itemID)
);