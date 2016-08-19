# Platform Infra Health Bot 

a sample bot that demonstrates the framework to build a bot using Cisco Spark webhooks to fetch disk usage information. 

check [InfraHealthBot.py](https://github.com/ObjectIsAdvantag/InfraHealthBot/blob/master/InfraHealthBot.py)
1. sendSparkGET: retrieves message text when the webhook is triggered with a message.
2. sendSparkPOST: posts a message to the spark room to confirm that a command was received and processed.
3. Spark Bot identification details and bearer token is captured in the code.
4. The example Webhook allows to POST/GET message to and from the spark room in which the bot is mentioned to the server using HTTP requests with a JSON payload. 


# How to run

Detailed instructions can be found in this DZone article: [Building Bots using Webhooks](https://dzone.com/articles/building-bots-using-webhooks).


# Roadmap

This is a proof of concept that I build on top of [Spark Demo Bot blog code] (https://developer.ciscospark.com/blog/blog-details-8110.html) and [disk_usage python script](https://github.com/giampaolo/psutil/blob/master/scripts/disk_usage.py). 

Planning to add features such as CPU usage, memory utilization, process management, etc. incrementally.

*You can learn more about Spark Webhooks by taking this [Cisco DevNet Learning Lab](https://learninglabs.cisco.com/lab/collab-sparkwebhook/step/1)*





