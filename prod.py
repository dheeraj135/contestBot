from selenium import webdriver
from time import sleep
import re
import datetime
import zulip
printall=0;
def gettimeleft_cs(time):
	data = re.findall("\d+",time);
	data = list(map(int,data));
	time_left=(datetime.datetime(data[2],data[1],data[0],data[5],data[6])-datetime.datetime.utcnow()).total_seconds()
	return int(time_left);
def posttozulip_cs(data,t):
	s ="***Contest Update***\nCS Academy "+data[0]+" of Duration "+data[2]+" to start at "+data[1]+"\n";
	s+="***Time Remaining: ";
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
	
	s+="***\n";
	print(s);
	client = zulip.Client(config_file="zuliprc");
	request = {
		"type" : "stream",
		"to": "test here",
		"subject": "Script Testing",
		"content": s
	}
	result = client.send_message(request);
	print(result)

def csacademy():
	options= webdriver.FirefoxOptions();
	options.add_argument('-headless');
	browser = webdriver.Firefox(firefox_options=options)
	browser.get("https://csacademy.com/contests/");
	sleep(4);
	waste = browser.find_element_by_tag_name("body");
	sleep(4);
	waste = browser.find_element_by_tag_name("body");
	sleep(4);	
	table_id = browser.find_element_by_tag_name("table");
	rows = table_id.find_elements_by_tag_name("tr");
	arr =[]
	i=0;
	for row in rows:
		arr.append([])
		col = row.find_elements_by_tag_name("td");
		for c in col:
			arr[i].append(c.text);
		i+=1;
	browser.quit();
	arr=[r for r in arr if r!=[] ]
	print(arr);
	for r in arr:
		if gettimeleft_cs(r[1])<=86400 or printall:
			print('ONE DAY LEFT!');
			posttozulip_cs(r,gettimeleft_cs(r[1]));


def gettimeleft_cf(time):
	data = re.findall("\d+",time);
	data = list(map(int,data));
	time_left = ((((data[0]*24)+data[1])*60)+data[2])*60+data[3];
	return time_left;
def gettime_cf(t):
	now = datetime.datetime.now()
	now_plus_t = now+datetime.timedelta(seconds=t);
	return now_plus_t;
def printtime_cf(t):
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

def posttozulip_cf(data):
	s = "***Contest Update***\nCodeforces "+data[0]+" of Duration "+printtime_cf(gettimeleft_cf(data[1]));
	s+=" to start at "+gettime_cf(gettimeleft_cf(data[2])).strftime("%d %b %Y, %H:%M %Z")+"IST \n";
	s+="***Time Remaining: ";
	s+=printtime_cf(gettimeleft_cf(data[2]))
	s+="***\n";
	print(s);
	client = zulip.Client(config_file="zuliprc");
	request ={
		"type" : "stream",
		"to":	"test here",
		"subject": "Script Testing",
		"content": s
	}
	result = client.send_message(request);
	print(result)

def codeforces():
	options= webdriver.FirefoxOptions();
	options.add_argument('-headless');
	browser = webdriver.Firefox(firefox_options=options)
	browser.get("https://dheeraj135.github.io/contest.html");
	sleep(4);
	waste = browser.find_element_by_tag_name("body");
	sleep(4);
	waste = browser.find_element_by_tag_name("body");
	sleep(4);	
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
		if gettimeleft_cf(r[2]) <= 86400 or printall:
			print('ONE DAY LEFT!');
			posttozulip_cf(r);
			print(r); 

def gettimeleft_cc(time):
	data = re.findall("\d+",time);
	data = list(map(int,data));
	timeleft=(datetime.datetime.strptime(time,"%d %b %Y\n%H:%M:%S")-datetime.datetime.utcnow()).total_seconds();
	return timeleft-330*60;

def posttozulip_cc(data):
	s = "***Contest Update***\nCodechef "+data[1]+" of Duration "+printtime_cf((gettimeleft_cc(data[3])-gettimeleft_cc(data[2])));
	s+=" to start at "+gettime_cf(gettimeleft_cc(data[2])).strftime("%d %b %Y, %H:%M %Z")+"IST \n";
	s+="***Time Remaining: ";
	s+=printtime_cf(gettimeleft_cc(data[2]))
	s+="***\n";
#	if(gettimeleft_cc(data[2])<=60*60):
#		if(gettimeleft_cc(data[2])<=30*60&&gettimeleft_cc(data[2])>=24*60):
#			s+="Contest is about to start!!!\n";

	print(s);
	client = zulip.Client(config_file="zuliprc");
	request ={
		"type" : "stream",
		"to":	"test here",
		"subject": "Script Testing",
		"content": s
	}
	result = client.send_message(request);
	print(result)
def codechef():
	options= webdriver.FirefoxOptions();
	options.add_argument('-headless');
	browser = webdriver.Firefox(firefox_options=options)
	browser.get("https://www.codechef.com/contests");
	sleep(4);
	waste = browser.find_element_by_tag_name("body");
#	sleep(4);
	waste = browser.find_element_by_tag_name("body");
#	sleep(4);
	table_id = browser.find_elements_by_tag_name("table");
	rows = table_id[2].find_elements_by_tag_name("tr");
	arr = []
	i=0
	st=0
	for row in rows:
		if st==0:
			st=1;
			continue;
		arr.append([]);
		col = row.find_elements_by_tag_name("td");
		for c in col:
			arr[i].append(c.text);
		i+=1;
	browser.quit();
	arr = [r for r in arr if r!=[]]
	print(arr);
	for r in arr:
		if gettimeleft_cc(r[2]) <=86400 or printall:
			posttozulip_cc(r);
			print(r);
while 1:
	try:
		csacademy();
		codeforces();
		codechef();
		sleep(5*60);
	except Exception:
		print('EROR!');
		sleep(10*60);
