# -*- coding: utf-8 -*-f
import bs4
#mport urllib2
import urllib
urllib2 = urllib.request

def scrape_visit_philly():
    source = urllib2.urlopen('http://www.visitphilly.com/events/view-all/').read()
    soup = bs4.BeautifulSoup(source, "lxml")
    wrapper = soup.find("ul", {"class": "summary-alt"})
    events = wrapper.find_all("li")
    
    event_list = []
    for event in events:
        data = dict()
        gamma = event.find(class_="gamma")
        link = gamma.find("a")
        title = link.get_text()
        title = title.strip(' \t\n\r')
        
        url = "http://www.visitphilly.com" + link['href']
        
        
        desc = event.find("p", class_=False)
        if desc:
            if desc.em:
                date = desc.em.extract()
            if desc.i:
                date = desc.i.extract()
        else:
            desc = soup.find("nosuchtag")
            date = soup.find("nosuchtag")
            
        data["title"] = title
        data["link"] = url
        if desc:
            data["description"] = desc.get_text()
        else:
            data["description"] = ""
        #data["description"] = desc.get_text()
        if date:
            data["date"] = date.get_text()
        else:
            data["date"] = ""
        event_list.append(data)
    
    source = urllib2.urlopen('http://www.visitphilly.com/events/view-all/'+'P30').read()
    soup = bs4.BeautifulSoup(source, "lxml")
    wrapper = soup.find("ul", {"class": "summary-alt"})
    events = wrapper.find_all("li")
    
    for event in events:
        data = dict()
        gamma = event.find(class_="gamma")
        link = gamma.find("a")
        title = link.get_text()
        title = title.strip(' \t\n\r')
        
        url = "http://www.visitphilly.com" + link['href']
        
        
        desc = event.find("p", class_=False)
        if desc:
            if desc.em:
                date = desc.em.extract()
            if desc.i:
                date = desc.i.extract()
        else:
            desc = soup.find("nosuchtag")
            date = soup.find("nosuchtag")
            
        data["title"] = title
        data["link"] = url
        if desc:
            data["description"] = desc.get_text()
        else:
            data["description"] = ""
        #data["description"] = desc.get_text()
        if date:
            data["date"] = date.get_text()
        else:
            data["date"] = ""
        event_list.append(data)
        
    
    return event_list