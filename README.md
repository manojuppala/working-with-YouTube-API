# YouTube-API
<a href='https://www.youtube.com/channel/UCX93oEN0tza6KfuAWfI61vQ'>
<img src="images/download.png" alt="Visit my youtube channel" width="175" height="100">
</a>

## YouTube Data API v3
> [instance methods](http://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html) (for reference)
<br>
<b>Getting started with YouTube API :<b>
<br>
> [Setup](https://github.com/googleapis/google-api-python-client/blob/master/docs/start.md#setup)<br>
> [Authenication and Authorization](https://github.com/googleapis/google-api-python-client/blob/master/docs/start.md#authentication-and-authorization)<br>
> [Building and calling a service](https://github.com/googleapis/google-api-python-client/blob/master/docs/start.md#building-and-calling-a-service)
<br><br>
> Know more about build() here :- (http://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html#build)
  
### Retrieving simple statistics [code snippet](https://github.com/manojuppala/YouTube-API/blob/master/channel_statistics.py)
> step 1: from googleapiclient.discovery import build<br>
> step 2: assign the build function to a variable (view the syntax of build function from [here](http://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html#build))<br>
> step 3: view all the instance methods that can be used along with build() [here](http://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html)<br>
> step 4: I have used channels method. Know how the channels:lists works [here](https://developers.google.com/youtube/v3/docs/channels/list)<br>
<b>Note :<b> incase your channel doesn't have a custom url use 'id' attribute and assign the channel id to it.
