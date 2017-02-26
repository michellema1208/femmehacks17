# -*- coding: utf-8 -*-f
import bs4
#mport urllib2
import urllib
urllib2 = urllib.request
import re

def scrape_philly_calendar():
    toplevel = 'http://www.thephillycalendar.com/'
    source = urllib2.urlopen(toplevel).read()
    soup = bs4.BeautifulSoup(source, "lxml")
    
    wrapper = soup.find(id = "events")
    
    events = wrapper.find_all(class_ = "event")
    event_list = []
    for event in events:
        clear = event.find(class_="clear")
        data = dict()
        title = event.find(itemprop="name")
        if title:
            title = title.get_text()
        else:
            title = ""
        link = clear.find_next_sibling(itemprop="url")
        if link:
            url = link['href']
        else:
            url = ""
        date = clear.find_next_sibling(itemprop="startDate")
        if date:
            date = date['content']
        else:
            date = ""
            
        imglink = event.find(class_="img-link")
        if imglink:
            imgurl = toplevel + imglink['href']
            descscource = urllib2.urlopen(imgurl).read()
            descsoup = bs4.BeautifulSoup(descscource, "lxml")
            desc = descsoup.find(id="event_description")
            if desc:
                desctext = desc.get_text()
                desctext = re.sub(r'[\s+]', ' ', desctext)
                data["description"] = desctext
            else:
                desc = ""
        else:
            desc = ""
        
            
        data["title"]= title
        data["link"] = url
        data["date"] = date
        event_list.append(data)
    return event_list
