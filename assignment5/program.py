import sys
import json
import requests
from bands import Band
import collections
import bs4


EventInfo = collections.namedtuple('EventInfo',
                                    'city, state')

def main():
    usage_str = 'Usage: program.py ["bands", "venues"]'
    if len(sys.argv) != 2:
        print(usage_str)
    elif(sys.argv[1] == 'bands'):
        band_list = InstantiateBands()
        
        # two courses of action here ... 
        # some bands use BandsInTown, others don't
        #
        # 
        
        for band in band_list:
            print(band.name)
            print('--------------------------------------------')
            if band.band_id:
                json_event_str = GetJSONFromBandsInTown(band.band_id)
                band.json_events = json_event_str
                parsed_json = json.loads(band.json_events)
                for event in parsed_json:
                    if event['venue']['region'] == 'CA' or event['venue']['region'] == 'NV':
                        print("{}, {}\n\t{}".format(event['venue']['city'], event['venue']['region'], event['formatted_datetime']))
            else:
                print('This band needs hand parsing.')
                html = GetHTMLFromWeb(band.url)
                #print(html)
                #import foo
                methodToCall = getattr(Band, band.scrape_func)
                event_info = methodToCall(html)
                #event_info = GetEventInfoFromHTML(html)
                
            print()
            print()
            
    elif(sys.argv[1] == 'venues'):
        print("Venues: not implemented yet")
        venue_list = InstantiateVenues()
        
    else:
        print("Unknown option.")
        print(usage_str)
        
def GetHTMLFromWeb(url):
    """
    This is straight web-scraping for those bands that
    don't fully utilize BandsInTown ... or who don't use it at all
    """
    response = requests.get(url)
    return response.text
    

