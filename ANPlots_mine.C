#include "TROOT.h"
#include "TSystem.h"
#include "TCanvas.h"

void ANPlots()
{

gSystem->Load("makeStack4_C.so");

makeStack("ht","isRegionA","Tprime1200_LH","H_{T} [GeV]", "Events/50 GeV","htRegionA_noHTWt-Fig28",1,1,20,1000,2600,"EvtWeight*EvtWtPV*WtTrig(ht)");
makeStack("ht","isRegionB","Tprime1200_LH","H_{T} [GeV]", "Events/50 GeV","htRegionB_noHTWt-Fig28",1,1,20,1000,2600,"EvtWeight*EvtWtPV*WtTrig(ht)*topSF(ptTopTagged)");
makeStack("ht","isRegionC","Tprime1200_LH","H_{T} [GeV]", "Events/50 GeV","htRegionC_noHTWt-Fig28",1,1,20,1000,2600,"EvtWeight*EvtWtPV*WtTrig(ht)*btagsf");

makeStack("npv","1","Tprime1200_LH","nPV","Events","npv_noHTWt-Fig10",1000,1,35,0,35,"EvtWeight*EvtWtPV*WtTrig(ht)");

makeStack("tau3AK8/tau2AK8","1","Tprime1200_LH","#tau_{32}","Jets","tau32_noHTWt-Fig8",1000,1,50,0,1,"EvtWeight*EvtWtPV*WtTrig(ht)");

makeStack("SoftDropMassAK8","1","Tprime1200_LH","SoftDropMass [Gev]","Jets","softDropMass_noHTWt-Fig7",1,1,40,0,800,"EvtWeight*EvtWtPV*WtTrig(ht)");

makeStack("min(sj0CSVAK8,sj1CSVAK8)","(sj0CSVAK8>0.605||sj1CSVAK8>0.605)","Tprime1200_LH","subjet CSV","Jets","sjCSV2ndh_noHTWt-Fig6",1000,1,50,0,1,"EvtWeight*EvtWtPV*WtTrig(ht)");

makeStack("sj0CSVAK8","1","Tprime1200_LH","subjet CSV","Jets","sj0CSV_noHTWt-Fig9",1000,1,50,0,1,"EvtWeight*EvtWtPV*WtTrig(ht)");

makeStack("sj1CSVAK8","1","Tprime1200_LH","subjet CSV","Jets","sj1CSV_noHTWt-Fig9",1000,1,50,0,1,"EvtWeight*EvtWtPV*WtTrig(ht)");

makeStack("tau2AK8/tau1AK8","1","Tprime1200_LH","#tau_{21}","Jets","tau21_noHTWt-Fig5",1000,1,50,0,1,"EvtWeight*EvtWtPV*WtTrig(ht)");

makeStack("PrunedMassAK8","1","Tprime1200_LH","Pruned Mass [GeV]","Jets","PrunedMass_noHTWt-Fig4",1,1,40,0,800,"EvtWeight*EvtWtPV*WtTrig(ht)");


makeStack("ht","isRegionA","Tprime1200_LH","H_{T} [GeV]", "Events/50 GeV","htRegionA_HTWt-Fig28",1,1,20,1000,2600,"EvtWeight*EvtWtHT*EvtWtPV*WtTrig(ht)");
makeStack("ht","isRegionB","Tprime1200_LH","H_{T} [GeV]", "Events/50 GeV","htRegionB_HTWt-Fig28",1,1,20,1000,2600,"EvtWeight*EvtWtHT*EvtWtPV*WtTrig(ht)*topSF(ptTopTagged)");
makeStack("ht","isRegionC","Tprime1200_LH","H_{T} [GeV]", "Events/50 GeV","htRegionC_HTWt-Fig28",1,1,20,1000,2600,"EvtWeight*EvtWtHT*EvtWtPV*WtTrig(ht)*btagsf");

makeStack("npv","1","Tprime1200_LH","nPV","Events","npv_HTWt-Fig10",1000,1,35,0,35,"EvtWeight*EvtWtHT*EvtWtPV*WtTrig(ht)");

makeStack("tau3AK8/tau2AK8","1","Tprime1200_LH","#tau_{32}","Jets","tau32_HTWt-Fig8",1000,1,50,0,1,"EvtWeight*EvtWtHT*EvtWtPV*WtTrig(ht)");

makeStack("SoftDropMassAK8","1","Tprime1200_LH","SoftDropMass [Gev]","Jets","softDropMass_HTWt-Fig7",1,1,40,0,800,"EvtWeight*EvtWtHT*EvtWtPV*WtTrig(ht)");

makeStack("min(sj0CSVAK8,sj1CSVAK8)","(sj0CSVAK8>0.605||sj1CSVAK8>0.605)","Tprime1200_LH","subjet CSV","Jets","sjCSV2ndh_HTWt-Fig6",1000,1,50,0,1,"EvtWeight*EvtWtHT*EvtWtPV*WtTrig(ht)");

makeStack("sj0CSVAK8","1","Tprime1200_LH","subjet CSV","Jets","sj0CSV_HTWt-Fig9",1000,1,50,0,1,"EvtWeight*EvtWtHT*EvtWtPV*WtTrig(ht)");

makeStack("sj1CSVAK8","1","Tprime1200_LH","subjet CSV","Jets","sj1CSV_HTWt-Fig9",1000,1,50,0,1,"EvtWeight*EvtWtHT*EvtWtPV*WtTrig(ht)");

makeStack("tau2AK8/tau1AK8","1","Tprime1200_LH","#tau_{21}","Jets","tau21_HTWt-Fig5",1000,1,50,0,1,"EvtWeight*EvtWtHT*EvtWtPV*WtTrig(ht)");

makeStack("PrunedMassAK8","1","Tprime1200_LH","Pruned Mass [GeV]","Jets","PrunedMass_HTWt-Fig4",1,1,40,0,800,"EvtWeight*EvtWtHT*EvtWtPV*WtTrig(ht)");
}
