Name:		texlive-arabi
Version:	44662
Release:	2
Summary:	(La)TeX support for Arabic and Farsi, compliant with Babel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/arabic/arabi
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabi.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/afm/arabi/arabeyes
%{_texmfdistdir}/fonts/enc/dvips/arabi
%{_texmfdistdir}/fonts/map/dvips/arabi
%{_texmfdistdir}/fonts/tfm/arabi/arabeyes
%{_texmfdistdir}/fonts/tfm/arabi/farsiweb
%{_texmfdistdir}/fonts/type1/arabi/arabeyes
%{_texmfdistdir}/fonts/type1/arabi/farsiweb
%{_texmfdistdir}/tex/latex/arabi
%doc %{_texmfdistdir}/doc/latex/arabi

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
