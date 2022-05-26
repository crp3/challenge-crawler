from extractors.vultr_extractor import VultrExtractor

if __name__ == '__main__':
    vultrExtractor = VultrExtractor('https://www.vultr.com/products/bare-metal/#pricing')
    vultrExtractor.extract()
