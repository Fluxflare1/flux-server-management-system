resource "aws_rds_cluster" "flux_cluster" {
  cluster_identifier      = "flux-cluster"
  engine                  = "aurora-mysql"
  engine_version          = "5.7"
  database_name           = "fluxdb"
  master_username         = var.db_user
  master_password         = var.db_password
  backup_retention_period = 7
  availability_zones      = ["us-east-1a", "us-east-1b"]
}

resource "aws_rds_cluster_instance" "flux_instance" {
  count               = 2
  cluster_identifier  = aws_rds_cluster.flux_cluster.id
  instance_class      = "db.t3.medium"
  publicly_accessible = true
}
