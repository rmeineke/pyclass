import json

json_str = r"""
[
{"id":12435072,"title":"Moonsville Collective @ Pappy \u0026 Harriet's in Pioneertown, CA","datetime":"2016-09-16T20:00:00","formatted_datetime":"Friday, September 16, 2016 at 8:00PM","formatted_location":"Pioneertown, CA","ticket_url":"http://www.bandsintown.com/event/12435072/buy_tickets?app_id=rsm\u0026artist=Moonsville+Collective\u0026came_from=67","ticket_type":"Tickets","ticket_status":"available","on_sale_datetime":"2016-07-05T10:25:44","facebook_rsvp_url":"http://www.bandsintown.com/event/12435072?app_id=rsm\u0026artist=Moonsville+Collective\u0026came_from=67","description":"Moonsville Collective","artists":[{"name":"Moonsville Collective","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/large/6893341.jpeg","thumb_url":"https://s3.amazonaws.com/bit-photos/thumb/6893341.jpeg","facebook_tour_dates_url":"http://www.bandsintown.com/MoonsvilleCollective/facebookapp?came_from=67","facebook_page_url":"https://www.facebook.com/moonsvillecollective","tracker_count":1543,"url":"MoonsvilleCollective","website":null}],"venue":{"name":"Pappy \u0026 Harriet's","place":"Pappy \u0026 Harriet's","city":"Pioneertown","region":"CA","country":"United States","latitude":34.156263,"longitude":-116.493175}},
{"id":12401354,"title":"Moonsville Collective @ Long Beach Folk Revival in Long Beach, CA","datetime":"2016-09-17T11:00:00","formatted_datetime":"Saturday, September 17, 2016 at 11:00AM","formatted_location":"Long Beach, CA","ticket_url":"http://www.bandsintown.com/event/12401354/buy_tickets?app_id=rsm\u0026artist=Moonsville+Collective\u0026came_from=67","ticket_type":"Tickets","ticket_status":"available","on_sale_datetime":null,"facebook_rsvp_url":"http://www.bandsintown.com/event/12401354?app_id=rsm\u0026artist=Moonsville+Collective\u0026came_from=67","description":"The 4th Annual Long Beach Folk Revival Festival returns to Rainbow Lagoon Park on September 17th, 2016! \n\n Without further ado, we are downright thrilled to present:\nNitty Gritty Dirt Band\n Celebrating 50 Years | Founded in Long Beach, CA in 1966\n\n WITH\nThe White Buffalo | Chuck Ragan (Official) | JD McPherson\nLeo Bud Welch | Willy Tea Taylor | Big Sandy and his Fly-Rite Boys | The Lowest Pair | Moonsville Collective | Pearl Charles | Paige Anderson \u0026 The Fearless Kin | McDougall | Big Bad Rooster | Honey Whiskey Trio | The Hollow Trees | Echo Mountain | \u0026 introducing Smoggy Mountain String Band\n\nhttp://www.folkrevivalfestival.com/tickets\n Ticket are on sale now and are $35 in advance \n (pre-sale price to increase to $40 August 1st) \n and $50 at the door.\n\n Kids 12 and under as well as Seniors 75 or older get in free.\n\n In addition to the great music, all the fan favorites from last year are back including the signature contests (pie eating, beard \u0026 mustache, banjo), amazing gourmet food trucks \u0026 craft beers, interactive kid\u2019s area with the \u201cInstrument Petting Zoo\u201d, and the ever popular \u201cVintage Bazaar\u201d shopping experience and Craft Pavilion.\n\n ABOUT OUR HEADLINER\n Founded in Long Beach, CA in 1966, The Nitty Gritty Dirt Band are celebrating their Golden (50th) Anniversary together and will headline this year\u2019s Folk Revival Festival. Often cited as a catalyst for an entire movement in Country Rock and American Roots Music, garnering multi-platinum and gold records, strings of top ten hits such as \"Fishin' In The Dark\" and \"Mr. Bojangles\", multiple Grammy, IBMA, CMA Awards and nominations and their groundbreaking \"Will The Circle Be Unbroken\" album has recently been inducted into the U.S. Library of Congress as well as the Grammy Hall of Fame.\n\n \"We're really excited to be coming back to Long Beach for the Folk Revival Festival this September! Most of us grew up there and our band got its start jamming at McCabe's in Long Beach in 1966, so it seems totally fitting that we celebrate our 50th Year in the city where it all began for NGDB!\" says Jeff Hanna, founding Nitty Gritty Dirt Band member.\n\n It has been over 40 years since the Nitty Gritty Dirt Band has played a show in their hometown and they plan on Circlin\u2019 Back to where it all started for one historic night in beautiful downtown Long Beach\u2019s Rainbow Lagoon Park.\n\n\n _________________________________________________\n\n\n DIRECTIONS TO THE FESTIVAL\n\n The Folk Revival Festival is conveniently located in beautiful downtown Long Beach, CA right along the ocean front at Rainbow Lagoon Park. The official address is: E Shoreline Dr Long Beach, CA 90802\n\n We love to keep things green and sustainable at the festival and if you could help us out by using an alternative type of transportation to get here we would really appreciate it and so would Mother Earth!\n\n ON A BIKE\n\n We will have a bike valet at the festival FREE of charge for you to park your bike and not have to worry about it. It will be attended by good people at Bike Loca at all times. The festival location is nestled right along a Class I Bike Path that connects to the LA River Bike Path as well as the Beach Path just below the Bluffs that takes you all the way to Belmont Shore. \n\n BY BUS\n\n Taking the bus is a great way to reduce that carbon footprint and once you are in downtown Long Beach you can catch the Passport bus for FREE and it takes you right to the festival location. \n\n BY CAR\n\n If you have to come by car we ask that you carpool with a friend! Getting to the festival by car could not be any easier and all you have to do is take the 405 Fwy to the 710 Fwy South and the 710 turns into Shoreline Village Dr. \n\n PARKING\n\n Parking around Rainbow Lagoon Park is plentiful and there are many options. The most convenient parking is adjacent to the park in the LB Convention Center Parking Lot which is $10 for all day parking as well as Shoreline Village \u0026 The Marina parking lots.\n\n\n FREQUENTLY ASKED QUESTIONS\n\n Do I need a ticket? And what is the cost?\n Yes. This is a ticketed event, but Kids 12 \u0026 under as well as Seniors 75 \u0026 over are FREE! Please refer to the TICKETS page for more info.\n\n What time does the show start?\n Doors open at 11am. The first musical act starts at 11:15 am. The festival is over at 11pm.\n\n What can I do after the festival is over?\n TBA\n\n Is there seating available?\n General Admission tickets for this event do not guarantee a seat. Seating is limited so please arrive early. We will be letting all patrons bring a low backed chair or blanket to sit on this year!\n\n Where can I eat?\n There will be gourmet food trucks \u0026 booths at our food court with a range of dining choices. No outside food or drink is permitted. More info on our vendors is on the Food \u0026 Craft Beer page.\n\n Is alcohol permitted?\n There will be several full service bars within the venue pouring your favorite local craft brews as well as hard liquor \u0026 wine. You may not bring alcohol into the venue and consumption of alcohol is not permitted in public spaces. See our Food \u0026 Craft Beer page for more details.\n\n Can I go in and out of the venue?\n Yes you can go in and out of the venue freely and we encourage you to check out the local shops, businesses, and art galleries near by.\n\n Is there an age limit to attend?\n The Folk Revival Festival is an all ages event, but alcohol will be served throughout the festival premises to those with a valid ID showing they are 21 years of age.\n\n Are pets allowed?\n Pets are NOT allowed at the festival.\n\n Is smoking permitted?\n Smoking is only permitted in the designated smoking areas or please step outside the event (at least 15 feet from the entrance) if you would like to smoke.\n\n What items are NOT allowed inside the venue?\n\n Bikes\n Glass bottles\n Food \n Liquids in glass or plastic (other than 1 bottle of unopened water)\n Large Umbrellas\n Markers\n Weapons of any kind\n Professional video/audio equipment (contact media@folkrevivalfestival.com for more info)\n\n What happens if it rains?\n In the unlikely event that there is rain, we suggest you dress appropriately. LB Folk Revival Festival is a \u2018rain or shine\u2019 event.\n\n Will Recycling be available?\n Yes, recycling is available and we encourage you to use them and help us move closer to being a Zero waste event. Help us keep the park clean by leaving with all you came with! In addition we will also be composting food waste and biodegradable packaging. Please do your part to keep our festival green!\n\n Where is first aid located?\n If you require first aid assistance, please visit the Medical booth next to the Kids Area. If it is an emergency, please call 911.\n\n Where is the lost and found?\n Please visit the Ticket Booth/Tent for any lost items.\n\n For other questions: \n info@folkrevivalfestival.com","artists":[{"name":"Moonsville Collective","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/large/6893341.jpeg","thumb_url":"https://s3.amazonaws.com/bit-photos/thumb/6893341.jpeg","facebook_tour_dates_url":"http://www.bandsintown.com/MoonsvilleCollective/facebookapp?came_from=67","facebook_page_url":"https://www.facebook.com/moonsvillecollective","tracker_count":1543,"url":"MoonsvilleCollective","website":null},{"name":"Nitty Grtty Dirt Band","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/NittyGrttyDirtBand/facebookapp?came_from=67","facebook_page_url":null,"tracker_count":1,"url":"NittyGrttyDirtBand","website":null},{"name":"The White Buffalo","mbid":"2d1997f7-5cb9-43b0-80bf-9ff9555561ac","image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/TheWhiteBuffalo/facebookapp?came_from=67","facebook_page_url":"https://www.facebook.com/thewhitebuffalomusic","tracker_count":56020,"url":"TheWhiteBuffalo","website":"http://www.thewhitebuffalo.com"},{"name":"JD McPHERSON","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/JdMcpherson/facebookapp?came_from=67","facebook_page_url":"https://www.facebook.com/jdmcphersonhistyle","tracker_count":37403,"url":"JdMcpherson","website":null},{"name":"PAIGE ANDERSON","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/PaigeAnderson/facebookapp?came_from=67","facebook_page_url":null,"tracker_count":55,"url":"PaigeAnderson","website":null},{"name":"Willie Tea Taylor","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/WillieTeaTaylor/facebookapp?came_from=67","facebook_page_url":null,"tracker_count":42,"url":"WillieTeaTaylor","website":null},{"name":"Honey Whiskey Trio","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/HoneyWhiskeyTrio/facebookapp?came_from=67","facebook_page_url":null,"tracker_count":402,"url":"HoneyWhiskeyTrio","website":null},{"name":"Big Sandy and the Fly-Right Boys","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/BigSandyAndTheFly-rightBoys/facebookapp?came_from=67","facebook_page_url":null,"tracker_count":0,"url":"BigSandyAndTheFly-rightBoys","website":null},{"name":"The Lowest Pair","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/TheLowestPair/facebookapp?came_from=67","facebook_page_url":"http://www.facebook.com/pages/The%20Lowest%20Pair/119655678232593","tracker_count":4658,"url":"TheLowestPair","website":null},{"name":"Big Bad Rooster","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/BigBadRooster/facebookapp?came_from=67","facebook_page_url":"http://www.facebook.com/pages/Big%20Bad%20Rooster/141438179274207","tracker_count":162,"url":"BigBadRooster","website":null},{"name":"PEARL CHARLES","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/PearlCharles/facebookapp?came_from=67","facebook_page_url":"http://www.facebook.com/pages/Pearl%20Charles/1459031800988156","tracker_count":1595,"url":"PearlCharles","website":null}],"venue":{"name":"Long Beach Folk Revival","place":"Rainbow Lagoon","city":"Long Beach","region":"CA","country":"United States","latitude":33.76212,"longitude":-118.187933}},
{"id":12401461,"title":"Moonsville Collective @ TBA in Nashville, TN","datetime":"2016-09-21T20:00:00","formatted_datetime":"Wednesday, September 21, 2016 at 8:00PM","formatted_location":"Nashville, TN","ticket_url":"http://www.bandsintown.com/event/12401461/buy_tickets?app_id=rsm\u0026artist=Moonsville+Collective\u0026came_from=67","ticket_type":"Tickets","ticket_status":"available","on_sale_datetime":null,"facebook_rsvp_url":"http://www.bandsintown.com/event/12401461?app_id=rsm\u0026artist=Moonsville+Collective\u0026came_from=67","description":"We are honored to perform at the 2016 Americana Music Awards Festival. \n\nAll the info for tickets to the Festival is on their website. We will keep you posted with more details as we get closer. \n\n\nNew to the Lineup Include: Amanda Shires, Billy Bragg \u0026 Joe Henry, \n Bruce Hornsby \u0026 the Noisemakers, Dori Freeman, Howe Gelb, Jack Ingram, John Fullbright, John Prine, Kaia Kater, Motel Mirrors, \n My Bubba, Sam Outlaw, Sean Watkins, Shawn Colvin \u0026 Steve Earle, \n The Cordovas, The O'Connor Band featuring Mark O'Connor\n\nWristbands \u0026 Registrations On Sale Now!\n\n                                                                                               \nThe Americana Music Association proudly unveiled its second round of AmericanaFest 2016 performers today. Additions to this year\u2019s lineup include: Amanda Shires, Billy Bragg \u0026 Joe Henry, Bruce Hornsby \u0026 the Noisemakers, Dori Freeman, Howe Gelb, Jack Ingram, John Fullbright, John Prine, Kaia Kater, Motel Mirrors, My Bubba, Sam Outlaw, Sean Watkins, Shawn Colvin \u0026 Steve Earle, The Cordovas, and The O'Connor Band featuring Mark O'Connor.\n\nToday\u2019s additions bring the 17th Annual AmericanaFest artist list to 121 and more than 180 artists will be announced by the first week in September. \n\nShowcase wristbands are currently on sale ($60) and allow admission into all showcase venues, some sanctioned parties and special events, and can be purchased here. Festival and Conference registrations ($275 for members/$375 for non-members) offer priority admission into all showcase venues, sanctioned parties and events, daytime educational panels. Conference registrants may purchase a ticket to the Americana Honors \u0026 Awards show at the historic Ryman Auditorium, and can be purchased here.\n  \n\nCurrent List of Confirmed Performers: \n (*New additions in bold)\n\nAaron Lee Tasjan\n The Accidentals\n Amanda Shires\n Amelia Curran\n The Americans\n Amy Helm\n Aoife O'Donovan\nApplewood Road\n Aubrie Sellers\n B R U N S\n The Ballroom Thieves\n Bart Crow\nBilly Bragg \u0026 Joe Henry\n Birger Olsen (of Denver)\n BJ Barham (of American Aquarium)\n The Black Lillies\nBobby Rush\n Bonnie Bishop\n The Bottle Rockets\n Brent Cobb\n Brian Whelan\n Brian Wright\nBruce Hornsby \u0026 The Noisemakers\n Buddy Miller\nC.W. Stoneking\n The Cactus Blossoms\nCaleb Caudle\n Carl Anderson\n Cedric Burnside Project\nCharlie Faye \u0026 The Fayettes\n Charlie Parr\n Ciaran Lavery\nThe Cordovas\n David Ramirez\n Dead Horses\n Derik Hultquist\nDex Romweber\n Dietrich Strause\nDori Freeman\n Dylan LeBlanc\nThe Fearless Kin\n Front Country\n Grant-Lee Phillips\n Green River Ordinance\n The Handsome Family\nHarpoonist \u0026 the Axe Murderer\n Hollis Brown\nHowe Gelb\n Indianola\n Indigo Girls\n The Infamous Stringdusters\nJack Ingram\n Jason Eady\n Jay Nash\n Jesse Malin\nJim Lauderdale\n Joe Purdy\nJohn Fullbright\n John Paul White\nJohn Prine\n Kaia Kater\n Kasey Chambers\n Larkin Poe\n Larry Campbell \u0026 Teresa Williams\n The Last Bandoleros\n LAU\n Lee Ann Womack\nLewis \u0026 Leigh\n The Lonely Heartstring Band\n Lori McKenna\nLowland Hum\n Luke Bell\n Lydia Loveless\nMandolin Orange\n Marlon Williams\nMatt Haeck\n Mindy Smith\nMolly Parden\n Moonsville Collective\nMotel Mirrors\n My Bubba\n The O'Connor Band featuring Mark O'Connor\n Paper Bird\n Parker Millsap\n Penny \u0026 Sparrow\n Peter Bruntnell\n Phil Cody\n The Pines\n Quiet Life\nRed Shahan\n Reverend Peyton's Big Damn Band\nRiver Whyless\n Rob Baird\n Robert Vincent\n Ruby Amanfu\n Ruby Boots\n Ruston Kelly\n Ryan Beaver\nSam Lewis\n Sam Outlaw\n Sammy Brue\n Sara Watkins\n Sarah Potenza\nSean McConnell\n Sean Watkins\n Shane Nicholson\n Shawn Colvin \u0026 Steve Earle\n Shawn Mullins\n Sons of Bill\nSteve Poltz\n Sunny Sweeney\n Susto\n Teddy Thompson \u0026 Kelly Jones\nTony Joe White\n Whitney Rose\n Will Hoge\n William Clark Green\nWilliam the Conqueror\n Willie Watson\n Wynonna \u0026 The Big Noise\nYola Carter \n\nMore than 180 artists are slated to perform during the 17th Annual Americana Music Festival \u0026 Conference, which runs from September 20-25 in Nashville, TN. The six-day festival will fill Music City with legends, newcomers, award winners, and buzz bands, showcasing the breadth of Americana's influence.\n\n \n\n\n  \n\nhttp://americanamusic.org/about-americanafest","artists":[{"name":"Moonsville Collective","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/large/6893341.jpeg","thumb_url":"https://s3.amazonaws.com/bit-photos/thumb/6893341.jpeg","facebook_tour_dates_url":"http://www.bandsintown.com/MoonsvilleCollective/facebookapp?came_from=67","facebook_page_url":"https://www.facebook.com/moonsvillecollective","tracker_count":1543,"url":"MoonsvilleCollective","website":null},{"name":"Steve Earle","mbid":"ec863030-7c13-45a3-a025-a69195d3a020","image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/SteveEarle/facebookapp?came_from=67","facebook_page_url":"https://www.facebook.com/SteveEarleMusic","tracker_count":183679,"url":"SteveEarle","website":"http://www.steveearle.com"},{"name":"John Prine","mbid":"e86492c1-0376-4df0-8042-8ba058c83960","image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/JohnPrine/facebookapp?came_from=67","facebook_page_url":"http://www.facebook.com/pages/John%20Prine/49424414445","tracker_count":96811,"url":"JohnPrine","website":"http://www.johnprine.net"},{"name":"Billy Bragg \u0026 Joe Henry","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/BillyBraggAndJoeHenry/facebookapp?came_from=67","facebook_page_url":null,"tracker_count":1,"url":"BillyBraggAndJoeHenry","website":null},{"name":"Amy Helm","mbid":"34a977be-ef17-4ab9-b34d-959a89e7e534","image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/AmyHelm/facebookapp?came_from=67","facebook_page_url":"https://www.facebook.com/AmyHelmMusic","tracker_count":7714,"url":"AmyHelm","website":""},{"name":"The Americans","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/TheAmericans/facebookapp?came_from=67","facebook_page_url":"http://www.facebook.com/pages/The%20Americans/184120396629","tracker_count":2045,"url":"TheAmericans","website":""},{"name":"Sam Outlaw","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/SamOutlaw/facebookapp?came_from=67","facebook_page_url":"http://www.facebook.com/pages/Sam%20Outlaw/124951044224903","tracker_count":4756,"url":"SamOutlaw","website":null},{"name":"The Fearless Kinn","mbid":null,"image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/TheFearlessKinn/facebookapp?came_from=67","facebook_page_url":null,"tracker_count":0,"url":"TheFearlessKinn","website":null},{"name":"The Infamous Stringdusters","mbid":"43e088bd-2520-4a84-bb8e-827c86d2cf84","image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/TheInfamousStringdusters/facebookapp?came_from=67","facebook_page_url":"https://www.facebook.com/thestringdusters","tracker_count":34913,"url":"TheInfamousStringdusters","website":"http://thestringdusters.com/"},{"name":"Jim Lauderdale","mbid":"563c84bf-b1e4-423e-b871-a46c68998d10","image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/JimLauderdale/facebookapp?came_from=67","facebook_page_url":"https://www.facebook.com/JimLauderdaleOfficial","tracker_count":10666,"url":"JimLauderdale","website":"http://jimlauderdale.com"},{"name":"John Paul White","mbid":"41476780-c7b2-4521-9752-67ce823b3695","image_url":"https://s3.amazonaws.com/bit-photos/artistLarge.jpg","thumb_url":"https://s3.amazonaws.com/bit-photos/artistThumb.jpg","facebook_tour_dates_url":"http://www.bandsintown.com/JohnPaulWhite/facebookapp?came_from=67","facebook_page_url":"http://www.facebook.com/pages/John%20Paul%20White/8627638950","tracker_count":21111,"url":"JohnPaulWhite","website":"http://www.johnpaulwhite.net"}],"venue":{"name":"TBA","place":"TBA","city":"Nashville","region":"TN","country":"United States","latitude":36.1658333,"longitude":-86.7844444}}
]
"""


#print(json_str)
parsed_json = json.loads(json_str)
for event in parsed_json:
    print("{}, {}\t: {}".format(event['venue']['city'], event['venue']['region'], event['formatted_datetime']))
