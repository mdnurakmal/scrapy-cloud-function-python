import scrapy

class Wikicfppider(scrapy.Spider):
    name = "wikicfp"

    custom_settings = {
        'FEED_FORMAT': 'xlsx',
        'FEED_URI': 'wikicfp_calendar.xlsx'
    }

    def start_requests(self):
        urls=[
            'http://www.wikicfp.com/cfp/servlet/tool.search?q=finance&year=f'
        ]
    
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        urls = response.xpath('//td[@align="center"]/h3/a/@href').getall()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.parse_items)
    
    def parse_items(self, response):
        urls = response.xpath('//td[@align="left"]/a[contains(@href, "eventid")]/@href').getall()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.detail_parse)

        #next page
        next_page = response.xpath('//a[contains(., "next")]/@href').get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_items)
    
    
    def detail_parse(self, response):
        title = response.xpath('//span[@property="v:description"]/text()').get().strip()
        link = response.xpath('//tr/td[contains(., "Link:")]/a/text()').get()

        when = response.xpath('//tr/th[contains(., "When")]/parent::node()/td/text()').get().strip()
        where = response.xpath('//tr/th[contains(., "Where")]/parent::node()/td/text()').get().strip()
        submission_deadline = response.xpath('//span[@property="v:startDate"]/text()').get().strip()

        categories_ = response.xpath('//td/h5/a/b[contains(., "Categories")]/parent::node()/parent::node()/a/text()').getall()
        categories = ' '.join(x.strip() for x in categories_)
        
        cfp = response.xpath('//td/div[contains(., "Place")]/parent::node()//text()').getall()
        call_for_papers = ' '.join(x.strip() for x in cfp)

        yield {
                'url': response.url,
                'Title': title,
                'Link': link,
                'When': when,
                'Where': where,
                'Submission Deadline': submission_deadline,
                'Categories': categories,
                'Call For Papers': call_for_papers
            }