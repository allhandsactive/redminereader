import feedparser, re, smtplib, unicodedata

def strip_tags(value):
    return re.sub(r'<[^>]*?>', '', value)

def send_mail(msg):
    from config import username,password,fromad,fromname,toad,subject
    fullmsg = "From: "+fromname+" <" +fromad+ ">\nTo: "+toad+\
            "\nSubject: "+subject+"\n\n\n"+ msg
    print fullmsg
    return
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.set_debuglevel(1)
    server.starttls()
    server.login(username,password)
    server.sendmail(fromad, toad, unicodedata.normalize('NFKD', fullmsg).encode('ascii','ignore'))
    server.quit()

def read(url):
    feedObj = feedparser.parse(url)
    msgbody = ''
    for i in feedObj['entries']:
        msgbody += i['title'] + ' -- ' + i['id'] + \
            "\nFrom: " + i['author'] + \
            "\n"+ '-'*72 +"\n" \
            + re.sub(r"(\s)+", r"\1", strip_tags(i['subtitle'])) + "\n\n"
    return msgbody

if __name__ == '__main__':
    from config import feedurl
    send_mail(read(feedurl))
