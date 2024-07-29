import boto3
import sys
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

def StopInstance():
    try:
        response = ec2.stop_instances(InstanceIds=[''], DryRun=False);
        currentState = response['StoppingInstances'][0]['CurrentState']['Name']
        print(currentState)
        if(currentState == 'stopping' or currentState == 'stopped'):
            print('EC2 instance is stopped!!!!')
    except ClientError as e:
        print(e)


StopInstance()