from selenium import webdriver
from time import sleep
import re
import datetime
import zulip
def gettimeleft(time):
	data = re.findall("\d+",time);
	data = list(map(int,data));
	time_left = ((((data[0]*24)+data[1])*60)+data[2])*60+data[3];
	return time_left;
def gettime(t):
	now = datetime.datetime.now()
	now_plus_t = now+datetime.timedelta(seconds=t);
	return now_plus_t;
def printtime(t):
	s="";
	if(int(t/(3600*24))>0):	
		m = int(t/(3600*24));
		s+=str(m)+" day(s) ";
		t-=m*3600*24;

	if(int(t/3600)>0):
		m = int(t/3600);
		s += str(m)+" hour(s) ";
		t-=m*3600;
	
	if(int(t/60)>0):
		m = int(t/60);
		s+= str(m)+" minute(s)";
		t-=m*60;
	return s;

def posttozulip(data):
	s = "***Contest Update***\nCodeforces "+data[0]+" of Duration "+printtime(gettimeleft(data[1]));
	s+=" to start at "+gettime(gettimeleft(data[2])).strftime("%d %b %Y, %H:%M %Z")+"IST \n";
	s+="***Time Remaining: ";
	s+=printtime(gettimeleft(data[2]))
	s+="***\n";
	print(s);
	client = zulip.Client(config_file="zuliprc");
	request ={
		"type" : "stream",
		"to":	"test here",
		"subject": "contest bot",
		"content": s
	}
	result = client.send_message(request);
	print(result)
browser = webdriver.Firefox();
browser.get("https://dheeraj135.github.io/contest.html");
sleep(5);
table_id=browser.find_element_by_tag_name("table");
rows = table_id.find_elements_by_tag_name("tr");
arr=[]
i=0;
st=0;
for row in rows:
	if st ==0 :
		st=1;
		continue;
	arr.append([]);
	col=row.find_elements_by_tag_name("td");
	for c in col:
		arr[i].append(c.text);
	i+=1;
browser.quit();
arr = [r for r in arr if r!=[] ]
print(arr);
for r in arr:
	if gettimeleft(r[2]) <= 86400:
		print('ONE DAY LEFT!');
		posttozulip(r);
		print(r);