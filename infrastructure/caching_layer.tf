resource "aws_elasticache_cluster" "redis" {
  cluster_id           = "flux-redis-cluster"
  engine               = "redis"
  node_type            = "cache.t3.micro"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis3.2"
}
