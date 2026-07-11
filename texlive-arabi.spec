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
BuildSystem:	texlive
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

