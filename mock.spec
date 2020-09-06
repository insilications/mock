#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : mock
Version  : 20.09.06
Release  : 63
URL      : file:///insilications/build/clearlinux/packages/mock/mock-20.09.06.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/mock/mock-20.09.06.tar.gz
Summary  : Builds packages inside chroots
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: mock-bin = %{version}-%{release}
Requires: mock-data = %{version}-%{release}
Requires: mock-libexec = %{version}-%{release}
Requires: mock-man = %{version}-%{release}
Requires: mock-python = %{version}-%{release}
Requires: mock-python3 = %{version}-%{release}
Requires: Jinja2
Requires: distro
Requires: pyroute2
Requires: six
BuildRequires : Jinja2
BuildRequires : distro
BuildRequires : findutils
BuildRequires : pyroute2
BuildRequires : python3
BuildRequires : six
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Mock takes an SRPM and builds it in a chroot.

%package bin
Summary: bin components for the mock package.
Group: Binaries
Requires: mock-data = %{version}-%{release}
Requires: mock-libexec = %{version}-%{release}

%description bin
bin components for the mock package.


%package data
Summary: data components for the mock package.
Group: Data

%description data
data components for the mock package.


%package libexec
Summary: libexec components for the mock package.
Group: Default

%description libexec
libexec components for the mock package.


%package man
Summary: man components for the mock package.
Group: Default

%description man
man components for the mock package.


%package python
Summary: python components for the mock package.
Group: Default
Requires: mock-python3 = %{version}-%{release}

%description python
python components for the mock package.


%package python3
Summary: python3 components for the mock package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mock package.


%prep
%setup -q -n mock
cd %{_builddir}/mock

%build
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599398517
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
# -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-common -Wno-error -Wp,-D_REENTRANT
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fPIC"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags1 end
##
%define _lto_cflags 1
##
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1599398517
rm -rf %{buildroot}
%make_install
## install_append content
install -d %{buildroot}/usr/share/defaults/sudo/sudoers.d
install -m 440 mock.sudoers %{buildroot}/usr/share/defaults/sudo/sudoers.d/mock

ln -sf clear.cfg %{buildroot}/usr/share/defaults/mock/default.cfg
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mock
/usr/bin/mock-parse-buildlog
/usr/bin/mockchain

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/mock
/usr/share/defaults/mock/clear.cfg
/usr/share/defaults/mock/default.cfg
/usr/share/defaults/mock/logging.ini
/usr/share/defaults/mock/site-defaults.cfg
/usr/share/defaults/sudo/sudoers.d/mock
/usr/share/pam.d/mock

%files libexec
%defattr(-,root,root,-)
/usr/libexec/mock/create_default_route_in_container.sh

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mock-parse-buildlog.1
/usr/share/man/man1/mock.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
