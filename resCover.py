import pandas as pd
import numpy as np
from ast import literal_eval
import pickle
import json

#placeList=['achham', 'afganistan', 'america', 'arghakhanchi', 'assam', 'australia', 'baglung', 'baitadi', 'bajhang', 'bajura', 'baltimore', 'bangladesh', 'banke', 'bara', 'bardiya', 'bengal', 'bhaktapur', 'bhojpur', 'bihar', 'china', 'chitwan', 'dadeldhura', 'dailekh', 'darchula', 'dhading', 'dhankuta', 'dhanusa', 'dolakha', 'dolpa', 'doti', 'gorka', 'gorkha', 'gorkhas', 'gujrat', 'gulmi', 'himachalpradesh', 'humla', 'ilam', 'india', 'israel', 'jajarkot', 'jhapa', 'jumla', 'kailali', 'kalikot', 'kanchanpur', 'kapilvast', 'karanchi', 'kaski', 'kathmand', 'kavrepalanchok', 'khotang', 'lalitpur', 'lamjung', 'mahottari', 'makwanpur', 'manang', 'morang', 'mug', 'mustangdang', 'myagdi', 'myanmar', 'nawalparasi', 'nepal', 'nepalee', 'nepali', 'nepals', 'nuwakot', 'okhaldhunga', 'pakistan', 'palpa', 'panchthar', 'parbat', 'parsa', 'patna', 'punjab', 'pyuthan', 'ramechhap', 'rasuwa', 'rautahat', 'rolpa', 'rukumsalyan', 'rupandehi', 'samastipur', 'sankhuwasabha', 'saptari', 'sarlahi', 'sindhuli', 'sindhupalchok', 'siraha', 'solukhumb', 'sunsari', 'surkhet', 'syangja', 'tanahun', 'taplejung', 'terhathum', 'tibet', 'udayapur', 'up', 'us', 'usa', 'uttarakhand', 'uttarpradesh']


placeList=['achham', 'america', 'arghakhanchi', 'assam', 'australia', 'baglung', 'baitadi', 'bajhang', 'bajura', 'baltimore', 'bangladesh', 'banke', 'bara', 'bardiya', 'bengal', 'bhaktapur', 'bhojpur', 'bihar', 'china', 'chitwan', 'dadeldhura', 'dailekh', 'darchula', 'dhading', 'dhankuta', 'dhanusa', 'dolakha', 'dolpa', 'doti', 'gorka', 'gorkha', 'gorkhas', 'gujrat', 'gulmi', 'himachalpradesh', 'humla', 'ilam', 'india', 'israel', 'jajarkot', 'jhapa', 'jumla', 'kailali', 'kalikot', 'kanchanpur', 'kapilvast', 'karanchi', 'kaski', 'kathmand', 'kavrepalanchok', 'khotang', 'lalitpur', 'lamjung', 'mahottari', 'makwanpur', 'manang', 'morang', 'mug', 'mustangdang', 'myagdi', 'myanmar', 'nawalparasi', 'nepal', 'nepalee', 'nepali', 'nepals', 'nuwakot', 'okhaldhunga', 'pakistan', 'palpa', 'panchthar', 'parbat', 'parsa', 'patna', 'punjab', 'pyuthan', 'ramechhap', 'rasuwa', 'rautahat', 'rolpa', 'rukumsalyan', 'rupandehi', 'samastipur', 'sankhuwasabha', 'saptari', 'sarlahi', 'sindhuli', 'sindhupalchok', 'siraha', 'solukhumb', 'sunsari', 'surkhet', 'syangja', 'tanahun', 'taplejung', 'terhathum', 'tibet', 'udayapur', 'up', 'us', 'usa', 'uttarakhand', 'uttarpradesh', 'papua', 'guinea', 'delhi', 'gorkha', 'pakistan', 'bengal',  'uk', 'mount', 'siliguri', 'bhaktapur', 'gujarat', 'kutch', 'patna', 'japan', 'assam', 'mumbai', 'nicobar', 'andaman', 'guwahati',  'pokhara', 'island', 'port', 'haiti', 'khudi', 'los', 'angeles', 'blair', 'valley', 'south', 'kashmir', 'srinagar', 'kodari', 'kokopo', 'kolkata', 'jhapa',  'bhutan', 'hawaii', 'yemen', 'hyderabad',  'sikkim', 'lamjung', 'usa',  'bangladesh', 'london', 'mexico', 'canada', 'lucknow', 'rasuwa', 'kerala', 'australia', 'noida', 'lalitpur']

