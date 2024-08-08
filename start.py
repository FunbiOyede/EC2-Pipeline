import boto3
from botocore.exceptions import ClientError
from Constants import Pending, Running, AWS_SERVICE

ec2 = boto3.client(AWS_SERVICE)


def StartInstance():
    try:
        response = ec2.start_instances(InstanceIds=['i-020aaf861101680e9'], DryRun=False);
        currentState = response['StartingInstances'][0]['CurrentState']['Name']
        if(currentState == Pending or currentState == Running):
            print('EC2 instance is staring up!!!!')

    except ClientError as e:
        print(e)


StartInstance()