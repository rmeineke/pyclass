import sys
import json
import requests
from bands import Band

def main():
    usage_str = 'Usage: program.py ["bands", "venues"]'
    if len(sys.argv) != 2:
        print(usage_str)
    elif(sys.argv[1] == 'bands'):
        band_list = InstantiateBands()
        for band in band_list:
            json_event_str = GetJSONFromBandsInTown(band.band_id)
            band.json_events = json_event_str
            #print(band.json_events)
    elif(sys.argv[1] == 'venues'):
        print("Venues: not implemented yet")
    else:
        print("Unknown option.")
        print(usage_str)
        
    
    
def InstantiateBands():
    print("Instantiating bands...")
    band_list = []
    with open('bands.json') as data_file:
        data = json.load(data_file)
        for band in data:
            new_band_obj = Band(band['band_name'], band['website_tour_url'], band['bandsintown_id'])
            band_list.append(new_band_obj)
    return band_list
    
    
def GetJSONEvents(name):
    return
#def InstantiateBands():
    #print("Instantiating bands...")
    #band_list = []
    #with open('bands.json') as data_file:
        #data = json.load(data_file)
        #for band in data:
            #new_band_obj = Band(band['band_name'], band['website_tour_url'], band['bandsintown_id'])
            #json_event_str = GetJSONFromBandsInTown(band['bandsintown_id'])
            #setattr(new_band_obj, 'json_str', json_event_str)
            #print(new_band_obj)
            

def GetJSONFromBandsInTown(band_name):
    url = "http://api.bandsintown.com/artists/{}/events.json?api_version=2.0&app_id=rsm".format(band_name)
    response = requests.get(url)
    return response.text
    
    
def ProcessVenues():
    pass
    
    
if __name__ == '__main__':
    main()
