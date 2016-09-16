# commit-alarm
> You must commit! commit! commit! today.
>
> commit-alarm is daily commit alarm pusher to remind you to commit/coding every day.
>
> It push the alarm message to you if there are no commits today.

<br>

### Install & Setting the github, slack config
* Run install.sh

    ```bash
    ./install.sh
    ```

    Then, you can setting the github, slack config during install

    ```
    Slack incoming webhook : <your DM webhook>
    Github username : <github username>
    Github password : <github password>
    ```

<br>

### Setting the aws config
* Setting the AWS credentials.

  > Follow [Setting AWS credentials](https://github.com/apex/apex/blob/master/docs/aws-credentials.md)
* Modify the profile field in `project.json`

  ```
  {
    ...
    "profile": "<your-profile>"
    ...
  }
  ```
  But, if you want to use default profile, remove the "profile" field
* Replace `role` attribute values in `project.json`, `function.json` with yours
  * project.json

    ```
    {
      ...
      "role": "<your-role-arn-of-lambda>",
      ...
    }
    ```
  * functions/push_message/function.json

    ```
    {
      ...
      "role": "<your-role-arn-of-lambda>",
      ...
    }
    ```

<br>

### Deploy & Test
-
* Deploy!

  ```bash
  apex deploy
  ```
* You should set trigger for scheduling using AWS CloudWatch on AWS console
* You can test it with apex

  ```bash
  apex invoke push_message
  ```

  ![push receive](images/push_receive.png)

  Oh! I'm going to commit now

### Telegram version
[MuhunKim/DailyCommit](https://github.com/MuhunKim/DailyCommit)
