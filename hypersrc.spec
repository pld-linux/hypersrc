Name:		hypersrc
Version:	2.1.6
Release:	1
Summary:	hypersrc is a GUI program for browsing source code 
License:	GPL
Group:		Development
Group(de):	Entwicklung
Group(pl):	Programowanie
Source0:	ftp://ftp.jimbrooks.org/hypersrc/%{name}-%{version}.tar.gz
Patch0:		installdir.patch
URL:		http://www.jimbrooks.org/web/hypersrc/hypersrc.html 
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	ctags >= 4.0.2
Requires:	gtk+ >= 1.2.3

%description
hypersrc is a GUI program for browsing source code, built with GTK+.
It provides a list widget containing sorted source code tags. A
programmer can click a tag to hyperlink to a particular tagged line in
a source code file.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} INSTALL_DIR=$RPM_BUILD_ROOT%{_bindir} install


sed -e "s|/var/tmp/hypersrc-root%{_bindir}/hypersrc|%{_libdir}/hypersrc/hypersrc|; \
    s|/var/tmp/hypersrc-root%{_bindir}/ctags.pl|%{_libdir}/hypersrc/ctags.pl|; \
    s|/var/tmp/hypersrc-root%{_bindir}/ctags|%{_bindir}/ctags|" Hypersrc.pl >> Hypersrc.pl.new

install -d $RPM_BUILD_ROOT%{_libdir}/hypersrc
install ctags.pl $RPM_BUILD_ROOT%{_libdir}/hypersrc 
install Hypersrc.pl.new $RPM_BUILD_ROOT%{_bindir}/Hypersrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt 
%attr(755,root,root) %{_bindir}/*
%{_libdir}/hypersrc
