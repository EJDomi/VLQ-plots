#!/usr/bin/env python

import os, re, sys, optparse, commands, shutil, imp
import math, ROOT

tdrstyle = imp.load_source('tdrstyle', './tdrstyle.py')
CMS_lumi = imp.load_source('CMS_lumi', './CMS_lumi.py') 

def DrawPresel(fin, hist, xlow, xhigh, doratiofit, xLabel, yLabel, useLog): 

  ROOT.gROOT.SetBatch()
  ROOT.gROOT.SetStyle('Plain')
  ROOT.gStyle.SetOptTitle(0) 
  ROOT.gStyle.SetOptStat(0000) 
  ROOT.gStyle.SetOptFit(0111) 
  ROOT.gStyle.SetErrorX(0.0001);
  
  fin = ROOT.TFile(fin,'READ')
  
  hdata      = fin.Get('Data')
  httjets    = fin.Get('TTJets')
  hsingletop = fin.Get('ST')
  hwjets     = fin.Get('WJets')
  hqcd       = fin.Get('histQCD')
  htp1200LH    = fin.Get('Tprime1200_LH')
 # htp1500LH    = fin.Get('Tp1500__'+hist)
 # htp1800LH    = fin.Get('Tp1800__'+hist)
  
  ndata      = hdata.Integral() 
  nttjets    = httjets.Integral() 
  nsingletop = hsingletop.Integral() 
  nwjets     = hwjets.Integral() 
  nqcd       = hqcd.Integral() 
  
  rescalescd = ndata - nttjets - nsingletop - nwjets
  
  hqcd.Scale(rescalescd/nqcd)
  
  hbkg = hqcd.Clone('kbkg')
  hbkg . Add(hsingletop) 
  hbkg . Add(httjets) 
  hbkg . Add(hwjets) 
  
  hratio = hdata.Clone('hratio')
  hratio.Divide(hbkg)
  
  fun = ROOT.TF1('fun','[0] + [1]*x', 1000, 3000)
  if doratiofit:
    fun.SetParameter(0,1.05)
    fun.SetParameter(1,-0.004)
    fun.SetParName(0,'intercept')
    fun.SetParName(1,'slope')
    fitres = hratio.Fit('fun', 'S')
    cov = fitres.GetCovarianceMatrix()
    fitres.Print('V')
    fitres.Write()
  
  hdata       . SetMarkerStyle(20) 
  hdata       . SetLineStyle(1) 
  hdata       . SetLineWidth(2) 
  hdata       . SetLineColor(1)  
    
  hbkg        . SetLineStyle(1) 
  hbkg        . SetLineWidth(1) 
  hbkg        . SetLineColor(1)  
  hbkg        . SetFillColor(0)  
    
  hsingletop  . SetLineColor(46)  
  hwjets      . SetLineColor(36)  
  httjets     . SetLineColor(26)  
  hqcd        . SetLineColor(16)  
  
  htp1200LH     . SetLineColor(3)  
  #htp1800LH     . SetLineColor(4)  
  
  htp1200LH     . SetLineWidth(2)  
  #htp1800LH     . SetLineWidth(2)  
  
  htp1200LH     . SetLineStyle(1)  
  #htp1800LH     . SetLineStyle(2)  
  
  hsingletop  . SetFillColor(46)  
  hsingletop  . SetFillColor(46)  
  hwjets      . SetFillColor(36)  
  httjets     . SetFillColor(26)  
  hqcd        . SetFillColor(16)  
  
  htp1200LH     . SetFillColor(0)  
  #htp1800LH     . SetFillColor(0)  
  
  hratio      . SetMarkerStyle(20) 
  hratio      . SetLineStyle(1) 
  hratio      . SetLineWidth(2) 
  hratio      . SetLineColor(1)  
    
  hsbkg = ROOT.THStack('hsbkg','')
  hsbkg.Add(hsingletop)
  hsbkg.Add(hwjets)
  hsbkg.Add(httjets)
  hsbkg.Add(hqcd)
  
  c0 = ROOT.TCanvas('c_data_mc_'+hist,'',800,600)
  c0.cd()
  pad0 = ROOT.TPad("pad0","",0.0,0.3,1.0,1.0)
  pad1 = ROOT.TPad("pad1","",0.0,0.0,1.0,0.3)
  
  #pad0.SetLogy()
  pad0.Draw() 
  pad0.cd()
  pad1.SetBottomMargin(0.05)
  
  hdata.GetXaxis().SetTitleSize(0.14*0.3/0.7)
  hdata.GetXaxis().SetTitleOffset(0.5) 
  hdata.GetYaxis().SetTitle(yLabel)
  hdata.GetYaxis().SetTitleSize(0.14*0.3/0.7)
  hdata.GetYaxis().SetLabelSize(0.14*0.3/0.7)
  hdata.GetYaxis().SetTitleOffset(0.28*7/3)
  
  hdata.Draw("e1")
  hsbkg.Draw('histsame')
  hbkg.Draw('histsame')
  hdata.Draw('e1same')
  htp1200LH.Draw('histsame')
  #htp1800LH.Draw('histsame')

  hdata.GetXaxis().SetRangeUser(xlow,xhigh)
  
  hdata.GetXaxis().SetTitle(xLabel)
  hdata.GetXaxis().SetLabelSize(0)

  pad0.RedrawAxis()
  
  pad0.Update()

  xmin = pad0.GetUxmin();
  ymin = hdata.GetMinimum();
  xmax = pad0.GetUxmax();
  ymax = hdata.GetMaximum();
  print " pad0 Uymax = ", ymax 
  hdata.SetMaximum(ymax*5000)
  hdata.SetMinimum(0.1)

  leg = ROOT.TLegend(0.12,0.66,0.88,0.88,'','brNDC')
  leg.SetBorderSize(0)
  leg.SetFillColor(0)
  leg.SetTextSize(0.040)
  leg.SetMargin(0.2)  
  leg.SetNColumns(4)
  leg.SetColumnSeparation(0.1)
  leg.SetEntrySeparation(0.1)
  leg.AddEntry(hdata      ,"Data            " , "ep")
  leg.AddEntry(hqcd       ,"Multijets       " , "fl")
  leg.AddEntry(hwjets     ,"W+jets          " , "fl")
  leg.AddEntry(htp1200LH    ,"M(T) = 1200 GeV " , "fl")
  leg.AddEntry(hbkg       ,"Total background" , "fl")
  leg.AddEntry(httjets    ,"t#bar{t}+jets   " , "fl")
  leg.AddEntry(hsingletop ,"Single top: tW  " , "fl")
  #leg.AddEntry(htp1800LH    ,"M(T) = 1800 GeV " , "fl")

  #if doratiofit:
  #  leg.AddEntry(fun        ,"Data/MC fit         " , "l" );

  leg.Draw()
  
  c0.cd()
  
  pad1.Draw() 
  pad1.cd()
  pad1.SetTopMargin(0.05)
  pad1.SetBottomMargin(0.3)
  
  hratio.GetXaxis().SetTitleSize(0.14)
  hratio.GetXaxis().SetLabelSize(0.14)
  hratio.GetXaxis().SetTickLength(hdata.GetXaxis().GetTickLength()*7/3)
  
  hratio.GetYaxis().SetTitle("Data/MC")
  hratio.GetYaxis().SetTitleSize(0.14)
  hratio.GetYaxis().SetLabelSize(0.14)
  hratio.GetYaxis().SetTickLength(hdata.GetYaxis().GetTickLength())
  hratio.GetYaxis().SetTitleOffset(0.28)
  hratio.GetYaxis().SetNdivisions(504)
  
  hratio.Draw("e1")

  hratio.GetXaxis().SetRangeUser(xlow,xhigh)
  hratio.SetMinimum(0.5)
  hratio.SetMaximum(1.5)

  if doratiofit:
    fun.Draw('same')
    pad1.Update()
    pavestats = hratio.FindObject("stats")
    pavestats.SetX1NDC(0.50)
    pavestats.SetX2NDC(0.88)
    pavestats.SetY1NDC(0.70)
    pavestats.SetY2NDC(0.92) 
    pavestats.SetBorderSize(0)
    pavestats.SetStatFormat('6.4f')
    pad1.Modified();  

  line = ROOT.TLine(xlow,1,xhigh,1)
  line.Draw()
  
  pad1.RedrawAxis()

  c0.cd()

  CMS_lumi.lumi_13TeV = "2.2/ fb"
  CMS_lumi.writeExtraText = 1
  CMS_lumi.extraText = "Preliminary"
  
  iPos = 0
  if( iPos==0 ): CMS_lumi.relPosX = 0.13
  
  CMS_lumi.CMS_lumi(c0, 4, iPos)
  c0.Update() 

  c0.SaveAs('PlotsNoHTWt/'+c0.GetName()+'.pdf')
  c0.SaveAs('PlotsNoHTWt/'+c0.GetName()+'.root')
