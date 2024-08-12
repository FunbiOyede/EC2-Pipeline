import boto3
from botocore.exceptions import ClientError
from Constants import Pending, Running, AWS_SERVICE
import os

ec2 = boto3.client(AWS_SERVICE)
INSTANCE_ID = os.environ['EC2_INSTANCE_NAME']


def StartInstance():
    try:
        response = ec2.start_instances(InstanceIds=[INSTANCE_ID], DryRun=False);
        currentState = response['StartingInstances'][0]['CurrentState']['Name']
        if(currentState == Pending or currentState == Running):
            print('EC2 instance is staring up!!!!')

    except ClientError as e:
        print(e)


StartInstance()