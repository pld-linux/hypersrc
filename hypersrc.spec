Summary:	hypersrc is a GUI program for browsing source code
Summary(pl):	Program GUI do przegl±dania kodu ¼ród³owego
Name:		hypersrc
Version:	4.4.15
Release:	0.1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.jimbrooks.org/hypersrc/latest/%{name}-%{version}.tar.gz
# Source0-md5:	8f4fbc8e5228dc34f29b652b82600ea6
Patch0:		installdir.patch
URL:		http://www.jimbrooks.org/web/hypersrc/hypersrc.html
BuildRequires:	gtk+-devel >= 1.2.3
Requires:	ctags >= 4.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hypersrc is a GUI program for browsing source code, built with GTK+.
It provides a list widget containing sorted source code tags. A
programmer can click a tag to hyperlink to a particular tagged line in
a source code file.

%description -l pl
hypersrc to program z graficznym interfejsem u¿ytkownika w GTK+ do
przegl±dania kodu ¼ród³owego. Daje widget z list± zawieraj±c±
posortowane tagi ze ¼róde³. Programista mo¿e klikn±æ na tag, aby
przej¶æ do otagowanej linii w pliku z kodem ¼ród³owym.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make}
# TODO: optflags

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_bindir}

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
%doc README.txt
%attr(755,root,root) %{_bindir}/*
%{_libdir}/hypersrc
