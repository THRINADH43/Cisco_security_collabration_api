"""Generation Base64 encoding using base64 library"""
import base64
encoded=base64.b64encode( "devasc:strongpassword".encode ('UTF8')).decode('ASCII')
print(encoded)
