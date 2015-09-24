#define MyHeader_cxx
#include "MyHeader.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TLorentzVector.h>
#include <TArray.h>


using namespace std;

void monoZ_cutflow_INPUT_ADAP_NAME() {

    // Root macro to read D3PD and make histograms.
    
    //#################
    TString dataDir("/home/ameliajb/workarea/SiMs_AtlasExternal_v2/ConvertHepMC2root/rootFiles");
    TString treeName("Physics");
    TString outRootFile("rootFiles/INPUT_NAME.root");
    
    TString outTxtFile("cutFlow.txt");
    
    //********************************
    enum {nFiles = 1};
    std::string inFile[nFiles];
    inFile[0] = "OUTPUT_INPUT_NAME.root";
 
    //#################
    
    TH1F *lepton_pT_absolute = new TH1F("lepton_pT_absolute","pT of leptons before ANY selection",50,0,300);
    TH1F *lepton_eta_absolute = new TH1F("lepton_eta_absolute","Eta of leptons before ANY selection",30,-3,3);
    TH1F *lepton_pT = new TH1F("lepton_pT","pT of leptons",50,0,300);
    TH1F *charge_hist = new TH1F("charge_hist", "Multiplied charge of the selected lepton pair", 7, -3, 3);
    TH1F *Z_invmass = new TH1F("Z_invmass","Invariant mass of Z",40,50,130);
    TH1F *Z_phi_hist = new TH1F("Z_phi_hist", "Phi of Z", 12, -6, 6);
    TH1F *Z_eta_hist = new TH1F("Z_eta_hist","Eta of Z",30,-3,3);
    TH1F *MET = new TH1F("MET", "MET", 40, 0, 400);
    TH1F *MET_phi = new TH1F("MET_phi", "Phi of MET", 12, -6, 6);
    TH1F *MET_el_events = new TH1F("MET_el_events", "MET for electron pair events", 80, 0, 400);
    TH1F *MET_mu_events = new TH1F("MET_mu_events", "MET for muon pair events", 80, 0, 400);
    TH1F *phiDiff_hist = new TH1F("phiDiff_hist", "Phi difference between Z and MET", 70, -7, 7);
    TH1F *frac_diff_hist = new TH1F("frac_diff_hist", "Fractional pT difference between Z and MET", 50, 0, 1);  //changed from 100, 0, 1
    TH1F *MET_post_cuts = new TH1F("MET_post_cuts", "MET_post_cuts", 40, 0, 400);
    TH1F *MET_post_cuts_full = new TH1F("MET_post_cuts_full", "MET_post_cuts_full", 100, 0, 1000);
    
    // Chain D3PD and read in tree/ntuple
    std::string inFile2[nFiles];
    TChain * fChain = new TChain(treeName);
    for(int i=0;i<nFiles;i++) { // Chain input files
        inFile2[i]=dataDir;
        inFile2[i].append("/");
        inFile2[i].append(inFile[i]);
        fChain-> Add(inFile2[i].c_str());
        
    }
    
    
    TTree * tree = fChain;
    MyHeader *trd3 = new MyHeader(tree);
    
    // variables for number of events after cuts
    int n_GRL = 0;
    int num_eta_total = 0;
    
    int GeV = 1000.;
    
    int num_el_events=0;
    int num_mu_events=0;
    
    int num_post_dilep = 0;
    int num_post_3lepveto = 0;
    int num_post_OS = 0;
    int num_post_Zmass = 0;
    int num_post_METcut = 0;
    int num_post_dPhi = 0;
    int num_post_fracpt = 0;
    int num_post_Zeta = 0;
    int num_post_jetveto = 0;
    int num_post_MET150 = 0;
    int num_post_MET250 = 0;
    int num_post_MET350 = 0;
    int num_post_MET450 = 0;
    int num_post_finalMETcut = 0;
    
    // Loop over events and fill histograms
    Int_t nevent =(Int_t)trd3->GetEntries(); // number of events
    //   cout << "Number of event = " << nevent << endl;
    for (Int_t i=0;i<nevent;i++) { // loop over events
    //for (Int_t i=0;i<5;i++) { // loop over events		
        if (i%1000 == 0) {
            cout << "processing event # " << i << endl;
        }
        
        trd3->GetEntry(i);
        n_GRL++;
        
        int n_leptons = 0;
        
        bool is_el_pair = 0;
        bool is_mu_pair = 0;
      
 
        ////////////////////////   Overlap removal   //////////////////////////
       
        std::vector<int> es_post_pt_eta;
        std::vector<int> es_post_muon_overlap;
        std::vector<int> es_post_jet_overlap;
        std::vector<int> es_pT20;
        std::vector<int> mus_post_pt_eta;
        std::vector<int> mus_post_jet_overlap;
        std::vector<int> mus_pT20;
        std::vector<int> jets_post_pt_eta;
        std::vector<int> jets_post_el_overlap;
        std::vector<int> jets_pT25_eta;

	//cout << "Number of electrons: " << trd3->el_truth_n << endl;
	//cout << "Number of muons: " << trd3->mu_truth_n << endl;
	//cout << "Number of jets: " << trd3->jet_AntiKt4_truth_n << endl; 
        
        for(int e=0; e<trd3->el_truth_n; e++) {                                      		// Loop over electrons
	    //cout << "electron pt is " << (trd3->el_truth_pt->at(e))/GeV << " GeV" << endl;
            lepton_pT_absolute->Fill((trd3->el_truth_pt->at(e))/GeV);
            lepton_eta_absolute->Fill(trd3->el_truth_eta->at(e));
            if (fabs(trd3->el_truth_eta->at(e)) < 2.47 && trd3->el_truth_pt->at(e) > 7000){  	// Add to allowed electrons list if passes basic selection. Leave as pT here.
                es_post_pt_eta.push_back(e);
                lepton_pT->Fill((trd3->el_truth_pt->at(e))/GeV);                            	// Lepton pT histogram filled by leptons passing the basic selection
            }
        }
        
        for(int m=0; m<trd3->mu_truth_n; m++) {                                 		// Loop over muons
	    //cout << "muon pt is " << (trd3->mu_truth_pt->at(m))/GeV << " GeV" << endl;
            lepton_pT_absolute->Fill((trd3->mu_truth_pt->at(m))/GeV);
            lepton_eta_absolute->Fill(trd3->mu_truth_eta->at(m));
            if (fabs(trd3->mu_truth_eta->at(m)) < 2.5 && trd3->mu_truth_pt->at(m) > 7000){
                mus_post_pt_eta.push_back(m);
                lepton_pT->Fill((trd3->mu_truth_pt->at(m))/GeV);                      		// Lepton pT histogram filled by leptons passing the basic selection
            }
        }
        
        for(int j=0; j<trd3->jet_AntiKt4_truth_n; j++) {                     			// Loop over jets
	    //cout << "jet pt is " << (trd3->jet_AntiKt4_truth_pt->at(j))/GeV << " GeV" << endl;
            if (fabs(trd3->jet_AntiKt4_truth_eta->at(j)) < 4.5 && trd3->jet_AntiKt4_truth_pt->at(j) > 20000){
                jets_post_pt_eta.push_back(j);
            }
        }
        
        //cout << "Number of electrons before muon overlap removal is " << es_post_pt_eta.size() << endl;
        
        ///////////////////// Remove electrons overlapping with muons  ////////////////////
        
        for (int e=0; e<es_post_pt_eta.size(); e++){                            		// Loops over the indices of good electrons
            int el_index = es_post_pt_eta.at(e);                                		// defines the index of the good electron
            TLorentzVector elec_v;                                              		// Define 4-vector of the electron
            elec_v.SetPtEtaPhiE(trd3->el_truth_pt->at(el_index), trd3->el_truth_eta->at(el_index), trd3->el_truth_phi->at(el_index), trd3->el_truth_E->at(el_index));
            bool overlap = 0;
            for (int m=0; m<mus_post_pt_eta.size(); m++){
                int mu_index = mus_post_pt_eta.at(m);
                TLorentzVector mu_v;                                            		// Define 4-vector of muon
                mu_v.SetPtEtaPhiE(trd3->mu_truth_pt->at(mu_index), trd3->mu_truth_eta->at(mu_index), trd3->mu_truth_phi->at(mu_index), trd3->mu_truth_E->at(mu_index));
                float deltaR_el_mu = elec_v.DeltaR(mu_v);
                if (deltaR_el_mu < 0.2) {
		    //cout << "Overlap! Removing electron." << endl;
                    overlap = 1;
                    break;
                }
            }
            if (overlap == 0){
                es_post_muon_overlap.push_back(el_index);
            }
        }
        
        //cout << "Number of electrons after muon overlap removal is " << es_post_muon_overlap.size() << endl;
        
        //cout << "Number of jets before el removal is " << jets_post_pt_eta.size() << endl;
        
        ///////////////////// Remove jets overlapping with electrons  ////////////////////
        
        for (int j=0; j<jets_post_pt_eta.size(); j++){                            		// Loops over the indices of good jets
            int jet_index = jets_post_pt_eta.at(j);                                		// defines the index of the good jet
            TLorentzVector jet_v;                                              			// Define 4-vector of the jet
            jet_v.SetPtEtaPhiE(trd3->jet_AntiKt4_truth_pt->at(jet_index), trd3->jet_AntiKt4_truth_eta->at(jet_index), trd3->jet_AntiKt4_truth_phi->at(jet_index), trd3->jet_AntiKt4_truth_E->at(jet_index));
            bool overlap = 0;
            for (int e=0; e<es_post_muon_overlap.size(); e++){
                int el_index = es_post_muon_overlap.at(e);
                TLorentzVector elec_v;                                            		// Define 4-vector of electron
                elec_v.SetPtEtaPhiE(trd3->el_truth_pt->at(el_index), trd3->el_truth_eta->at(el_index), trd3->el_truth_phi->at(el_index), trd3->el_truth_E->at(el_index));
                float deltaR_jet_el = jet_v.DeltaR(elec_v);
                if (deltaR_jet_el < 0.2) {
		    //cout << "Overlap! Removing jet." << endl;
                    overlap = 1;
                    break;
                }
            }
            if (overlap == 0){
                jets_post_el_overlap.push_back(jet_index);
            }
        }
        
        //cout << "Number of jets after overlap with el is " << jets_post_el_overlap.size() << endl;
        
        ///////////////////// Remove electrons overlapping with jets  ////////////////////
        
        for (int e=0; e<es_post_muon_overlap.size(); e++){                            		// Loops over the indices of good electrons
            int el_index = es_post_muon_overlap.at(e);                                		// defines the index of the good electron
            TLorentzVector elec_v;                                              		// Define 4-vector of the electron
            elec_v.SetPtEtaPhiE(trd3->el_truth_pt->at(el_index), trd3->el_truth_eta->at(el_index), trd3->el_truth_phi->at(el_index), trd3->el_truth_E->at(el_index));
            bool overlap = 0;
            for (int j=0; j<jets_post_el_overlap.size(); j++){
                int jet_index = jets_post_el_overlap.at(j);
                TLorentzVector jet_v;                                            		// Define 4-vector of jet
                jet_v.SetPtEtaPhiE(trd3->jet_AntiKt4_truth_pt->at(jet_index), trd3->jet_AntiKt4_truth_eta->at(jet_index), trd3->jet_AntiKt4_truth_phi->at(jet_index), trd3->jet_AntiKt4_truth_E->at(jet_index));
                float deltaR_el_jet = elec_v.DeltaR(jet_v);
                if (deltaR_el_jet < 0.4) {
		    //cout << "Overlap! Removing electron." << endl;
                    overlap = 1;
                    break;
                }
            }
            if (overlap == 0){
                es_post_jet_overlap.push_back(el_index);
            }
        }
        
        //cout << "Number of electrons after overlap with jets is " << es_post_jet_overlap.size() << endl;
        
        ///////////////////// Remove muons overlapping with jets  ////////////////////
        
        for (int m=0; m<mus_post_pt_eta.size(); m++){                            		// Loops over the indices of good muons
            int mu_index = mus_post_pt_eta.at(m);                                		// defines the index of the good muona
            TLorentzVector mu_v;                                              			// Define 4-vector of the muon
            mu_v.SetPtEtaPhiE(trd3->mu_truth_pt->at(mu_index), trd3->mu_truth_eta->at(mu_index), trd3->mu_truth_phi->at(mu_index), trd3->mu_truth_E->at(mu_index));
            bool overlap = 0;
            for (int j=0; j<jets_post_el_overlap.size(); j++){
                int jet_index = jets_post_el_overlap.at(j);
                TLorentzVector jet_v;                                            		// Define 4-vector of jet
                jet_v.SetPtEtaPhiE(trd3->jet_AntiKt4_truth_pt->at(jet_index), trd3->jet_AntiKt4_truth_eta->at(jet_index), trd3->jet_AntiKt4_truth_phi->at(jet_index), trd3->jet_AntiKt4_truth_E->at(jet_index));
                float deltaR_mu_jet = mu_v.DeltaR(jet_v);
                if (deltaR_mu_jet < 0.4) {
		    //cout << "Overlap! Removing muon." << endl;
                    overlap = 1;
                    break;
                }
            }
            if (overlap == 0){
                mus_post_jet_overlap.push_back(mu_index);
            }
        }
        
        ////////////////////////   Select dileptons   //////////////////////////
        
        for (int e=0; e<es_post_jet_overlap.size(); e++){                            		// Loops over the indices of good electron
            int el_index = es_post_jet_overlap.at(e);                               	 	// Defines the index of the good electron
            if (trd3->el_truth_Et->at(el_index) > 20* GeV) {   					// change this pT to Et                           
                es_pT20.push_back(el_index);
            }
        }
        
        for (int m=0; m<mus_post_jet_overlap.size(); m++){                            		// Loops over the indices of good muon
            int mu_index = mus_post_jet_overlap.at(m);                                		// Defines the index of the good muon
            if (trd3->mu_truth_pt->at(mu_index) > 20* GeV) {
                mus_pT20.push_back(mu_index);
            }
        }
        
        int num_el20 = es_pT20.size();
        int num_mu20 = mus_pT20.size();
        
        if ((num_el20 != 2 && num_mu20 != 2) || (num_el20 == 2 && num_mu20 == 2)) continue;

        TLorentzVector lep_vector1;                 						// If two leptons, define the TLorentzVectors they will be
        TLorentzVector lep_vector2;
        
        if (num_el20==2){
            is_el_pair = 1;
            int el_index1 = es_pT20.at(0);
            int el_index2 = es_pT20.at(1);
            lep_vector1.SetPtEtaPhiE(trd3->el_truth_pt->at(el_index1), trd3->el_truth_eta->at(el_index1), trd3->el_truth_phi->at(el_index1), trd3->el_truth_E->at(el_index1));		// leave this pt as is
            lep_vector2.SetPtEtaPhiE(trd3->el_truth_pt->at(el_index2), trd3->el_truth_eta->at(el_index2), trd3->el_truth_phi->at(el_index2), trd3->el_truth_E->at(el_index2));
        }
        
        if (num_mu20==2){
            is_mu_pair = 1;
            int mu_index1 = mus_pT20.at(0);
            int mu_index2 = mus_pT20.at(1);
            lep_vector1.SetPtEtaPhiE(trd3->mu_truth_pt->at(mu_index1), trd3->mu_truth_eta->at(mu_index1), trd3->mu_truth_phi->at(mu_index1), trd3->mu_truth_E->at(mu_index1));
            lep_vector2.SetPtEtaPhiE(trd3->mu_truth_pt->at(mu_index2), trd3->mu_truth_eta->at(mu_index2), trd3->mu_truth_phi->at(mu_index2), trd3->mu_truth_E->at(mu_index2));
        }
        
        //cout << "Passed select dilepton" << endl;
        num_post_dilep++;
 
        
        ////////////////////////   Third lepton veto   //////////////////////////

        int num_el7 = es_post_jet_overlap.size();
        int num_mu7 = mus_post_jet_overlap.size();
        
        if ((num_el7 + num_mu7) > 2) continue;
        
        if (num_el20==2){
            int el_index1 = es_pT20.at(0);
            int el_index2 = es_pT20.at(1);
        }
        if (num_mu20==2){
            int mu_index1 = mus_pT20.at(0);
            int mu_index2 = mus_pT20.at(1);
        }
        
        
        //cout << "Passed third lepton veto" << endl;
        
        num_post_3lepveto++;
        
        ////////////////////////   Select OS leptons   //////////////////////////
        
        int charge1;
        int charge2;
        
        if (is_el_pair == 1){
            charge1 = trd3->el_truth_charge->at(es_pT20.at(0));
            charge2 = trd3->el_truth_charge->at(es_pT20.at(1));
        }
        
        if (is_mu_pair == 1){
            charge1 = trd3->mu_truth_charge->at(mus_pT20.at(0));
            charge2 = trd3->mu_truth_charge->at(mus_pT20.at(1));
        }
        
        //cout << "charge 1 is " << charge1 << endl;
        //cout << "charge 2 is " << charge2 << endl;
        
        charge_hist->Fill(charge1*charge2);
        
        if (charge1 * charge2 != -1) continue;
        
        //cout << "Passed opposite sign cut" << endl;
        
        num_post_OS++;
    
        ////////////////////////   Mass of Z   //////////////////////////
        
        TLorentzVector Z_vec;
        Z_vec = lep_vector1 + lep_vector2;
        float Z_mass = Z_vec.M() / GeV;
        float Z_pT = Z_vec.Pt() / GeV;
        float Z_eta = Z_vec.Eta();
        float Z_phi = Z_vec.Phi();
        
        TVector2 Z_vec2;                    							// Define a 2-vector with just length and angle (length set to 1 as is irrelevant)
        Z_vec2.SetMagPhi(1., Z_phi);          							// Angle is taken from the TLorentzVector, so is defined between -pi and pi.
        
        //cout << "Z mass is " << Z_mass << endl;
        //cout << "Z pt is " << Z_pT << endl;
        //cout << "Z eta is " << Z_eta << endl;
        //cout << "Z phi is " << Z_phi << endl;
        
        Z_invmass->Fill(Z_mass);
        Z_phi_hist->Fill(Z_phi);
        
        if (Z_mass < 76 || Z_mass > 106) continue;
        
        //cout << "Passed Z mass cut" << endl;
        
        num_post_Zmass++;
        
        ////////////////////////   MET cut   //////////////////////////
        
	float met = trd3->MET_truth_et / GeV;
	float met_phi = trd3->MET_truth_phi;

        if (met_phi > 3.1415) met_phi = met_phi - 6.283;            				// Phi between pi and 2pi moved to -pi to 0. - CHECK IF NEEDED
        TVector2 MET_vector_correctphi;
        MET_vector_correctphi.SetMagPhi(1, met_phi);

        //cout << "The MET is " << met << endl;
        
        if (is_el_pair==1) MET_el_events->Fill(met);
        if (is_mu_pair==1) MET_mu_events->Fill(met);
        
        MET->Fill(met);
        MET_phi->Fill(met_phi);
        
        //if (met < 100) continue;
        
        //cout << "Passed MET cut" << endl;
        
        num_post_METcut++;

        ////////////////////////   Delta_phi between MET and Z   //////////////////////////
        
        float phiDiff = Z_vec2.DeltaPhi(MET_vector_correctphi);
        
        phiDiff_hist->Fill(phiDiff);
        //cout << "phiDiff is " << phiDiff << endl;
        
        if (fabs(phiDiff) < 2.5) continue;
        
        //cout << "Passes phi diff cut" << endl;
        
        num_post_dPhi++;
        
        ////////////////////////   Fractional pT cut   //////////////////////////
        
        float frac_diff = fabs((Z_pT - met)/Z_pT);                           			// fractional difference between Z pT and MET
       	//cout << "frac diff is " << frac_diff << endl;
        
        frac_diff_hist->Fill(frac_diff);
        
        if (frac_diff >= 0.5) continue;
        
        //cout << "Passes fractional difference cut " << endl;
        
        num_post_fracpt++;
        
        ////////////////////////   Eta of Z   //////////////////////////
        
        //cout << "Z eta is " << Z_eta << endl;
        
        Z_eta_hist->Fill(Z_eta);
        
        if (fabs(Z_eta) >= 2.5) continue;
        
        //cout << "Passes Z eta cut " << endl;
        
        num_post_Zeta++;
        
        
        ////////////////////////   Jet veto   //////////////////////////
        
        
        if (is_el_pair == 1) num_el_events++;
        if (is_mu_pair == 1) num_mu_events++;
        
        for (int j=0; j<jets_post_el_overlap.size(); j++){                            		// Loops over the indices of good jets
            int jet_index = jets_post_el_overlap.at(j);                                		// defines the index of the good jet
            if (trd3->jet_AntiKt4_truth_pt->at(jet_index) > 25000 && fabs(trd3->jet_AntiKt4_truth_eta->at(jet_index)) < 2.5) {
                jets_pT25_eta.push_back(jet_index);
            }
            //cout << "jet pt is " << trd3->jet_AntiKt4TopoNewEM_pt->at(jet_index) << endl;
            //cout << "jet eta is " << trd3->jet_AntiKt4TopoNewEM_eta->at(jet_index) << endl;
            //cout << "jet phi is " << trd3->jet_AntiKt4TopoNewEM_phi->at(jet_index) << endl;
            
        }
        
        int num_jets = jets_pT25_eta.size();
                
        if (num_jets != 0) continue;
        
        //cout << "Passes jet veto" << endl;
        
        num_post_jetveto++;
        
        ////////////////////////   MET cut    //////////////////////////

	MET_post_cuts->Fill(met);
	MET_post_cuts_full->Fill(met);       

	if (met < 150.) continue;

	num_post_MET150++;
 
        if (met < 250.) continue;  					// This is not applied here, instead the efficiency is taken by counting events in the final histogram
       
	num_post_MET250++;

	if (met < 350.) continue;

        num_post_MET350++;

	if (met < 450.) continue;

        num_post_MET450++;
 
        //cout << "Passed MET cut" << endl;
        
        num_post_finalMETcut++;
        
        
        ////////////////////////   End of cuts   //////////////////////////
        
    }

    float acc_150 = float(num_post_MET150)/float(nevent);
    float acc_250 = float(num_post_MET250)/float(nevent);
    float acc_350 = float(num_post_MET350)/float(nevent);
    float acc_450 = float(num_post_MET450)/float(nevent);

    float statunc_150 = 1.96*sqrt(acc_150*(1.-acc_150)/float(nevent));
    float statunc_250 = 1.96*sqrt(acc_250*(1.-acc_250)/float(nevent));
    float statunc_350 = 1.96*sqrt(acc_350*(1.-acc_350)/float(nevent));
    float statunc_450 = 1.96*sqrt(acc_450*(1.-acc_450)/float(nevent));

    cout << "nevent is " << nevent << endl;

    cout << "Number of electron events is " << num_el_events << endl;
    cout << "Number of muon events is " << num_mu_events << endl;

    cout << "num_post_dilep : " << num_post_dilep << endl;
    cout << "num_post_3lepveto : " << num_post_3lepveto << endl;
    cout << "num_post_OS : " << num_post_OS << endl;
    cout << "num_post_Zmass : " << num_post_Zmass << endl;
    cout << "num_post_METcut : " << num_post_METcut << endl;
    cout << "num_post_dPhi : " << num_post_dPhi << endl;
    cout << "num_post_fracpt : " << num_post_fracpt << endl;
    cout << "num_post_Zeta : " << num_post_Zeta << endl;
    cout << "num_post_jetveto : " << num_post_jetveto << endl;
    cout << "num_post_MET150 : " << num_post_MET150 << endl;
    cout << "num_post_MET250 : " << num_post_MET250 << endl;
    cout << "num_post_MET350 : " << num_post_MET350 << endl;
    cout << "num_post_MET450 : " << num_post_MET450 << endl;
    cout << "num_post_finalMETcut : " << num_post_finalMETcut << endl;

    // BEGIN IMPORTANT OUTPUT LINES

    cout << "acc MET > 150 : " << acc_150 << endl;
    cout << "acc MET > 250 : " << acc_250 << endl;
    cout << "acc MET > 350 : " << acc_350 << endl;
    cout << "acc MET > 450 : " << acc_450 << endl;

    cout << "MET stat > 150 : " << statunc_150 << endl;
    cout << "MET stat > 250 : " << statunc_250 << endl;
    cout << "MET stat > 350 : " << statunc_350 << endl;
    cout << "MET stat > 450 : " << statunc_450 << endl;

    // END IMPORTANT OUTPUT LINES

    // Save histograms
    TFile *f = new TFile(outRootFile,"RECREATE");
    
    lepton_pT_absolute->Write();
    lepton_eta_absolute->Write();
    lepton_pT->Write();
    charge_hist->Write();
    Z_invmass->Write();
    Z_phi_hist->Write();
    Z_eta_hist->Write();
    MET_el_events->Write();
    MET_mu_events->Write();
    MET->Write();
    MET_post_cuts->Write();
    MET_post_cuts_full->Write();
    MET_phi->Write();
    phiDiff_hist->Write();
    frac_diff_hist->Write();

    f->Write();
    f->Close();
    
//    cout << "outTxtFile = " << outTxtFile << endl;
    
//    Open output file and save results. #####
    ofstream outFile(outTxtFile); //open output file
    if (!outFile) {
        cout << "Cannot open file " << outFile << endl;
    }
    outFile.setf(ios::fixed);
    outFile.setf(ios::showpoint);
    outFile.close();
}
