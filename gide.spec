Summary:	GTK+ Integrated Development Environment for C
Summary(pl.UTF-8):   Zintegrowane środowisko developersje dla C napisane w GTK+
Name:		gide
Version:	0.3.0
Release:	6
License:	GPL
Group:		Development/Tools
Source0:	http://gide.pn.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	b7195eef0c3155ed239adef252428ffc
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


%description
Gide is a GTK+-based Integrated Development Environment for the C
programming language.

%description -l pl.UTF-8
Gide jest bazującym na GTK+ zintegrowanym środowiskiem programisty do
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
