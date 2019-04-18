from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import re
import datetime
import traceback
import zulip
#from flask import Flask
printall=1;
printall2=0;
contest_data =[]
#os.system("cp geckodriver /app/.heroku/python/bin");
#os.system("echo $PATH");
def appendcontest(s,t):
	if(t>60*43.5):
		temp=[]
		x =datetime.datetime.utcnow()+datetime.timedelta(seconds=t-60*60); 
		temp.append(x);
		sm=" 45 minutes Left!**\n@**stream**";
		temp.append(s+sm);
		contest_data.append(temp);
	'''
	if(t>60*60*24-1.5*60):
		temp=[]
		x =datetime.datetime.utcnow()+datetime.timedelta(seconds=t-60*60*24); 
		temp.append(x);
		sm=" One Day Left!***";
		temp.append(s+sm);
		contest_data.append(temp);
	if(t>60*28.5):
		temp=[]
		x =datetime.datetime.utcnow()+datetime.timedelta(seconds=t-60*30); 
		temp.append(x);
		sm=" 30 Minutes Left!*** @**stream**";
		temp.append(s+sm);
		contest_data.append(temp);
	'''
def gettimeleft_cs(time):
	data = re.findall("\d+",time);
	data = list(map(int,data));
	time_left=(datetime.datetime(data[2],data[1],data[0],data[5],data[6])-datetime.datetime.utcnow()).total_seconds()
	return int(time_left);
def printtime_cs(t):
	s=""
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
	return s;

def posttozulip_cs(data,t):
	s ="***Contest Update***\nCS Academy: "+data[0]+"\nDuration: "+data[2]+"\n**Start Time: "+gettime_cf(t).strftime("%d %b %Y, %H:%M %Z")+"**\n";
	link = re.findall("\d+",data[0]);
	link = list(map(int,link));
	link = "Link: https://csacademy.com/contest/round-"+str(link[0])+"/\n";
	s+=link;
	s+="**Time Remaining: ";
	appendcontest(s,t);

def csacademy():
	'''
	options= Options();
	#options.add_argument('-headless');

	binary = FirefoxBinary('/app/firefox/firefox');
	binary.add_command_line_options('-headless');
	binary.add_command_line_options('--disable-gpu');
	binary.add_command_line_options('--no-sandbox');
	#browser = webdriver.Firefox(firefox_binary=binary,firefox_options=options,executable_path=r'/app/geckodriver')
	browser = webdriver.Firefox(firefox_binary=binary)
	'''
	options = Options();
	options.binary_location = '/app/.apt/usr/bin/google-chrome';
	browser=webdriver.Chrome(executable_path='/app/.chromedriver/bin/chromedriver',chrome_options=options)
	browser.get("https://csacademy.com/contests/");
	sleep(4);
	waste = browser.find_element_by_tag_name("body");
	sleep(4);
	waste = browser.find_element_by_tag_name("body");
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
	#print(arr);
	for r in arr:
		if gettimeleft_cs(r[1])<=86400 or printall:
			#print('ONE DAY LEFT!');
			posttozulip_cs(r,gettimeleft_cs(r[1]));


def gettimeleft_cf(time):
	data = re.findall("\d+",time);
	data = list(map(int,data));
	time_left = ((((data[0]*24)+data[1])*60)+data[2])*60+data[3];
	return time_left;
def gettime_cf(t):
	now = datetime.datetime.now()
	now_plus_t = now+datetime.timedelta(seconds=t)+datetime.timedelta(minutes=330);
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
	if(data[0].find("(Div. 1)")==-1):
		s = "***Contest Update***\nContest: "+data[0]+"\nDuration: "+printtime_cf(gettimeleft_cf(data[1]));
		s+="\n**Start Time: "+gettime_cf(gettimeleft_cf(data[2])).strftime("%d %b %Y, %H:%M %Z")+"IST **\n";
		s+="Link: "+"https://codeforces.com/contests/"+data[3]+"\n";
		s+="**Time Remaining: ";
		t = gettimeleft_cf(data[2]);
		#print(s);
		appendcontest(s,t);
	
def codeforces():
	options = Options();
	options.binary_location = '/app/.apt/usr/bin/google-chrome';
	browser=webdriver.Chrome(executable_path='/app/.chromedriver/bin/chromedriver',chrome_options=options)
	browser.get("https://students.iitmandi.ac.in/~b17041/contest.html");
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
	#print(arr);
	for r in arr:
		if gettimeleft_cf(r[2]) <= 86400 or printall:
			posttozulip_cf(r);
			#	print(r); 

def gettimeleft_cc(time):
	data = re.findall("\d+",time);
	data = list(map(int,data));
	timeleft=(datetime.datetime.strptime(time,"%d %b %Y\n%H:%M:%S")-datetime.datetime.utcnow()).total_seconds();
	return timeleft-330*60;

def posttozulip_cc(data):
	s = "***Contest Update***\nCodechef "+data[1]+" of Duration "+printtime_cf((gettimeleft_cc(data[3])-gettimeleft_cc(data[2])));
	s+=" ***to start at "+gettime_cf(gettimeleft_cc(data[2])).strftime("%d %b %Y, %H:%M %Z")+"IST ***\n";
	s+="**Time Remaining: ";
	#	s+=printtime_cf(gettimeleft_cc(data[2]))
	#	s+="***\n";
	t = gettimeleft_cc(data[2]);
	appendcontest(s,t);
	
def codechef():
	options = Options();
	options.binary_location = '/app/.apt/usr/bin/google-chrome';
	browser=webdriver.Chrome(executable_path='/app/.chromedriver/bin/chromedriver',chrome_options=options)
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
	#print(arr);
	for r in arr:
		if gettimeleft_cc(r[2]) <=86400 or printall:
			posttozulip_cc(r);
			print(r);

def post(s):
	client = zulip.Client(config_file="zuliprc");
	request ={
		"type" : "stream",
		"to":	"competitive",
		"subject": "Contest Reminders",
		"content": s
	}
	result = client.send_message(request);
	print(result);

def getdata():
	csacademy();
	#	post("Testing for CS!");
	codeforces();
	#	post("Testing for CF!");
	codechef();
	#	post("Scrapped data from CS,CF and CC!\n"); s
def test(s):
	client = zulip.Client(config_file="zuliprc");
	request ={
		"type" : "stream",
		"to":	"test here",
		"subject": "Script Testing",
		"content": s
	}
	result = client.send_message(request);
	print(result);


def process():
	i =0;
	print("Processing Contests!");
	while(i<len(contest_data)):
		print(contest_data[i][1]);
		if(contest_data[i][0]<datetime.datetime.utcnow() or printall2):
			print(contest_data[i][0].strftime("%H:%M:%S %d-%b-%Y")+contest_data[i][1]);
			post(contest_data[i][1]);
			del contest_data[i];
			i=-1;
		i+=1;

with open("logs.txt","a") as f:
			f.write("Welcome My Nigga!\n");
print(datetime.datetime.utcnow())
while 1:
	try:
		contest_data=[];
		getdata();
		#	test("Hello");
		i=0;
		while i<75:
			process();
			sleep(5*60);
			i+=1;
	except Exception as e:
		#	post("Unable to find geckodriver!");
		#	test("Another Exception!");
		#	print(traceback.format_exec());
		print("Exception!!!");
		print(e)
		sleep(2*60);
