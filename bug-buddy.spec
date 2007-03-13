Summary:	Utility to ease the reporting of bugs within the GNOME
Summary(pl.UTF-8):	Narzędzie ułatwiające zgłaszanie błędów w środowisku GNOME
Name:		bug-buddy
Version:	2.18.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/bug-buddy/2.18/%{name}-%{version}.tar.bz2
# Source0-md5:	3b3d99f2450f300d73a201bc5c00498d
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.18.0.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.10.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.18.0
BuildRequires:	gnome-doc-utils >= 0.10.1
BuildRequires:	gnome-menus-devel >= 2.17.92
BuildRequires:	gnome-vfs2-devel >= 2.18.0.1
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.18.0
BuildRequires:	libgtop-devel >= 2.14.8
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	libxslt-progs >= 1.1.20
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.8
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	libgnomeui >= 2.18.0
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
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__gnome_doc_common}
%{__aclocal}
%{__autoconf}
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

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install bug-buddy.schemas
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall bug-buddy.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/bug-buddy.png
%{_sysconfdir}/gconf/schemas/bug-buddy.schemas
