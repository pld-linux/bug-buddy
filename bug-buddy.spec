Summary:	Utility to ease the reporting of bugs within the GNOME
Summary(pl):	Narzêdzie u³atwiaj±ce zg³aszanie b³êdów w ¶rodowisku GNOME
Name:		bug-buddy
Version:	2.7.91
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	54b0d38bd247004022e84e5a61f5e129
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.7.91
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	gnome-desktop-devel >= 2.7.91
BuildRequires:	gnome-vfs2-devel >= 2.7.91
BuildRequires:	intltool >= 0.29
BuildRequires:	libglade2-devel >= 1:2.3.6
BuildRequires:	libgnomeui-devel >= 2.7.91
BuildRequires:	libxml2-devel >= 2.4.6
BuildRequires:	scrollkeeper >= 0.3.8
Requires(post):	GConf2 >= 2.7.91
Requires(post):	scrollkeeper
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

rm po/no.po

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
