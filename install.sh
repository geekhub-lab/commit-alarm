#!/bin/sh

# install apex to deploy to AWS Lambda
apex=apex

if ! apex_loc="$(type -p "$apex")" || [ -z "$apex" ]; then 
    echo "Installing apex ..."
    curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh
else
    echo "Apex is already installed."
fi

echo "\n"

# slack configuration
while [[ -z "$slack_webhook" ]]
do
    read -p "Slack incoming webhook : " slack_webhook
done

# github configuration
while [[ -z "$username" ]]
do
    read -p "Github username : " username
done

while [[ -z "$password" ]]
do
    read -s -p "Github password : " password
done

touch functions/push_message/github.ini
touch functions/push_message/slack.ini 

cat << EOF > functions/push_message/slack.ini
[slack]
incoming_webhook_url: $slack_webhook
EOF

cat << EOF > functions/push_message/github.ini
[github]
username: $username
password: $password
EOF

echo "\n\nDone."
