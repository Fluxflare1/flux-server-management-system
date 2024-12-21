resource "aws_lb" "global_lb" {
  name               = "${var.project_name}-global-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.lb_sg.id]
  subnets            = aws_subnet.public_subnet.*.id
}

resource "aws_lb_listener" "frontend_listener" {
  load_balancer_arn = aws_lb.global_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type = "forward"
    target_group_arn = aws_lb_target_group.frontend_tg.arn
  }
}
