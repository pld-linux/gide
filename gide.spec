Summary:	Gtk Integrated Development Environment for C
Summary(pl):	Zintegrowane ¶rodowisko developersje dla C napisane w Gtk
Name:		gide
Version:	0.3.0
Release:	6
License:	GPL
Group:		Development/Tools
Source0:	http://gide.pn.org/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fix.patch
URL:		http://gide.pn.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	guile-devel >= 1.4
BuildRequires:	libglade-gnome-devel >= 0.11
BuildRequires:	libltdl-devel
BuildRequires:	libtool
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
%patch0 -p1

%build
rm -f missing acinclude.m4
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Developmentdir=%{_applnkdir}/Development

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/gide
%dir %{_libdir}/gide/plugins
%dir %{_libdir}/gide/plugins/%{version}
%attr(755,root,root) %{_libdir}/gide/plugins/%{version}/*la
%attr(755,root,root) %{_libdir}/gide/plugins/%{version}/*so*
%{_applnkdir}/Development/*
%{_datadir}/gide
%{_pixmapsdir}/*
%{_mandir}/man1/*
