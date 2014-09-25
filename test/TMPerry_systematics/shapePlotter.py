#!/usr/bin/env python
'''
Makes nice plots with ratio from histograms made using makeHistos.py
Author: T.M.Perry UW
'''
import ROOT
from ROOT import THStack,TH1F,TFile
from ROOT import TLegend,TCanvas,TPad,TLatex,TLine
from ROOT import gROOT,gStyle
import sys
#import histoRange as hr
#import cmsPrelim as cpr
#import TheParameters as p

wflav = sys.argv[1]
ttsample = sys.argv[2]
where = './plots'

dataFile_wbb = TFile("./roots/Data_Renamed4F_%s.root"%(sys.argv[3]))
dataFile_tt  = TFile("./roots/Data_Renamed4F_%s.root"%(sys.argv[4]))
theFile  = TFile("./roots/mlfit_full_%s_%s.root"%(wflav,ttsample))
biasFile = TFile("./roots/mlfit_full_%s_%s_fitbias.root"%(wflav,ttsample))

#if ttsample == '1m1e':
# dataFile_tt = TFile("./roots/Data_Renamed4F_PS6c_05sptr_Datacard_2j2525_2bt_1m1e_mt.root")
# if wflav == 'Wbb':
#  theFile  = TFile("./roots/mlfit_full_Wbb_1m1e.root")
#  biasFile = TFile("./roots/mlfit_full_Wbb_1m1e_fitbias.root")
# if wflav == 'W4F':
#  theFile  = TFile("./roots/mlfit_full_W4F_1m1e.root")
#  biasFile = TFile("./roots/mlfit_full_W4F_1m1e_fitbias.root")
#if ttsample == '3j':
# dataFile_tt = TFile("./roots/Data_Renamed4F_PS6c_08sptr_Datacard_3j2525_2bt_mt.root")
# if wflav == 'Wbb':
#  theFile  = TFile("./roots/mlfit_full_Wbb_3j.root")
#  biasFile = TFile("./roots/mlfit_full_Wbb_3j_fitbias.root")
# if wflav == 'W4F':
#  theFile  = TFile("./roots/mlfit_full_W4F_3j.root")
#  biasFile = TFile("./roots/mlfit_full_W4F_3j_fitbias.root")

ratioRange = 0.3
rebin = 1
errorBand = True
if wflav == 'W4F': fourF = True
if wflav == 'Wbb': fourF = False
#canvas attributes
#canx = 800 # for one plot on page
#canx = 550 # for two plots on page with text
canx = 1200 # for two plots on page just title
#canx = 500 # for three plots on page with text
#canx = 400 # for three plots on page with just title

cany = 900

#color scheme
d = 1

q =   ROOT.EColor.kRed+1
z =   ROOT.EColor.kOrange-3
vv =   ROOT.EColor.kYellow-3
tt =  ROOT.EColor.kGreen+1
ts =  ROOT.EColor.kGreen-5
ttw = ROOT.EColor.kGreen+3 
ttb = ROOT.EColor.kGreen-9
wl =  ROOT.EColor.kAzure+10
wc =  ROOT.EColor.kBlue+1
wcc = ROOT.EColor.kAzure+2
wbb = 51#ROOT.EColor.kCyan

tex = ROOT.TLatex()
tex.SetTextSize(0.07)
tex.SetTextAlign(13)
tex.SetNDC(True)
gStyle.SetOptStat('')

##  TTBar 
##
##########

c = TCanvas('c','Canvas Named c',canx,cany)
c.Size(canx,cany)
#p1 = TPad('p1','p1',0,0.3,1,1)
#p1.SetBottomMargin(0.08)
#p1.Draw()
#p1.cd()

samples_ttbar = [
                 "W+bb",
                 "TTbar",
                 "Top",
                 "Tbar",
                 "T tW",
                 "QCD",
                 "Total MC",
]

samples_wbb = [
               "W+bb",
               "W+cc",
               "W+udscg",
               "TTbar",
               "Top",
               "Tbar",
               "T tW",
               "Drell-Yan",
               "Diboson",
               "QCD",
               "Total MC"
]

sizes_ttbar_prefit = []
sizes_ttbar_postfit = []
sizes_ttbar_part_prefit = []
sizes_ttbar_part_postfit = []
sizes_wbb_prefit = []
sizes_wbb_postfit = []
sizes_wbb_part_prefit = []
sizes_wbb_part_postfit = []

