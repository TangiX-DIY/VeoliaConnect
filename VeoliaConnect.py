#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 11:01:40 2015

@author: tangix
"""

import argparse
import cookielib,urllib2,urllib

# Logger
def Logger(pMessage):
    file = open('/var/log/veoliaconnect.log', 'a')
    file.write("%s/n" % pMessage)
    file.close()

# On active le support des cookies pour urllib2
cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    '-l', '--login',
    help='your login on VeoliaEau website'
)
parser.add_argument(
    '-p', '--password',
    help='your password on VeoliaEau website'
)
parser.add_argument(
    '-s', '--spreadsheet',
    type=argparse.FileType('r'),
    help='use this spreadsheet insted of website one')
parser.add_argument(
    '-o', '--output',
    help='store the spreadsheet'
)
parser.add_argument(
    '-f', '--format',
    default='text',
    choices=['text', 'json', 'xml', 'none'],
    help='change output format'
)
args = parser.parse_args()
args.web = args.login is not None and args.password is not None
if not args.web and args.spreadsheet is None:
    parser.error('No action requested, add credentials or spreadsheet')
    
# WebSite gathering
if args.web:
    urlConnect = 'https://www.service-client.veoliaeau.fr/home.loginAction.do#inside-space'
    urlConso1 = 'https://www.service-client.veoliaeau.fr/home/espace-client/votre-consommation.html'
    urlConso2 = 'https://www.service-client.veoliaeau.fr/home/espace-client/votre-consommation.html?vueConso=historique'
    urlXls = 'https://www.service-client.veoliaeau.fr/home/espace-client/votre-consommation.exportConsommationData.do?vueConso=historique'
    urlDisconnect = 'https://www.service-client.veoliaeau.fr/logout'
    
    param = {'veolia_username' : args.login,
             'veolia_password' : args.password,
             'login' : 'OK'}
    
    # Connect to Veolia website
    Logger('Connection au site Véolia Eau')
    data = urllib.urlencode(param)
    request = urllib2.Request(urlConnect, data)
    request.add_header('Referer', 'https://www.service-client.veoliaeau.fr/home.html')
    response = urlOpener.open(request)
    Logger(response.getcode())
    Logger(response.info())
    #file = open('/tmp/home.html', 'w')
    #file.write(response.read())
    #file.close()
    
    # page votre consomation
    #print 'Conso 1'
    response = urlOpener.open(urlConso1)
    #print response.getcode()
    #print response.info()
    #file = open('/tmp/conso1.html', 'w')
    #file.write(response.read())
    #file.close()
    
    #print 'Conso 2'
    response = urlOpener.open(urlConso2)
    #print response.getcode()
    #print response.info()
    #file = open('/tmp/conso2.html', 'w')
    #file.write(response.read())
    #file.close()
    
    # Download XLS file
    #print 'Téléchargement du fichier'
    response = urlOpener.open(urlXls)
    #print response.getcode()
    #print response.info()
    content = response.read()
    #file = open('/tmp/data.xls', 'w')
    #file.write(content)
    #file.close()
    
    #logout
    #print "Déconnection du site Véolia Eau"
    response = urlOpener.open(urlDisconnect)
    #print response.getcode()
    #print response.info()

# Get external spreadsheet content
if args.spreadsheet is not None:
    #TODO
    print 'TODO read spreadsheet'
    
# Store spreadsheet content
if args.output is not None:
    file = open(args.output, 'w')
    file.write(content)
    file.close()
    
# Parse spreadsheet contents
if args.format != 'none':
    #TODO
    print 'TODO parse data'


