import scrapy
import re

class AfajofSpider(scrapy.Spider):
    name = "afajof"

    custom_settings = {
        'FEED_FORMAT': 'xlsx',
        'FEED_URI': '/user_code/afajof_calendar.xlsx'
    }

    def start_requests(self):
        urls=[
            'https://www.trumba.com/s.aspx?filterview=conference&template=&calendar=afa-conferences&widget=main&spudformat=xhr'
        ]
    
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        events = re.findall(r'url\.eventid\=\"(.*?)\" onclick\=\"Trumba\.Spuds', response.text);
        for eventid in events:
            url = 'https://www.trumba.com/s.aspx?filterview=conference&template=&view=event&eventid=' + eventid + '&calendar=afa-conferences&widget=main&spudformat=xhr'
            yield scrapy.Request(url, callback=self.detail_parse)

        #next page
        next_page = response.xpath('//a[@class="twPagerBtn left"]/@href').get()
        if next_page:
            next_date= re.search(r'date\=(.*?)\'', next_page);
            if next_date:
                next_page = next_date.group(1).replace('&index=-1','')
                next_page = 'https://www.trumba.com/s.aspx?filterview=conference&template=&calendar=afa-conferences&widget=main&mixin=1386134&date=' + next_page + '&index=-1&spudformat=xhr'
                yield scrapy.Request(next_page, callback=self.parse)
    
    
    def detail_parse(self, response):
        title = response.xpath('//span[@class="twEDDescription"]/text()').get().strip()
        event_dates = response.xpath('//span[@class="twEDStartEndRange"]/text()').get().strip()

        description_ = response.xpath('//div[@class="twEDNotes"]//text()').getall()
        description = ' '.join(x.strip() for x in description_)

        location_ = response.xpath('//tr/th/span[contains(., "Location")]/parent::node()/parent::node()/td/a/text()').getall()
        location = ' '.join(x.strip() for x in location_)

        country = response.xpath('//tr/th/span[contains(., "Country")]/parent::node()/parent::node()/td/text()').get()
        event_type = response.xpath('//tr/th/span[contains(., "Event Type")]/parent::node()/parent::node()/td/text()').get()
        papers_deadline = response.xpath('//tr/th/span[contains(., "Call for Papers Deadline")]/parent::node()/parent::node()/td/text()').get()
        submission_cost = response.xpath('//tr/th/span[contains(., "Submission Cost (USD)")]/parent::node()/parent::node()/td/text()').get()
        conference_cost = response.xpath('//tr/th/span[contains(., "Conference Cost (USD)")]/parent::node()/parent::node()/td/text()').get()
        event_contact_name = response.xpath('//tr/th/span[contains(., "Event Contact Name")]/parent::node()/parent::node()/td/text()').get()
        event_ontact_phone = response.xpath('//tr/th/span[contains(., "Event Contact Phone#")]/parent::node()/parent::node()/td/text()').get()

        
        event_contact_email = response.xpath('//tr/th/span[contains(., "Event Contact Email")]/parent::node()/parent::node()/td/a/text()').get()
        host_institution = response.xpath('//tr/th/span[contains(., "Host Institution")]/parent::node()/parent::node()/td/text()').get()
        registration_deadline = response.xpath('//tr/th/span[contains(., "Registration Deadline")]/parent::node()/parent::node()/td/text()').get()
        registration_link = response.xpath('//tr/th/span[contains(., "Registration Link")]/parent::node()/parent::node()/td/a/@href').get()
        link = response.xpath('//tr/th/span[text()="Link"]/parent::node()/parent::node()/td/a/@href').get()

        yield {
                'url': response.url,
                'Title': title,
                'Description': description,
                'Event dates': event_dates,
                'Location': location,
                'Country': country,
                'Event Type': event_type,
                'Call for Papers Deadline': papers_deadline,
                'Submission Cost (USD)': submission_cost,
                'Conference Cost (USD)': conference_cost,
                'Event Contact Name': event_contact_name,
                'Event Contact Phone#': event_ontact_phone,
                'Event Contact Email': event_contact_email,
                'Host Institution': host_institution,
                'Registration Deadline': registration_deadline,
                'Registration Link': registration_link,
                'Link': link
            }