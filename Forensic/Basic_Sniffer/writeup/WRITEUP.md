Basic Sniffing
Writeup - Forensic (Easy)

Challenge: I got a file seems it's from packet capture. Would you please help to check if there is any secret inside

Hint: The capture is based on Fiddler (https://www.telerik.com/download/fiddler)

Flag: MOCSCTF{B@5ic_Sn1ff1ng_Y0u_P@55!!}

Writeup:
1. Open the captured file using Fiddler.
2. Pay attention to the connection to https://apac.ng.msg.teams.microsoft.com
3. On right hand upper side on Fiddler GUI, check "Raw" of the related packets.
4. In 28th packet, you can see payload as below
{"content":"<p>Just to say hi and here TU9DU0NURntCQDVpY19TbjFmZjFuZ19ZMHVfUEA1NSEhfQ==</p>","messagetype":"RichText/Html","contenttype":"text","amsreferences":[],"clientmessageid":"2967705139208561798","imdisplayname":"onprem User41","properties":{"importance":"","subject":""}}
5. Seems TU9DU0NURntCQDVpY19TbjFmZjFuZ19ZMHVfUEA1NSEhfQ== is Base64 encoded. Use Base64 decoder (e.g. https://www.base64decode.org/) to decode, get the flag: MOCSCTF{B@5ic_Sn1ff1ng_Y0u_P@55!!}