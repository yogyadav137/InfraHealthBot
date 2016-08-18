
Platform Infra Health Bot is a sample bot that demonstrates the framework to build a bot using Cisco Spark webhooks to fetch disk usage information. This is a proof of concept that I build on top of Spark Demo Bot blog code [https://developer.ciscospark.com/blog/blog-details-8110.html] and disk_usage python script [https://github.com/giampaolo/psutil/blob/master/scripts/disk_usage.py]. Planning to add features such as CPU usage, memory utilization, process management, etc. incrementally.

1. sendSparkGET Method is used for retrieving message text when the webhook is triggered with a message.
2. sendSparkPOST Method is used to post a message to the spark room to confirm that a command was received and processed.
3. Spark Bot identification details and bearer token is captured in the code.
4. The example Webhook allows to POST/GET message to and from the spark room in which the bot is mentioned to the server using HTTP requests with a JSON payload. 

<b>Learn more about Spark Webhooks on Cisco DevNet Learning Labs</b> 
Here https://learninglabs.cisco.com/lab/collab-sparkwebhook/step/1

<b>Want to know how to configure and run this script?</b>
Please refer my blog here https://dzone.com/articles/building-bots-using-webhooks



