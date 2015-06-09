#include <TColor.h>
#include <TLatex.h>
#include <cmath>

void graph_couplings() {
   
   TCanvas *c1 = new TCanvas("c1","coupling_limits",200,10,700,600);
   gPad->SetLeftMargin(0.13);
   gPad->SetRightMargin(0.2);           // measured from the right-hand side... 
   //gPad->SetGridx(1);  
   //gPad->SetGridy(1); 

   //TPad* p1 = new TPad("p1","p1",0.1,0.5,0.9,0.9,0); 
   //p1->Draw();

   TGraph2D *gr1 = new TGraph2D("text_graphs/couplinglimits_TSD_1.txt");
   //TGraphErrors *gr2 = new TGraphErrors("text_graphs/limits_SVD_Med1200_1.txt");

   TString xAxTitle = TString("m_{#chi} [GeV]");
   TString yAxTitle = TString("m_{med} [GeV]");
   TString zAxTitle = TString("upper limit on #sqrt{g_{q} g_{DM}}");

   gr1->SetTitle("");
   gr1->GetHistogram()->GetXaxis()->SetTitle(xAxTitle);
   gr1->GetHistogram()->GetYaxis()->SetTitle(yAxTitle);
   gr1->GetHistogram()->GetZaxis()->SetTitle(zAxTitle);
   gr1->GetXaxis()->CenterTitle();
   gr1->GetYaxis()->CenterTitle();
   gr1->GetZaxis()->CenterTitle();
   gr1->GetXaxis()->SetTitleOffset(1.2);
   gr1->GetYaxis()->SetTitleOffset(1.5);
   gr1->GetZaxis()->SetTitleOffset(1.5);   

   gr1->GetXaxis()->SetLimits(0., 1400.);
   gr1->GetYaxis()->SetLimits(0., 1400.);
   gr1->GetZaxis()->SetRangeUser(0., 12.56);


   //gr1->SetLineColor(kOrange+7);
   //gr1->SetLineWidth(2);
   //gr1->SetMarkerColor(kOrange+7);
   //gr1->SetMarkerStyle(21);

   const Int_t NRGBs = 6;
   const Int_t NCont = 999;

   Double_t stops[NRGBs] = { 0.00, 0.1, 0.34, 0.61, 0.84, 1.00 };
   Double_t red[NRGBs]   = { 0.99, 0.0, 0.00, 0.87, 1.00, 0.51 };
   Double_t green[NRGBs] = { 0.00, 0.0, 0.81, 1.00, 0.20, 0.00 };
   Double_t blue[NRGBs]  = { 0.99, 0.0, 1.00, 0.12, 0.00, 0.00 };

   TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
   gStyle->SetNumberContours(NCont);

   //h->GetZaxis()->SetRangeUser(min, max)

   Double_t contours[] = {0.2, 0.4, 0.6, 0.8, 1, 2, 4, 6, 8, 12.56, 20};
   gr1->GetHistogram()->SetContour(10,contours);

   //p1->cd();
   gr1->Draw("cont4z");
   // TCanvas::Update() draws the frame, after which one can change it
   c1->Update();

   TLegend* l = new TLegend(.55, .70, .89, .85);
   l->SetTextSize(0.035);
   l->SetTextFont(42);
   l->SetBorderSize(0);
   l->AddEntry(gr1,"m_{med} = 1000 GeV","l");
   //l->AddEntry(gr2,"m_{med} = 1200 GeV","l");
   l->SetFillColor(0);
   //l->Draw();

   //t21 = new TText(0.05,0.8,"This is pad21");
   //t21->SetTextSize(0.1);
   //t21->Draw("same");

   TLatex line;
   line.SetTextSize(0.03);
   line.SetTextFont(42);
   line.SetNDC();		// lets coordinates be relative to canvas, not to pad
   //line.SetTextAngle(30.);
   //line.DrawLatex(0.6, 0.8, "#sqrt{s} = 8 TeV");
   //line.DrawLatex(0.6, 0.74, "g_{q}/g_{DM} = 1");
   //line.DrawLatex(0.6, 0.65, "#int L dt = 20.3 fb^{-1}");

   line.DrawLatex(0.6, 0.4, "#sqrt{s} = 8 TeV");
   line.DrawLatex(0.6, 0.34, "g_{q}/g_{DM} = 1");
   line.DrawLatex(0.6, 0.25, "#int L dt = 20.3 fb^{-1}");

   //for (int i=0; i<n1; i++) {
   //   l.DrawLatex(x1[i],y1[i],Form("(%g,%g)",x1[i],y1[i]));
   //   l.DrawLatex(x2[i],y2[i],Form("(%g,%g)",x2[i],y2[i]));
   //}

   c1->Modified();
   c1->SaveAs("coupling_limits_TSD_1.pdf");
}

