from flask import Flask, request ,redirect,abort
from SecretEncode import decode
from os import system,urandom

app = Flask(__name__)

blacklist=["..","'","&", ";", "$", "`", "||", "|", ">", "<", "(", ")", "{", "}", "[", "]", "IFS", "PATH", "echo", "printf", "read", "cat", "bash", "nc", "socat", "python", "perl", "ruby", "lua", "php", "gcc", "g++", "javac", "java", "ncat", "wget", "curl", "ftp", "scp", "ssh", "telnet", "ping", "nslookup", "traceroute", "nmap", "tcpdump", "wireshark","whoami","mocsctf","rb916120","flag"]

@app.route('/')
def index():
    return "welcome to Order as a service, you can place your order with /service?Order=&lt;query&gt; and see your result in /service?Show=&lt;query&gt;<br/><br/><b>Example:</b><br/>good query:<a href='/service?Order=😱😲😳😵'>/service?Order=😱😲😳😵</a><br/>bad query:<a href='/service?Order=😔😔'>/service?Order=😔😔</a><br/>bad query:<a href='/service?Order=😔😔😿🙅😳🙉😳🙊😸'>/service?Order=😔😔😿🙅😳🙉😳🙊😸</a><br/>bad query:<a href='/service?Order=😔😔😱😲😳😵⚓⚠⚡⚪'>/service?Order=😔😔😱😲😳😵⚓⚠⚡⚪</a><br/>"

@app.route('/service', methods=['GET'])
def service():
    Order=request.args.get('Order')
    Show=request.args.get('Show')
    safe=True
    if Order:
        decoded_Order = decode(Order).lower()

        for s in blacklist:
            if s in decoded_Order:
                safe=False
                return f"Hakcer!! <b>{decode(Order)}</b> is not allow"

        if safe:
            Order_id = str(urandom(32).hex())
            system(f"mkdir /tmp/{Order_id}")
            system(f"cp /flag.txt /tmp/{Order_id}/{decoded_Order}.txt")
            system(f"rm -f /tmp/{Order_id}/*.txt")
            return f"Your Order ID is : {Order_id}"

    elif Show:
        for s in blacklist:
            if s in Show.lower():
                safe=False
                return "Hacker!!"

        if safe:
            try:
                return open(f"/tmp/{Show}","r").readline()
            except:
                return abort(404)

    else:
        return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "No....Accesssssssssss..", 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9999)