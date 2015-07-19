# revision 25095
# category Package
# catalog-ctan /language/arabic/arabi
# catalog-date 2011-12-04 22:44:34 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-arabi
Version:	1.1
Release:	11
Summary:	(La)TeX support for Arabic and Farsi, compliant with Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/arabic/arabi
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabi.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the Arabic and Farsi script support for
TeX without the need of any external pre-processor, and in a
way that is compatible with babel. The bi-directional
capability supposes that the user has a TeX engine that knows
the four primitives \beginR, \endR, \beginL and \endL. That is
the case in both the TeX--XeT and e-TeX engines. Arabi will
accept input in several 8-bit encodings, including UTF-8. Arabi
can make use of a wide variety of Arabic and Farsi fonts; PDF
files generated using Arabi may be searched, and text may be
copied from them and pasted elsewhere.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/arabi/arabeyes/ae_almohanad_boldItalitalic.afm
%{_texmfdistdir}/fonts/afm/arabi/arabeyes/ae_almohanad_thin.afm
%{_texmfdistdir}/fonts/afm/arabi/arabeyes/ae_almohanad_xxbold.afm
%{_texmfdistdir}/fonts/enc/dvips/arabi/ararabeyes.enc
%{_texmfdistdir}/fonts/enc/dvips/arabi/ardtpnaskh.enc
%{_texmfdistdir}/fonts/enc/dvips/arabi/ardtpthuluth.enc
%{_texmfdistdir}/fonts/enc/dvips/arabi/armonotype.enc
%{_texmfdistdir}/fonts/enc/dvips/arabi/aromega.enc
%{_texmfdistdir}/fonts/enc/dvips/arabi/arsimplified.enc
%{_texmfdistdir}/fonts/enc/dvips/arabi/arunicode.enc
%{_texmfdistdir}/fonts/enc/dvips/arabi/farsitex.enc
%{_texmfdistdir}/fonts/enc/dvips/arabi/farsiwebencoding.enc
%{_texmfdistdir}/fonts/enc/dvips/arabi/frmonotype.enc
%{_texmfdistdir}/fonts/enc/dvips/arabi/frsimple.enc
%{_texmfdistdir}/fonts/enc/dvips/arabi/frsimplified.enc
%{_texmfdistdir}/fonts/enc/dvips/arabi/frunicode.enc
%{_texmfdistdir}/fonts/map/dvips/arabi/arabi.map
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/ae_almohanad_xxbold.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/ae_alyermook.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/ae_arab.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/ae_tholoth.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aealbattar.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aealmateen.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aealmohanadb.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aealmohanadbolditalic.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aealmothnna.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aealyermook.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aearab.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aecortoba.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aedimnah.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aefurat.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aegranada.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aegraph.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aehani.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aehor.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aekayrawan.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aekhalid.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aemashq.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aemetal.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aenada.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aenagham.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aenice.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aeostorah.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aeouhod.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aepetra.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aerehan.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aesalem.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aeshado.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aesharjah.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aesindibad.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aetarablus.tfm
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes/aetholoth.tfm
%{_texmfdistdir}/fonts/tfm/arabi/farsiweb/homa.tfm
%{_texmfdistdir}/fonts/tfm/arabi/farsiweb/nazli.tfm
%{_texmfdistdir}/fonts/tfm/arabi/farsiweb/nazlib.tfm
%{_texmfdistdir}/fonts/tfm/arabi/farsiweb/nazlibout.tfm
%{_texmfdistdir}/fonts/tfm/arabi/farsiweb/nazliout.tfm
%{_texmfdistdir}/fonts/tfm/arabi/farsiweb/titr.tfm
%{_texmfdistdir}/fonts/tfm/arabi/farsiweb/titrout.tfm
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_albattar.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_almateen.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_almohanad_bold.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_almohanad_boldItalitalic.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_almohanad_thin.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_almohanad_xxbold.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_almothnna.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_alyermook.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_arab.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_cortoba.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_dimnah.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_furat.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_granada.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_graph.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_hani.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_hor.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_kayrawan.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_khalid.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_mashq.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_metal.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_nada.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_nagham.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_nice.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_ostorah.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_ouhod.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_petra.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_rehan.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_salem.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_shado.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_sharjah.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_sindibad.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_tarablus.pfb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes/ae_tholoth.pfb
%{_texmfdistdir}/fonts/type1/arabi/farsiweb/homa.pfb
%{_texmfdistdir}/fonts/type1/arabi/farsiweb/nazli.pfb
%{_texmfdistdir}/fonts/type1/arabi/farsiweb/nazlib.pfb
%{_texmfdistdir}/fonts/type1/arabi/farsiweb/titr.pfb
%{_texmfdistdir}/tex/latex/arabi/8859-6.def
%{_texmfdistdir}/tex/latex/arabi/PPRarabic.sty
%{_texmfdistdir}/tex/latex/arabi/arabi4ht.cfg
%{_texmfdistdir}/tex/latex/arabi/arabic.cfg
%{_texmfdistdir}/tex/latex/arabi/arabic.ldf
%{_texmfdistdir}/tex/latex/arabi/arabicfnt.sty
%{_texmfdistdir}/tex/latex/arabi/arabicore.sty
%{_texmfdistdir}/tex/latex/arabi/arabiftoday.sty
%{_texmfdistdir}/tex/latex/arabi/arabnovowel.sty
%{_texmfdistdir}/tex/latex/arabi/arfonts.sty
%{_texmfdistdir}/tex/latex/arabi/calendrierfpar.sty
%{_texmfdistdir}/tex/latex/arabi/calendrierfpmodified.sty
%{_texmfdistdir}/tex/latex/arabi/cp1256.def
%{_texmfdistdir}/tex/latex/arabi/farsi.ldf
%{_texmfdistdir}/tex/latex/arabi/farsifnt.sty
%{_texmfdistdir}/tex/latex/arabi/fmultico.sty
%{_texmfdistdir}/tex/latex/arabi/fnum.sty
%{_texmfdistdir}/tex/latex/arabi/frfonts.sty
%{_texmfdistdir}/tex/latex/arabi/haparabica.sty
%{_texmfdistdir}/tex/latex/arabi/laeaealbattar.fd
%{_texmfdistdir}/tex/latex/arabi/laeaealmateen.fd
%{_texmfdistdir}/tex/latex/arabi/laeaealmohanadb.fd
%{_texmfdistdir}/tex/latex/arabi/laeaealmothnna.fd
%{_texmfdistdir}/tex/latex/arabi/laeaealyermook.fd
%{_texmfdistdir}/tex/latex/arabi/laeaearab.fd
%{_texmfdistdir}/tex/latex/arabi/laeaecortoba.fd
%{_texmfdistdir}/tex/latex/arabi/laeaedimnah.fd
%{_texmfdistdir}/tex/latex/arabi/laeaefurat.fd
%{_texmfdistdir}/tex/latex/arabi/laeaegranada.fd
%{_texmfdistdir}/tex/latex/arabi/laeaegraph.fd
%{_texmfdistdir}/tex/latex/arabi/laeaehani.fd
%{_texmfdistdir}/tex/latex/arabi/laeaehor.fd
%{_texmfdistdir}/tex/latex/arabi/laeaekayrawan.fd
%{_texmfdistdir}/tex/latex/arabi/laeaekhalid.fd
%{_texmfdistdir}/tex/latex/arabi/laeaemashq.fd
%{_texmfdistdir}/tex/latex/arabi/laeaemetal.fd
%{_texmfdistdir}/tex/latex/arabi/laeaenada.fd
%{_texmfdistdir}/tex/latex/arabi/laeaenagham.fd
%{_texmfdistdir}/tex/latex/arabi/laeaenice.fd
%{_texmfdistdir}/tex/latex/arabi/laeaeostorah.fd
%{_texmfdistdir}/tex/latex/arabi/laeaeouhod.fd
%{_texmfdistdir}/tex/latex/arabi/laeaepetra.fd
%{_texmfdistdir}/tex/latex/arabi/laeaerehan.fd
%{_texmfdistdir}/tex/latex/arabi/laeaesalem.fd
%{_texmfdistdir}/tex/latex/arabi/laeaeshado.fd
%{_texmfdistdir}/tex/latex/arabi/laeaesharjah.fd
%{_texmfdistdir}/tex/latex/arabi/laeaesindibad.fd
%{_texmfdistdir}/tex/latex/arabi/laeaetarablus.fd
%{_texmfdistdir}/tex/latex/arabi/laeaetholoth.fd
%{_texmfdistdir}/tex/latex/arabi/laeandlso.fd
%{_texmfdistdir}/tex/latex/arabi/laeararial.fd
%{_texmfdistdir}/tex/latex/arabi/laearcour.fd
%{_texmfdistdir}/tex/latex/arabi/laearomega.fd
%{_texmfdistdir}/tex/latex/arabi/laearsimpo.fd
%{_texmfdistdir}/tex/latex/arabi/laeartimes.fd
%{_texmfdistdir}/tex/latex/arabi/laeasv.fd
%{_texmfdistdir}/tex/latex/arabi/laecmr.fd
%{_texmfdistdir}/tex/latex/arabi/laecmss.fd
%{_texmfdistdir}/tex/latex/arabi/laecmtt.fd
%{_texmfdistdir}/tex/latex/arabi/laedthuluth.fd
%{_texmfdistdir}/tex/latex/arabi/laedtpn.fd
%{_texmfdistdir}/tex/latex/arabi/laedtpnsp.fd
%{_texmfdistdir}/tex/latex/arabi/laeenc.def
%{_texmfdistdir}/tex/latex/arabi/laeenc.dfu
%{_texmfdistdir}/tex/latex/arabi/laekacstbook.fd
%{_texmfdistdir}/tex/latex/arabi/laemaghribi.fd
%{_texmfdistdir}/tex/latex/arabi/laenaskhi.fd
%{_texmfdistdir}/tex/latex/arabi/laereqaa.fd
%{_texmfdistdir}/tex/latex/arabi/laetraditionalarabic.fd
%{_texmfdistdir}/tex/latex/arabi/lagally.sty
%{_texmfdistdir}/tex/latex/arabi/lfecmr.fd
%{_texmfdistdir}/tex/latex/arabi/lfecmss.fd
%{_texmfdistdir}/tex/latex/arabi/lfecmtt.fd
%{_texmfdistdir}/tex/latex/arabi/lfeelham.fd
%{_texmfdistdir}/tex/latex/arabi/lfeenc.def
%{_texmfdistdir}/tex/latex/arabi/lfefandlso.fd
%{_texmfdistdir}/tex/latex/arabi/lfefarsismpl.fd
%{_texmfdistdir}/tex/latex/arabi/lfefrarial.fd
%{_texmfdistdir}/tex/latex/arabi/lfefrtimes.fd
%{_texmfdistdir}/tex/latex/arabi/lfeftraditionalarabic.fd
%{_texmfdistdir}/tex/latex/arabi/lfehoma.fd
%{_texmfdistdir}/tex/latex/arabi/lfekoodak.fd
%{_texmfdistdir}/tex/latex/arabi/lfenazli.fd
%{_texmfdistdir}/tex/latex/arabi/lfenazliout.fd
%{_texmfdistdir}/tex/latex/arabi/lferoya.fd
%{_texmfdistdir}/tex/latex/arabi/lfesmplarabic.fd
%{_texmfdistdir}/tex/latex/arabi/lfeterafik.fd
%{_texmfdistdir}/tex/latex/arabi/lfetitr.fd
%{_texmfdistdir}/tex/latex/arabi/lfetitrout.fd
%{_texmfdistdir}/tex/latex/arabi/mosq.def
%{_texmfdistdir}/tex/latex/arabi/poetry.sty
%{_texmfdistdir}/tex/latex/arabi/puenc-ar.def
%{_texmfdistdir}/tex/latex/arabi/transcmr.fd
%{_texmfdistdir}/tex/latex/arabi/translit.sty
%doc %{_texmfdistdir}/doc/latex/arabi/README
%doc %{_texmfdistdir}/doc/latex/arabi/bblopts.cfg
%doc %{_texmfdistdir}/doc/latex/arabi/big2.pdf
%doc %{_texmfdistdir}/doc/latex/arabi/big2.tex
%doc %{_texmfdistdir}/doc/latex/arabi/fontchart_arabic.pdf
%doc %{_texmfdistdir}/doc/latex/arabi/fontchart_farsi.pdf
%doc %{_texmfdistdir}/doc/latex/arabi/lion.pdf
%doc %{_texmfdistdir}/doc/latex/arabi/lppl.tex
%doc %{_texmfdistdir}/doc/latex/arabi/samplebook.css
%doc %{_texmfdistdir}/doc/latex/arabi/samplebook.html
%doc %{_texmfdistdir}/doc/latex/arabi/samplebook.pdf
%doc %{_texmfdistdir}/doc/latex/arabi/samplebook.tex
%doc %{_texmfdistdir}/doc/latex/arabi/test_beamer.pdf
%doc %{_texmfdistdir}/doc/latex/arabi/testplaintex.pdf
%doc %{_texmfdistdir}/doc/latex/arabi/testplaintex.tex
%doc %{_texmfdistdir}/doc/latex/arabi/user_guide.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-3
+ Revision: 762528
- Update to latest upstream package

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 749290
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 717847
- texlive-arabi
- texlive-arabi
- texlive-arabi
- texlive-arabi
- texlive-arabi

