Summary:	Utility to ease the reporting of bugs within the GNOME
Summary(pl):	Narzêdzie u³atwiaj±ce zg³aszanie b³êdów w ¶rodowisku GNOME
Name:		bug-buddy
Version:	2.3.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	a6b03f8b4393a60654e137c45aa5d55c
URL:		http://www.gnome.org/
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	libglade2-devel
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libxml2-devel
BuildRequires:	scrollkeeper
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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO docs/multiple_bts.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/application-registry/*
%{_datadir}/bug-buddy
%{_datadir}/mime-info/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/*