#shapes = ["shapes_fit_s","shapes_prefit"]
#samples = ["Wbb"]
#samples = ["TTbar"]
shapes = ["shapes_prefit","shapes_fit_s"]
samples = ["TTbr","UUbb"]
I = 4
F = 20

fit_s = theFile.Get("fit_s")
fpf_s = fit_s.floatParsFinal()
nuis_s = fpf_s.find('r')
r = nuis_s.getVal()
r_error = nuis_s.getError()

bias_s = biasFile.Get("fit_s")
bpf_s = bias_s.floatParsFinal()
b_bias_s = bpf_s.find('r')
bias = b_bias_s.getVal()
bias_error = b_bias_s.getError()

for shape in shapes:
 for sample in samples:
  c.Clear()
  c.cd()
  if shape=="shapes_fit_s": shp = "Fitted"
  if shape=="shapes_prefit": shp = "PreFit"
  if sample=="TTbar" or sample=="TTbr":
   smp="TTbar"
   
   if not fourF: tt_wbbh = theFile.Get("%s/%s/Wbb"%(shape,sample))
   if fourF: tt_wbbh = theFile.Get("%s/%s/W4F"%(shape,sample))
   tt_wbbh.SetName('tt_wbbh')
   tt_wbbh.SetFillColor(wbb)
   tt_wbbh.Draw('hist')
   tt_wbbh_size = tt_wbbh.Integral()
   tt_wbbh_size_part = tt_wbbh.Integral(I,F)
   if shp=="PreFit":
    sizes_ttbar_prefit.append(tt_wbbh_size)
    sizes_ttbar_part_prefit.append(tt_wbbh_size_part)
   else: 
    sizes_ttbar_postfit.append(tt_wbbh_size)
    sizes_ttbar_part_postfit.append(tt_wbbh_size_part)
   
   tt_tth = theFile.Get("%s/%s/TTbar"%(shape,sample))
   tt_tth.SetName('tt_tth')
   tt_tth.SetFillColor(ttb)
   tt_tth.Draw('hist')
   tt_tth_size = tt_tth.Integral()
   tt_tth_size_part = tt_tth.Integral(I,F)
   if shp=="PreFit": 
    sizes_ttbar_prefit.append(tt_tth_size)
    sizes_ttbar_part_prefit.append(tt_tth_size_part)
   else:
    sizes_ttbar_postfit.append(tt_tth_size)
    sizes_ttbar_part_postfit.append(tt_tth_size_part)
   
   tt_th = theFile.Get("%s/%s/T"%(shape,sample))
   tt_th.SetName('tt_th')
   tt_th.SetFillColor(tt)
   tt_th.Draw('hist')
   tt_th_size = tt_th.Integral()
   tt_th_size_part = tt_th.Integral(I,F)
   if shp=="PreFit":
    sizes_ttbar_prefit.append(tt_th_size)
    sizes_ttbar_part_prefit.append(tt_th_size_part)
   else:
    sizes_ttbar_postfit.append(tt_th_size)
    sizes_ttbar_part_postfit.append(tt_th_size_part)

   tt_tbh = theFile.Get("%s/%s/Tbar"%(shape,sample))
   tt_tbh.SetName('tt_tbh')
   tt_tbh.SetFillColor(ts)
   tt_tbh.Draw('hist')
   tt_tbh_size = tt_tbh.Integral()
   tt_tbh_size_part = tt_tbh.Integral(I,F)
   if shp=="PreFit":
    sizes_ttbar_prefit.append(tt_tbh_size)
    sizes_ttbar_part_prefit.append(tt_tbh_size_part)
   else:
    sizes_ttbar_postfit.append(tt_tbh_size)
    sizes_ttbar_part_postfit.append(tt_tbh_size_part)
   
   tt_twh = theFile.Get("%s/%s/tW"%(shape,sample))
   tt_twh.SetName('tt_twh')
   tt_twh.SetFillColor(ttw)
   tt_twh.Draw('hist')
   tt_twh_size = tt_twh.Integral()
   tt_twh_size_part = tt_twh.Integral(I,F)
   if shp=="PreFit": 
    sizes_ttbar_prefit.append(tt_twh_size)
    sizes_ttbar_part_prefit.append(tt_twh_size_part)
   else:
    sizes_ttbar_postfit.append(tt_twh_size)
    sizes_ttbar_part_postfit.append(tt_twh_size_part)
   
   tt_qh = theFile.Get("%s/%s/QCD"%(shape,sample))
   tt_qh.SetName('tt_qh')
   tt_qh.SetFillColor(q)
   tt_qh.Draw('hist')
   tt_qh_size = tt_qh.Integral()
   tt_qh_size_part = tt_qh.Integral(I,F)
   if shp=="PreFit":
    sizes_ttbar_prefit.append(tt_qh_size)
    sizes_ttbar_part_prefit.append(tt_qh_size_part)
   else:
    sizes_ttbar_postfit.append(tt_qh_size)
    sizes_ttbar_part_postfit.append(tt_qh_size_part)
   
   tt_dh = dataFile_tt.Get("data_obs")
   tt_dh.SetName('tt_dh')
   tt_dh.Sumw2()
   tt_dh.SetLineWidth(2)
   tt_dh.Draw('')
   tt_dh_size = tt_dh.Integral()
   tt_dh_size_part = tt_dh.Integral(I,F)
   
   tt_stack = THStack('tt_stack','')
   tt_stack.Add(tt_qh)
   tt_stack.Add(tt_th)
   tt_stack.Add(tt_tbh)
   tt_stack.Add(tt_twh)
   tt_stack.Add(tt_tth)
   tt_stack.Add(tt_wbbh)
   
   tt_err = tt_qh.Clone()
   tt_err.SetName('tt_qh')
   tt_err.Add(tt_th)
   tt_err.Add(tt_tbh)
   tt_err.Add(tt_twh)
   tt_err.Add(tt_tth)
   tt_err.Add(tt_wbbh)
   tt_err.SetFillStyle(3244)
   tt_err.SetFillColor(1)
   
   leg=TLegend(0.7,0.4,0.89,0.89)
   leg.SetFillColor(0)
   leg.SetBorderSize(0)
   leg.AddEntry(tt_err,'MC error','f')
   leg.AddEntry(tt_wbbh,'W(#mu#nu)+b#bar{b}','f')
   leg.AddEntry(tt_tth,'t#bar{t}','f')
   leg.AddEntry(tt_twh,'t_tW','f')
   leg.AddEntry(tt_tbh,'#bar{t}','f')
   leg.AddEntry(tt_th,'t','f')
   leg.AddEntry(tt_qh,'QCD','f')
   
   tt_dh.SetTitle('%s %s'%(smp,shp))
   tt_dh.Draw('')
   tt_stack.Draw('hist,sames')
   tt_dh.Draw('sames')
   tt_err.Draw('E2,sames')
   leg.Draw('sames')
   c.Print(where+"/%s_%s_%s_%s.png"%(wflav,ttsample,sample,shp))
   print("%s %s"%(sample,shp))
   print(" tt_wbb %s"%(tt_wbbh_size))
   print(" tt_tth %s"%(tt_tth_size))
   print(" tt_twh %s"%(tt_twh_size))
   print(" tt_tbh %s"%(tt_tbh_size))
   print(" tt_th  %s"%(tt_th_size))
   print(" tt_qh  %s"%(tt_qh_size))
  
  if sample=="Wbb" or sample=="UUbb":
   smp="Wbb"
   if not fourF: wbb_wbbh = theFile.Get("%s/%s/Wbb"%(shape,sample))
   if fourF: wbb_wbbh = theFile.Get("%s/%s/W4F"%(shape,sample))
   wbb_wbbh.SetName('wbb_wbbh')
   wbb_wbbh.SetFillColor(wbb)
   wbb_wbbh.Draw('hist')
   wbb_wbbh_size = wbb_wbbh.Integral()
   wbb_wbbh_size_part = wbb_wbbh.Integral(I,F)
   if shp=="PreFit":
    sizes_wbb_prefit.append(wbb_wbbh_size)
    sizes_wbb_part_prefit.append(wbb_wbbh_size_part)
   else:
    sizes_wbb_postfit.append(wbb_wbbh_size)
    sizes_wbb_part_postfit.append(wbb_wbbh_size_part)
   
   wbb_wcch = theFile.Get("%s/%s/Wcc"%(shape,sample))
   wbb_wcch.SetName('wbb_wcch')
   wbb_wcch.SetFillColor(wcc)
   wbb_wcch_size = wbb_wcch.Integral()
   wbb_wcch_size_part = wbb_wcch.Integral(I,F)
   if shp=="PreFit":
    sizes_wbb_prefit.append(wbb_wcch_size)
    sizes_wbb_part_prefit.append(wbb_wcch_size_part)
   else:
    sizes_wbb_postfit.append(wbb_wcch_size)
    sizes_wbb_part_postfit.append(wbb_wcch_size_part)
   
   wbb_wlh = theFile.Get("%s/%s/Wl"%(shape,sample))
   wbb_wlh.SetName('wbb_wlh')
   wbb_wlh.SetFillColor(wl)
   wbb_wlh_size = wbb_wlh.Integral()
   wbb_wlh_size_part = wbb_wlh.Integral(I,F)
   if shp=="PreFit":
    sizes_wbb_prefit.append(wbb_wlh_size)
    sizes_wbb_part_prefit.append(wbb_wlh_size_part)
   else:
    sizes_wbb_postfit.append(wbb_wlh_size)
    sizes_wbb_part_postfit.append(wbb_wlh_size_part)
   
   wbb_tth = theFile.Get("%s/%s/TTbar"%(shape,sample))
   wbb_tth.SetName('wbb_tth')
   wbb_tth.SetFillColor(ttb)
   wbb_tth.Draw('hist')
   wbb_tth_size = wbb_tth.Integral()
   wbb_tth_size_part = wbb_tth.Integral(I,F)
   if shp=="PreFit":
    sizes_wbb_prefit.append(wbb_tth_size)
    sizes_wbb_part_prefit.append(wbb_tth_size_part)
   else:
    sizes_wbb_postfit.append(wbb_tth_size)
    sizes_wbb_part_postfit.append(wbb_tth_size_part)
   
   wbb_th = theFile.Get("%s/%s/T"%(shape,sample))
   wbb_th.SetName('wbb_th')
   wbb_th.SetFillColor(tt)
   wbb_th.Draw('hist')
   wbb_th_size = wbb_th.Integral()
   wbb_th_size_part = wbb_th.Integral(I,F)
   if shp=="PreFit":
    sizes_wbb_prefit.append(wbb_th_size)
    sizes_wbb_part_prefit.append(wbb_th_size_part)
   else:
    sizes_wbb_postfit.append(wbb_th_size)
    sizes_wbb_part_postfit.append(wbb_th_size_part)
   
   wbb_tbh = theFile.Get("%s/%s/Tbar"%(shape,sample))
   wbb_tbh.SetName('wbb_tbh')
   wbb_tbh.SetFillColor(ts)
   wbb_tbh.Draw('hist')
   wbb_tbh_size = wbb_tbh.Integral()
   wbb_tbh_size_part = wbb_tbh.Integral(I,F)
   if shp=="PreFit":
    sizes_wbb_prefit.append(wbb_tbh_size)
    sizes_wbb_part_prefit.append(wbb_tbh_size_part)
   else:
    sizes_wbb_postfit.append(wbb_tbh_size)
    sizes_wbb_part_postfit.append(wbb_tbh_size_part)
   
   wbb_twh = theFile.Get("%s/%s/tW"%(shape,sample))
   wbb_twh.SetName('wbb_twh')
   wbb_twh.SetFillColor(ttw)
   wbb_twh.Draw('hist')
   wbb_twh_size = wbb_twh.Integral()
   wbb_twh_size_part = wbb_twh.Integral(I,F)
   if shp=="PreFit":
    sizes_wbb_prefit.append(wbb_twh_size)
    sizes_wbb_part_prefit.append(wbb_twh_size_part)
   else:
    sizes_wbb_postfit.append(wbb_twh_size)
    sizes_wbb_part_postfit.append(wbb_twh_size_part)
   
   wbb_zh = theFile.Get("%s/%s/Drell"%(shape,sample))
   wbb_zh.SetName('wbb_zh')
   wbb_zh.SetFillColor(z)
   wbb_zh.Draw('hist')
   wbb_zh_size = wbb_zh.Integral()
   wbb_zh_size_part = wbb_zh.Integral(I,F)
   if shp=="PreFit":
    sizes_wbb_prefit.append(wbb_zh_size)
    sizes_wbb_part_prefit.append(wbb_zh_size_part)
   else:
    sizes_wbb_postfit.append(wbb_zh_size)
    sizes_wbb_part_postfit.append(wbb_zh_size_part)
   
   wbb_vvh = theFile.Get("%s/%s/VV"%(shape,sample))
   wbb_vvh.SetName('wbb_vvh')
   wbb_vvh.SetFillColor(vv)
   wbb_vvh_size = wbb_vvh.Integral()
   wbb_vvh_size_part = wbb_vvh.Integral(I,F)
   if shp=="PreFit":
    sizes_wbb_prefit.append(wbb_vvh_size)
    sizes_wbb_part_prefit.append(wbb_vvh_size_part)
   else:
    sizes_wbb_postfit.append(wbb_vvh_size)
    sizes_wbb_part_postfit.append(wbb_vvh_size_part)
   
   wbb_qh = theFile.Get("%s/%s/QCD"%(shape,sample))
   wbb_qh.SetName('wbb_qh')
   wbb_qh.SetFillColor(q)
   wbb_qh.Draw('hist')
   wbb_qh_size = wbb_qh.Integral()
   wbb_qh_size_part = wbb_qh.Integral(I,F)
   if shp=="PreFit":
    sizes_wbb_prefit.append(wbb_qh_size)
    sizes_wbb_part_prefit.append(wbb_qh_size_part)
   else:
    sizes_wbb_postfit.append(wbb_qh_size)
    sizes_wbb_part_postfit.append(wbb_qh_size_part)
   
   wbb_dh = dataFile_wbb.Get("data_obs")
   wbb_dh.SetName('wbb_dh')
   wbb_dh.Sumw2()
   wbb_dh.SetLineWidth(2)
   wbb_dh.Draw('')
   wbb_dh_size = wbb_dh.Integral()
   wbb_dh_size_part = wbb_dh.Integral(I,F)
   
   print("%s %s"%(sample,shp))
   print(" wbb_qh   %s"%wbb_qh.Integral())
   print(" wbb_zh   %s"%wbb_zh.Integral())
   print(" wbb_vvh  %s"%wbb_vvh.Integral())
   print(" wbb_th   %s"%wbb_th.Integral())
   print(" wbb_tbh  %s"%wbb_tbh.Integral())
   print(" wbb_twh  %s"%wbb_twh.Integral())
   print(" wbb_tth  %s"%wbb_tth.Integral())
   print(" wbb_wlh  %s"%wbb_wlh.Integral())
   print(" wcc_wcch %s"%wbb_wcch.Integral())
   print(" wbb_wbbh %s"%wbb_wbbh.Integral())

   wbb_stack = THStack('wbb_stack','')
   wbb_stack.Add(wbb_qh)
   wbb_stack.Add(wbb_zh)
   wbb_stack.Add(wbb_vvh)
   wbb_stack.Add(wbb_th)
   wbb_stack.Add(wbb_tbh)
   wbb_stack.Add(wbb_twh)
   wbb_stack.Add(wbb_tth)
   wbb_stack.Add(wbb_wlh)
   wbb_stack.Add(wbb_wcch)
   wbb_stack.Add(wbb_wbbh)
   
   wbb_err = wbb_qh.Clone()
   wbb_err.SetName('wbb_err')
   wbb_err.Add(wbb_zh)
   wbb_err.Add(wbb_vvh)
   wbb_err.Add(wbb_th)
   wbb_err.Add(wbb_tbh)
   wbb_err.Add(wbb_twh)
   wbb_err.Add(wbb_tth)
   wbb_err.Add(wbb_wlh)
   wbb_err.Add(wbb_wcch)
   wbb_err.Add(wbb_wbbh)
   wbb_err.SetFillColor(1)
   wbb_err.SetFillStyle(3244)
   
   leg=TLegend(0.7,0.4,0.89,0.89)
   leg.SetFillColor(0)
   leg.SetBorderSize(0)
   leg.AddEntry(wbb_err,'MC error','f')
   leg.AddEntry(wbb_wbbh,'W+b#bar{b}','f')
   leg.AddEntry(wbb_wcch,'W+c#bar{c}','f')
   leg.AddEntry(wbb_wlh,'W+light','f')
   leg.AddEntry(wbb_tth,'t#bar{t}','f')
   leg.AddEntry(wbb_twh,'t_tW','f')
   leg.AddEntry(wbb_tbh,'#bar{t}','f')
   leg.AddEntry(wbb_th,'t','f')
   leg.AddEntry(wbb_vvh,'WW,WZ,ZZ','f')
   leg.AddEntry(wbb_zh,'Drell-Yan','f')
   leg.AddEntry(wbb_qh,'QCD','f')
   
   wbb_dh.Draw("")
   wbb_dh.SetTitle("%s %s"%(smp,shp))
   tex.SetTextAlign(13)
   tex.SetTextSize(0.04)
   if shp == "Fitted":
    tex.DrawLatex(0.15,0.89,"r = %0.3f #pm %0.3f"%(r,r_error))
   wbb_stack.Draw('hist,sames')
   wbb_err.Draw('E2,sames')
   wbb_dh.Draw("sames")
   leg.Draw("sames")
   c.Print(where+"/%s_%s_%s_%s.png"%(wflav,ttsample,sample,shp))

