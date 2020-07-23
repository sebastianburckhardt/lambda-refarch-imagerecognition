# importing google_images_download module 
from google_images_download import google_images_download  
  
# creating object 
# response = google_images_download.googleimagesdownload()  
  
# search_queries = ['apple'] 
  
  
# def downloadimages(query): 
#     # keywords is the search query 
#     # format is the image file format 
#     # limit is the number of images to be downloaded 
#     # print urs is to print the image file url 
#     # size is the image size which can 
#     # be specified manually ("large, medium, icon") 
#     # aspect ratio denotes the height width ratio 
#     # of images to download. ("tall, square, wide, panoramic") 
#     arguments = {"keywords": query, 
#                  "format": "jpg", 
#                 #  "limit":2, 
#                  "print_urls":True, 
#                 #  "size": "large"
#                 }
#     try: 
#         return response.download(arguments) 
      
#     # Handling File NotFound Error     
#     except e:
#         print("Error:", e)
#         pass
  
# # Driver Code 
# for query in search_queries: 
#     paths = downloadimages(query)  
#     print("Paths:", paths)  


from icrawler.builtin import BingImageCrawler, GoogleImageCrawler

# google_crawler = GoogleImageCrawler(storage={'root_dir': '.'})
# google_crawler.crawl(keyword='nature', max_num=100)

bing_crawler = BingImageCrawler(downloader_threads=4,
                                storage={'root_dir': 'nature_images'})
filters = {'size':'large'}                                
bing_crawler.crawl(keyword='nature', filters=filters, offset=0, max_num=1000)