#  c0.SaveAs('Plots/'+c0.GetName()+'.C')

def DrawPreselPlots():
  fin = ['PrunedMass_noHTWt-Fig4.root',
         'tau21_noHTWt-Fig5.root',
         'sjCSV2ndh_noHTWt-Fig6.root',
         'softDropMass_noHTWt-Fig7.root',
         'tau32_noHTWt-Fig8.root',
         'npv_noHTWt-Fig10.root',
         'sjCSV_noHTWt-Fig9.root',
         'htRegionA_noHTWt-Fig28.root',
         'htRegionB_noHTWt-Fig28.root',
         'htRegionC_noHTWt-Fig28.root',
         ]
  hists = ['PrunedMass',
           'tau21',
           'subJetCSV2ndh',
           'softDropMass',
           'tau32',
           'npv',
           'subJetCSV',
           'htRegionA',
           'htRegionB',
           'htRegionC' 
          ]
  xLabel = ['Pruned Mass [GeV]',
            '#tau_{21}',
            'subjet CSV',
            'Softdrop Mass [GeV]',
            '#tau_{32}',
            'nPV',
            'subjet CSV',
            'H_{T} [GeV]',
            'H_{T} [GeV]',
            'H_{T} [GeV]'
           ]
  yLabel = ['Jets',
            'Jets',
            'Jets',
            'Jets',
            'Jets',
            'Events'
            'Jets',
            'Events',
            'Events',
            'Events'
           ]
  isLog = [0,  0,   0,  1 , 1, 1,  0, 1, 1, 1] 
  xlow  = [0 , 0  , 0  ,0  ,0  ,0 , 0, 1000, 1000, 1000 ]
  xhigh = [800, 1  ,1  ,800  ,1 ,35, 1, 2600, 2600, 2600 ]
  for hist in hists:
    doratiofit=False
#    if 'HT' or 'tau21' in hist:
#      doratiofit = True

    DrawPresel(fin[hists.index(hist)], hist, xlow[hists.index(hist)], xhigh[hists.index(hist)], doratiofit,xLabel[hists.index(hist)], yLabel[hist.index(hist)], isLog[hist.index(hist)])

DrawPreselPlots()

