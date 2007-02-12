Summary:	hypersrc is a GUI program for browsing source code
Summary(pl.UTF-8):   Program GUI do przeglądania kodu źródłowego
Name:		hypersrc
Version:	5.4.20
Release:	0.1
License:	GPL v2
Group:		X11/Development/Tools
Source0:	ftp://ftp.jimbrooks.org/hypersrc/latest/%{name}-%{version}.tar.gz
# Source0-md5:	5ef719a9bda943e69f92172bb8013627
URL:		http://www.jimbrooks.org/web/hypersrc/hypersrc.php
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	libart_lgpl-devel
Requires:	ctags >= 4.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hypersrc is a GUI program for browsing source code, built with GTK+.
It provides a list widget containing sorted source code tags. A
programmer can click a tag to hyperlink to a particular tagged line in
a source code file.

%description -l pl.UTF-8
hypersrc to program z graficznym interfejsem użytkownika w GTK+ do
przeglądania kodu źródłowego. Daje widget z listą zawierającą
posortowane tagi ze źródeł. Programista może kliknąć na tag, aby
przejść do otagowanej linii w pliku z kodem źródłowym.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}"
# TODO: optflags

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT{%{_libdir}/hypersrc,%{_mandir}/man1}
install ctags.pl $RPM_BUILD_ROOT%{_libdir}/hypersrc
install Hypersrc.pl $RPM_BUILD_ROOT%{_bindir}/Hypersrc
install hypersrc.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/*
%{_libdir}/hypersrc
%{_mandir}/man1/hypersrc.1.*
