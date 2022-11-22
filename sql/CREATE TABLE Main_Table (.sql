CREATE TABLE Main_Table (
    id int IDENTITY(1, 1) PRIMARY KEY,
    BTS varchar(150) DEFAULT NULL,
    Terminals varchar(150) DEFAULT NULL,
    Servers varchar(150) DEFAULT NULL,
    Services varchar(150) DEFAULT NULL,
    Others varchar(150) DEFAULT NULL,
    Remarks varchar(500) DEFAULT NULL 
);