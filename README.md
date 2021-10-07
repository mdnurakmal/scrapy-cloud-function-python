# scrapy-cloud-function-python

# Usage

Link repo to cloud source repository in GCP
Create build trigger from push event using cloud build configuration
Cloud build will automatically deploy cloud function


# Learning notes

Cloud function directory
/user_code
/workspace

- Scrappy need to be run in a child process
- The only writeable part of the filesystem is the /tmp directory, 