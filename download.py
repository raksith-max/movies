import urllib.request
import ssl
import zipfile
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file_id = "1jhYGqZdYyJpl-bc4ChrHoiPWOruvZSor"
# We can use the standard export URL or confirm URL.
# Sometimes Drive requires a confirmation token for large files, but for small files (507 KB), direct uc works.
url = f"https://drive.google.com/uc?export=download&id={file_id}"
output_zip = "Take_Home_Assignment.zip"

print(f"Downloading {url} to {output_zip}...")
try:
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'}
    )
    with urllib.request.urlopen(req, context=ctx) as response:
        content = response.read()
        
    with open(output_zip, 'wb') as f:
        f.write(content)
        
    print(f"Download complete. Size: {len(content)} bytes.")
    
    # Let's verify if it's a valid zip file and unzip it
    if zipfile.is_zipfile(output_zip):
        print("Extracting zip file...")
        with zipfile.ZipFile(output_zip, 'r') as zip_ref:
            zip_ref.extractall(".")
        print("Extraction complete!")
        # List contents of directory
        print("Contents of current directory:")
        for root, dirs, files in os.walk("."):
            print(f"Root: {root}")
            print(f"Dirs: {dirs}")
            print(f"Files: {files}")
            break # only show top level
    else:
        print("Error: The downloaded file is not a valid zip file. Content:")
        print(content[:500])

except Exception as e:
    print("An error occurred:", e)
