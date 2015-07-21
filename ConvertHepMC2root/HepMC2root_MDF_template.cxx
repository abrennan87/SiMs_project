// Adapted from Jim Henderson, CERN user (January 2013 James.Henderson@cern.ch)
// Takes HepMC input, runs FastJet, defines truth MET, fills a ROOT histogram similar to ATLAS NTUP.

// Adapted to look at two types of jets - antiKt and fat-jets. The latter come from Cambridge-Aachen jets, with mass-drop tagging (to ensure two balanced subjets) and filtering (removes everything outside the three hardest subjets within the original jet).

#include "HepMC2root_MDF.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <stdlib.h>
#include <math.h>
#include <random>
using namespace std;

//#include <TVector.h>
#include <TTree.h>

int main(int argc, char *argv[]){
  
  string line = "";						
  ifstream infile;
  delim = ' ';
  good_E = 0;

  R_antiKt = 0.4;
  R_CA = 1.2;

  string in_file_string = "/home/ameliajb/workarea/SiMs_AtlasExternal_v2/pythia8201/share/Pythia8/examples/HepMC_out/INPUT_NAME.dat";
  if ( argc > 1 ) in_file_string = string(argv[1]);				

  infile.open( in_file_string.c_str() );
  outfile = new TFile( "rootFiles/OUTPUT_INPUT_NAME.root","RECREATE");
  output_tree = new TTree("Physics", "Physics");

  fastjet::JetDefinition jet_def_antiKt(fastjet::antikt_algorithm, R_antiKt);		// definition of jets for FastJet
  fastjet::JetDefinition jet_def_CA(fastjet::cambridge_algorithm, R_CA);

  // Input mass-drop details, used for mass-drop tagging
  double mu=0.67, y_cut=0.16;                                            // Need to find out which mu value to use?? NEW: y changed from 0.09, is this correct?? Should it be 0.16?
  fastjet::MassDropTagger tagger(mu, y_cut);					 

  output_tree->Branch("mc_n", &(mc_n));					// all truth particles, before FastJet
  output_tree->Branch("mc_pdgID", &(mc_pdgID_v) );			
  output_tree->Branch("mc_px", &(mc_px_v) );				
  output_tree->Branch("mc_py", &(mc_py_v) );
  output_tree->Branch("mc_pz", &(mc_pz_v) );
  output_tree->Branch("mc_pt", &(mc_pt_v) );
  output_tree->Branch("mc_E", &(mc_E_v) );				
  output_tree->Branch("mc_m", &(mc_m_v) );				
  output_tree->Branch("mc_eta", &(mc_eta_v) );				
  output_tree->Branch("mc_phi", &(mc_phi_v) );				

  output_tree->Branch("el_truth_n", &(el_n));                 		// all electrons 
  output_tree->Branch("el_truth_px", &(el_px_v) );                      
  output_tree->Branch("el_truth_py", &(el_py_v) );			 
  output_tree->Branch("el_truth_pz", &(el_pz_v) );			 
  output_tree->Branch("el_truth_pt", &(el_pt_v) );			 
  output_tree->Branch("el_truth_E", &(el_E_v) );                        
  output_tree->Branch("el_truth_Et", &(el_Et_v) ); 
  output_tree->Branch("el_truth_m", &(el_m_v) );                         
  output_tree->Branch("el_truth_eta", &(el_eta_v) );                     
  output_tree->Branch("el_truth_phi", &(el_phi_v) );                     
  output_tree->Branch("el_truth_charge", &(el_charge_v) );		// set manually to +/- 1

  output_tree->Branch("mu_truth_n", &(mu_n));                           // all muons
  output_tree->Branch("mu_truth_px", &(mu_px_v) );                      
  output_tree->Branch("mu_truth_py", &(mu_py_v) );                       
  output_tree->Branch("mu_truth_pz", &(mu_pz_v) );                       
  output_tree->Branch("mu_truth_pt", &(mu_pt_v) );                       
  output_tree->Branch("mu_truth_E", &(mu_E_v) );                         
  output_tree->Branch("mu_truth_m", &(mu_m_v) );                         
  output_tree->Branch("mu_truth_eta", &(mu_eta_v) );                    
  output_tree->Branch("mu_truth_phi", &(mu_phi_v) );                     
  output_tree->Branch("mu_truth_charge", &(mu_charge_v) );              // set manually, see above

  output_tree->Branch("ph_truth_n", &(ph_n));                           // all muons
  output_tree->Branch("ph_truth_px", &(ph_px_v) );
  output_tree->Branch("ph_truth_py", &(ph_py_v) );
  output_tree->Branch("ph_truth_pz", &(ph_pz_v) );
  output_tree->Branch("ph_truth_pt", &(ph_pt_v) );
  output_tree->Branch("ph_truth_E", &(ph_E_v) );
  output_tree->Branch("ph_truth_m", &(ph_m_v) );
  output_tree->Branch("ph_truth_eta", &(ph_eta_v) );
  output_tree->Branch("ph_truth_phi", &(ph_phi_v) );

  output_tree->Branch("jet_AntiKt4_truth_n", &(jet_AntiKt4_n));			// all antiKt jets after FastJet		
  output_tree->Branch("jet_AntiKt4_truth_E", &(jet_AntiKt4_E_v) );
  output_tree->Branch("jet_AntiKt4_truth_pt", &(jet_AntiKt4_pt_v) );
  output_tree->Branch("jet_AntiKt4_truth_eta", &(jet_AntiKt4_eta_v) );
  output_tree->Branch("jet_AntiKt4_truth_phi", &(jet_AntiKt4_phi_v) );
  output_tree->Branch("jet_AntiKt4_truth_m", &(jet_AntiKt4_m_v) );	

  output_tree->Branch("jet_fat_truth_n", &(jet_fat_n));                 // all C-A jets before filtering               
  output_tree->Branch("jet_fat_truth_E", &(jet_fat_E_v) );
  output_tree->Branch("jet_fat_truth_pt", &(jet_fat_pt_v) );
  output_tree->Branch("jet_fat_truth_eta", &(jet_fat_eta_v) );
  output_tree->Branch("jet_fat_truth_phi", &(jet_fat_phi_v) );
  output_tree->Branch("jet_fat_truth_m", &(jet_fat_m_v) );
 
  output_tree->Branch("jet_MDF_truth_n", &(jet_MDF_n));                 // all mass-drop-filtered jets               
  output_tree->Branch("jet_MDF_truth_E", &(jet_MDF_E_v) );
  output_tree->Branch("jet_MDF_truth_pt", &(jet_MDF_pt_v) );
  output_tree->Branch("jet_MDF_truth_eta", &(jet_MDF_eta_v) );
  output_tree->Branch("jet_MDF_truth_phi", &(jet_MDF_phi_v) );
  output_tree->Branch("jet_MDF_truth_m", &(jet_MDF_m_v) );
 	
  output_tree->Branch("MET_truth_et", &(MET_et));
  output_tree->Branch("MET_truth_phi", &(MET_phi));

  output_tree->Branch("V_X", &(Vertex_x_v) );				// Information on vertices, not useful for now but included
  output_tree->Branch("V_Y", &(Vertex_y_v) );
  output_tree->Branch("V_Z", &(Vertex_z_v) );
  output_tree->Branch("Sum_pt", &(Sum_pt));				
  output_tree->Branch("weight", &(weight));				

  event_number = 0;
  mc_n = 0;
  el_n = 0;
  mu_n = 0;
  ph_n = 0;
  Sum_pt = 0;
  MET_et = 0;
  MET_phi = 0;

  cout << "Setup Complete, starting processing." << endl;

  int done_p = 0;							
  weight = 0;
  next_weight = 0;

  while (!infile.eof())							
    {
      getline(infile, line);						

      //if ( done_p > 5 ) break;					// stop after 5 events	

      // Look for the start of an event
      starts_str = "E";
      alt_starts_str = "HepMC::IO_GenEvent-END_EVENT_LISTING";
      if ( (line.compare( 0, starts_str.length(), starts_str ) == 0) || (line.compare( 0, alt_starts_str.length(), alt_starts_str ) == 0)  ){

	stringstream ss(line);			
        while( getline(ss, item, delim)) {	
          line_tokens.push_back(item);	
        }

	weight = next_weight;
	next_weight = atof(line_tokens.at( line_tokens.size() - 1 ).c_str());		

	if (event_number%1000 == 0)
	  cout << "Processed event number: " << event_number << endl;
	event_number += 1;

	if (good_E){							// All particles are found below, the information is filled here for the previous event 

	  MET_p = fastjet::PseudoJet(0.,0.,0.,0.);			// MET_p is a 'jet' vector, initially empty, then added to by the neutrinos/DM
          el_count = 0;
	  mu_count = 0;
	  ph_count = 0;
	  for ( int p = 0; p < particles.size(); p++ ){			// Particles is a vector filled with the 4-vector (pT,E) of every particle, each is a PseudoJet.
	   
	    //cout << "ID is " << mc_pdgID_v.at( p ) << endl;
	    this_PID = fabs(mc_pdgID_v.at( p ));					
	    if ( this_PID == 12 || this_PID == 14 || this_PID == 16 || this_PID == 9000010){	// Neutrinos + DM included in the MET
	      MET_p += particles[p];						
	    }
	    //if (this_PID == 9000010) cout << "pT of chi is " << (particles[p].pt())/1000. << endl;
	    mc_pt_v.push_back( particles[p].pt() );			// access particle momentum, fill vectors
	    mc_px_v.push_back( particles[p].px() );
	    mc_py_v.push_back( particles[p].py() );
	    mc_pz_v.push_back( particles[p].pz() );
	    mc_m_v.push_back( particles[p].m() );			
	    mc_E_v.push_back( particles[p].E() );
	    mc_eta_v.push_back( particles[p].eta() );
	    mc_phi_v.push_back( particles[p].phi() );	
	    Sum_pt += particles[p].pt();					// Sum_pT sums the pT value of all particles

	    if (this_PID == 11){
	      el_count+=1;
	      //cout << "electron pT is " << (particles[p].pt())/1000. << endl;
	      // smearing the ET and PT of electrons. Taking values on ET smearing from fig 351 of 1407.5063. Applying the same values to pT for now.
	      //random_device rd;
              //mt19937 e2(rd());                                                           // random generator
	      //normal_distribution<> dist_el_low(0,0.01);
              //normal_distribution<> dist_el_med(0, 0.01);
              //normal_distribution<> dist_el_high(0, 0.01);
	      std::default_random_engine e4;
	      std::default_random_engine e8;
	      std::normal_distribution<double> dist_el(0, 0.01);
              float smear_factor_el = dist_el(e4) + 1.;
	      float smear_factor_el_ET = dist_el(e8) + 1.;
              //if (particles[p].Et() < 20000) {smear_factor_el = 1. + dist_el_low(e2);}
              //else if (20000 < particles[p].Et() < 60000) {smear_factor_el = 1. + dist_el_med(e2);}
              //else {smear_factor_el = 1. + dist_el_high(e2);}                                        // take from normal distribution with mean 0, standard dev = uncertainty on el/gamma resolution = 4% (ET < 20) / 2.7% (ET < 60) / 1.5% (ET > 60) 
              //float el_pT_unsmeared = particles[p].pt();
              //float el_pT_smeared = el_pT_unsmeared*smear_factor_el;                               // apply smearing
	      //float el_ET_unsmeared = particles[p].Et();				// don't think this will work - might need to calculate Et from E and phi/theta/eta
	      //float el_ET_smeared = el_ET_unsmeared*smear_factor_el;
              el_pt_v.push_back( particles[p].pt() * smear_factor_el );
              el_px_v.push_back( particles[p].px() );
              el_py_v.push_back( particles[p].py() );
              el_pz_v.push_back( particles[p].pz() );
              el_m_v.push_back( particles[p].m() );                                   
              el_E_v.push_back( particles[p].E() );
	      el_Et_v.push_back( particles[p].Et()*smear_factor_el_ET );
              el_eta_v.push_back( particles[p].eta() );
              el_phi_v.push_back( particles[p].phi() );
	      if (mc_pdgID_v.at( p ) == 11) el_charge_v.push_back( -1. );        // electrons
              else if (mc_pdgID_v.at( p ) == -11) el_charge_v.push_back( 1. );   // positrons
	      else cout << "Problem with electron PDG ID" << endl;
	    }
	    
	    if (this_PID == 13){
              mu_count+=1;
	      //cout << "muon pT is " << (particles[p].pt())/1000. << endl;
	      //random_device rd;
              //mt19937 e2(rd());                                                           // random generator
              std::default_random_engine e5;
              std::normal_distribution<> dist_mu(0, 0.008);                                        // take from normal distribution with mean 0, standard dev = uncertainty on muon resolution = 4% (conservative)
              float smear_factor_mu = 1. + dist_mu(e5);
              //float mu_pT_unsmeared = particles[p].pt();
              //float mu_pT_smeared = mu_pT_unsmeared*smear_factor_mu;                               // apply smearing
              mu_pt_v.push_back( particles[p].pt()*smear_factor_mu );
              mu_px_v.push_back( particles[p].px() );
              mu_py_v.push_back( particles[p].py() );
              mu_pz_v.push_back( particles[p].pz() );
              mu_m_v.push_back( particles[p].m() );                               
              mu_E_v.push_back( particles[p].E() );
              mu_eta_v.push_back( particles[p].eta() );
              mu_phi_v.push_back( particles[p].phi() );
	      if (mc_pdgID_v.at( p ) == 13) mu_charge_v.push_back( -1. );        // muons
              else if (mc_pdgID_v.at( p ) == -13) mu_charge_v.push_back( 1. );   // anti-muons
              else cout << "Problem with muon PDG ID" << endl;
            }

	   if (this_PID == 22){
              ph_count+=1;
              //cout << "photon pT is " << (particles[p].pt())/1000. << endl;
              // smearing is not working, not sure why - fix up later
              //random_device rd;
              //mt19937 e2(rd());                                                           // random generator
              //normal_distribution<> dist_ph(0, 0.05);                                        // take from normal distribution with mean 0, standard dev = uncertainty on muon resolution = 5% - need to check this!
              //float smear_factor_ph = 1. + dist_ph(e2);
              //float ph_pT_unsmeared = particles[p].pt();
              //float ph_pT_smeared = ph_pT_unsmeared*smear_factor_ph;                               // apply smearing
              //ph_pt_v.push_back( ph_pT_smeared );
              ph_pt_v.push_back( particles[p].pt() );
              ph_px_v.push_back( particles[p].px() );
              ph_py_v.push_back( particles[p].py() );
              ph_pz_v.push_back( particles[p].pz() );
              ph_m_v.push_back( particles[p].m() );
              ph_E_v.push_back( particles[p].E() );
              ph_eta_v.push_back( particles[p].eta() );
              ph_phi_v.push_back( particles[p].phi() );
            } 

	  }

	  el_n = el_count;
	  mu_n = mu_count;
	  ph_n = ph_count;

	  MET_phi = MET_p.phi();						// Calculates MET_phi
	  MET_et = MET_p.pt();							// MET defined as missing transverse momentum
	  
	  fastjet::ClusterSequence cs_antiKt(jet_seeds, jet_def_antiKt);			// Clusters the jets with jet_seeds (see below) as input
	  jets_antiKt.clear();								
	  jets_antiKt = fastjet::sorted_by_pt(cs_antiKt.inclusive_jets());			// Groups the post-clustering jets and orders by pT. Note these are INCLUSIVE_JETS.

	  fastjet::ClusterSequence cs_CA(jet_seeds, jet_def_CA);                        // Clusters the jets with jet_seeds (see below) as input
          jets_CA.clear();
          jets_CA = fastjet::sorted_by_pt(cs_CA.inclusive_jets());

	  
//	  // Inspecting the constituents and final jets
//	  cout << "Clustered with " << jet_def_antiKt.description() << endl;

//	  // print the jets
//	  cout << "         pt       y       phi" << endl;
//	  for (unsigned i = 0; i < jets_antiKt.size(); i++) {
//	    cout << "jet " << i << ": "<< (jets_antiKt[i].perp())/1000. << " " << jets_antiKt[i].rap() << " " << jets_antiKt[i].phi() << endl;
//	    constituents = jets_antiKt[i].constituents();
//	    for (unsigned j = 0; j < constituents.size(); j++) {
//	      cout << " constituent " << j << "’s pt: "<< (constituents[j].perp())/1000. << endl;
//	    }
//	  }


	  jet_AntiKt4_n = jets_antiKt.size();
          for ( int j = 0; j < jet_AntiKt4_n; j++ ) {                                   // Final-state antiKt jets
            //random_device rd;
            //mt19937 e2(rd());                                                           // random generator
            std::default_random_engine e2;
            std::normal_distribution<double> dist(0, 0.05);                                        // take from normal distribution with mean 0, standard dev = uncertainty on jet resolution = 5% (conservative)
            float smear_factor = 1. + dist(e2);
            //cout << "e2: " << e2 << endl;
            //cout << "smear_factor: " << smear_factor << endl;
            //float pT_unsmeared = jets_antiKt[j].perp();
            //float pT_smeared = pT_unsmeared*smear_factor;                               // apply smearing
            //cout << "pT_unsmeared: " << pT_unsmeared << endl;
            //cout << "pT_smeared: " << pT_smeared << endl;
            jet_AntiKt4_pt_v.push_back( jets_antiKt[j].perp()*smear_factor );                                   // fill jet pt vector with smeared values
            jet_AntiKt4_E_v.push_back( jets_antiKt[j].E() );
            jet_AntiKt4_eta_v.push_back( jets_antiKt[j].eta() );
            jet_AntiKt4_phi_v.push_back( jets_antiKt[j].phi() );
            jet_AntiKt4_m_v.push_back( jets_antiKt[j].m() );
          }

	  jet_fat_n = jets_CA.size();
	  int num_filt_jets = 0;
	  for ( int k = 0; k < jet_fat_n; k++ ) {					// Final-state CA jets
	    // apply smearing
	    //random_device rd;
            //mt19937 e2(rd());                                                           // random generator
	    //mt19937 e3(rd());								// second random value for smearing mass - is e3 ok? 
	    std::default_random_engine e3;
	    std::default_random_engine e7;
            std::normal_distribution<double> dist(0, 0.05);						// picked 5% smearing on jet mass and pT, both should be checked. See 1306.4945.
	    float smear_factor_pt = 1. + dist(e3);
	    float smear_factor_m = 1. + dist(e7);
	    //float fj_pT_unsmeared = jets_CA[k].perp();
	    //float fj_pT_smeared = fj_pT_unsmeared * smear_factor_pt;
	    //float fj_m_unsmeared = jets_CA[k].m();
	    //float fj_m_smeared = fj_m_unsmeared * smear_factor_m;
	    // Fill the vector of fat jets before filtering applied
	    jet_fat_pt_v.push_back( jets_CA[k].perp() * smear_factor_pt ); 
            jet_fat_E_v.push_back( jets_CA[k].E() );
            jet_fat_eta_v.push_back( jets_CA[k].eta() );
            jet_fat_phi_v.push_back( jets_CA[k].phi() );
            jet_fat_m_v.push_back( jets_CA[k].m()*smear_factor_m );

	    // Apply mass-drop tagging
	    fastjet::PseudoJet tagged_jet = tagger(jets_CA[k]);				// Checks all input CA jets for passing mu, y_cut values, tags 0 if fails
	    if (tagged_jet != 0) {
	      num_filt_jets++;
	      double this_mu = tagged_jet.structure_of<fastjet::MassDropTagger>().mu();		// The calculated value of mu measured against the set value
	      double this_y = tagged_jet.structure_of<fastjet::MassDropTagger>().y();		// Same for y
	      tagged_pieces = tagged_jet.pieces();						// Obtain the two pieces of the jet
	      //cout << "First subjet pT is " << tagged_pieces[0].perp() << endl;
	      //cout << "Second subjet pT is " << tagged_pieces[1].perp() << endl;

	      // The new clustering radius comes from the deltaR between the subjets
	      Rfilt = min(0.3, 0.5 * tagged_pieces[0].delta_R(tagged_pieces[1]));
	      //cout << "DeltaR is " << Rfilt << endl;
	      
	      // Apply the filtering (Reclusters the jets using the new Rfilt, keeps only the three hardest subjets)
	      filtered_tagged_jet.clear();
	      fastjet::PseudoJet filtered_tagged_jet = fastjet::Filter(Rfilt, fastjet::SelectorNHardest(3))(tagged_jet);

	      // Fill the vectors of the filtered jets
	      jet_MDF_pt_v.push_back( filtered_tagged_jet.perp() );
              jet_MDF_E_v.push_back( filtered_tagged_jet.E() );
              jet_MDF_eta_v.push_back( filtered_tagged_jet.eta() );
              jet_MDF_phi_v.push_back( filtered_tagged_jet.phi() );
              jet_MDF_m_v.push_back( filtered_tagged_jet.m() );

	    }
  	     //else cout << "jet failed tagging " << endl;
	  }
	  jet_MDF_n = num_filt_jets;

	  // Fill our tree
	  output_tree->Fill();							// Fills tree and clears everything
	  done_p += 1;
	  // Reset all tree variables
	  mc_n = 0;
	  el_n = 0;
	  mu_n = 0;
	  Sum_pt = 0;
	  MET_et = 0;
	  MET_phi = 0;
	  jet_AntiKt4_n = 0;
	  mc_pdgID_v.clear();
	  mc_px_v.clear();
	  mc_py_v.clear();
	  mc_pz_v.clear();
	  mc_pt_v.clear();
	  mc_E_v.clear();
	  mc_m_v.clear();
	  mc_eta_v.clear();
	  mc_phi_v.clear();
          el_px_v.clear();
          el_py_v.clear();
          el_pz_v.clear();
          el_pt_v.clear();
          el_E_v.clear();
	  el_Et_v.clear();
          el_m_v.clear();
          el_eta_v.clear();
          el_phi_v.clear();
	  el_charge_v.clear();
	  mu_px_v.clear();
          mu_py_v.clear();
          mu_pz_v.clear();
          mu_pt_v.clear();
          mu_E_v.clear();
          mu_m_v.clear();
          mu_eta_v.clear();
          mu_phi_v.clear();
	  mu_charge_v.clear();
          ph_px_v.clear();
          ph_py_v.clear();
          ph_pz_v.clear();
          ph_pt_v.clear();
          ph_E_v.clear();
          ph_m_v.clear();
          ph_eta_v.clear();
          ph_phi_v.clear();
	  jet_AntiKt4_E_v.clear();
	  jet_AntiKt4_pt_v.clear();
	  jet_AntiKt4_eta_v.clear();
	  jet_AntiKt4_phi_v.clear();
	  jet_AntiKt4_m_v.clear();
	  jet_fat_E_v.clear();
          jet_fat_pt_v.clear();
          jet_fat_eta_v.clear();
          jet_fat_phi_v.clear();
          jet_fat_m_v.clear();
	  jet_MDF_E_v.clear();
          jet_MDF_pt_v.clear();
          jet_MDF_eta_v.clear();
          jet_MDF_phi_v.clear();
          jet_MDF_m_v.clear();
	  Vertex_x_v.clear();
	  Vertex_y_v.clear();
	  Vertex_z_v.clear();
	  particles.clear();
	  jet_seeds.clear();
	  this_vertex_x = 0;
	  this_vertex_y = 0;
	  this_vertex_z = 0;
	}
	good_E = 1;								
      }


      // Looking though HepMC input for particles
      starts_str = "P";
      if ( line.compare( 0, starts_str.length(), starts_str ) == 0 ){		// Looks for lines with P for particle information
	
	line_tokens.clear();
	stringstream ss(line);
	while( getline(ss, item, delim)) {
	  line_tokens.push_back(item);						// Separates the elements of each particle line
	}

	if (line_tokens.at(8) == '1'){						// Requires final-state particle.
	  mc_n += 1;
	  mc_pdgID_v.push_back( atof(line_tokens.at(2).c_str()) );			// PDG ID number.
	  
	  p_x = atof(line_tokens.at(3).c_str()) ;				// pT and E of particles
	  p_y = atof(line_tokens.at(4).c_str());
	  p_z = atof(line_tokens.at(5).c_str());	  
	  E = atof(line_tokens.at(6).c_str());

	  particles.push_back( fastjet::PseudoJet( p_x, p_y, p_z, E ) );	// Each final-state particle (pre-FastJet) is put into a PseudoJet, this is just a 4-vector containing kinematic information.
	  
	  Vertex_x_v.push_back( this_vertex_x );				
	  Vertex_y_v.push_back( this_vertex_y);
	  Vertex_z_v.push_back( this_vertex_z);

	  // All final-state particles are considered input to the jet clustering algorithm EXCEPT neutrinos, DM and muons + electrons.
	  this_PID_v2 = fabs(atof(line_tokens.at(2).c_str()));
	  if (this_PID_v2 != 12 && this_PID_v2 != 14 && this_PID_v2 != 16 && this_PID_v2 != 9000010 && this_PID_v2 != 11 && this_PID_v2 != 13){
	  //if (this_PID_v2 != 12 && this_PID_v2 != 14 && this_PID_v2 != 16 && this_PID_v2 != 9000010){							// use leptons to seed jets for mono-jet channel
	    jet_seeds.push_back( fastjet::PseudoJet( p_x, p_y, p_z, E ) );
	  }

	}
      }
      
      // Look for vertices
      starts_str = "V";
      if ( line.compare( 0, starts_str.length(), starts_str ) == 0 ){

	line_tokens.clear();
	stringstream ss(line);
	while( getline(ss, item, delim)) {
	  line_tokens.push_back(item);						// Separates vertex line elements
	}

	// Get the vertex information for the upcoming particles:
        this_vertex_x = atof(line_tokens.at(3).c_str() ) ;				
	this_vertex_y = atof(line_tokens.at(4).c_str() ) ;
	this_vertex_z = atof(line_tokens.at(5).c_str() ) ;
      }
    }
  
  cout << "Successfully processed " << event_number - 1 <<  " events in total. Closing." << endl;
  output_tree->Write();
  outfile->Close();
  infile.close();
}
