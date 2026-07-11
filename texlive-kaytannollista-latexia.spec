%global tl_name kaytannollista-latexia
%global tl_revision 77555

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2026
Release:	%{tl_revision}.1
Summary:	Practical manual for LaTeX (Finnish)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/kaytannollista-latexia
License:	cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kaytannollista-latexia.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kaytannollista-latexia.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
"Kaytannollista Latexia" is a practical manual for LaTeX written in the
Finnish language. The manual covers most of the topics that a typical
document author needs. So it can be a useful guide for beginners as well
as a reference manual for advanced users.

