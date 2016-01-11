//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Tue Nov 11 04:30:35 2014 by ROOT version 5.34/21
// from TTree Physics/Physics
// found on file: testing.root
//////////////////////////////////////////////////////////

#ifndef MyHeader_h
#define MyHeader_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

#include <vector>

using namespace std;

// Fixed size dimensions of array or collections stored in the TTree if any.

class MyHeader {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Int_t           mc_n;
   vector<int>     *mc_pdgID;
   vector<double>  *mc_px;
   vector<double>  *mc_py;
   vector<double>  *mc_pz;
   vector<double>  *mc_pt;
   vector<double>  *mc_E;
   vector<double>  *mc_m;
   vector<double>  *mc_eta;
   vector<double>  *mc_phi;
   Int_t           el_truth_n;
   vector<double>  *el_truth_px;
   vector<double>  *el_truth_py;
   vector<double>  *el_truth_pz;
   vector<double>  *el_truth_pt;
   vector<double>  *el_truth_E;
   vector<double>  *el_truth_Et;
   vector<double>  *el_truth_m;
   vector<double>  *el_truth_eta;
   vector<double>  *el_truth_phi;
   vector<double>  *el_truth_charge;
   Int_t           mu_truth_n;
   vector<double>  *mu_truth_px;
   vector<double>  *mu_truth_py;
   vector<double>  *mu_truth_pz;
   vector<double>  *mu_truth_pt;
   vector<double>  *mu_truth_E;
   vector<double>  *mu_truth_m;
   vector<double>  *mu_truth_eta;
   vector<double>  *mu_truth_phi;
   vector<double>  *mu_truth_charge;
   Int_t           ph_truth_n;
   vector<double>  *ph_truth_pt;
   vector<double>  *ph_truth_eta;
   Int_t           jet_AntiKt4_truth_n;
   vector<double>  *jet_AntiKt4_truth_E;
   vector<double>  *jet_AntiKt4_truth_pt;
   vector<double>  *jet_AntiKt4_truth_eta;
   vector<double>  *jet_AntiKt4_truth_phi;
   vector<double>  *jet_AntiKt4_truth_m;
   Double_t        MET_truth_et;
   Double_t        MET_truth_phi;
   vector<double>  *V_X;
   vector<double>  *V_Y;
   vector<double>  *V_Z;
   Double_t        Sum_pt;
   Double_t        weight;

   // List of branches
   TBranch        *b_mc_n;   //!
   TBranch        *b_mc_pdgID;   //!
   TBranch        *b_mc_px;   //!
   TBranch        *b_mc_py;   //!
   TBranch        *b_mc_pz;   //!
   TBranch        *b_mc_pt;   //!
   TBranch        *b_mc_E;   //!
   TBranch        *b_mc_m;   //!
   TBranch        *b_mc_eta;   //!
   TBranch        *b_mc_phi;   //!
   TBranch        *b_el_truth_n;   //!
   TBranch        *b_el_truth_px;   //!
   TBranch        *b_el_truth_py;   //!
   TBranch        *b_el_truth_pz;   //!
   TBranch        *b_el_truth_pt;   //!
   TBranch        *b_el_truth_E;   //!
   TBranch        *b_el_truth_Et;   //!
   TBranch        *b_el_truth_m;   //!
   TBranch        *b_el_truth_eta;   //!
   TBranch        *b_el_truth_phi;   //!
   TBranch        *b_el_truth_charge;   //!
   TBranch        *b_mu_truth_n;   //!
   TBranch        *b_mu_truth_px;   //!
   TBranch        *b_mu_truth_py;   //!
   TBranch        *b_mu_truth_pz;   //!
   TBranch        *b_mu_truth_pt;   //!
   TBranch        *b_mu_truth_E;   //!
   TBranch        *b_mu_truth_m;   //!
   TBranch        *b_mu_truth_eta;   //!
   TBranch        *b_mu_truth_phi;   //!
   TBranch        *b_mu_truth_charge;   //!
   TBranch        *b_ph_truth_n;   //!
   TBranch        *b_ph_truth_pt;   //!
   TBranch        *b_ph_truth_eta;   //!
   TBranch        *b_jet_AntiKt4_truth_n;   //!
   TBranch        *b_jet_AntiKt4_truth_E;   //!
   TBranch        *b_jet_AntiKt4_truth_pt;   //!
   TBranch        *b_jet_AntiKt4_truth_eta;   //!
   TBranch        *b_jet_AntiKt4_truth_phi;   //!
   TBranch        *b_jet_AntiKt4_truth_m;   //!
   TBranch        *b_MET_truth_et;   //!
   TBranch        *b_MET_truth_phi;   //!
   TBranch        *b_V_X;   //!
   TBranch        *b_V_Y;   //!
   TBranch        *b_V_Z;   //!
   TBranch        *b_Sum_pt;   //!
   TBranch        *b_weight;   //!

