Summary:	hypersrc is a GUI program for browsing source code
Summary(pl):	Program GUI do przegl�dania kodu �r�d�owego
Name:		hypersrc
Version:	4.4.15
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.jimbrooks.org/hypersrc/latest/%{name}-%{version}.tar.gz
Patch0:		installdir.patch
URL:		http://www.jimbrooks.org/web/hypersrc/hypersrc.html 
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	ctags >= 4.0.2
BuildRequires:	gtk+-devel >= 1.2.3

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
hypersrc is a GUI program for browsing source code, built with GTK+.
It provides a list widget containing sorted source code tags. A
programmer can click a tag to hyperlink to a particular tagged line in
a source code file.

%description -l pl
hypersrc to program z graficznym interfejsem u�ytkownika w GTK+ do
przegl�dania kodu �r�d�owego. Daje widget z list� zaieraj�c�
posortowane tagi ze �r�de�. Programista mo�e klikn�� na tag, aby
przej�� do otagowanej linii w pliku z kodem �r�d�owym.

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

gzip -9nf LICENSE.txt README.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt.gz README.txt.gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/hypersrc
