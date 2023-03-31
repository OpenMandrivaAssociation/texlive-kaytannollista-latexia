Name:		texlive-kaytannollista-latexia
Version:	64278
Release:	2
Summary:	Practical manual for LaTeX (Finnish)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kaytannollista-latexia
License:	cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kaytannollista-latexia.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kaytannollista-latexia.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
"Kaytannollista Latexia" is a practical manual for LaTeX
written in the Finnish language. The manual covers most of the
topics that a typical document author needs. So it can be a
useful guide for beginners as well as a reference manual for
advanced users.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/kaytannollista-latexia

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
