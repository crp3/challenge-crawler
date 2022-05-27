import re

def multiple_replace(dict_, text):
    regex = re.compile("|".join(map(re.escape, dict_.keys())))
    return regex.sub(lambda match: dict_[match.string[match.start():match.end()]], text)

def remove_separators(text):
    separator_mapper = {
        '\t': '',
        '\n': ''
    }

    return multiple_replace(separator_mapper, text)

def replace_commas(text):
    return re.sub(',', '.', text)

def extract_tag_content(tag):
    return tag.contents[0]

def is_cpu(text):
    return 'Intel' in text

def is_storage(text):
    return 'TB' in text
