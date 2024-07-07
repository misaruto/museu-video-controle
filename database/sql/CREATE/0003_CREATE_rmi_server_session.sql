IF NOT EXISTS(SELECT 1 FROM sys.tables WHERE NAME = 'rmi_server_session')
BEGIN
  CREATE TABLE museu.dbo.rmi_server_session (
    id_rmi_server_session BIGINT NOT NULL IDENTITY(1,1),
    id_rmi_server_auth_code BIGINT NOT NULL,
    cd_rmi_server_session_token VARCHAR(36) NOT NULL,
    in_rmi_server_session_expired BIT NOT NULL DEFAULT 0,
    dtf_expected_rmi_server_session DATETIME NOT NULL,
    qt_session_duration_seconds INT NULL,
    dtf_rmi_server_session DATETIME NULL,
    dt_created DATETIME NOT NULL DEFAULT GETDATE(),
    nm_user_created_session VARCHAR(30) NULL,
    CONSTRAINT PK_rmi_server_session PRIMARY KEY (id_rmi_server_session),
    CONSTRAINT FK01_rmi_server_session_X_rmi_server_auth_code FOREIGN KEY (id_rmi_server_auth_code) REFERENCES museu.dbo.rmi_server_auth_code(id_rmi_server_auth_code) 
  );
END;