Name:       oprofile
Summary:    System wide profiler
Version:    1.2.0
Release:    1
Group:      Development/Tools
License:    GPL v2 or later
URL:        https://github.com/sailfishos/oprofile
Source0:    %{name}-%{version}.tar.gz

Requires(pre): shadow-utils
BuildRequires: pkgconfig(popt)
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libxslt
BuildRequires: libtool
BuildRequires: binutils-devel
BuildRequires: fdupes

%description
OProfile is a profiling system for systems running Linux. The
profiling runs transparently during the background, and profile data
can be collected at any time. OProfile makes use of the hardware performance
counters provided on Intel P6, and AMD Athlon family processors, and can use
the RTC for profiling on other x86 processor types.

See the HTML documentation for further details.

%package devel
Summary:    System-Wide Profiler for Linux Systems
License:    GPL v2 or later; LGPL v2.1 or later
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   binutils-devel

%description devel
Header files and libraries for developing apps which will use oprofile.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
sh autogen.sh

%configure --disable-static \
    --prefix=%{_prefix} \
    --mandir=%{_mandir} \
    --libdir=%{_libdir} \
    --with-kernel-support

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%fdupes  %{buildroot}/%{_datadir}

%pre
/usr/sbin/groupadd -r oprofile 2>/dev/null || :
/usr/sbin/useradd -r -g oprofile -d /var/lib/empty -s /bin/false -c "Special user account to be used by OProfile" oprofile 2>/dev/null || :

%files
%defattr(-,root,root,-)
%doc COPYING README TODO
%doc %{_docdir}/oprofile/*
%dir %{_libdir}/oprofile
%{_bindir}/*
%{_datadir}/oprofile
%{_libdir}/oprofile/*.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_libdir}/oprofile
%{_includedir}/*
%{_libdir}/oprofile/*.so
%{_mandir}/man1/*

