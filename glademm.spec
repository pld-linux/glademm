%define ver      	0.5.7
%define RELEASE		1
#%define CUSTOM_RELEASE	SNAP
%define rel     	%{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define prefix   	/usr

Summary: C++ frontent for glade
Name: glademm
Version: %ver
Release: %rel
Copyright: GPL
Group: Gnome/Development
Source: %{name}-%{ver}.tar.gz
BuildRoot: /tmp/%{name}-%{ver}-root
URL: http://home.wtal.de/petig/Gtk/index.html
Prefix: %prefix

%description
This is a C++ frontent for glade, the GUI designer for Gtk.

%prep
%setup -q

if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
    ./autogen.sh %{_target_platform} --prefix=%{prefix}
else
  CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
    ./configure  %{_target_platform} --prefix=%{prefix}
fi

%build

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install-strip

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README TODO
%doc docs/*.txt docs/KNOWN docs/*html

%{prefix}/bin/*
