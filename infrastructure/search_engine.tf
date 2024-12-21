resource "aws_elasticsearch_domain" "search" {
  domain_name           = "flux-search"
  elasticsearch_version = "7.10"
  node_to_node_encryption {
    enabled = true
  }

  ebs_options {
    ebs_enabled = true
    volume_size = 10
    volume_type = "gp2"
  }
}
