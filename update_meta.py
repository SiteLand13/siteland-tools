import os
import re
import glob

files = glob.glob('src/routes/index.tsx') + glob.glob('src/routes/index.ts')
if not files:
    print('No route file found')
    exit(0)

f = files[0]
content = open(f).read()
site_name = os.environ.get('SITE_NAME', '')
site_desc = os.environ.get('SITE_DESCRIPTION', '')
og_image = os.environ.get('SITELAND_OG_IMAGE', '')

content = re.sub(r'\{ title: "[^"]*" \}', '{ title: "' + site_name + '" }', content)
content = re.sub(r'\{ name: "description", content: "[^"]*" \}', '{ name: "description", content: "' + site_desc + '" }', content)
content = re.sub(r'\{ property: "og:title", content: "[^"]*" \}', '{ property: "og:title", content: "' + site_name + '" }', content)
content = re.sub(r'\{ property: "og:description", content: "[^"]*" \}', '{ property: "og:description", content: "' + site_desc + '" }', content)
content = re.sub(r'\{ property: "og:image", content: "[^"]*" \}', '{ property: "og:image", content: "' + og_image + '" }', content)

open(f, 'w').write(content)
print('Meta updated in', f)
