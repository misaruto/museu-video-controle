IF NOT EXISTS(SELECT 1 FROM sys.tables WHERE NAME = 'rmi_server')
BEGIN
  CREATE TABLE museu.dbo.rmi_server (
    id_rmi_server BIGINT NOT NULL IDENTITY(1,1),
    nm_rmi_server VARCHAR(30) NOT NULL,
    nm_rmi_server_uri VARCHAR(60) NOT NULL,
    dt_created DATETIME NOT NULL DEFAULT GETDATE(),
    dt_disabled DATETIME NULL,
    in_active BIT NOT NULL DEFAULT 1,
    CONSTRAINT PK_rmi_server PRIMARY KEY (id_rmi_server)
  );
END;