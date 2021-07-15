#  encoding: utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import json
from jinja2 import Environment, FileSystemLoader
import os
print("""
Auth:Mi2ac1e
OneforallReporter
version:1.1
Fix some logic problem
""")
rname=input("[input]Named your Project,Don't use any symbol such as xx.com:")
json_name=input("[input]Input your json file name such as:tysec Do not include suffixes: ")

pwd=os.getcwd()
os.mkdir(pwd+'/'+rname)
os.makedirs(pwd+'/'+rname+'/'+'Screen')
print("[info]The project has been established")

# 从json中提取URL并写入到urls.txt
def urlwrite():
    with open(json_name+'.json','r',encoding='utf-8')as fp:
        json_data=json.load(fp)
        print(json_data)
        try:
            for urls in json_data:
                if(urls['url']!=None):
                    f=open(json_name+'.txt','a+')
                    f.write(urls['url']+'\n')
        except:print("[Error]Something wrong")

urlwrite()
print("[info]Urls has been writen")

# 读取url，并添加到url_list中
url_list=[]
f=open(json_name+'.txt','r')
b=0
for lines in f:
   url_list.append(lines)
   b=b+1
f.close()
print("[info]url list has been loaded")
url_list_lengh=len(url_list)
# 屏幕截图
def ChromeDriverNOBrowser():
   chrome_options = Options()
   chrome_options.add_argument('--headless')
   chrome_options.add_argument('--disable-gpu')
   driverChrome = webdriver.Chrome(options=chrome_options)
   """

   在我把这个ofaReporter移植到我的攻击平台的时，他出现了这样的提示：

   cannot find Chrome binary

   你可以用下面的语句指定你的Chrome安装路径：

   chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

   你需要自己更改一下你的Chrome安装目录

   """
   return driverChrome

driver=ChromeDriverNOBrowser()
driver.set_window_size(1920,1080)
i=0
for i in range(int(url_list_lengh)):
   try:

      driver.get(url_list[i])
      sleep(0.3)
#网页截图并保存
      driver.get_screenshot_as_file(rname+'/'+'Screen/'+str(i)+'.png')
      print("The"+str(i)+"pictrue has been capture")
   except:
      print("[--Error--]")
print("[info]Screen capture has been Finished")

def generate_html(body,starttime):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('template.html')
    with open(rname+'/'+"result.html",'w+') as fout:
        html_content = template.render(start_time=starttime ,
                                        body=body,


                                        )
        fout.write(html_content)

body = []
pic = []
k=0

with open(json_name+'.json', 'r', encoding='utf-8')as res:
    json_data = json.load(res)
    for mdata in json_data:
        if (mdata['url'] == None):break
        picpath = {'pic_path': 'Screen/' + str(k) + '.png'}
        mdata.update(picpath)
        result=mdata
        body.append(result)

        k = k + 1

generate_html(body,2021)
print("[info]Finished")

