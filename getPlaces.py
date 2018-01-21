import pandas as pd
from ast import literal_eval
import pickle
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

dfArt=pd.DataFrame()


def eval(x):
	x[0]=literal_eval(x[0])	
	return x	

def readDf():
	dfA=pd.read_csv("dfArticlesCover.csv")
	dfT=pd.read_csv("dfTweetsCover.csv")
	return dfA, dfT
	
def lowering(x):
	x[0]=[w.lower() for w in x[0]]
	x[0]=[w.replace("\n","") for w in x[0]]
	x[0]=[w.replace(" ","") for w in x[0]]
	return x
	
def relevanceArt(x, token, plcL):
	##relScore=tweetstext with articles text ...................................................relevance function to be coded
	tweetsToken=token;tfidf=x["artToken"]
	relScore= len( list( set( set(tweetsToken) & set(tfidf) ) ) )*100.0/len(list(set(tweetsToken)))
	if relScore>=30.0:
		plcL.extend(x["artPlaces"])
	return x
	
def relArt(token):
	global dfArt
	plcL=[]
	dfArt.apply(relevanceArt, args=(token, plcL,), axis=1)
	return plcL	

def setPlaces(x,resD,plcCol,noCol):
	plcL=x[plcCol]
	#if noCol=="twNo" and not plcL:
		#print (x[noCol],x["twPlaces"])
	#	plcL=relArt(x["twToken"]) ##noCol twNo or artNo
	for p in plcL:
		if x[noCol] not in resD[p][noCol]:
			resD[p][noCol].append(x[noCol])
	return x
		
def getPlaces(dfA, dfT):
	global dfArt
	dfA["artPlaces"]=dfA[["artPlaces"]].apply(eval, axis=1, reduce=False)
	dfA["artPlaces"]=dfA[["artPlaces"]].apply(lowering, axis=1, reduce=False)
	dfArt=dfA
	#dfT=dfT[:100]
	dfT["twPlaces"]=dfT[["twPlaces"]].apply(eval, axis=1, reduce=False)
	dfT["twPlaces"]=dfT[["twPlaces"]].apply(lowering, axis=1, reduce=False)
	places=[]
	places=list(dfA["artPlaces"])+list(dfT["twPlaces"])
	places=[x for lis in places for x in lis]
	places=sorted( list( set( places) ) )
	print (places, len(places))
	resD={}
	for p in places:
		resD[p]={}
		resD[p]["artNo"]=[]
		resD[p]["twNo"]=[]
	print ("setting places")
	dfA.apply(setPlaces, args=(resD, "artPlaces", "artNo",), axis=1)
	dfT.apply(setPlaces, args=(resD, "twPlaces", "twNo"), axis=1)
	print ("storing")
	dff=pd.DataFrame()
	dff["places"]=[p for p in sorted(resD)]
	dff["artNo"]=[resD[p]["artNo"] for p in sorted(resD)]
	dff["twNo"]=[resD[p]["twNo"] for p in sorted(resD)]
	dff["artCount"]=[len(resD[p]["artNo"]) for p in sorted(resD)]
	dff["twCount"]=[len(resD[p]["twNo"]) for p in sorted(resD)]
	dff.to_csv("dfArtTweetsPlacesUQ.csv", index=False)
	f=open("placeDUQ.txt", "w")
	pickle.dump(resD, f)
	f.close()
	return resD, dff
	
dfA, dfT=readDf()
resD, dff=getPlaces(dfA, dfT)
print ("done")

	
	
	
