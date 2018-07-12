import mechanize
import cookielib
import time

class Twitter:
    def __init__(self):
        self.logged_in = False
        #browser initialization
        self.br = mechanize.Browser()

        # set cookies
        cookies = cookielib.LWPCookieJar()
        self.br.set_cookiejar(cookies)

        # browser settings (used to emulate a browser)
        self.br.set_handle_equiv(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_robots(False)
        self.br.set_debug_http(False)
        self.br.set_debug_responses(False)
        self.br.set_debug_redirects(False)
        self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


    def login(self, username, password):
        if(self.logged_in):
            return "Already logged in"

        self.br.open('https://mobile.twitter.com/login') # open twitter
        self.br.select_form(nr=1) # select the form
        self.br['session[username_or_email]'] = username
        self.br['session[password]'] = password
        self.br.submit() # submit the login data
        self.logged_in = True

    def tweet(self, message):
        self.br.open("https://mobile.twitter.com/compose/tweet")

        # If given a redicrected prompt, follow the link
        if(self.br.response().read().find("redirected")):
            self.br.follow_link(nr=0)

        # Send tweet
        self.br.select_form(nr=1)
        self.br['tweet[text]'] = message
        self.br.submit()
