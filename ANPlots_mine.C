#include "TROOT.h"
#include "TSystem.h"
#include "TCanvas.h"

void ANPlots()
{

gSystem->Load("makeStack4_C.so");

makeStack("ht","isRegionA","Tprime1200_LH","H_{T} [GeV]", "Events/50 GeV","htRegionA_noHTWt-Fig28",1,1,20,1000,2600,"EvtWeight*EvtWtPV");
makeStack("ht","isRegionB","Tprime1200_LH","H_{T} [GeV]", "Events/50 GeV","htRegionB_noHTWt-Fig28",1,1,20,1000,2600,"EvtWeight*EvtWtPV*topSF(ptTopTagged)");
makeStack("ht","isRegionC","Tprime1200_LH","H_{T} [GeV]", "Events/50 GeV","htRegionC_noHTWt-Fig28",1,1,20,1000,2600,"EvtWeight*EvtWtPV*btagsf");

makeStack("npv","1","Tprime1200_LH","nPV","Events","npv_noHTWt-Fig10",1000,1,35,0,35,"EvtWeight*EvtWtPV");

makeStack("tau3AK8/tau2AK8","1","Tprime1200_LH","#tau_{32}","Jets","tau32_noHTWt-Fig8",1000,1,50,0,1,"EvtWeight*EvtWtPV");

makeStack("SoftDropMassAK8","1","Tprime1200_LH","SoftDropMass [Gev]","Jets","softDropMass_noHTWt-Fig7",1,1,40,0,800,"EvtWeight*EvtWtPV");

makeStack("min(sj0CSVAK8,sj1CSVAK8)","(sj0CSVAK8>0.605||sj1CSVAK8>0.605)","Tprime1200_LH","subjet CSV","Jets","sjCSV2ndh_noHTWt-Fig6",1000,1,50,0,1,"EvtWeight*EvtWtPV");

makeStack("sj0CSVAK8","1","Tprime1200_LH","subjet CSV","Jets","sj0CSV_noHTWt-Fig9",1000,1,50,0,1,"EvtWeight*EvtWtPV");

makeStack("sj1CSVAK8","1","Tprime1200_LH","subjet CSV","Jets","sj1CSV_noHTWt-Fig9",1000,1,50,0,1,"EvtWeight*EvtWtPV");

makeStack("tau2AK8/tau1AK8","1","Tprime1200_LH","#tau_{21}","Jets","tau21_noHTWt-Fig5",1000,1,50,0,1,"EvtWeight*EvtWtPV");

makeStack("PrunedMassAK8","1","Tprime1200_LH","Pruned Mass [GeV]","Jets","PrunedMass_noHTWt-Fig4",1,1,40,0,800,"EvtWeight*EvtWtPV");
}
