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
## upstream patches
#Patch0:         0001-Make-sure-liblastfm-creates-the-dirs-it-tries-to-wor.patch
Patch1:         0003-Add-LASTFM_LIB_VERSION_SUFFIX-to-include-dir-as-well.patch
Patch2:         liblastfm-1.0.9-fix-build-against-qt-5.11.0.patch
### Qt4 BuildRequires
BuildRequires:	cmake
BuildRequires:	ruby
#BuildRequires:	qt4-devel
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
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/liblastfm5.so.%{major}*
%{_libdir}/liblastfm5.so.%{version}*

%files -n %{libnamefinger}
%{_libdir}/liblastfm_fingerprint5.so.%{major}*
%{_libdir}/liblastfm_fingerprint5.so.%{version}*

%files -n %{devname}
%doc COPYING
%{_libdir}/*.so
%{_includedir}/*

