import re


def generate_affiliation_link(url):
    new_str = "http://www.amazon.com/dp/{}/?tag=pyb0f-20"
    m = re.search(r"http.*/dp/(\w+).*", url)
    return new_str.format(m.group(1))
