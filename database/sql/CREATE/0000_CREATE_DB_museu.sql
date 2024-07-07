USE master; 
GO

-- Verifica se o banco de dados 'museu' existe e cria se não existir
IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = 'museu')
BEGIN
    CREATE DATABASE museu;
END;
GO

-- Verifica se o login 'usr_museu' existe e cria se não existir
IF NOT EXISTS (SELECT 1 FROM sys.server_principals WHERE name = 'usr_museu')
BEGIN
    CREATE LOGIN usr_museu WITH PASSWORD = 'u5r_mu53u';
END;
GO

-- Conecta ao banco de dados 'museu'
USE museu;
GO

-- Verifica se o usuário 'usr_museu' existe no banco de dados 'museu' e cria se não existir
IF NOT EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'usr_museu')
BEGIN
    CREATE USER usr_museu FOR LOGIN usr_museu;
    ALTER ROLE db_owner ADD MEMBER usr_museu;  -- Ajuste de permissão, pode ser necessário
END;
GO

-- Concede permissões necessárias ao usuário 'usr_museu'
GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA::dbo TO usr_museu;
GO