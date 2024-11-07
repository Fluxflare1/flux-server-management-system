#!/bin/bash

# Load environment variables
source config/environments/development.env

# Define metrics to monitor
CPU_THRESHOLD=80
MEMORY_THRESHOLD=80
DISK_THRESHOLD=80

# Monitor resource usage and send metrics to CloudWatch
while true; do
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *[0-9.]*%* id.*/\1/" | awk '{print 100 - $1}')
    MEMORY_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
    DISK_USAGE=$(df -h | grep '/dev/sda1' | awk '{print $5}' | sed 's/%//g')

    # Send metrics to AWS CloudWatch
    aws cloudwatch put-metric-data --metric-name CPUUsage --namespace ServerMetrics --value "$CPU_USAGE" --unit Percent
    aws cloudwatch put-metric-data --metric-name MemoryUsage --namespace ServerMetrics --value "$MEMORY_USAGE" --unit Percent
    aws cloudwatch put-metric-data --metric-name DiskUsage --namespace ServerMetrics --value "$DISK_USAGE" --unit Percent

    # Check thresholds and trigger alerts
    if (( $(echo "$CPU_USAGE > $CPU_THRESHOLD" |bc -l) )); then
        echo "High CPU usage detected: $CPU_USAGE%"
    fi
    if (( $(echo "$MEMORY_USAGE > $MEMORY_THRESHOLD" |bc -l) )); then
        echo "High memory usage detected: $MEMORY_USAGE%"
    fi
    if (( $(echo "$DISK_USAGE > $DISK_THRESHOLD" |bc -l) )); then
        echo "High disk usage detected: $DISK_USAGE%"
    fi

    sleep 60
done