sortedTimeList=['42504', '42508', '42512', '42516', '42520', '42524', '42604', '42608', '42612', '42616', '42620', '42624', '42704', '42708', '42712', '42716', '42720', '42724', '42804', '42808', '42812', '42816', '42820', '42824', '42904', '42908', '42912', '42916', '42920', '42924', '43004', '43008', '43012', '43016', '43020', '43024', '50104', '50108', '50112', '50116', '50120', '50124', '50204', '50208', '50212', '50216', '50220', '50224', '50304', '50308', '50312', '50316', '50320', '50324', '50404', '50408', '50412', '50416', '50420', '50424', '50504', '50508', '50512', '50516', '50520', '50524', '50604', '50608', '50612', '50616', '50620', '50624', '50704', '50708', '50712', '50716', '50720', '50724', '50804', '50808', '50812', '50816', '50820', '50824', '50904', '50908', '50912', '50916', '50920', '50924', '51004', '51008', '51012', '51016', '51020', '51024']

reqPlaceList=[ 'assam', 'australia', 'baltimore', 'bangladesh', 'banke', 'bengal', 'bhaktapur', 'bihar', 'china', 'dadeldhura', 'dailekh', 'darchula', 'dhading', 'dhankuta', 'dhanusa', 'dolakha', 'dolpa', 'gorka', 'gorkha', 'gujrat', 'india', 'israel', 'kathmandu', 'khotang', 'lalitpur', 'myanmar', 'nawalparasi', 'nepal', 'nuwakot', 'pakistan', 'patna', 'rasuwa',  'samastipur', 'saptari', 'sindhuli', 'sindhupalchok', 'tibet', 'udayapur',  'usa']

dfArt=pd.DataFrame()

placeD={} ##{place1 : { artNo : [] , timeSlot1 :{ twNo:[], negSentiFreq:0.0, negSenti:0.0, infDmg:0.0, imgDmgNt:0.0 }, timeSlot2 :{..} ....}, place2....      }

def eval(x):	
	x[0]=literal_eval(x[0])
	return x

def lowering(x):
	x[0]=[w.lower() for w in x[0]]
	return x
	
def buildPDA(x, placeD):
	pLis=x["artPlaces"]
	if pLis:
		for p in pLis:
			if p not in placeD:
				placeD[p]={}
				placeD[p]["artNo"]=[]
			placeD[p]["artNo"].append(x["artNo"])
	return x

def processArt(artFile, placeD):
	global dfArt
	dfArt=pd.read_csv(artFile)
	dfArt["artPlaces"]=dfArt[["artPlaces"]].apply(eval, axis=1, reduce=False)
	dfArt["artPlaces"]=dfArt[["artPlaces"]].apply(lowering, axis=1, reduce=False)
	dfArt["artToken"]=dfArt[["artToken"]].apply(eval, axis=1, reduce=False)
	dfArt["artToken"]=dfArt[["artToken"]].apply(lowering, axis=1, reduce=False)
	dfArt.apply(buildPDA, args=(placeD,), axis=1, reduce=False)
	return
	
def setPlace(x, plc, token):
	if x["artPlaces"]:
		lis=list( set(x["artToken"]) & set(token) )
		if lis:
			if len(lis)*100.0/len(token) >=30:
				plc.appned([w for w in x["artPlaces"]])
	return x
	
def getArtPlaces(token):
	global dfArt
	plc=[]
	dfArt.apply(setPlace, args=(plc,token,), axis=1, reduce=False)
	plc=list(set(plc))
	return plc
	
