Summary:	C++ frontent for glade
Name:		glademm
Version:	0.5_11d
Release:	1
License:	GPL
Group:		Development/Building
Group(de):	Entwicklung/Bauen
Group(pl):	Programowanie/Budowanie
Source0:	http://home.wtal.de/petig/Gtk/%{name}-%{version}.tar.gz
URL:		http://home.wtal.de/petig/Gtk/index.html
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtkmm-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix   	/usr

%description
This is a C++ backend for glade, the GUI designer for Gtk. This means
this program reads glade files and outputs a C++ program source
skeleton for you. Each (public) GUI class has a derivative user class
for you to modify and extend.

%description -l pl
Glademm to ³±cze do glade dla C++. Dziêki niemu z plików glade mozna
uzyskaæ szkielet kodu wynikowego w C++. Ka¿da (publiczna) klasa GUI
posiada klasê pochodn± uzytkownika, któr± mo¿na modyfikowaæ i
rozwijaæ.

%prep
%setup -q

%build
CXXFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} -fno-rtti -fno-exceptions"
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS ChangeLog NEWS README TODO docs/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*gz
%attr(755, root,root) %{_bindir}/*
