resource "aws_sqs_queue" "task_queue" {
  name                        = "flux-task-queue"
  visibility_timeout_seconds  = 30
  message_retention_seconds   = 345600
  max_message_size            = 262144
}
