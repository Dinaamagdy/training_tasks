import requests
from bs4 import BeautifulSoup

class links_class:

    history_all=[] #class member variable will hold all links
    all_links={}   #class member dictionary will use it to stor all links good or not
    #tryyyyy that 
    def __init__(self, url):
        self.url = url
        #global history_all
        #global all_links
        first_ls=[]
        responce= requests.get(self.url)
        if responce.status_code == requests.codes.ok :
            self.history_all.append(self.url)
            data=responce.text
            soup =BeautifulSoup(data)
            for link in soup.find_all('a'):
                first_ls.append((link.get('href')))

            self.all_links[self.url]=first_ls
            self.redirection(self.filterization(first_ls))
        else:
            print 'website not found'


     ##########################
    def filterization(self,unfilterized_list):
        self.history_all
        if len(unfilterized_list) != 0:
            for link in unfilterized_list:
                if link == './':
                    unfilterized_list.remove(link)
                elif link in self.history_all:
                    unfilterized_list.remove(link)
                elif 'http' in link :
                    unfilterized_list.remove(link)
                elif 'https' in link :
                    unfilterized_list.remove(link)
                else:
                    self.history_all.append(link)

        return unfilterized_list

     #####################################
    def redirection(self,filterized_list):
        self.all_links
        temp = {}
        if len(filterized_list) > 0:
            for link in filterized_list :
                list_all=[]
                if 'http' in link:
                    url=link
                else:
                    url=self.url+link
                response= requests.get(url)
                data=response.text
                if response.status_code == requests.codes.ok :
                    soup =BeautifulSoup(data)
                    for link in soup.find_all('a'):
                        list_all.append(str(link.get('href')))
                    temp[link] = list_all
                    self.all_links[url]=list_all
                    #self.redirection(self.filterization(list_all))

            for k in temp:
                temp[k]=self.filterization(temp[k])

            for k in temp:
                self.redirection(temp[k])

################################main_body#######################
first_obj=links_class('http://test-v.000webhostapp.com/test/') #creat_object form class
print first_obj.history_all                   #print all links in the given link

for key in first_obj.all_links:                #print links inside every link in the given page

    print key
    print first_obj.all_links[key]
