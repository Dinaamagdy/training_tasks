import unittest
import requests
from bs4 import BeautifulSoup


class links_class:

    history_all=[] #class member variable will hold all links
    all_links={}   #class member dictionary will use it to stor all links good or no
    initlist=[]
    filterlist=[]
    redirectlist=[]
    def __init__(self, url):
        self.url = url
        #global history_all
        #global all_links
        #first_ls=[]
        responce= requests.get(self.url)
        if responce.status_code == requests.codes.ok :
            self.history_all.append(self.url)
            data=responce.text
            soup =BeautifulSoup(data)
            for link in soup.find_all('a'):
                self.initlist.append((link.get('href')))

            self.all_links[self.url]=self.initlist
            #self.redirection(self.filterization(first_ls))
        else :
            self.initlist.append('website not found')
            self.all_links[self.url]='website not found'


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
                    self.redirectlist= list_all[:]
                    self.all_links[url]=list_all
                    #self.redirection(self.filterization(list_all))
            for k in temp:
                temp[k]=self.filterization(temp[k])

            for k in temp:
                self.redirection(temp[k])

################################main_body#######################
class my_test(unittest.TestCase):
    #first_obj=links_class('http://test-v.000webhostapp.com/test/') #creat_object form class
    def setUp(self):
        #first_obj=links_class('http://test-v.000webhostapp.com/test/') #creat_object form class
        pass
    def testfilterization_method(self):
        first_obj=links_class('http://test-v.000webhostapp.com/test/')
        unfilterlist=['photos.html', 'photos.html', 'videos.html', 'documents.html', 'music.html', 'https://web.telegram.org/#/im', 'http://test-v.000webhostapp.com/test/videos.html', 'http://test-v.000webhostapp.com/test/video.html']
        result= ['photos.html', 'videos.html', 'documents.html', 'music.html', 'http://test-v.000webhostapp.com/test/videos.html']
        #print first_obj.filterization(unfilterlist)
        filterizedlist=first_obj.filterization(unfilterlist)
        listsEqual = len(filterizedlist) == len(result) and all(x in result for x in filterizedlist)
        self.assertTrue(listsEqual)

    def testinit_method(self):
        result={}
        url='http://test-v.000webhostapp.com/test/video.html'
        first_obj=links_class(url)
        result[url]= 'website not found'
        self.assertEqual(result[url],first_obj.all_links[url])
    def testredirection_method(self):
        url='http://test-v.000webhostapp.com/test/'
        first_obj2=links_classs(url)
        inputredir= [ 'videos.html']
        first_obj2.redirection(inputredir)
        result=[]
        self.assertEqual(result,first_obj2.redirectlist)
    def testintegration(self):
        url='http://test-v.000webhostapp.com/test/'
        first_obj2=links_class(url)
        first_obj2.redirection(first_obj2.filterization((first_obj2.initlist)))
        result=['http://test-v.000webhostapp.com/test/', 'photos.html', 'documents.html', 'music.html', 'http://test-v.000webhostapp.com/test/', 'videos.html', 'album1.html', 'album2.html', 'album3.html']
        listsEqual = len(first_obj2.history_all) == len(result) and all(x in result for x in first_obj2.history_all)
        self.assertTrue(listsEqual)


    def testintegration2(self):
        first_obj3=links_class('http://test-v.000webhostapp.com/test/video.html')
        first_obj3.redirection(first_obj3.filterization((first_obj3.initlist)))
        result=['website not found']
        self.assertEqual(result,first_obj3.history_all)

if __name__ == '__main__':
    unittest.main()-v
