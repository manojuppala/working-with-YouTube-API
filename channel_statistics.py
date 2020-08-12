import os
from googleapiclient.discovery import build
# youtube-api key
api_key=os.environ.get('api_key')
#calling the service using the build function
youtube=build('youtube','v3',developerKey=api_key)
request=youtube.channels().list(
    part='statistics',
    id="UCX93oEN0tza6KfuAWfI61vQ"
)
response=request.execute()
print(response['items'][0]['statistics'])
