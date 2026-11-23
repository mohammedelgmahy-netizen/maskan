import re,sys
src=open('/mnt/project-files/maskan-app/index.html',encoding='utf-8').read()
# drop embedded artifact data so server data is used
src=re.sub(r'<script type="application/json" id="siteData">.*?</script>','<script type="application/json" id="siteData"></script>',src,count=1,flags=re.S)
head='''<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0F5C4D">
<meta name="description" content="مسكن للتسويق العقاري: شقق وفلل وشاليهات ومحلات للبيع والإيجار في مصر">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="manifest" href="manifest.json">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="format-detection" content="telephone=no">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="مسكن">
<style>:root{color-scheme:light}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.min.js"></script>
<script src="config.js"></script>
</head>
<body>
'''
open('index.html','w',encoding='utf-8').write(head+src+'\n</body>\n</html>\n')
print("built")
