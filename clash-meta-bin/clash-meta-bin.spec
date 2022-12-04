%global debug_package %{nil}

Name:           clash-meta-bin
Version:        1.13.2
Release:        1%{?dist}
Summary:        Another Clash Kernel.
License:        GPLv3
URL:            https://github.com/MetaCubeX/Clash.Meta
Source0:        %{url}/releases/download/v%{version}/Clash.Meta-linux-amd64-v%{version}.gz
Source1:        https://github.com/valig5/fedora/raw/main/clash-meta-bin/clash-meta@.service
Source2:        https://github.com/valig5/fedora/raw/main/clash-meta-bin/clash-meta.service
Source3:        https://github.com/valig5/fedora/raw/main/clash-meta-bin/config.yaml
BuildArch:      x86_64

BuildRequires:  bash
BuildRequires:  gzip

%description
Another Clash Kernel.


%prep
mkdir -p %{_builddir}/%{name}-%{version}
cd %{_builddir}/%{name}-%{version}
cp %{S:0} ./
gzip -d ./*


%build
# Nothing to build


%install
cd %{_builddir}/%{name}-%{version}
install -Dm755 Clash.Meta-linux-amd64 %{buildroot}/%{_bindir}/clash-meta
install -Dm644 %{S:1} %{buildroot}/%{_libdir}/systemd/system/clash-meta@.service
install -Dm644 %{S:2} %{buildroot}/%{_libdir}/systemd/user/clash-meta.service
install -Dm644 %{S:3} %{buildroot}/etc/clash-meta/config.yaml

%files
%{_bindir}/clash-meta
%{_libdir}/systemd/system/clash-meta@.service
%{_libdir}/systemd/user/clash-meta.service
/etc/clash-meta/config.yaml

%changelog