%define	pname	libglade-java
%define	api	2.3
%define	gtkapi	2.3
%define	gnomeapi	2.5
Summary:	Java interface for libglade
Summary(pl):	Wrapper Java dla libglade
Name:		java-libglade
Version:	2.3.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pname}/2.3/%{pname}-%{version}.tar.bz2
# Source0-md5:	e9b2d33d1d606a8a7da5146d286fb636
Patch0:		%{name}-configure.patch
Patch1:		%{name}-version_vars.patch
Patch2:		%{name}-gcjjar.patch
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 3.3.2
BuildRequires:	gtk+2-devel >= 2.3.2
BuildRequires:	java-gtk-devel >= 2.3.5
BuildRequires:	java-libgnome-devel >= 2.5.5
BuildRequires:	libgcj-devel >= 3.3.2
BuildRequires:	libglade2-devel >= 2.3.2
BuildRequires:	libgnomeui-devel >= 2.5.4
Obsoletes:	libglade-java
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java interface for libglade.

%description -l pl
Wrapper Java dla libglade.

%package devel
Summary:	Header files for java-libglade library
Summary(pl):	Pliki nag³ówkowe biblioteki java-libglade
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libglade-java-devel

%description devel
Header files for java-libglade library.

%description devel -l pl
Pliki nag³ówkowe biblioteki java-libglade.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
version="%{version}"; export version
apiversion="%{api}"; export apiversion
gtkapiversion="%{gtkapi}"; export gtkapiversion
gnomeapiversion="%{gnomeapi}"; export gnomeapiversion
%{__autoconf}
%configure \
	GCJ_JAR=`echo /usr/share/java/libgcj*.jar`
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/java-gnome,%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/java-gnome/*
