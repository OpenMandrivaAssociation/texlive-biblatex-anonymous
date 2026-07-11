%global tl_name biblatex-anonymous
%global tl_revision 48548

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.6.2
Release:	%{tl_revision}.1
Summary:	A tool to manage anonymous work with BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-anonymous
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-anonymous.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-anonymous.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides tools to help manage anonymous work with BibLaTeX.
It will be useful, for example, in history or classical philology.

