Summary:	Utility to ease the reporting of bugs within the GNOME
Summary(pl):	Narz�dzie u�atwiaj�ce zg�aszanie b��d�w w �rodowisku GNOME
Name:		bug-buddy
Version:	2.10.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/bug-buddy/2.10/%{name}-%{version}.tar.bz2
# Source0-md5:	c821a933f3d7be64071c7bfcb07ee1ac
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-desktop-devel >= 2.10.0-2
BuildRequires:	gnome-menus-devel >= 2.10.1
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libxml2-devel >= 1:2.6.19
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
bug-budy jest narz�dziem przeprowadzaj�cym Ci� przez proces sk�adania
raportu o b��dzie w �rodowisku GNOME. Potrafi on automatycznie uzyska�
�lady ze stosu (backtrace) z plik�w core lub wywracaj�cych si�
aplikacji. Wspierane s� r�wnie� systemy obs�ugi b��d�w Debiana oraz
KDE.

%prep
%setup -q
%patch0 -p1

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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no
rm -r $RPM_BUILD_ROOT%{_datadir}/{application-registry,mime-info}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install /etc/gconf/schemas/bug-buddy.schemas
/usr/bin/scrollkeeper-update -q
/usr/bin/update-desktop-database

%preun
if [ $1 = 0 ]; then
	%gconf_schema_uninstall /etc/gconf/schemas/bug-buddy.schemas
fi

%postun
if [ $1 = 0 ]; then
	/usr/bin/scrollkeeper-update -q
	/usr/bin/update-desktop-database
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO docs/multiple_bts.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/*
%{_sysconfdir}/gconf/schemas/*
