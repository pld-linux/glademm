Summary:	C++ frontent for glade
Name:		glademm
Version:	0.5.7c
Release:	1
License:	GPL
Group:		Development/Building
Group(pl):	Programowanie/Budowanie
Source0:	http://home.wtal.de/petig/Gtk/%{name}-%{version}.tar.gz
URL:		http://home.wtal.de/petig/Gtk/index.html
BuildRequires:	libstdc++-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtkmm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix   	/usr

%description
This is a C++ backend for glade, the GUI designer for Gtk. This means this
program reads glade files and outputs a C++ program source skeleton for
you. Each (public) GUI class has a derivative user class for you to modify
and extend.

%prep
%setup -q

%build
%configure

make CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT

make install-strip DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS ChangeLog NEWS README TODO docs/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*gz
%attr(755, root,root) %{_bindir}/*
