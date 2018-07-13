# C2_DDR

#### Full C2 using legitimate services

C2_DDR is a proof-of-concept to perform data exfiltration using popular
3rd parties such as Twitter, Gmail, or DropBox. C2_DDR was built in
inspiration of the popular repository, [DET](https://github.com/sensepost/DET).

The difference, however, is that **C2_DDR is an emulation of a browser
window, whereas DET uses the Twitter API**. This difference is substantial when
 looking at IDS logs and network activity, since API calls will create an SSL
 handshake and certificate exchange *for every GET request the API malware
 creates*, whereas normal browsing will only produce this handshake and exchange
 per browsing session. 
 
 I believe this method of exfiltration is more realistic as the attacker 
 would hide (more) in plain sight, as well as be able to use new Twitter 
 accounts that are uncomfirmed.
 
 Pg. 19 of [this report] describes the exchange in more
 detail, but here's basically what I'm talking about:

![image](/GET_vs_Browsing.png)

Current, C2_DDR does the following:
* converts a message or file into base64
* Logs in to mobile.twitter.com
* parses the base64 message into 280 characters 
* sends each one until the file as been exfiltrated

Features to add:
* Use 3rd party mediums such as Gmail and DropBox
* Create a server script that will fetch exfiltrated data
