# Use the official Python image.
FROM python:3.7

# Install production dependencies.
RUN pip install Scrapy
RUN pip install scrapy-xlsx
RUN chmod +x init.sh

CMD scrapy crawl afajof