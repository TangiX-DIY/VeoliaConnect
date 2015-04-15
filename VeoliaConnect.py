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
    file = open('veoliaconnect.log', 'a')
    file.write("%s\n" % pMessage)
    file.close()
    
class URL:
    
    def __init__(self):
        # On active le support des cookies pour urllib2
        cookiejar = cookielib.CookieJar()
        self.urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    
    def call(self, url, params = None, referer = None, output = None):
        Logger('Calling url')
        data = None if params == None else urllib.urlencode(params)
        request = urllib2.Request(url, data)
        if referer is not None:
            request.add_header('Referer', referer)
        response = self.urlOpener.open(request)
        Logger(" -> %s" % response.getcode())
        if output is not None:
            file = open(output, 'w')
            file.write(response.read())
            file.close()
        return response

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
    url = URL()
    
    urlConnect = 'https://www.service-client.veoliaeau.fr/home.loginAction.do#inside-space'
    urlConso1 = 'https://www.service-client.veoliaeau.fr/home/espace-client/votre-consommation.html'
    urlConso2 = 'https://www.service-client.veoliaeau.fr/home/espace-client/votre-consommation.html?vueConso=historique'
    urlXls = 'https://www.service-client.veoliaeau.fr/home/espace-client/votre-consommation.exportConsommationData.do?vueConso=historique'
    urlDisconnect = 'https://www.service-client.veoliaeau.fr/logout'
    
    # Connect to Veolia website
    Logger('Connection au site Véolia Eau')
    params = {'veolia_username' : args.login,
         'veolia_password' : args.password,
         'login' : 'OK'}
    referer = 'https://www.service-client.veoliaeau.fr/home.html'
    url.call(urlConnect, params, referer)
    
    # Page 'votre consomation'
    Logger('Page de consommation')
    url.call(urlConso1)
    
    # Page 'votre consomation : historique'
    Logger('Page de consommation : historique')
    url.call(urlConso2)
    
    # Download XLS file
    Logger('Téléchargement du fichier')
    response = url.call(urlXls)
    content = response.read()
    
    # logout
    Logger('Déconnection du site Véolia Eau')
    url.call(urlDisconnect)

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