sizes_ttbar_prefit.append(sum(sizes_ttbar_prefit))
sizes_ttbar_postfit.append(sum(sizes_ttbar_postfit))
sizes_ttbar_part_postfit.append(sum(sizes_ttbar_part_postfit))
sizes_ttbar_part_prefit.append(sum(sizes_ttbar_part_prefit))
sizes_wbb_prefit.append(sum(sizes_wbb_prefit))
sizes_wbb_postfit.append(sum(sizes_wbb_postfit))
sizes_wbb_part_postfit.append(sum(sizes_wbb_part_postfit))
sizes_wbb_part_prefit.append(sum(sizes_wbb_part_prefit))

tt_dratio = tt_dh_size / sizes_ttbar_postfit[-1]
wbb_dratio = wbb_dh_size / sizes_wbb_postfit[-1]
tt_dratio_part = tt_dh_size_part / sizes_ttbar_part_postfit[-1]
wbb_dratio_part = wbb_dh_size_part / sizes_wbb_part_postfit[-1]

wflav,ttsample

log = open(where+"/%s_%s_ttbar.tex"%(wflav,ttsample),'w')
log.write("\documentclass{article}\n")
#log.write("\documentclass{standalone}\n")
#log.write("\input{/Users/rhombus/Documents/Madison/Latex/style}\n")
log.write("\\begin{document}\n\n")
log.write("\\begin{tabular}{r|l|l|l|l|l|l}\n")
log.write('\\bf{TTbar} & \multicolumn{3}{c|}{Full $m_T$ range} & \multicolumn{3}{|c}{$m_T>45$}\\\\ \n')
log.write('%s & PreFit & PostFit & Ratio & PreFit & PostFit & Ratio \\\\ \hline \n'%(ttsample))
for i,j,k,l,m in zip(samples_ttbar,sizes_ttbar_prefit,sizes_ttbar_postfit,sizes_ttbar_part_prefit,sizes_ttbar_part_postfit):
 log.write('%s  & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f\\\\ \n'%(i,j,k,k/j,l,m,m/l))