   MyHeader(TTree *tree=0);
   virtual ~MyHeader();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntries();
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   //virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef MyHeader_cxx
MyHeader::MyHeader(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("testing.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("testing.root");
      }
      f->GetObject("Physics",tree);

   }
   Init(tree);
}

MyHeader::~MyHeader()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t MyHeader::GetEntries()
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntries();
}

Int_t MyHeader::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t MyHeader::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void MyHeader::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   mc_pdgID = 0;
   mc_px = 0;
   mc_py = 0;
   mc_pz = 0;
   mc_pt = 0;
   mc_E = 0;
   mc_m = 0;
   mc_eta = 0;
   mc_phi = 0;
   el_truth_px = 0;
   el_truth_py = 0;
   el_truth_pz = 0;
   el_truth_pt = 0;
   el_truth_E = 0;
   el_truth_Et = 0;
   el_truth_m = 0;
   el_truth_eta = 0;
   el_truth_phi = 0;
   el_truth_charge = 0;
   mu_truth_px = 0;
   mu_truth_py = 0;
   mu_truth_pz = 0;
   mu_truth_pt = 0;
   mu_truth_E = 0;
   mu_truth_m = 0;
   mu_truth_eta = 0;
   mu_truth_phi = 0;
   mu_truth_charge = 0;
   jet_AntiKt4_truth_E = 0;
   jet_AntiKt4_truth_pt = 0;
   jet_AntiKt4_truth_eta = 0;
   jet_AntiKt4_truth_phi = 0;
   jet_AntiKt4_truth_m = 0;
   V_X = 0;
   V_Y = 0;
   V_Z = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("mc_n", &mc_n, &b_mc_n);
   fChain->SetBranchAddress("mc_pdgID", &mc_pdgID, &b_mc_pdgID);
   fChain->SetBranchAddress("mc_px", &mc_px, &b_mc_px);
   fChain->SetBranchAddress("mc_py", &mc_py, &b_mc_py);
   fChain->SetBranchAddress("mc_pz", &mc_pz, &b_mc_pz);
   fChain->SetBranchAddress("mc_pt", &mc_pt, &b_mc_pt);
   fChain->SetBranchAddress("mc_E", &mc_E, &b_mc_E);
   fChain->SetBranchAddress("mc_m", &mc_m, &b_mc_m);
   fChain->SetBranchAddress("mc_eta", &mc_eta, &b_mc_eta);
   fChain->SetBranchAddress("mc_phi", &mc_phi, &b_mc_phi);
   fChain->SetBranchAddress("el_truth_n", &el_truth_n, &b_el_truth_n);
   fChain->SetBranchAddress("el_truth_px", &el_truth_px, &b_el_truth_px);
   fChain->SetBranchAddress("el_truth_py", &el_truth_py, &b_el_truth_py);
   fChain->SetBranchAddress("el_truth_pz", &el_truth_pz, &b_el_truth_pz);
   fChain->SetBranchAddress("el_truth_pt", &el_truth_pt, &b_el_truth_pt);
   fChain->SetBranchAddress("el_truth_E", &el_truth_E, &b_el_truth_E);
   fChain->SetBranchAddress("el_truth_Et", &el_truth_Et, &b_el_truth_Et);
   fChain->SetBranchAddress("el_truth_m", &el_truth_m, &b_el_truth_m);
   fChain->SetBranchAddress("el_truth_eta", &el_truth_eta, &b_el_truth_eta);
   fChain->SetBranchAddress("el_truth_phi", &el_truth_phi, &b_el_truth_phi);
   fChain->SetBranchAddress("el_truth_charge", &el_truth_charge, &b_el_truth_charge);
   fChain->SetBranchAddress("mu_truth_n", &mu_truth_n, &b_mu_truth_n);
   fChain->SetBranchAddress("mu_truth_px", &mu_truth_px, &b_mu_truth_px);
   fChain->SetBranchAddress("mu_truth_py", &mu_truth_py, &b_mu_truth_py);
   fChain->SetBranchAddress("mu_truth_pz", &mu_truth_pz, &b_mu_truth_pz);
   fChain->SetBranchAddress("mu_truth_pt", &mu_truth_pt, &b_mu_truth_pt);
   fChain->SetBranchAddress("mu_truth_E", &mu_truth_E, &b_mu_truth_E);
   fChain->SetBranchAddress("mu_truth_m", &mu_truth_m, &b_mu_truth_m);
   fChain->SetBranchAddress("mu_truth_eta", &mu_truth_eta, &b_mu_truth_eta);
   fChain->SetBranchAddress("mu_truth_phi", &mu_truth_phi, &b_mu_truth_phi);
   fChain->SetBranchAddress("mu_truth_charge", &mu_truth_charge, &b_mu_truth_charge);
   fChain->SetBranchAddress("ph_truth_n", &ph_truth_n, &b_ph_truth_n);
   fChain->SetBranchAddress("ph_truth_pt", &ph_truth_pt, &b_ph_truth_pt);
   fChain->SetBranchAddress("ph_truth_eta", &ph_truth_eta, &b_ph_truth_eta);
   fChain->SetBranchAddress("jet_AntiKt4_truth_n", &jet_AntiKt4_truth_n, &b_jet_AntiKt4_truth_n);
   fChain->SetBranchAddress("jet_AntiKt4_truth_E", &jet_AntiKt4_truth_E, &b_jet_AntiKt4_truth_E);
   fChain->SetBranchAddress("jet_AntiKt4_truth_pt", &jet_AntiKt4_truth_pt, &b_jet_AntiKt4_truth_pt);
   fChain->SetBranchAddress("jet_AntiKt4_truth_eta", &jet_AntiKt4_truth_eta, &b_jet_AntiKt4_truth_eta);
   fChain->SetBranchAddress("jet_AntiKt4_truth_phi", &jet_AntiKt4_truth_phi, &b_jet_AntiKt4_truth_phi);
   fChain->SetBranchAddress("jet_AntiKt4_truth_m", &jet_AntiKt4_truth_m, &b_jet_AntiKt4_truth_m);
   fChain->SetBranchAddress("MET_truth_et", &MET_truth_et, &b_MET_truth_et);
   fChain->SetBranchAddress("MET_truth_phi", &MET_truth_phi, &b_MET_truth_phi);
   fChain->SetBranchAddress("V_X", &V_X, &b_V_X);
   fChain->SetBranchAddress("V_Y", &V_Y, &b_V_Y);
   fChain->SetBranchAddress("V_Z", &V_Z, &b_V_Z);
   fChain->SetBranchAddress("Sum_pt", &Sum_pt, &b_Sum_pt);
   fChain->SetBranchAddress("weight", &weight, &b_weight);
   Notify();
}

Bool_t MyHeader::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void MyHeader::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t MyHeader::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef MyHeader_cxx
