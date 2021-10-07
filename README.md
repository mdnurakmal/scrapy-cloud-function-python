# scrapy-cloud-function-python

![Alt text](/img/1.png?raw=true "Title")

# Project Info
- Migrate existing scrapy project to cloud function
- Upload scrapy result to cloud storage
- Setup Cloud Scheduller to trigger this cloud function at specified time daily.

# Usage

Link repo to cloud source repository in GCP
Create build trigger from push event using cloud build configuration
Cloud build will automatically deploy cloud function


# Learning notes

Cloud function directory
/user_code
/workspace
/tmp

- Scrappy need to be run in a child process
- The only writeable part of the filesystem is the /tmp directory, 