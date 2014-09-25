#!/usr/bin/env python
'''
Resize histograms for 8TeV datacards 
Author: T.M.Perry
'''
import ROOT
from ROOT import TH1F,TFile,gROOT
import sys

#inFilename = raw_input ('Name of File to be Renamed (no .root):\n')
#nBinsStr = raw_input ('Number of bins: \n')
#nBins = int(nBinsStr)

inFilenames =  [
                'Renamed4F_'+sys.argv[1],
                'Renamed4F_'+sys.argv[2],
                'Renamed4F_'+sys.argv[3],
               ]
for inFilename in inFilenames:
 inFile = TFile(inFilename+'.root')
 
 outFile=gROOT.FindObject('Data_'+inFilename+'.root')
 if outFile : outFile.Close()
 outFile = TFile('Data_'+inFilename+'.root','RECREATE','xaxis as bin number')
 
 data_obs_INFILE = inFile.Get("data_obs")
 data_obs_INFILE.SetName("data_obs_INFLIE")
 nBins = data_obs_INFILE.GetNbinsX()
 data_obs = TH1F('data_obs','data_obs',nBins,0,nBins)
 for i in xrange(1,nBins+1):
  data_obs.SetBinContent(i,data_obs_INFILE.GetBinContent(i))
 
 outFile.Write()
