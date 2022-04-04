import boto3
import time

# Create CloudWatch client
cloudwatch = boto3.client("cloudwatch")


def list_cw_alarms():
    try:
        paginator = cloudwatch.get_paginator("describe_alarms")
        for res in paginator.paginate(StateValue="INSUFFICIENT_DATA"):
            alarms = res.get("MetricAlarms", "")
            if alarms:
                for alarm in alarms:
                    print(alarm.get("AlarmName"))
                    print(alarm.get("AlarmDescription"))
                    print("*" * 20)
            print(res.get("MetricAlarms", ""))
    except ConnectionError:
        print("Not able to connect!")


def create_cw_alarm():
    try:
        cloudwatch.put_metric_alarm(
            AlarmName="Web_Server_CPU_Utilization",
            ComparisonOperator="GreaterThanThreshold",
            EvaluationPeriods=1,
            MetricName="CPUUtilization",
            Namespace="AWS/EC2",
            Period=60,
            Statistic="Average",
            Threshold=70.0,
            ActionsEnabled=False,
            AlarmDescription="Alarm when server CPU exceeds 70%",
            Dimensions=[
                {
                    "Name": "InstanceId",
                    "Value": "INSTANCE_ID"
                },

            ],
            Unit="Seconds"
        )
        print("Alarm crated!")

    except ConnectionError:
        print("Not able to connect!")


def delete_alarm():
    try:
        paginator = cloudwatch.get_paginator("describe_alarms")
        for res in paginator.paginate(StateValue="INSUFFICIENT_DATA"):
            alarms = res.get("MetricAlarms", "")
            if alarms:
                cloudwatch.delete_alarms(
                    AlarmNames=["Web_Server_CPU_Utilization"]
                )
                print("Waiting for AWS to finish")
                time.sleep(5)
                print("AWS probably finished by now, executing next task if any.")

    except ConnectionError:
        print("Couldn't connect I guess :/")


if __name__ == "__main__":
    delete_alarm()
    list_cw_alarms()
