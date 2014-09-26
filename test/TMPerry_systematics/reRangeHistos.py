## TO DO: merge Wc and Wcc

#!/usr/bin/env python
'''
Resize histograms for 8TeV datacards 
Author: T.M.Perry
'''
import ROOT
from ROOT import TH1F,TFile,gROOT
import sys

def rename(name,old,new):
 if(name==old):
  return new
 else:
  return name

def mergeHistos(histos,outname):
 h = histos[0].Clone()
 h.SetName(outname)
 histos.pop(0)
 for histo in histos:
  h.Add(histo)
 return h

inFilenames=[
sys.argv[1],sys.argv[2],sys.argv[3]
]
Wbb4Fnames=[
sys.argv[4],sys.argv[5],sys.argv[6]
]

for inFilename,Wbb4Fname in zip(inFilenames,Wbb4Fnames):
 inFile = TFile(inFilename+'.root')
 w4fFile = TFile(Wbb4Fname+'.root')

 outFile=gROOT.FindObject('Renamed4F_'+inFilename+'.root')
 if outFile : outFile.Close()
 outFile = TFile('Renamed4F_'+inFilename+'.root','RECREATE','renamed histograms')
 log = open('Renamed4F_'+inFilename+'.log','a')

 #Wcc_infile = inFile.Get('Wcc')
 #Wc_infile = inFile.Get('Wc')
 #Wcc = mergeHistos([Wcc_infile,Wc_infile],'Wcc')
 #Wcc_infile.Delete()
 #Wc_infile.Delete()
 #Wcc_infile.SetName('Wcc_infile')

 for key in inFile.GetListOfKeys():
  obj = key.ReadObj()
  if obj.GetName=='Wc' : continue
  if obj.GetName=='Wcc' : continue
  if(obj.IsA().InheritsFrom("TH1")):
   h_name = obj.GetName()
   h_name = rename(h_name,"Wbb","Wbb5F")
   nBins = obj.GetNbinsX()
   h_new = TH1F(h_name,h_name,nBins+1,0,nBins+1)
   for i in xrange(1,nBins+2):
    h_new.SetBinContent(i,obj.GetBinContent(i))
   #print h_new.GetName()
   #print h_new.Integral()
   outFile.cd()
   outFile.Write()

