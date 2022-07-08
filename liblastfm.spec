%define major 1
%define libname %mklibname lastfm %{major}
%define libnamefinger %mklibname lastfm_fingerprint %{major}
%define devname %mklibname lastfm -d

Summary:	Liblastfm is a collection of libraries to help you integrate Last.fm services
Name:		liblastfm
Version:	1.1.0
Release:	1
License:	GPLv3
Group:		System/Libraries
Url:		https://github.com/lastfm/liblastfm
Source0:	https://github.com/lastfm/liblastfm/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ruby
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(fftw3)
#qt5
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Test) 	
BuildRequires:  qmake5

%description
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%package -n %{libname}
Group:		System/Libraries
Summary:	Liblastfm is a collection of libraries to help you integrate Last.fm services

%description -n %{libname}
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%package -n %{libnamefinger}
Group:		System/Libraries
Summary:	Liblastfm is a collection of libraries to help you integrate Last.fm services

%description -n %{libnamefinger}
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%package -n %{devname}
Group:		Development/C
Summary:	%{name} development header
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libnamefinger} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Install this package if you want do compile applications i
using the libtag library.

%prep
%setup -q
%autopatch -p1

%build
#%if "%{_lib}" == "lib64"
#	for name in $(find . -name *.pro); do
#		sed -i "s,target.path.*, target.path = /lib64,g" $name
#	done
#%endif

%cmake -DBUILD_FINGERPRINT=ON -DBUILD_WITH_QT4=OFF ../..
%make_build

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/liblastfm5.so.%{major}*
%files -n %{libnamefinger}
%{_libdir}/liblastfm_fingerprint5.so.%{major}*

%files -n %{devname}
%doc COPYING
%{_libdir}/*.so
%{_includedir}/*

