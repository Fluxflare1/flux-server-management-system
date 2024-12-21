resource "aws_db_instance" "primary" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "13.4"
  instance_class       = "db.t3.micro"
  name                 = "fluxdb"
  username             = var.db_user
  password             = var.db_password
  publicly_accessible  = true
  multi_az             = true
  storage_type         = "gp2"
}

resource "aws_db_instance" "replica" {
  replicate_source_db = aws_db_instance.primary.id
  instance_class      = "db.t3.micro"
}