def GetEventInfoFromHTML(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for litag in soup.find_all('li', {'class': 'event'}):
        for h5tag in litag.find('h5'):
            print(h5tag)
      

def InstantiateVenues():
    """
    Reads the venues.json file for individual venue info.
    """
    
    
    pass
    
    
def InstantiateBands():
    """
    Reads the bands.json file for individual band info.
    Instantiates a new 'band' object for each band and 
    appends the object to a list of band objects.
    Finally, the list of objects is returned.
    """
    print("Instantiating bands...")
    band_list = []
    with open('bands.json') as data_file:
        data = json.load(data_file)
        for band in data:
            new_band_obj = Band(band['band_name'], band['website_tour_url'], band['bandsintown_id'], band['scrape_function'])
            band_list.append(new_band_obj)
    return band_list
    
    
def GetJSONEvents(name):
    return
            

def GetJSONFromBandsInTown(band_name):
    """
    Cobble together a url to send to the BandsInTown api.
    Call get for the response and return the text of the response.
    """
    url = "http://api.bandsintown.com/artists/{}/events.json?api_version=2.0&app_id=rsm".format(band_name)
    response = requests.get(url)
    return response.text
    
    
def ProcessVenues():
    pass
    
    
if __name__ == '__main__':
    main()



"""

</div></div><div class="sqs-block socialaccountlinks-v2-block sqs-block-socialaccountlinks-v2" data-block-type="54" id="block-yui_3_17_2_13_1427398652169_42962"><div class="sqs-block-content"><nav class="sqs-svg-icon--list social-icon-alignment-center social-icons-color-standard social-icons-size-large social-icons-shape-square social-icons-style-knockout"><a href="https://www.facebook.com/RioTheatreSantaCruz?ref=hl" target="_blank" class="sqs-svg-icon--wrapper facebook" style=""><div><svg class="sqs-svg-icon--social" viewBox="0 0 64 64"><use class="sqs-use--background" xlink:href="/universal/svg/social-accounts.svg#background"></use><use class="sqs-use--icon" xlink:href="/universal/svg/social-accounts.svg#facebook-icon"></use><use class="sqs-use--mask" xlink:href="/universal/svg/social-accounts.svg#facebook-mask"></use></svg></div></a></nav></div></div><div class="sqs-block horizontalrule-block sqs-block-horizontalrule" data-block-type="47" id="block-yui_3_17_2_14_1427273229959_17235"><div class="sqs-block-content"><hr /></div></div><div class="sqs-block html-block sqs-block-html" data-block-type="2" id="block-yui_3_17_2_17_1427773069616_11311"><div class="sqs-block-content"><h2 class="text-align-center">EVENTS</h2><p>SEPT 10 <a href="http://www.riotheatre.com/events-2/2016/9/10/2016-wbfa-santa-cruz-championships">2016 WBFA Championships</a><br />SEPT 13 <a href="http://www.riotheatre.com/events-2/2016/9/13/milk-carton-kids">Milk Carton Kids</a><br />SEPT 14 <a href="http://www.riotheatre.com/events-2/2016/9/14/brett-dennen">Brett Dennen</a><br />SEPT 22 <a href="http://www.riotheatre.com/events-2/2016/9/22/guitar-army-robben-ford-lee-roy-parnell-and-joe-robinson">Guitar Army</a><br />SEPT 23 <a href="http://www.riotheatre.com/events-2/2016/9/23/barry-mcguire-trippin-the-sixties-with-john-york">Barry McGuire</a><br />SEPT 24 <a href="http://www.riotheatre.com/events-2/2016/9/24/santa-cruz-guitar-company-40th-anniversary-celebration">Santa Cruz Guitar Co.</a><br />SEPT 25 <a href="http://www.riotheatre.com/events-2/2016/9/25/banff-mountain-film-festival-radical-reels-tour">Radical Reels Tour</a><br />SEPT 29 <a href="http://www.riotheatre.com/events-2/2016/9/29/dave-rawlings-machine">Dave Rawlings Machine</a><br />SEPT 30 <a href="http://www.riotheatre.com/events-2/2016/9/30/hot-tuna">Hot Tuna</a><br /><br />OCT 06 <a href="http://www.riotheatre.com/events-2/2016/10/6/reel-rock-11">Reel Rock 11</a><br />OCT 07 <a href="http://www.riotheatre.com/events-2/2016/10/7/santa-cruz-surf-film-festival">Santa Cruz Surf Film Festival</a><br />OCT 08 <a href="http://www.riotheatre.com/events-2/2016/10/8/santa-cruz-surf-film-festival">Santa Cruz Surf Film Festival</a><br />OCT 09 <a href="http://www.riotheatre.com/events-2/2016/10/9/marc-broussard">Marc Broussard</a><br />OCT 12 <a href="http://www.riotheatre.com/events-2/2016/10/12/the-julie-ruin">The Julie Ruin</a><br />OCT 13 <a href="http://www.riotheatre.com/events-2/2016/10/13/crowder">Crowder</a><br />OCT 16 <a href="http://www.riotheatre.com/events-2/2016/10/16/ian-harris-extraordinary">Ian Harris "ExtraOrdinary"</a><br />OCT 18 <a href="http://www.riotheatre.com/events-2/2016/10/18/the-proclaimers">The Proclaimers</a><br />OCT 21 <a href="http://www.riotheatre.com/events-2/2016/10/21/film-journey-in-sensuality">Film: Journey in Sensuality</a><br />OCT 22 <a href="http://www.riotheatre.com/events-2/2016/10/22/taking-back-sunday">Taking Back Sunday</a><br />OCT 23 <a href="http://www.riotheatre.com/events-2/2016/10/23/television">Television</a><br /><br />NOV 11 <a href="http://www.riotheatre.com/events-2/2016/11/11/john-mayall">J</a><a href="http://www.riotheatre.com/events-2/2016/11/11/john-mayall">ohn Mayall</a><br />NOV 12 <a href="http://www.riotheatre.com/events-2/2016/11/12/telluride-mountain-film-tour">Telluride Mountain Film</a><br />NOV 15 <a href="http://www.riotheatre.com/events-2/2016/11/15/neko-case">Neko Case</a><br />NOV 17 <a href="http://www.riotheatre.com/events-2/2016/11/17/warren-millers-here-there-everywhere">Warren Miller's Film</a><br />NOV 18 <a href="http://www.riotheatre.com/events-2/2016/11/18/asleep-at-the-wheel">Asleep at the Wheel</a><br />NOV 29 <a href="http://www.riotheatre.com/events-2/2016/11/29/charles-lloyd-the-marvels-featuring-bill-frisell-reuben-rogers-eric-harland-and-greg-leisz">Charles Lloyd &amp; the Marvels</a><br /><br />DEC 06 <a href="http://www.riotheatre.com/events-2/2016/12/6/holiday-circus">Holiday Circus</a><br />DEC 08 <a href="http://www.riotheatre.com/events-2/2016/12/8/alone-together-again-dave-mason">Dave Mason</a><br />DEC 20 <a href="http://www.riotheatre.com/events-2/2016/12/20/sweet-honey-in-the-rock">Sweet Honey in the Rock</a><br /><br />FEB 04 <a href="http://www.riotheatre.com/events-2/2017/2/4/the-comic-strippers">The Comic Strippers</a><br /><br />APR 22 <a href="http://www.riotheatre.com/events-2/2017/4/22/zep-live-the-led-zeppelin-concert-experience">Zep Live</a></p></div></div><div class="sqs-block horizontalrule-block sqs-block-horizontalrule" data-block-type="47" id="block-yui_3_17_2_62_1427309714001_42704"><div class="sqs-block-content"><hr /></div></div><div class="sqs-block html-block sqs-block-html" data-block-type="2" id="block-yui_3_17_2_62_1427309714001_42784"><div class="sqs-block-content"><h2 class="text-align-center">Become a Riozen!</h2><p class="text-align-center" dir="ltr">Sign up to receive our newsletter.</p></div></div><div class="sqs-block code-block sqs-block-code" data-block-type="23" id="block-yui_3_17_2_11_1427790235516_7598"><div class="sqs-block-content"><div align="center">
<table border="0" cellspacing="0" cellpadding="3" bgcolor="#000000" style="border:2px solid #000000;">
<tr>
</tr>
<tr>
"""
