#!/usr/bin/env python
'''
Resize histograms for 8TeV datacards 
Author: T.M.Perry
'''
import ROOT
from ROOT import TH1F,TFile,gROOT
import sys

inFilenames =  [
                'Renamed4F_'+sys.argv[1],
                'Renamed4F_'+sys.argv[2],
                'Renamed4F_'+sys.argv[3],
               ]
for inFilename in inFilenames:
 inFile = TFile(inFilename+'.root')
 
 outFile=gROOT.FindObject('ReRanged_'+inFilename+'.root')
 if outFile : outFile.Close()
 outFile = TFile('ReRanged_'+inFilename+'.root','RECREATE','xaxis as bin number')
  
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
  
