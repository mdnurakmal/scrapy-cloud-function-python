import scrapy

class EconbizSpider(scrapy.Spider):
    name = "econbiz"

    custom_settings = {
        'FEED_FORMAT': 'xlsx',
        'FEED_URI': 'econbiz_calendar.xlsx'
    }

    def start_requests(self):
        urls=[
            'https://www.econbiz.de/Events/Results?date=all&type=AllFields&filter%5B%5D=%7Ejel%3A%22g2%22&filter%5B%5D=%7Ejel%3A%22c0%22'
        ]
    
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        urls = response.xpath('//a[@class="title print-no-url"]/@href').getall()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.detail_parse)

        #next page
        next_page = response.xpath('//a[@data-track-elem="next"]/@href').get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
    
    
    def detail_parse(self, response):
        title = response.xpath('//div[@class="title"]/h1/text()').get().strip()
        description = response.xpath('//div[@id="record-abstract"]/div/text()').get()
        alternative = response.xpath('//tr[@data-record-field="title_alternative"]/td/span/text()').get()
        event_dates_start = response.xpath('//span[@property="schema:startDate"]/text()').get()
        event_dates_end = response.xpath('//span[@property="schema:endDate"]/text()').get()
        event_dates = ''
        if event_dates_start: event_dates = event_dates_start + ' – ' + event_dates_end

        application_deadline = response.xpath('//tr/th[contains(., "Application deadline:")]/parent::node()/td/text()').get()
        deadline_call = response.xpath('//tr/th[contains(., "Deadline Call for Papers:")]/parent::node()/td/text()').get()
        organisateur = response.xpath('//tr/th[contains(., "Organizer:")]/parent::node()/td/div/a/text()').get()
        pays = response.xpath('//span[@property="schema:addressCountry"]/span/text()').get()
        conference_venue = response.xpath('//span[@property="schema:location"]/span/text()').get()
        contact = response.xpath('//tr/th[contains(., "Contact:")]/parent::node()/td/div/text()').get()
        classification = response.xpath('//span[@property="schema:about"]/span/text()').get()
        langue = response.xpath('//span[@property="schema:inLanguage"]/text()').get()
        event_type = response.xpath('//tr/th[contains(., "Event type:")]/parent::node()/td/text()').get()

        yield {
                'url': response.url,
                'Title': title,
                'Description': description,
                'Alternative title': alternative,
                'Event dates': event_dates,
                'Application deadline': application_deadline,
                'Deadline Call for Papers': deadline_call,
                'Organisateur': organisateur,
                'Pays': pays,
                'Conference venue': conference_venue,
                'Contact': contact,
                'Classification': classification,
                'Langue': langue,
                'Event type': event_type
            }