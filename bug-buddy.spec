Summary:	Utility to ease the reporting of bugs within the GNOME
Summary(pl.UTF-8):	Narzędzie ułatwiające zgłaszanie błędów w środowisku GNOME
Name:		bug-buddy
Version:	2.32.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/bug-buddy/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	86a84389c206396eba680e93288d04c8
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	elfutils-devel
BuildRequires:	evolution-data-server-devel >= 2.26.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	libbonobo-devel >= 2.24.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgtop-devel >= 2.14.8
BuildRequires:	libsoup-devel >= 2.26.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.8
BuildRequires:	sed >= 4.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	gtk+2 >= 2:2.16.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bug-buddy is a druid based tool which steps you through the GNOME bug
submission process. It can automatically obtain stack traces from core
files or crashed applications. Debian and KDE bug tracking systems are
also supported.

%description -l pl.UTF-8
bug-budy jest narzędziem przeprowadzającym Cię przez proces składania
raportu o błędzie w środowisku GNOME. Potrafi on automatycznie uzyskać
ślady ze stosu (backtrace) z plików core lub wywracających się
aplikacji. Wspierane są również systemy obsługi błędów Debiana oraz
KDE.

%prep
%setup -q

sed -i -e 's/^en@shaw//' po/LINGUAS
rm -f po/en@shaw.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__gnome_doc_common}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/libgnomesegvhandler.la

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install bug-buddy.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall bug-buddy.schemas

%postun
/sbin/ldconfig
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/bug-buddy
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libgnomesegvhandler.so
%{_datadir}/%{name}
%{_desktopdir}/bug-buddy.desktop
%{_iconsdir}/hicolor/*/*/bug-buddy.png
%{_iconsdir}/hicolor/*/*/bug-buddy.svg
%{_sysconfdir}/gconf/schemas/bug-buddy.schemas
%{_mandir}/man1/*.1*
