%global tl_name arabi
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	(La)TeX support for Arabic and Farsi, compliant with Babel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/arabic/arabi
License:	lppl1.3b
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabi.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an Arabic and Farsi script support for TeX without
the need of any external pre-processor, and in a way that is compatible
with babel. The bi-directional capability supposes that the user has a
TeX engine that knows the four primitives \beginR, \endR, \beginL and
\endL. That is the case in both the TeX--XeT and e-TeX engines. Arabi
will accept input in several 8-bit encodings, including UTF-8. Arabi can
make use of a wide variety of Arabic and Farsi fonts, and provides one
of its own. PDF files generated using Arabi may be searched, and text
may be copied from them and pasted elsewhere.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/arabi
%dir %{_datadir}/texmf-dist/fonts/afm/arabi
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/arabi
%dir %{_datadir}/texmf-dist/fonts/type1/arabi
%dir %{_datadir}/texmf-dist/tex/latex/arabi
%dir %{_datadir}/texmf-dist/fonts/afm/arabi/arabeyes
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/arabi
%dir %{_datadir}/texmf-dist/fonts/map/dvips/arabi
%dir %{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes
%dir %{_datadir}/texmf-dist/fonts/tfm/arabi/farsiweb
%dir %{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes
%dir %{_datadir}/texmf-dist/fonts/type1/arabi/farsiweb
%doc %{_datadir}/texmf-dist/doc/latex/arabi/README
%doc %{_datadir}/texmf-dist/doc/latex/arabi/bblopts.cfg
%doc %{_datadir}/texmf-dist/doc/latex/arabi/big2.pdf
%doc %{_datadir}/texmf-dist/doc/latex/arabi/big2.tex
%doc %{_datadir}/texmf-dist/doc/latex/arabi/fontchart_arabic.pdf
%doc %{_datadir}/texmf-dist/doc/latex/arabi/fontchart_farsi.pdf
%doc %{_datadir}/texmf-dist/doc/latex/arabi/lion.pdf
%doc %{_datadir}/texmf-dist/doc/latex/arabi/lppl.tex
%doc %{_datadir}/texmf-dist/doc/latex/arabi/samplebook.css
%doc %{_datadir}/texmf-dist/doc/latex/arabi/samplebook.html
%doc %{_datadir}/texmf-dist/doc/latex/arabi/samplebook.pdf
%doc %{_datadir}/texmf-dist/doc/latex/arabi/samplebook.tex
%doc %{_datadir}/texmf-dist/doc/latex/arabi/test_beamer.pdf
%doc %{_datadir}/texmf-dist/doc/latex/arabi/testplaintex.pdf
%doc %{_datadir}/texmf-dist/doc/latex/arabi/testplaintex.tex
%doc %{_datadir}/texmf-dist/doc/latex/arabi/user_guide.pdf
%{_datadir}/texmf-dist/fonts/afm/arabi/arabeyes/ae_almohanad_boldItalitalic.afm
%{_datadir}/texmf-dist/fonts/afm/arabi/arabeyes/ae_almohanad_thin.afm
%{_datadir}/texmf-dist/fonts/afm/arabi/arabeyes/ae_almohanad_xxbold.afm
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/ararabeyes.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/ardtpnaskh.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/ardtpthuluth.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/armonotype.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/aromega.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/arsimplified.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/arunicode.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/farsitex.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/farsiwebencoding.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/frmonotype.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/frsimple.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/frsimplified.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arabi/frunicode.enc
%{_datadir}/texmf-dist/fonts/map/dvips/arabi/arabi.map
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/ae_almohanad_xxbold.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/ae_alyermook.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/ae_arab.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/ae_tholoth.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aealbattar.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aealmateen.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aealmohanadb.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aealmohanadbolditalic.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aealmothnna.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aealyermook.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aearab.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aecortoba.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aedimnah.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aefurat.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aegranada.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aegraph.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aehani.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aehor.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aekayrawan.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aekhalid.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aemashq.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aemetal.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aenada.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aenagham.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aenice.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aeostorah.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aeouhod.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aepetra.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aerehan.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aesalem.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aeshado.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aesharjah.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aesindibad.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aetarablus.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/arabeyes/aetholoth.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/farsiweb/homa.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/farsiweb/nazli.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/farsiweb/nazlib.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/farsiweb/nazlibout.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/farsiweb/nazliout.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/farsiweb/titr.tfm
%{_datadir}/texmf-dist/fonts/tfm/arabi/farsiweb/titrout.tfm
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_albattar.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almateen.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_bold.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_boldItalitalic.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_thin.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almohanad_xxbold.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_almothnna.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_alyermook.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_arab.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_cortoba.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_dimnah.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_furat.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_granada.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_graph.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_hani.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_hor.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_kayrawan.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_khalid.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_mashq.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_metal.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_nada.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_nagham.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_nice.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_ostorah.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_ouhod.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_petra.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_rehan.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_salem.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_shado.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_sharjah.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_sindibad.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_tarablus.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/arabeyes/ae_tholoth.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/farsiweb/homa.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/farsiweb/nazli.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/farsiweb/nazlib.pfb
%{_datadir}/texmf-dist/fonts/type1/arabi/farsiweb/titr.pfb
%{_datadir}/texmf-dist/tex/latex/arabi/8859-6.def
%{_datadir}/texmf-dist/tex/latex/arabi/PPRarabic.sty
%{_datadir}/texmf-dist/tex/latex/arabi/arabi4ht.cfg
%{_datadir}/texmf-dist/tex/latex/arabi/arabic.cfg
%{_datadir}/texmf-dist/tex/latex/arabi/arabic.ldf
%{_datadir}/texmf-dist/tex/latex/arabi/arabicfnt.sty
%{_datadir}/texmf-dist/tex/latex/arabi/arabicore.sty
%{_datadir}/texmf-dist/tex/latex/arabi/arabiftoday.sty
%{_datadir}/texmf-dist/tex/latex/arabi/arabipoetry.sty
%{_datadir}/texmf-dist/tex/latex/arabi/arabnovowel.sty
%{_datadir}/texmf-dist/tex/latex/arabi/arfonts.sty
%{_datadir}/texmf-dist/tex/latex/arabi/calendrierfpar.sty
%{_datadir}/texmf-dist/tex/latex/arabi/calendrierfpmodified.sty
%{_datadir}/texmf-dist/tex/latex/arabi/cp1256.def
%{_datadir}/texmf-dist/tex/latex/arabi/farsi.ldf
%{_datadir}/texmf-dist/tex/latex/arabi/farsifnt.sty
%{_datadir}/texmf-dist/tex/latex/arabi/fmultico.sty
%{_datadir}/texmf-dist/tex/latex/arabi/fnum.sty
%{_datadir}/texmf-dist/tex/latex/arabi/frfonts.sty
%{_datadir}/texmf-dist/tex/latex/arabi/haparabica.sty
%{_datadir}/texmf-dist/tex/latex/arabi/laeaealbattar.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaealmateen.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaealmohanadb.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaealmothnna.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaealyermook.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaearab.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaecortoba.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaedimnah.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaefurat.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaegranada.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaegraph.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaehani.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaehor.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaekayrawan.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaekhalid.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaemashq.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaemetal.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaenada.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaenagham.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaenice.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaeostorah.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaeouhod.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaepetra.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaerehan.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaesalem.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaeshado.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaesharjah.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaesindibad.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaetarablus.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeaetholoth.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeandlso.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeararial.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laearcour.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laearomega.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laearsimpo.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeartimes.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeasv.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laecmr.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laecmss.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laecmtt.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laedthuluth.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laedtpn.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laedtpnsp.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laeenc.def
%{_datadir}/texmf-dist/tex/latex/arabi/laeenc.dfu
%{_datadir}/texmf-dist/tex/latex/arabi/laekacstbook.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laemaghribi.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laenaskhi.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laereqaa.fd
%{_datadir}/texmf-dist/tex/latex/arabi/laetraditionalarabic.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lagally.sty
%{_datadir}/texmf-dist/tex/latex/arabi/lfecmr.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfecmss.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfecmtt.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfeelham.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfeenc.def
%{_datadir}/texmf-dist/tex/latex/arabi/lfefandlso.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfefarsismpl.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfefrarial.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfefrtimes.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfeftraditionalarabic.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfehoma.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfekoodak.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfenazli.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfenazliout.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lferoya.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfesmplarabic.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfeterafik.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfetitr.fd
%{_datadir}/texmf-dist/tex/latex/arabi/lfetitrout.fd
%{_datadir}/texmf-dist/tex/latex/arabi/mosq.def
%{_datadir}/texmf-dist/tex/latex/arabi/puenc-ar.def
%{_datadir}/texmf-dist/tex/latex/arabi/transcmr.fd
%{_datadir}/texmf-dist/tex/latex/arabi/translit.sty
