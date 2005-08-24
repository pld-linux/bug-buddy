Summary:	Utility to ease the reporting of bugs within the GNOME
Summary(pl):	Narzêdzie u³atwiaj±ce zg³aszanie b³êdów w ¶rodowisku GNOME
Name:		bug-buddy
Version:	2.11.92
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/bug-buddy/2.11/%{name}-%{version}.tar.bz2
# Source0-md5:	fd6affcdb1a205b2acfc866eb4844c4a
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.11.90-2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.10.0-2
BuildRequires:	gnome-doc-utils >= 0.3.1
BuildRequires:	gnome-menus-devel >= 2.10.1
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	libxslt-progs >= 1.1.14
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.8
Requires(post,preun):	GConf2 >= 2.10.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bug-buddy is a druid based tool which steps you through the GNOME bug
submission process. It can automatically obtain stack traces from core
files or crashed applications. Debian and KDE bug tracking systems are
also supported.

%description -l pl
bug-budy jest narzêdziem przeprowadzaj±cym Ciê przez proces sk³adania
raportu o b³êdzie w ¶rodowisku GNOME. Potrafi on automatycznie uzyskaæ
¶lady ze stosu (backtrace) z plików core lub wywracaj±cych siê
aplikacji. Wspierane s± równie¿ systemy obs³ugi b³êdów Debiana oraz
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no
rm -r $RPM_BUILD_ROOT%{_datadir}/{application-registry,mime-info}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install bug-buddy.schemas
%scrollkeeper_update_post
%update_desktop_database_post

%preun
%gconf_schema_uninstall bug-buddy.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO docs/multiple_bts.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_mandir}/man1/*
%{_omf_dest_dir}/*
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/bug-buddy.schemas
