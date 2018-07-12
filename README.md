# DET_Emulation

DET_Emulation is a proof of concept built to perform data exfiltration using popular
3rd parties such as Twitter, Gmail, or DropBox. DET_Emulation was built in
inspiration of [the popular repository, DET](https://github.com/sensepost/DET).
The difference, however, is that *DET_Emulation is an emulation of a browser
window, whereas DET uses the Twitter API*. This difference is substantial when
 looking at IDS logs and network activity, since API calls will create an SLL
 handshake and certificate exchange *for every GET request the API malware
 creates*, whereas normal browsing will only produce this handshake and exchange
 per browsing session. pg. 19 of [this report] describes the exchange in more
 detail, but here's basically what I'm talking about:
