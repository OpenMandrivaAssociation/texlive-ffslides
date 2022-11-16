Name:		texlive-ffslides
Version:	38895
Release:	1
Summary:	Freeform slides based on the article class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ffslides
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ffslides.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ffslides.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The ffslides ("freeform slides") class is intended to make it
easier to place various types of content freely on the page,
and therefore easier to design documents with a strong visual
component: presentations, posters, research or lecture notes,
and so on. The goal of the class is to be less rigid and less
complex than some of the popular presentation-making options.
It is essentially a small set of macros added to the article
class. A well-organized template file is included, and the
documentation is itself an extensive example of the class's
capabilities.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ffslides
%doc %{_texmfdistdir}/doc/latex/ffslides

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
