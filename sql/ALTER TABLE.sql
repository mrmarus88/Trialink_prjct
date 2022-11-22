ALTER TABLE dbo.BTS  /* add column */
ADD TempID VARCHAR(20) NULL, TempID_2 INT NULL ;

ALTER TABLE dbo.BTS  /* add relationship */
   ADD CONSTRAINT FK_TempID_BTS FOREIGN KEY (TempID)
      REFERENCES dbo.Main_Table (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
;
