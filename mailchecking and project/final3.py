import email
import imaplib
username='xuetianhc@gmail.com'
password='your own pass'

mail=imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)
mail.select("inbox")

type, data = mail.search(None, 'ALL')

for num in data[0].split():
    type, data=mail.fetch(num, '(RFC822)')
    if type!='OK':
        print("sorry ho say no mail")
    msg=email.message_from_bytes(data[0][1])
    hdr=email.header.make_header(email.header.decode_header(msg['subject']))

    subject=str(hdr)
    print(subject)

    hdr = email.header.make_header(email.header.decode_header(msg['from']))
    frm=str(hdr)
    print(frm)

    hdr = email.header.make_header(email.header.decode_header(msg['to']))
    frm = str(hdr)
    print(frm)

    msg2 = email.message_from_bytes(data[0][1])
    msg3=msg2.get_payload(0)
    msg3=str(msg3)
    print(msg3)

