Name:		texlive-biblatex-anonymous
Version:	48548
Release:	2
Summary:	A tool to manage anonymous work with BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-anonymous
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-anonymous.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-anonymous.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides tools to help manage anonymous work with
BibLaTeX. It will be useful, for example, in history or
classical philology.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-anonymous
%doc %{_texmfdistdir}/doc/latex/biblatex-anonymous

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
