%define major           0
%define penge_name      penge
%define libname         %mklibname %{penge_name} %{major}
%define develname       %mklibname %{penge_name} -d

Name: moblin-panel-myzone
Summary: Myzone panel for Moblin
Group: Graphical desktop/Other 
Version: 0.0.11
License: LGPL 2.1
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: libGConf2-devel
BuildRequires: clutter-devel
BuildRequires: jana-devel
BuildRequires: gtk2-devel
BuildRequires: nbtk-devel
BuildRequires: moblin-panel-devel
BuildRequires: mojito-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common

%description
Moblin myzone panel for Moblin

%package -n %{libname}
Summary: Moblin's myzone library
Group: System/Libraries

%description -n %{libname}
Moblin's myzone library

%package -n %{develname}
Summary: Moblin's myzone library (development files)
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}

%description -n %{develname}
Moblin's myzone library (development files)

%prep
%setup -q 

%build
NOCONFIGURE=nil ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING NEWS README AUTHORS ChangeLog
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/*service

%files -n %{libname}
%{_libdir}/lib%{penge_name}*.so.*

%files -n %{develname}
%{_libdir}/lib%{penge_name}*.so
%{_libdir}/lib%{penge_name}*.la
%{_libdir}/lib%{penge_name}*.a
