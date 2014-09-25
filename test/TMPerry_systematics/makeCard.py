import sys, ast
import operator
cardname = sys.argv[1]
wbb = sys.argv[2]
ttbar_ps = sys.argv[3]
syst_dontuse = sys.argv[4]

wbb_file   = "Renamed4F_"+sys.argv[5]+".root"
ttbar_file = "Renamed4F_"+sys.argv[6]+".root"

syst_list = ['beff','beffC','beffL','bgT','bgTOP','bgTbar','bgVV','bgWcc','bgZjet','bgtW','effT','lumi','muonE','qcd','wlight','jet','UCE','muon']
#syst_list = ast.literal_eval(sys.argv[5])
if syst_dontuse in syst_list: syst_list.remove(syst_dontuse)

#if ttbar_ps == "3j":   ttbar_file = "../Renamed4F_PS6c_08sptr_Datacard_3j2525_2bt_mt.root"
#if ttbar_ps == "1m1e": ttbar_file = "../Renamed4F_PS6c_05sptr_Datacard_2j2525_2bt_1m1e_mt.root"
#wbb_file = "../Renamed4F_PS6c_08sptr_Datacard_2j2525_2bt_mt.root"

wbb_samples = [wbb,"Tbar","tW","Wl","Wcc","T","VV","QCD","TTbar","Drell"]
tt_samples = [wbb,"Tbar","tW","T","QCD","TTbar"]

syst_dict = {
"beff"  :["lnN  ","1.12 ","1.12 "," 1.12","-    ","-    ","1.12 ","1.12 ","-  ","1.12 ","1.12 ","1.12 ","1.12 ","1.12 ","1.12 ","-  ","1.12 "],
"beffC" :["lnN  ","-    ","-    ","-    ","-    ","1.24 ","-    ","-    ","-  ","-    ","-    ","-    ","-    ","-    ","-    ","-  ","-    "],
"beffL" :["lnN  ","-    ","-    ","-    ","1.15 ","-    ","-    ","-    ","-  ","-    ","-    ","-    ","-    ","-    ","-    ","-  ","-    "],
"bgT"   :["lnN  ","-    ","-    ","-    ","-    ","-    ","1.08 ","-    ","-  ","-    ","-    ","-    ","-    ","-    ","1.08 ","-  ","-    "],
"bgTOP" :["lnN  ","-    ","-    ","-    ","-    ","-    ","-    ","-    ","-  ","1.2  ","-    ","-    ","-    ","-    ","-    ","-  ","1.2  "],
"bgTbar":["lnN  ","-    ","1.1  ","-    ","-    ","-    ","-    ","-    ","-  ","-    ","-    ","-    ","1.1  ","-    ","-    ","-  ","-    "],
"bgVV"  :["lnN  ","-    ","-    ","-    ","-    ","-    ","-    ","1.17 ","-  ","-    ","-    ","-    ","-    ","-    ","-    ","-  ","-    "],
"bgWcc" :["lnN  ","-    ","-    ","-    ","-    ","1.5  ","-    ","-    ","-  ","-    ","-    ","-    ","-    ","-    ","-    ","-  ","-    "],
"bgZjet":["lnN  ","-    ","-    ","-    ","-    ","-    ","-    ","-    ","-  ","-    ","1.1  ","-    ","-    ","-    ","-    ","-  ","-    "],
"bgtW"  :["lnN  ","-    ","-    ","1.3  ","-    ","-    ","-    ","-    ","-  ","-    ","-    ","-    ","-    ","1.3  ","-    ","-  ","-    "],
"effT"  :["lnN  ","-    ","-    ","-    ","-    ","-    ","-    ","-    ","-  ","-    ","-    ","-    ","1.06 ","-    ","1.06 ","-  ","1.06 "],
"lumi"  :["lnN  ","1.026","1.026","1.026","1.026","1.026","1.026","1.026","-  ","1.026","1.026","1.026","1.026","1.026","1.026","-  ","1.026"],
"muonE" :["lnN  ","1.01 ","1.01 ","1.01 ","1.01 ","1.01 ","1.01 ","1.01 ","-  ","1.01 ","1.01 ","1.01 ","1.01 ","1.01 ","1.01 ","-  ","1.01 "],
"qcd"   :["lnN  ","-    ","-    ","-    ","-    ","-    ","-    ","-    ","1.5","-    ","-    ","-    ","-    ","-    ","-    ","1.5","-    "],
"wlight":["lnN  ","-    ","-    ","-    ","1.5  ","-    ","-    ","-    ","-  ","-    ","-    ","-    ","-    ","-    ","-    ","-  ","-    "],
"jet"   :["shape","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","-  ","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","-  ","1.0  "],
"UCE"   :["shape","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","-  ","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","-  ","1.0  "],
"muon"  :["shape","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","-  ","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","1.0  ","-  ","1.0  "],
}


txt = open("%s.txt"%(cardname),"w")
txt.write("imax 2 number of bins\n")
txt.write("jmax 9 number of processes minus 1\n")
txt.write("kmax * \n")
txt.write("---------------------------------------------\n")
txt.write("shapes\t*\tTTbr\t%s\t$PROCESS\t$PROCESS_$SYSTEMATIC\n"%(ttbar_file))
txt.write("shapes\t*\tUUbb\t%s\t$PROCESS\t$PROCESS_$SYSTEMATIC\n"%(wbb_file))
txt.write("---------------------------------------------\n")
txt.write("bin\t\tUUbb\tTTbr\n")
txt.write("observation\t-1.0\t-1.0\n")
txt.write("---------------------------------------------\n")

txt.write("bin\t\t")
for x in wbb_samples: txt.write("UUbb\t")
for x in tt_samples:  txt.write("TTbr\t")
txt.write("\n")

txt.write("process\t\t")
for x in wbb_samples: txt.write("%s\t"%(x))
for x in tt_samples:  txt.write("%s\t"%(x))
txt.write("\n")

txt.write("process\t\t")
for x in range(0,len(wbb_samples)): txt.write("%s\t"%(x))
for x in range(0,len(tt_samples)):  txt.write("%s\t"%(x))
txt.write("\n")

txt.write("rate\t\t")
for x in wbb_samples: txt.write("-1\t")
for x in tt_samples:  txt.write("-1\t")
txt.write("\n")
txt.write("---------------------------------------------\n")

for x in syst_list:
 txt.write("%s\t"%(x))
 for y in syst_dict[x]:
  txt.write("%s\t"%(y))
 txt.write("\n")

txt.close()
