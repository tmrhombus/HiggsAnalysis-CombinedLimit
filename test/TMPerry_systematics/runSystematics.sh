## 
# Goes through all steps in performing and evaulating fit
# Author: T. Mastrianni Perry
#
# Define filenames as environment variables and put them in ./roots/
##

      wbb_file="2014sptr20_Dcrd_2j2525_2bt_mt_new"
  tt_1m1e_file="2014sptr20_Dcrd_2j2525_2bt_1m1e_mt_new"
    tt_3j_file="2014sptr20_Dcrd_3j2525_2bt_mt_new"
    wbb_4ffile="2014sptr20_Wbb_4F_mt_new"
tt_1m1e_4ffile="2014sptr20_TT_1m1e_4F_mt_new"
  tt_3j_4ffile="2014sptr20_TT_3j_4F_mt_new"

mkdir -p roots
pushd roots

python ../renameHistos.py \
 $wbb_file \
 $tt_1m1e_file \
 $tt_3j_file \
 $wbb_4ffile \
 $tt_1m1e_4ffile \
 $tt_3j_4ffile

python ../reRangeHistos.py \
 $wbb_file \
 $tt_1m1e_file \
 $tt_3j_file

for wbb in 'Wbb' 'W4F'
do
 for ttsample in '1m1e' '3j' 
 do
  for igno in 'full' 'beff' 'beffC' 'beffL' 'bgT' 'bgTOP' 'bgTbar' 'bgVV' 'bgWcc' 'bgZjet' 'bgtW' 'effT' 'lumi' 'muonE' 'qcd' 'wlight' 'jet' 'UCE' 'muon'
  do
   name=$igno"_"$wbb"_"$ttsample

   if [ "$ttsample" = "1m1e" ]
   then 
    tt_file=$tt_1m1e_file
   else 
    tt_file=$tt_3j_file
   fi

   echo -e "\nRunning: "$name 
   echo -e "\nMaking Card: "$name > $name".out"

   python ../makeCard.py  \
    "card_"$name \
    $wbb \
    $ttsample \
    $igno \
    $wbb_file \
    $tt_file \
    &>>$name".out" 2>&1

   combine -M MaxLikelihoodFit \
    --saveNormalizations \
    --saveShapes \
    --saveWithUncertainties \
    --customStartingPoint \
    "card_"$name".txt" \
    &>>$name".out" 2>&1

   mv mlfit.root "mlfit_"$name".root"

   combine -M MaxLikelihoodFit \
    "card_"$name".txt" -t -1 --expectSignal=1 \
    &>>$name".out" 2>&1

   mv mlfit.root "mlfit_"$name"_fitbias.root"
   echo -e "Just finished with "$name"\n"

  rm roostats*
  rm higgs*
  done
 done
done

popd

mkdir -p plots

for wbb in 'Wbb' #'W4F'
do
 for ttsample in '1m1e' #'3j'
 do

  if [ "$ttsample" = "1m1e" ]
  then 
   tt_file=$tt_1m1e_file
  else 
   tt_file=$tt_3j_file
  fi

  python shapePlotter.py \
   $wbb \
   $ttsample \
   $wbb_file \
   $tt_file

  pushd plots
  pdflatex $wbb'_'$ttsample'_ttbar.tex'
  pdflatex $wbb'_'$ttsample'_wbb.tex'
  popd

 done
done

python stabilityPlotter.py

