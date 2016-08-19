# Platform Infra Health Bot 

a sample bot that demonstrates the framework to build a bot using Cisco Spark webhooks to fetch disk usage information. 


## How it works

This Webhook allows to POST/GET message to and from the spark room in which the bot is mentioned to the server using HTTP requests with a JSON payload. 

Please check [InfraHealthBot.py](https://github.com/ObjectIsAdvantag/InfraHealthBot/blob/master/InfraHealthBot.py)

* sendSparkGET: retrieves message text when the webhook is triggered with a message.
* sendSparkPOST: posts a message to the spark room to confirm that a command was received and processed.
* Spark Bot identification details and bearer token are captured in the code.


## How to run

Detailed instructions to run the code can be found in this DZone article: [Building Bots using Webhooks](https://dzone.com/articles/building-bots-using-webhooks).

Create a Spark Bot account, and modify the script with your bot informations at the bottom of the [InfraHealthBot.py](https://github.com/ObjectIsAdvantag/InfraHealthBot/blob/master/InfraHealthBot.py) file.

*We recommend to read your Spark bearer token from an environment variable to keep it secret.*

```
bot_email = "infrahealthbot@sparkbot.io"
bot_name = "infrahealthbot"
bearer = "ZWFmZjJmNTItM2FlNS00NWVkLTg5ZTEtNjVhNWYwYzlhN2JlMGExYjBhNDUtZTFh"
```


## Roadmap

This is a proof of concept that I built on top of [Spark Demo Bot blog code] (https://developer.ciscospark.com/blog/blog-details-8110.html) and [disk_usage python script](https://github.com/giampaolo/psutil/blob/master/scripts/disk_usage.py). 

Planning to add features such as CPU usage, memory utilization, process management, etc. incrementally.

*You can learn more about Spark Webhooks by taking this [Cisco DevNet Learning Lab](https://learninglabs.cisco.com/lab/collab-sparkwebhook/step/1)*





