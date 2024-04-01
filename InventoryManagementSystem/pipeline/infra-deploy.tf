provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "ims_rg" {
  name     = "rg-ims-aue"
  location = "Australia East"
}

resource "azurerm_key_vault" "ims_kv" {
  name                        = "kv-ims"
  location                    = azurerm_resource_group.ims_rg.location
  resource_group_name         = azurerm_resource_group.ims_rg.name
  enabled_for_deployment      = true
  enabled_for_disk_encryption = true
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  sku_name = "standard"
}

resource "azurerm_key_vault_secret" "db_credentials" {
  name         = "db-credentials"
  value        = jsonencode({
    username = "dbAdmin",
    password = random_password.ims_result.result
  })
  key_vault_id = azurerm_key_vault.ims_kv.id
}

resource "random_password" "ims_result" {
  length           = 16
  special          = true
  override_special = "_%@"
}

resource "azurerm_sql_server" "ims_sql_server" {
  name                         = "sqlsrv-ims"
  resource_group_name          = azurerm_resource_group.ims_rg.name
  location                     = azurerm_resource_group.ims_rg.location
  version                      = "12.0"
  administrator_login          = "dbAdmin"
  administrator_login_password = random_password.ims_result.result
}

resource "azurerm_sql_database" "ims_sql_db" {
  name                = "sqldb-ims"
  resource_group_name = azurerm_resource_group.ims_rg.name
  location            = azurerm_resource_group.ims_rg.location
  server_name         = azurerm_sql_server.ims_sql_server.name
  edition             = "Basic"
  collation           = "SQL_Latin1_General_CP1_CI_AS"
  max_size_gb         = 2
}
