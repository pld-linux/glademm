Summary:	C++ frontent for glade
Summary(pl):	Interfejs C++ do glade
Name:		glademm
Version:	0.6.2b
Release:	1
License:	GPL
Group:		Development/Building
Group(cs):	Z�klad/V�voj
Group(da):	Udvikling/Bygge
Group(de):	Entwicklung/Bauen
Group(es):	Desarrollo/Construcci�n
Group(fr):	D�veloppement/Construction
Group(it):	Sviluppo/Sviluppo
Group(no):	Utvikling/Bygge
Group(pl):	Programowanie/Budowanie
Group(pt):	Desenvolvimento/Cria��o
Group(ru):	����������/��������
Group(sv):	Utveckling/Bygga
Group(uk):	��������/������
Source0:	http://home.wtal.de/petig/Gtk/%{name}-%{version}.tar.gz
Patch0:		%{name}-configure.patch
URL:		http://home.wtal.de/petig/Gtk/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtkmm-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a C++ backend for glade, the GUI designer for Gtk. This means
this program reads glade files and outputs a C++ program source
skeleton for you. Each (public) GUI class has a derivative user class
for you to modify and extend.

%description -l pl
Glademm to ��cze do glade dla C++. Dzi�ki niemu z plik�w glade mozna
uzyska� szkielet kodu wynikowego w C++. Ka�da (publiczna) klasa GUI
posiada klas� pochodn� uzytkownika, kt�r� mo�na modyfikowa� i
rozwija�.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS ChangeLog NEWS README TODO docs/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*gz
%attr(755, root,root) %{_bindir}/*
