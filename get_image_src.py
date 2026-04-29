from bs4 import BeautifulSoup

with open("/home/ubuntu/browser_html/faisalmushtaq_github_io_brainpop-website_1777325610945.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

# Find the div for Olivia Jones
person_card = soup.find("h3", string="Dr Olivia Jones")

if person_card:
    # Navigate up to the parent .person-card div
    person_card_div = person_card.find_parent("div", class_="person-card")
    if person_card_div:
        img_tag = person_card_div.find("img")
        if img_tag and img_tag.has_attr("src"):
            print(img_tag["src"])
        else:
            print("Image tag or src attribute not found for Dr Olivia Jones.")
    else:
        print("Parent person-card div not found for Dr Olivia Jones.")
else:
    print("Person card for Dr Olivia Jones not found.")
