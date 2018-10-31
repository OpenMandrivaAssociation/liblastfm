%define major 1
%define libname %mklibname lastfm %{major}
%define libnamefinger %mklibname lastfm_fingerprint %{major}
%define devname %mklibname lastfm -d

Summary:	Liblastfm is a collection of libraries to help you integrate Last.fm services
Name:		liblastfm
Version:	1.0.7
Release:	10
License:	GPLv3
Group:		System/Libraries
Url:		https://github.com/mxcl/liblastfm
Source0:	http://cdn.last.fm/client/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ruby
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(fftw3)

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

%build
%if "%{_lib}" == "lib64"
	for name in $(find . -name *.pro); do
		sed -i "s,target.path.*, target.path = /lib64,g" $name
	done
%endif

%cmake -DBUILD_FINGERPRINT=ON
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/liblastfm.so.%{major}*

%files -n %{libnamefinger}
%{_libdir}/liblastfm_fingerprint.so.%{major}*

%files -n %{devname}
%doc COPYING
%{_libdir}/*.so
%{_includedir}/*

