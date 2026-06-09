terraform {
  required_version = ">= 1.6.0"
}
variable "project_name" {
  type    = string
  default = "ecosaude"
}
# Credenciais devem ser fornecidas por variáveis de ambiente ou secret manager.
