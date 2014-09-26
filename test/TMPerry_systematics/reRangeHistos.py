#!/usr/bin/env python
'''
Resize histograms for 8TeV datacards 
Author: T.M.Perry
'''
import ROOT
from ROOT import TH1F,TFile,gROOT
import sys

inFilenames=[
sys.argv[1],sys.argv[2],sys.argv[3]
]

for inFilename in inFilenames:
 inFile = TFile(inFilename+'.root')

 outFile=gROOT.FindObject('Rescaled_'+inFilename+'.root')
 if outFile : outFile.Close()
 outFile = TFile('Rescaled_'+inFilename+'.root','RECREATE','rescaled histograms')
 log = open('Rescaled_'+inFilename+'.log','a')

 for key in inFile.GetListOfKeys():
  obj = key.ReadObj()
  if(obj.IsA().InheritsFrom("TH1")):
   h_name = obj.GetName()
   nBins = obj.GetNbinsX()
   h_new = TH1F(h_name,h_name,nBins+1,0,nBins+1)
   for i in xrange(1,nBins+2):
    h_new.SetBinContent(i,obj.GetBinContent(i))
   #print h_new.GetName()
   #print h_new.Integral()
   outFile.cd()
   outFile.Write()

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

