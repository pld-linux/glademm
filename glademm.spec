Summary:	C++ frontent for glade
Summary(pl):	Interfejs C++ do glade
Name:		glademm
Version:	2.6.0
Release:	1
License:	GPL
Group:		Development/Building
Source0:	http://home.wtal.de/petig/Gtk/%{name}-%{version}.tar.gz
# Source0-md5:	e88be4e895ff3b99d8ae39e799b714a2
Patch0:		%{name}-configure.patch
Patch1:		%{name}-gnome-config.patch
URL:		http://home.wtal.de/petig/Gtk/index.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	gtkmm-devel >= 2.4.0
BuildRequires:	libbonobouimm-devel >= 1.3.7
BuildRequires:	libgnomeuimm-devel >= 2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a C++ backend for glade, the GUI designer for Gtk. This means
this program reads glade files and outputs a C++ program source
skeleton for you. Each (public) GUI class has a derivative user class
for you to modify and extend.

%description -l pl
Glademm to ��cze do glade dla C++. Dzi�ki niemu z plik�w glade mo�na
uzyska� szkielet kodu wynikowego w C++. Ka�da (publiczna) klasa GUI
posiada klas� pochodn� u�ytkownika, kt�r� mo�na modyfikowa� i
rozwija�.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO docs/*.txt
%attr(755, root,root) %{_bindir}/*
