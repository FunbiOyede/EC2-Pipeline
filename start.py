import boto3
import sys
import json
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def StartInstance():
    try:
        response = ec2.start_instances(InstanceIds=[''], DryRun=False);
        currentState = response['StartingInstances'][0]['CurrentState']['Name']
        if(currentState == 'pending' or currentState == 'running'):
            print('EC2 instance is staring up!!!!')

    except ClientError as e:
        print(e)


StartInstance()