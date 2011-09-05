from fabric.api import *

env.s3_bucket = 'media.hacktyler.com'
    
"""
Commands - deployment
"""
def deploy():
    """
    Deploy assets to S3.
    """
    local(('s3cmd -P --guess-mime-type --recursive put ./assets/ s3://%(s3_bucket)s/') % env)

