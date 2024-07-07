IF NOT EXISTS(SELECT 1 FROM sys.tables WHERE NAME = 'rmi_server_auth_code')
BEGIN
  CREATE TABLE museu.dbo.rmi_server_auth_code (
    id_rmi_server_auth_code BIGINT NOT NULL IDENTITY(1,1),
    id_rmi_server BIGINT NOT NULL,
    cd_rmi_server_auth VARCHAR(6) NOT NULL,
    in_accessed BIT NOT NULL DEFAULT 0,
    dt_created DATETIME NOT NULL DEFAULT GETDATE(),
    CONSTRAINT PK_rmi_server_auth_code PRIMARY KEY (id_rmi_server_auth_code),
    CONSTRAINT FK01_rmi_server_auth_code_X_rmi_server FOREIGN KEY (id_rmi_server) REFERENCES rmi_server(id_rmi_server) 
  );
END;