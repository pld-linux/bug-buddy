Summary:	Utility to ease the reporting of bugs within the GNOME
Summary(pl):	Narz�dzie u�atwiaj�ce zg�aszanie b��d�w w �rodowisku GNOME
Name:		bug-buddy
Version:	2.5.90
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	f57c8e240f00fed51b1759beb5c58e1e
Source1:	%{name}-en_CA.po
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.3.1
BuildRequires:	gtk+2-devel >= 2.3.1
BuildRequires:	gnome-desktop-devel >= 2.5.90
BuildRequires:	gnome-vfs2-devel >= 2.5.3
BuildRequires:	intltool >= 0.29
BuildRequires:	libglade2-devel >= 2.3.1
BuildRequires:	libgnomeui-devel >= 2.5.90
BuildRequires:	libxml2-devel >= 2.4.6
BuildRequires:	scrollkeeper >= 0.3.8
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bug-buddy is a druid based tool which steps you through the GNOME bug
submission process. It can automatically obtain stack traces from core
files or crashed applications. Debian and KDE bug tracking systems are
also supported.

%description -l pl
bug-budy jest narz�dziem przeprowadzaj�cym Ci� przez proces sk�adania
raportu o b��dzie w �rodowisku GNOME. Potrafi on automatycznie uzyska�
�lady ze stosu (backtrace) z plik�w core lub wywracaj�cych si�
aplikacji. Wspierane s� r�wnie� systemy obs�ugi b��d�w Debiana oraz
KDE.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po
install %{SOURCE1} po/en_CA.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install

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
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO docs/multiple_bts.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/application-registry/*
%{_datadir}/%{name}
%{_datadir}/mime-info/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/*
%{_sysconfdir}/gconf/schemas/*
