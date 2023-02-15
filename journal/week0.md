# Week 0 — Billing and Architecture

## Add SSH keys to GITPOD to open the VSCode Desktop
Generated SSH keys and add the keys to the gitpod config to open the desktop VSCode without a prompt for password. Make sure to save the private key at ~/.ssh/id_ed25519. The copy the contents of the public key - id_ed25519.pub into the ssh keys under user settings https://gitpod.io/user/keys
```
ssh-keygen -t ed25519
```

## AWS CLI Installation

Modification to gitpod.yaml to include scripts to run the first time the workspace is established. This includes installing AWS cli and setting up the environment variable to get prompts for aws cli completion.

Update the `.gitpod.yml` with the following task defition.
```sh
tasks:
  - name: aws-cli
    env:
      AWS_CLI_AUTO_PROMPT: on-partial
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT
```

Also added environment variables that are needed in the GITPOD 
```
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_DEFAULT_REGION=us-east-1
export AWS_REGION=us-east-1
```

Save these environment variable into Gitpod for future workspaces
```
gp env AWS_ACCESS_KEY_ID=""
gp env AWS_SECRET_ACCESS_KEY=""
gp env AWS_DEFAULT_REGION=us-east-1
gp env AWS_REGION=us-east-1
```


### Create a new User and Generate AWS Credentials

- Create an IAM user - IAMADMIN
- Enable Console access for the user
- Create an Admin group and apply AdminstratorAccess
- Create Access key
- Download the access key CSV

