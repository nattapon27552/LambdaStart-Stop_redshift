import json
import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    REDSHIFT_CLUSTER_ID = os.environ["REDSHIFT_CLUSTER_ID"]
    
    try:
        redshift_client = boto3.client("redshift")    
        response = redshift_client.describe_clusters(ClusterIdentifier = REDSHIFT_CLUSTER_ID)
        
        if (response["Clusters"][0]["ClusterAvailabilityStatus"] == "Paused"):
            redshift_client.resume_cluster(ClusterIdentifier = REDSHIFT_CLUSTER_ID)
            logger.info("redshift cluster {0} is now resumed".format(REDSHIFT_CLUSTER_ID))
        else:
            logger.info("redshift cluster {0} is in a {1} state. cannot resume cluster".format(REDSHIFT_CLUSTER_ID, response["Clusters"][0]["ClusterAvailabilityStatus"]))
    except Exception as e:
        logger.error("Exception: {0}".format(e))

def lambda_handler(event, context):
    handler(event, context)

#config-env.
#Key                     Value
#REDSHIFT_CLUSTER_ID	name-redshift-nprd
