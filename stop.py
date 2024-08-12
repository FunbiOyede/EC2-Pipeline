import boto3
from botocore.exceptions import ClientError
from Constants import Stopping, Stopped, AWS_SERVICE
import os

ec2 = boto3.client(AWS_SERVICE)
INSTANCE_ID = os.environ['EC2_INSTANCE_NAME']

def StopInstance():
    try:
        response = ec2.stop_instances(InstanceIds=[INSTANCE_ID], DryRun=False);
        currentState = response['StoppingInstances'][0]['CurrentState']['Name']
        print(currentState)
        if(currentState == Stopping or currentState == Stopped):
            print('EC2 instance is stopped!!!!')
    except ClientError as e:
        print(e)


StopInstance()