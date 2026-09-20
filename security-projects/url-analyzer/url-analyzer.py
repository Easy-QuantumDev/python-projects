from urllib.parse import urlparse,parse_qs
import ipaddress
import requests


# security_headers= 
# [
# 'Content-Type',
# 'Server',
# 'Content-Length',
# 'Set-Cookie',
# 'Location',
# 'Strict-Transport-Security',
# 'X-Frame-Options',
# 'Content-Security-Policy'
# ]
url = 'https://stdn.iau.ir/Student/Pages/acmstd/loginPage.jsp'
result = urlparse(url)

print("\n========== URL ANALYSIS ==========\n")

response = requests.get(url)
if response.status_code == 200:
    print("[OK] Request successful")

elif response.status_code in [301, 302, 307, 308]:
    print("[INFO] Redirect detected")

elif response.status_code == 403:
    print("[INFO] Access forbidden")

elif response.status_code == 404:
    print("[INFO] Resource not found")

elif response.status_code >= 500:
    print("[WARNING] Server error")

else:
    print(f"[INFO] Status code: {response.status_code}")
    

print("\n========== RESPONSE HISTORY ==========\n")
print(f"{response.history}")

print(f'scheme : {result.scheme}')
print(f'netloc : {result.netloc}')
print(f'path : {result.path}')
print(f"params : {result.params}")
print(f'query : {result.query}')
print(f'fragmnet : {result.fragment}')
print(f"host name : {result.hostname}")
print(f'port : {result.port}')

print("\n========== SECURITY ==========\n")

if result.scheme == 'https':

    print("[ok] HTTPS is ok")

else:
    print("[WARNING] HTTPS is not enable ")
    

if result.username or result.password:
    
    print("[WARNING] username or password is in url")        

# test the hostname using a domain or ip address 

try:
    
    ipaddress.ip_address(result.hostname)
    print("[WARNING] url is using ip ")
except ValueError:
    print("[OK] url is using domain ")
                
param = parse_qs(result.query)
if param:
    print(f'[INFO] qs parse : {len(param)}')
else:
    print("[INFO] no query parameter")

allowed_schemes = ['http','https']
if result.scheme not in allowed_schemes:
    print('[WARNING] unusual scheme ')
else:
    print("[INFO] usaul scheme")                    
    
    

print("\n========== HEADERS ==========\n")

for header , value in response.headers.items():
    
    print(f'header {header} : {value}\n===================================')
print("\n========== COOKIES ==========\n")
for cookie in response.cookies:
    print(f'\n{cookie}\n===================================')
