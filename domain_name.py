def domain_name(url: str) -> str:
    # remove protocol
    if "http://" in url or "https://" in url:
        url = url.replace("http://", "").replace("https://", "")

    # remove www

    if "www." in url:
        url = url.replace("www.", "")

    # remove everything after the domain

    parts = url.split(".")

    return parts[0]


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))  # should return "zombie-bites"
print(domain_name("https://www.cnet.com"))  # should return "cnet