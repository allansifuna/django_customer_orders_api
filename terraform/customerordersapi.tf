terraform {
  required_providers {
    linode = {
      source  = "linode/linode"
      version = "2.7.2"
    }
  }
}

provider "linode" {
  token = var.token
}

resource "linode_lke_cluster" "customerordersapi" {
    k8s_version = var.k8s_version
    label = var.label
    region = var.region
    tags = var.tags

    dynamic "pool" {
        for_each = var.pools
        content {
            type  = pool.value["type"]
            count = pool.value["count"]
        }
    }
}

output "kubeconfig" {
  value = linode_lke_cluster.customerordersapi.kubeconfig
  sensitive = true
}

output "api_endpoints" {
  value = linode_lke_cluster.customerordersapi.api_endpoints
}

output "status" {
  value = linode_lke_cluster.customerordersapi.status
}

output "id" {
  value = linode_lke_cluster.customerordersapi.id
}

output "pool" {
  value = linode_lke_cluster.customerordersapi.pool
}

