#!/usr/bin/env python
'''
makes plot of r with systematics removed
'''
import ROOT
from ROOT import TH1F,TFile
from ROOT import TCanvas,TLine,TLatex
from ROOT import gStyle
import sys

wbbs=["Wbb","W4F"]
ttsamples=["3j","1m1e"]
ignos=["full","beff","beffC","beffL","bgT","bgTOP","bgTbar","bgVV","bgWcc","bgZjet","bgtW","effT","lumi","muonE","qcd","wlight","jet","UCE","muon"]

labels=["Full","bTag Eff B","bTag Eff C","bTag Eff L","Top","TTbar","TBar" ,"VV","W+cc","Drell Yan","T/Tbar tW","Eff T","Luminosity","Muon","QCD","W+light","Jet(s)","UCE(s)","Muon(s)"]

l = len(ignos)
low = 1
hi = 2

#for i,j in zip(igno,labels): print("%s %s"%(i,j))
canx = 1200
cany = 800
c = TCanvas('c','Canvas Named c',canx,cany)
c.Size(canx,cany)

tex = ROOT.TLatex()
tex.SetTextAlign(13)
tex.SetNDC(True)

gStyle.SetOptStat('')

for wbb in wbbs:
 if wbb == "Wbb": wb = "5Flavor"
 if wbb == "W4F": wb = "4Flavor"
 print(wbb)
 for ttsample in ttsamples:
  print(" "+ttsample)
  c.cd()
  i = 1
  theHist = TH1F("theHist","theHist",l,1,l)
  for igno,label in zip(ignos,labels):
   theFile = TFile("./roots/mlfit_%s_%s_%s.root"%(igno,wbb,ttsample))
   fit_s = theFile.Get("fit_s")
   if fit_s == None: continue
   fpf_s = fit_s.floatParsFinal()
   nuis_s = fpf_s.find('r')
   r = nuis_s.getVal()
   r_error = nuis_s.getError()
   theHist.SetBinContent(i,r)
   theHist.SetBinError(i,r_error)
   theHist.GetXaxis().SetBinLabel(i,label)
   theFile.Close()
   if igno == "full":
    y = r
    y_error = r_error
   i+=1

  theLine = TLine(1,y,l,y)
  theLine.SetLineStyle(2)
  theLine.SetLineWidth(2)
  theLine.SetLineColor(2)
  theHist.GetXaxis().SetTickLength(0)
  theHist.SetTitle("")
  theHist.GetYaxis().SetRangeUser(low,hi)
  theHist.Draw()
  theLine.Draw()
  tex.SetTextAlign(11)
  tex.SetTextSize(0.06)
  tex.DrawLatex(0.1,0.9,"Stability of Fits (Wbb: %s, TTbar: %s)"%(wb,ttsample))
  tex.SetTextAlign(13)
  tex.SetTextSize(0.04)
  tex.DrawLatex(0.15,0.89,"Full Fit: r = %0.3f #pm %0.3f"%(y,y_error))
  theHist.Draw("same")
  c.Print("./plots/%s_%s_FitStability.png"%(wbb,ttsample))
  theHist.Delete()
  c.Clear()

