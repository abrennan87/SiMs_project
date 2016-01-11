#include <TColor.h>

void graph_variedMedmass() {
   
   TCanvas *c1 = new TCanvas("c1","sigma_limits_variedMedmass",200,10,700,500);
   c1->SetLogx();

   TGraphErrors *gr1 = new TGraphErrors("text_graphs/limits_SVD_DM10_min_rat1.txt");
   TGraphErrors *gr2 = new TGraphErrors("text_graphs/limits_SVD_DM200_min_rat1.txt");
   TGraphErrors *gr3 = new TGraphErrors("text_graphs/limits_SVD_DM400_min_rat1.txt");
   TGraphErrors *gr4 = new TGraphErrors("text_graphs/limits_SVD_DM1000_min_rat1.txt");

   TString xAxTitle = TString("m_{med} [GeV]");
   TString yAxTitle = TString("#sigma(pp #rightarrow Z#chi#chi) #times BR(Z #rightarrow l+l-) [fb]");

   gr1->SetTitle("");
   gr1->GetXaxis()->SetTitle(xAxTitle);
   gr1->GetYaxis()->SetTitle(yAxTitle);
   gr1->GetYaxis()->SetTitleOffset(1.2);
   gr1->GetXaxis()->SetTitleOffset(1.2);
   //gr1->GetXaxis()->SetLimits(1000., 1200.);
   gr1->SetMinimum(0);
   gr1->SetMaximum(40);

   gr1->SetLineColor(kOrange+7);
   gr1->SetLineWidth(2);
   gr1->SetMarkerColor(kOrange+7);
   gr1->SetMarkerStyle(21);

   gr2->SetLineColor(kBlue-7);
   gr2->SetLineWidth(2);
   gr2->SetMarkerColor(kBlue-7);
   gr2->SetMarkerStyle(22); 

   gr3->SetLineColor(kMagenta+3);
   gr3->SetLineWidth(2);
   gr3->SetMarkerColor(kMagenta+3);
   gr3->SetMarkerStyle(22);

   gr4->SetLineColor(kGreen+2);
   gr4->SetLineWidth(2);
   gr4->SetMarkerColor(kGreen+2);
   gr4->SetMarkerStyle(22);  

   gr1->Draw("AP");
   gr2->Draw("same P");
   gr3->Draw("same P");
   gr4->Draw("same P");

   // TCanvas::Update() draws the frame, after which one can change it
   c1->Update();

   TLegend* l = new TLegend(.55, .70, .89, .85);
   l->SetTextSize(0.035);
   l->SetTextFont(42);
   l->SetBorderSize(0);
   l->AddEntry(gr1,"m_{#chi} = 10 GeV","l");
   l->AddEntry(gr2,"m_{#chi} = 200 GeV","l");
   l->AddEntry(gr3,"m_{#chi} = 400 GeV","l");
   l->AddEntry(gr4,"m_{#chi} = 1000 GeV","l");
   l->SetFillColor(0);
   l->Draw();

   c1->Modified();
   c1->SaveAs("sigma_limits_variedMedmass_SVD_min_rat1.pdf");
}

