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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides tools to help manage anonymous work with BibLaTeX.
It will be useful, for example, in history or classical philology.

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
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-anonymous
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-anonymous
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-anonymous/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-anonymous/biblatex-anonymous.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-anonymous/biblatex-anonymous.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-anonymous/latexmkrc
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-anonymous/makefile
%{_datadir}/texmf-dist/tex/latex/biblatex-anonymous/biblatex-anonymous.sty