def buildPDT(x, placeD, timeSlot):
	#print (x["twPlaces"], type(x["twPlaces"]))
	pLis=x["twPlaces"]
	#print (pLis)
	#if len(pLis)==0:
		#print ("here")
		#pLis=getArtPlaces(x["twToken"])
		#print (x["twNo"],pLis)
	#xx=input("enter a number")
	if pLis:
		for p in pLis:
			if p not in placeD:
				placeD[p]={}
				placeD[p]["artNo"]=[]
			if timeSlot not in placeD[p]:
					placeD[p][timeSlot]={}
					placeD[p][timeSlot]["twNo"]=[]
					placeD[p][timeSlot]["negSenti"]=0.0
					placeD[p][timeSlot]["negSentiFreq"]=0.0
					placeD[p][timeSlot]["infDmg"]=0.0
					placeD[p][timeSlot]["imgDmgNt"]=0.0
					placeD[p][timeSlot]["infDmgFreq"]=0.0
			placeD[p][timeSlot]["twNo"].append(x["twNo"])
			if x["twNeg"] > x["twPos"]:
				placeD[p][timeSlot]["negSentiFreq"]+=1
			placeD[p][timeSlot]["negSenti"]+=x["twNeg"]
			placeD[p][timeSlot]["infDmg"]+=x["twInfDmg"]
			placeD[p][timeSlot]["imgDmgNt"]+=x["twDmgNt"]
			if x["twLevel"]!=0:
				placeD[p][timeSlot]["infDmgFreq"]+=1
	return x			
	
def tmTwIter(x, dfT, placeD):
	timeSlot=str( x["m"]*10000+x["d"]*100+x["H"] )
	dTemp=dfT[ dfT["twNo"].isin(x["twNo"]) ]
	dTemp.apply(buildPDT, args=(placeD, timeSlot,), axis=1, reduce=False)
	return x	
	
def processTweetStreams(twFile, tmTweets):
	dfT=pd.read_csv(twFile)
	#dfT=dfT[:1000]
	dfT["twPlaces"]=dfT[["twPlaces"]].apply(eval, axis=1, reduce=False)
	dfT["twPlaces"]=dfT[["twPlaces"]].apply(lowering, axis=1, reduce=False)
	dfTm=pd.read_csv(tmTweets)
	dfTm["twNo"]=dfTm[["twNo"]].apply(eval, axis=1, reduce=False)
	dfTm.apply(tmTwIter, args=(dfT, placeD,), axis=1, reduce=False)
	del dfT, dfTm
	return 

placeList=[w.lower() for w in placeList]
placeList=sorted(list(set(placeList)))
#print ("placeList lowered",placeList)	
processArt("dfArticlesCover.csv", placeD)
print ("articles processed", len(sorted(placeD)))
processTweetStreams("dfTweetsCover.csv", "dfTimeTweets.csv")
print ("tweets processed",len(sorted(placeD)))
f=open("placeDUQ.txt", "w")
pickle.dump(placeD, f)
f.close()
print ("place details")
#cols=["places", "twNo", "negTwNo", "negSenti", "resNegSenti", "infDmg"]
features=["twNo", "negSentiFreq", "negSenti", "resNegSenti", "infDmg", "imgDmgNt", "infDmgFreq"]
dfRes=pd.DataFrame()
dfRes["timeSlot"]=sortedTimeList
for p in sorted(reqPlaceList):
	if p not in placeD:
		continue
	#print p, [t for t in placeD[p]]
	for c in features:
		#print c
		cL=[]
		for t in sortedTimeList:
			#print t
			if t not in placeD[p]:
				#print "no",t,c
				cL.append(0)
			else:
				#print "yes",t,c, placeD[p][t], placeD[p][t][c], type(placeD[p][t][c]),len(placeD[p][t][c]),c=="twNo"
				if c=="twNo":
					cL.append(len(placeD[p][t][c]))
				elif c=="resNegSenti":
					cL.append( ( placeD[p][t]["negSentiFreq"]*1.0/len(placeD[p][t]["twNo"]) )*placeD[p][t]["negSenti"] )
				else:
					cL.append(placeD[p][t][c])
		#print cL
		#for i in range(1, len(cL)):
		#	cL[i]=cL[i]+cL[i-1]
		dfRes[c+"_"+p]=cL	
dfRes.to_csv("ftSlotsAll.csv", index=False)
print ("done")
	
	
	
	
