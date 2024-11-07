#!/bin/bash

# Set up AWS autoscaling rules
aws autoscaling put-scaling-policy --auto-scaling-group-name my-auto-scaling-group \
    --policy-name cpu-scale-up \
    --scaling-adjustment 1 \
    --adjustment-type ChangeInCapacity \
    --cooldown 300 \
    --metric-aggregation-type "Average" \
    --target-tracking-configuration file://config/target_tracking_policy.json
