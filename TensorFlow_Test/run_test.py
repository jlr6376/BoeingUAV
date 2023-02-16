import definitions as definitions
import load_dataset as ld

#Make sure you run the load_dataset prior to verifying image

# By Heiko Gorski, Source: https://commons.wikimedia.org/wiki/File:Naxos_Taverna.jpg
image_url = "https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg"  #@param
downloaded_image_path = definitions.download_and_resize_image(image_url, 1280, 856, True)
definitions.run_detector(ld.detector, downloaded_image_path)