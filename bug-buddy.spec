Summary:	Utility to ease the reporting of bugs within the GNOME
Summary(pl):	Narzêdzie u³atwiaj±ce zg³aszanie b³êdów w ¶rodowisku GNOME
Name:		bug-buddy
Version:	2.2.99
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/2.0.0/releases/gnome-2.0-desktop-final/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	scrollkeeper
BuildRequires:	libgnomeui-devel
BuildRequires:	gnome-vfs2-devel >= 1.9.1
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libglade2-devel
BuildRequires:	libxml2-devel
Prereq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME2
%define		_localstatedir	/var
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

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

install -d $RPM_BUILD_ROOT%{_applnkdir}/Help

%{__make} DESTDIR=$RPM_BUILD_ROOT install \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

install src/*.desktop $RPM_BUILD_ROOT%{_applnkdir}/Help

%find_lang %{name} --with-gnome --all-name

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%{_applnkdir}/*/*.desktop

%{_datadir}/application-registry/*.*
%{_datadir}/applications/*.*
%{_datadir}/bug-buddy
%{_datadir}/mime-info/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}
