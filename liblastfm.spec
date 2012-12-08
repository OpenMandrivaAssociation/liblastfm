Name:		liblastfm
Version:	1.0.3
Release:	1
Summary:	Liblastfm is a collection of libraries to help you integrate Last.fm services
License:	GPLv3
Group:		System/Libraries
Source0:	http://cdn.last.fm/client/%{name}-%{version}.tar.gz
URL:		https://github.com/mxcl/liblastfm
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	ruby
BuildRequires:	cmake

%description
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

#---------------------------------------------------------------------

%define lastfm_major 1
%define libname %mklibname lastfm %{lastfm_major}

%package -n %{libname}
Group:		System/Libraries
Summary:	Liblastfm is a collection of libraries to help you integrate Last.fm services

%description -n %{libname}
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%files -n %{libname}
%{_libdir}/liblastfm.so.%{lastfm_major}*

#---------------------------------------------------------------------

%define finger_major 1
%define libnamefinger %mklibname lastfm_fingerprint %{finger_major}

%package -n %{libnamefinger}
Group:		System/Libraries
Summary:	Liblastfm is a collection of libraries to help you integrate Last.fm services

%description -n %{libnamefinger}
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%files -n %{libnamefinger}
%{_libdir}/liblastfm_fingerprint.so.%{finger_major}*

#---------------------------------------------------------------------

%define develname %mklibname lastfm -d

%package -n %{develname}
Group:		Development/C
Summary:	%{name} development header
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libnamefinger} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Install this package if you want do compile applications i
using the libtag library.

%files -n %{develname}
%doc COPYING
%{_libdir}/*.so
%{_includedir}/*

#---------------------------------------------------------------------

%prep
%setup -q

%build
%if "%_lib" == "lib64"
	for name in $(find . -name *.pro); do
		sed -i "s,target.path.*, target.path = /lib64,g" $name
	done
%endif

%cmake -DBUILD_FINGERPRINT=ON
%make

%install
%makeinstall_std -C build
