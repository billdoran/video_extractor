from bs4 import BeautifulSoup
import urllib2
import re
import ipdb
from models.Source import Source
from models.Video import Video

def get_page(url):
    data = urllib2.urlopen(url).read()
    return data

def parse_dir_structure(url):
    video_data = {}
    data = get_page(url)
    bs = BeautifulSoup(data)
    for td in bs.findAll('td', attrs={'valign':'top'}):
        img = td.find('img')
        if img['src'] == "/icons/folder.gif":
            next_dir = td.findNextSibling('td').find('a').contents[0]
            next_dir_url = url + '/' + td.findNextSibling('td').find('a')['href']
            next_dir_data = get_page(next_dir_url)
            next_bs = BeautifulSoup(next_dir_data)
            videos = []
            for td in next_bs.findAll('td', attrs={'valign':'top'}):
                if td.find('img')['src'] == "/icons/movie.gif":
                    video_name = td.findNextSibling('td').find('a').contents[0]
                    retrieval_date = td.findNextSibling('td').findNextSibling('td').contents[0]
                    video_size = td.findNextSibling('td').findNextSibling('td').findNextSibling('td').contents[0]
                    videos.append({
                        'name': video_name,
                        'size': video_size,
                        'retrieval_date': retrieval_date
                    })
            ipdb.set_trace()
            video_data[next_dir] = videos
    return video_data

def parse_filename(source, filename):
    
    

    return name, upload_date, location

def store_video_data(video_data):
    videos_to_save = []
    for source in video_data:
        new_source = Source({'org_name':source})
        for video in source:
            video['source_id'] = source.id
            video['name'],video['upload_date'],video['location'] = parse_filename(source, video['name'])
            videos_to_save.append(Video(video))
            
def main():
    url = ""
    video_data = parse_dir_structure(url)
    store_video_data(video_data)

if __name__=="__main__":
    main()