log.write('\hline \hline \n')
log.write('Data & \multicolumn{2}{c|}{%s} & %.3f & \multicolumn{2}{c|}{%s} & %.3f \n'%(tt_dh_size,tt_dratio,tt_dh_size_part,tt_dratio_part))
log.write("\\end{tabular}\\\n")
log.write("\end{document}")
log.close()

log = open(where+"/%s_%s_wbb.tex"%(wflav,ttsample),'w')
log.write("\documentclass{article}\n")
#log.write("\documentclass{standalone}\n")
#log.write("\input{/Users/rhombus/Documents/Madison/Latex/style}\n")
log.write("\\begin{document}\n\n")
log.write("\\begin{tabular}{r|l|l|l|l|l|l}\n")
log.write("\\bf{W+bb} & \multicolumn{6}{|c}{Fit Result: r = %.3f $\pm$ %.3f}\\\\ \n"%(r,r_error))
log.write("%s & \multicolumn{6}{|c}{Fit Bias: %.4f $\pm$ %.3f}\\\\ \n"%(wflav,bias,bias_error))
log.write('%s & \multicolumn{3}{c|}{Full $m_T$ range} & \multicolumn{3}{|c}{$m_T>45$}\\\\ \n'%(ttsample))
log.write('{} & PreFit & PostFit & Ratio & PreFit & PostFit & Ratio \\\\ \hline \n')
for i,j,k,l,m in zip(samples_wbb,sizes_wbb_prefit,sizes_wbb_postfit,sizes_wbb_part_prefit,sizes_wbb_part_postfit):
 log.write('%s  & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f\\\\ \n'%(i,j,k,k/j,l,m,m/l))
log.write('\hline \hline \n')
log.write('Data & \multicolumn{2}{c|}{%s} & %.3f & \multicolumn{2}{c|}{%s} & %.3f \n'%(wbb_dh_size,wbb_dratio,wbb_dh_size_part,wbb_dratio_part))
log.write("\\end{tabular}\n")
log.write("\end{document}")
log.close()
