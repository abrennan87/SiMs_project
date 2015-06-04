#include "fastjet/ClusterSequence.hh"
#include "fastjet/MassDropTagger.hh"
#include "fastjet/Filter.hh"
#include "fastjet/Selector.hh"
#include <TROOT.h>
#include <TChain.h>
#include <TTree.h>
#include <TFile.h>
#include <TSelector.h>
#include <TH2.h>
#include <TH1.h>
#include <TGraph.h>
#include <TProfile.h>
#include <TStyle.h>
#include <TMath.h>

#include <string>
#include <vector>
#include <iostream>
#include <stdlib.h>

using namespace std;

TTree * output_tree;
TFile * outfile;

std::vector<std::string> line_tokens;
string item;
char delim;

Double_t eta;
Double_t phi;

double R_antiKt;
double R_CA;
double Rfilt;

vector<fastjet::PseudoJet> particles;
vector<fastjet::PseudoJet> jet_seeds;
vector<fastjet::PseudoJet> jets_antiKt;
vector<fastjet::PseudoJet> jets_CA;
vector<fastjet::PseudoJet> filtered_tagged_jet;
vector<fastjet::PseudoJet> tagged_pieces;
vector<fastjet::PseudoJet> constituents;	// used for checking running of FastJet
fastjet::PseudoJet MET_p;
int this_PID;
int this_PID_v2;

vector<Int_t>     mc_pdgID_v;		
vector<Double_t>  mc_px_v;		
vector<Double_t>  mc_py_v;
vector<Double_t>  mc_pz_v;
vector<Double_t>  mc_pt_v;
vector<Double_t>  mc_E_v;		
vector<Double_t>  mc_m_v;
vector<Double_t>  mc_eta_v;
vector<Double_t>  mc_phi_v;

vector<Double_t>  el_px_v;		
vector<Double_t>  el_py_v;
vector<Double_t>  el_pz_v;
vector<Double_t>  el_pt_v;
vector<Double_t>  el_E_v;                       
vector<Double_t>  el_Et_v;
vector<Double_t>  el_m_v;
vector<Double_t>  el_eta_v;
vector<Double_t>  el_phi_v;
vector<Double_t>  el_charge_v;

vector<Double_t>  mu_px_v;		
vector<Double_t>  mu_py_v;
vector<Double_t>  mu_pz_v;
vector<Double_t>  mu_pt_v;
vector<Double_t>  mu_E_v;                       
vector<Double_t>  mu_m_v;
vector<Double_t>  mu_eta_v;
vector<Double_t>  mu_phi_v;
vector<Double_t>  mu_charge_v;

vector<Double_t>  ph_px_v;
vector<Double_t>  ph_py_v;
vector<Double_t>  ph_pz_v;
vector<Double_t>  ph_pt_v;
vector<Double_t>  ph_E_v;
vector<Double_t>  ph_m_v;
vector<Double_t>  ph_eta_v;
vector<Double_t>  ph_phi_v;

vector<Double_t>  jet_AntiKt4_pt_v;		
vector<Double_t>  jet_AntiKt4_E_v;
vector<Double_t>  jet_AntiKt4_eta_v;
vector<Double_t>  jet_AntiKt4_phi_v;
vector<Double_t>  jet_AntiKt4_m_v;		

vector<Double_t>  jet_fat_pt_v;
vector<Double_t>  jet_fat_E_v;
vector<Double_t>  jet_fat_eta_v;
vector<Double_t>  jet_fat_phi_v;
vector<Double_t>  jet_fat_m_v;

vector<Double_t>  jet_MDF_pt_v;
vector<Double_t>  jet_MDF_E_v;
vector<Double_t>  jet_MDF_eta_v;
vector<Double_t>  jet_MDF_phi_v;
vector<Double_t>  jet_MDF_m_v;

vector<Double_t>  Vertex_x_v;
vector<Double_t>  Vertex_y_v;
vector<Double_t>  Vertex_z_v;

Double_t this_vertex_x;
Double_t this_vertex_y;
Double_t this_vertex_z;

Double_t p_x;
Double_t p_y;
Double_t p_z;
Double_t E;

Double_t weight;
Double_t next_weight;

string starts_str;
string alt_starts_str;

bool premature_exit = 0;
int event_number = 0;
int jet_AntiKt4_n = 0;	
int jet_fat_n = 0;
int jet_MDF_n = 0;
bool good_E = 0;        
int mc_n = 0;	
int el_n = 0;	
int mu_n = 0;
int ph_n = 0;	
int el_count = 0;
int mu_count = 0;
int ph_count = 0;
double Sum_pt = 0;
double MET_et = 0;
double MET_phi = 0;
