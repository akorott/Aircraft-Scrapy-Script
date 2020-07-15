import scrapy


class AircraftSpiderSpider(scrapy.Spider):
    name = 'aircraft_spider'
    page_number = 2
    allowed_domains = ["www.avbuyer.com"] # it's important to have the correct url here. No extra spaces, slashes, etc.
    start_urls = ['https://www.avbuyer.com/aircraft/page-2?sort_field=item_price%7cdesc']
    base_url = ["https://www.avbuyer.com"]

    def parse(self, response):

        aircraft_on_page = response.xpath("//div[@class='grid-x list-content']") # this is needed because the aircraft_url needs to know where to look inside for the URL!

        for aircraft in aircraft_on_page:
            aircraft_url = self.base_url[0] + \
                           aircraft.xpath(".//div[@class='list-item-details']/h2/a/@href").extract_first()

            yield scrapy.Request(aircraft_url, callback=self.parse_aircraft)

        next_page_url = "https://www.avbuyer.com/aircraft/page-" + str(AircraftSpiderSpider.page_number) + "?sort_field=item_price%7cdesc"
        if AircraftSpiderSpider.page_number < 70:
            AircraftSpiderSpider.page_number += 1
            yield scrapy.Request(next_page_url, callback=self.parse)


    def parse_aircraft(self, response):
        category = response.css('.breadcrumbs a::text')[1].extract()

        if category != 'Helicopter':
            type = 'NA'
            make = response.css('.breadcrumbs a::text')[2].extract()
            model = response.css('.breadcrumbs a::text')[3].extract()
            price = response.css('.dtl-price::text').extract()
            location = response.xpath("//div[@class='other-dtl-box']/div[@class='list-item-location']/text()").extract_first()
            year = response.css('.medium-9::text')[0].extract()
            serial_num = response.css('.medium-9::text')[1].extract()
            registration = response.css('.medium-9::text')[2].extract()
            total_hours = response.css('.medium-9::text')[3].extract()
            airframe = response.xpath("//div[@class='large-6 cell']/h3[contains(text(),'AIRFRAME')]/parent::div/text()").extract()
            airframe = [x.strip() for x in airframe]
            engines = response.xpath("//div[@class='large-6 cell']/h3[contains(text(),'ENGINES')]/parent::div/text()").extract()
            engines = [x.strip() for x in engines]
            apu = response.xpath("//div[@class='large-6 cell']/h3[contains(text(),'APU')]/parent::div/text()").extract()
            apu = [x.strip() for x in apu]
            maintenance_and_inspection = response.xpath("//a[contains(text(), 'Maintenance')]/following-sibling::div//text()").extract()
            maintenance_and_inspection = [x.strip() for x in maintenance_and_inspection]
            avionics_and_connectivity = response.xpath("//a[contains(text(), 'AVIONICS')]/following-sibling::div//text()").extract()
            avionics_and_connectivity = [x.strip() for x in avionics_and_connectivity]
            interior_and_entertainment = response.xpath("//a[contains(text(), 'Interior')]/following-sibling::div//text()").extract()
            interior_and_entertainment = [x.strip() for x in interior_and_entertainment]
            exterior = response.xpath("//a[contains(text(), 'EXTERIOR')]/following-sibling::div//text()").extract()
            exterior = [x.strip() for x in exterior]
            additional_equip_and_info = response.xpath("//a[contains(text(), 'Additional')]/following-sibling::div//text()").extract()
            additional_equip_and_info = [x.strip() for x in additional_equip_and_info]
            highlights = response.xpath("//h2[contains(text(), 'Highlights')]/following-sibling::div//text()").extract()

            yield {
                'Price': price,
                'Category': category,
                'Year': year,
                'Piston/Turbine': type,
                'Make': make,
                'Model': model,
                'Location': location,
                'S/N': serial_num,
                'REG': registration,
                'Total Hours': total_hours,
                'Aircraft Summary': highlights,
                'Airframe': airframe,
                'Engines': engines,
                'APU': apu,
                'Maintenance & Inspections': maintenance_and_inspection,
                'Avionics & Connectivity': avionics_and_connectivity,
                'Interior & Entertainment': interior_and_entertainment,
                'Exterior': exterior,
                'Additional Equipment & Information': additional_equip_and_info
                }

        if category == 'Helicopter':
            type = response.css('.breadcrumbs a::text')[2].extract()
            make = response.css('.breadcrumbs a::text')[3].extract()
            model = response.css('.breadcrumbs a::text')[4].extract()
            price = response.css('.dtl-price::text').extract()
            location = response.xpath("//div[@class='other-dtl-box']/div[@class='list-item-location']/text()").extract_first()
            year = response.css('.medium-9::text')[0].extract()
            serial_num = response.css('.medium-9::text')[1].extract()
            registration = response.css('.medium-9::text')[2].extract()
            total_hours = response.css('.medium-9::text')[3].extract()
            airframe = response.xpath("//div[@class='large-6 cell']/h3[contains(text(),'AIRFRAME')]/parent::div/text()").extract()
            airframe = [x.strip() for x in airframe]
            engines = response.xpath("//div[@class='large-6 cell']/h3[contains(text(),'ENGINES')]/parent::div/text()").extract()
            engines = [x.strip() for x in engines]
            apu = response.xpath("//div[@class='large-6 cell']/h3[contains(text(),'APU')]/parent::div/text()").extract()
            apu = [x.strip() for x in apu]
            maintenance_and_inspection = response.xpath("//a[contains(text(), 'Maintenance')]/following-sibling::div//text()").extract()
            maintenance_and_inspection = [x.strip() for x in maintenance_and_inspection]
            avionics_and_connectivity = response.xpath("//a[contains(text(), 'AVIONICS')]/following-sibling::div//text()").extract()
            avionics_and_connectivity = [x.strip() for x in avionics_and_connectivity]
            interior_and_entertainment = response.xpath("//a[contains(text(), 'Interior')]/following-sibling::div//text()").extract()
            interior_and_entertainment = [x.strip() for x in interior_and_entertainment]
            exterior = response.xpath("//a[contains(text(), 'EXTERIOR')]/following-sibling::div//text()").extract()
            exterior = [x.strip() for x in exterior]
            additional_equip_and_info = response.xpath("//a[contains(text(), 'Additional')]/following-sibling::div//text()").extract()
            additional_equip_and_info = [x.strip() for x in additional_equip_and_info]
            highlights = response.xpath("//h2[contains(text(), 'Highlights')]/following-sibling::div//text()").extract()

            yield {
                'Price': price,
                'Category': category,
                'Year': year,
                'Piston/Turbine': type,
                'Make': make,
                'Model': model,
                'Location': location,
                'S/N': serial_num,
                'REG': registration,
                'Total Hours': total_hours,
                'Aircraft Summary': highlights,
                'Airframe': airframe,
                'Engines': engines,
                'APU': apu,
                'Maintenance & Inspections': maintenance_and_inspection,
                'Avionics & Connectivity': avionics_and_connectivity,
                'Interior & Entertainment': interior_and_entertainment,
                'Exterior': exterior,
                'Additional Equipment & Information': additional_equip_and_info
                }


