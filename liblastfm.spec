Name: liblastfm
Version: 0.3.3
Release: %mkrel 2
Summary: Liblastfm is a collection of libraries to help you integrate Last.fm services
License: GPLv3 
Group: System/Libraries
Source: http://download.github.com/liblastfm-%{version}.tar.gz
URL: https://github.com/mxcl/liblastfm
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: qt4-devel
BuildRequires: pkgconfig 
BuildRequires: libsamplerate-devel
BuildRequires: fftw3-devel
BuildRequires: ruby

%description
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

#---------------------------------------------------------------------

%define lastfm_major 0
%define libname %mklibname lastfm %{lastfm_major}

%package -n %{libname}
Group: System/Libraries
Summary: Liblastfm is a collection of libraries to help you integrate Last.fm services

%description -n %{libname}
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liblastfm.so.%{lastfm_major}*

#---------------------------------------------------------------------

%define finger_major 0
%define libnamefinger %mklibname lastfm_fingerprint %{finger_major}

%package -n %{libnamefinger}
Group: System/Libraries
Summary: Liblastfm is a collection of libraries to help you integrate Last.fm services

%description -n %{libnamefinger}
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software. It is officially supported software developed
by Last.fm staff.

%files -n %{libnamefinger}
%defattr(-,root,root)
%{_libdir}/liblastfm_fingerprint.so.%{finger_major}*

#---------------------------------------------------------------------

%define develname %mklibname lastfm -d

%package -n %{develname}
Group: Development/C
Summary: %name development header
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libnamefinger} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Summary: %name development header
Install this package if you want do compile applications i
using the libtag library.

%files -n %{develname}
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/*.so
%{_includedir}/*

#---------------------------------------------------------------------

%prep
%setup -qn mxcl-liblastfm-1c739eb

%build
%if "%_lib" == "lib64"
	for name in $(find . -name *.pro); do
		sed -i "s,target.path.*, target.path = /lib64,g" $name
	done
%endif

# This is a ruby configure, not standard one
./configure --prefix %{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}
