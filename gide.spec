Summary:	Gtk Integrated Development Environment for C
Summary(pl):	Zintegrowane ¶rodowisko developersje dla C napisane w Gtk
Name:		gide
Version:	0.3.0
Release:	1
License:	GPL
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://gide.pn.org/download/%{name}-%{version}.tar.gz
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	xpm-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	guile-devel
BuildRequires:	gettext-devel
BuildRequires:	libglade-devel >= 0.11
URL:		http://gide.pn.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gIDE

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gide is a Gtk-based Integrated Development Environment for the C
programming language.

%description -l pl
Gide jest bazuj±cym na Gtk zintegrowanym ¶rodowiskiem programisty do
pisania programów w C.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Developmentdir=%{_applnkdir}/Development

gzip -9nf README ChangeLog $RPM_BUILD_ROOT%{_mandir}/man1/*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.gz ChangeLog.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Development/*
%{_datadir}/gide
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
