Name     : mock
Version  : 1.2.7
Release  : 6
URL      : https://git.fedorahosted.org/cgit/mock.git/snapshot/mock-1.2.7.tar.xz
Source0  : https://git.fedorahosted.org/cgit/mock.git/snapshot/mock-1.2.7.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : pkgconfig(bash-completion)
BuildRequires : python
BuildRequires : python-dev
BuildRequires : python3
Patch1 : 0001-Stateless-conversion.patch
Patch2 : 0002-Do-not-reuse-mock-group-as-it-might-be-defined-in-th.patch

%description
These 3 src.rpms are setup to build on almost any rpm-based system.
They have a simple chain of buildrequires:

%prep
%setup -q -n mock-1.2.7
%patch1 -p1
%patch2 -p1

%build
%autogen --disable-static
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}/usr/share/pam.d
mkdir -p %{buildroot}/usr/share/defaults/mock
mv %{buildroot}/etc/mock/logging.ini %{buildroot}/usr/share/defaults/mock/
mv %{buildroot}/etc/pam.d/mock %{buildroot}/usr/share/pam.d/
rm -rf %{buildroot}/etc

%files
%defattr(-,root,root,-)
/usr/bin/mock
/usr/bin/mockchain
/usr/share/bash-completion/completions/mock
/usr/share/bash-completion/completions/mockchain
%doc /usr/share/man/man1/*
/usr/lib/python*/*
/usr/share/defaults/mock/*
/usr/share/pam.d/*
