CREATE TABLE Main_Table (
    id int AUTO_INCREMENT PRIMARY KEY,
    BTS varchar(150) DEFAULT NULL,
    Terminals varchar(150) DEFAULT NULL,
    Servers varchar(150) DEFAULT NULL,
    Services varchar(150) DEFAULT NULL,
    Others varchar(150) DEFAULT NULL,
    Remarks varchar(500) DEFAULT NULL 
);
CREATE TABLE Terminals (
    id int AUTO_INCREMENT PRIMARY KEY,
    Database_name varchar(150) DEFAULT NULL,
    Model varchar(150) DEFAULT NULL,
    Format varchar(150) DEFAULT NULL,
    OS varchar(150) DEFAULT NULL,
    Display varchar(150) DEFAULT NULL,
    Mobile varchar(150) DEFAULT NULL,
    LTE_Mode varchar(150) DEFAULT NULL,
    Radio varchar(150) DEFAULT NULL,
    WiFi varchar(150) DEFAULT NULL,
    SIM varchar(150) DEFAULT NULL,
    GEO varchar(150) DEFAULT NULL,
    Li_ion varchar(150) DEFAULT NULL,
    Protect varchar(150) DEFAULT NULL,
    Mass varchar(150) DEFAULT NULL,
    Equipment varchar(150) DEFAULT NULL,
    Description varchar(150) DEFAULT NULL,
    Remarks varchar(500) DEFAULT NULL 
);
CREATE TABLE Others (
        id int AUTO_INCREMENT PRIMARY KEY,
        Category varchar(150) DEFAULT NULL,
        Database_name varchar(150) DEFAULT NULL,
        Product varchar(150) DEFAULT NULL,
        Description varchar(150) DEFAULT NULL,
        Remarks varchar(150) DEFAULT NULL
);
CREATE TABLE Servers (
    id int AUTO_INCREMENT PRIMARY KEY,
    DataBase_name varchar(150) DEFAULT NULL,
    Model varchar(150) DEFAULT NULL,
    Users varchar(150) DEFAULT NULL,
    Design varchar(150) DEFAULT NULL,
    Description varchar(150) DEFAULT NULL,
    Remarks varchar(500) DEFAULT NULL 
);
CREATE TABLE BTS (
   id int AUTO_INCREMENT PRIMARY KEY,
   DataBase_name varchar(150) DEFAULT NULL,
   Product varchar(150) DEFAULT NULL,
   Work_Type varchar(150) DEFAULT NULL,
   Band varchar(150) DEFAULT NULL,
   Tx_Rx varchar(150) DEFAULT NULL,
   Output_Power varchar(150) DEFAULT NULL,
   Power_Consumption varchar(150) DEFAULT NULL,
   Power_Supply varchar(150) DEFAULT NULL,
   Vendor varchar(150) DEFAULT NULL,
   Model varchar(150) DEFAULT NULL,
   Design varchar(150) DEFAULT NULL,
   Description varchar(150) DEFAULT NULL,
   Remarks varchar(500) DEFAULT NULL
);
CREATE TABLE Services (
    id int AUTO_INCREMENT PRIMARY KEY,
    Database_name varchar(150) DEFAULT NULL,
    Product varchar(150) DEFAULT NULL,
    Description varchar(150) DEFAULT NULL,
    Remarks varchar(500) DEFAULT NULL 
);
CREATE TABLE Additional (
    id int AUTO_INCREMENT PRIMARY KEY,
    DataBase_name varchar(150) DEFAULT NULL,
    Product varchar(150) DEFAULT NULL,
    Description varchar(150) DEFAULT NULL,
    Vendor varchar(150) DEFAULT NULL,   
    Remarks varchar(500) DEFAULT NULL 
);


