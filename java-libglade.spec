%define		pname	libglade-java
Summary:	Java interface for libglade
Summary(pl):	Wrapper Java dla libglade
Name:		java-libglade
Version:	2.8.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pname}/2.8/%{pname}-%{version}.tar.bz2
# Source0-md5:	428aad7b148cb2e4d695a04593b52435
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	java-gtk-devel >= 2.4.6
BuildRequires:	java-libgnome-devel >= 2.8.2
BuildRequires:	libgcj-devel >= 5:3.3.2
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomeui-devel >= 2.8.0
BuildRequires:	pkgconfig
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

%build
%{__aclocal} -I `pkg-config --variable macro_dir gtk2-java`
%{__autoconf}
%configure \
	GCJ_JAR=`echo %{_datadir}/java/libgcj*.jar`

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_libdir},%{_pkgconfigdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_javadir}/*
%{_pkgconfigdir}/*.pc
