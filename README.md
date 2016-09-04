# commit-alarm
> You must commit! commit! commit! today.
>
> commit-alarm is daily commit alarm pusher

-

### Deploy & Run
* Install APEX and Setting the AWS credentials
  > APEX is AWS Lambda management tools

  Follow these [Install APEX](https://github.com/apex/apex/blob/master/docs/installation.md), [Setting AWS credentials](https://github.com/apex/apex/blob/master/docs/aws-credentials.md)
* Replace `role` attribute value in `package.json`, `function.json` with yours

  ```
  {
    ...
    "role": "<your-role-arn-of-lambda>",
    ...
  }
  ```
  ```
  {
    ...
    "role": "<your-role-arn-of-lambda>",
    ...
  }
  ```
* Setting the simple slack configuration. Make `slack.ini` in `functions/push_message` directory and write this

  ```
  [slack]
  incoming_webhook_url: https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX (your slack incoming webhook url)
  ```
* Deploy!

  ```bash
  apex deploy
  ```
* You should set trigger for scheduling using AWS CloudWatch on AWS console
* The commit-alarm pusher send the random messages to your slack periodically! (It could often bothered you)

