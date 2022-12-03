Name:           clash-meta-bin
Version:        1.13.2
Release:        1%{?dist}
Summary:        Another Clash Kernel by MetaCubeX
License:        GPLv3
URL:            https://github.com/Dreamacro/clash/releases/tag/premium
Source0:        https://github.com/MetaCubeX/Clash.Meta/releases/download/v%{version}/Clash.Meta-linux-amd64-v%{version}.gz
Source1:        https://github.com/valig5/fedora/raw/main/clash-meta-bin/clash-meta.service
Source2:        https://github.com/valig5/fedora/raw/main/clash-meta-bin/clash-meta@.service
Source3:        https://github.com/valig5/fedora/raw/main/clash-meta-bin/config.yaml
BuildArch:      x86_64

BuildRequires:  bash
BuildRequires:  tar

%description
Another Clash Kernel by MetaCubeX


%prep
%setup -c


%build
# Nothing to build


%install
install -Dm755 Clash.Meta-linux-amd64 %{buildroot}/%{_bindir}/clash
install -Dm644 %{S:1} %{buildroot}/%{_libdir}/systemd/system/clash-meta@.service
install -Dm644 %{S:2} %{buildroot}/%{_libdir}/systemd/system/clash-meta.service
install -Dm644 %{S:3} %{buildroot}/etc/clash-meta/config.yaml

%files
%dir /etc/clash-meta
/etc/clash-meta/config.yaml
%{_bindir}/clash-meta
%{_libdir}/systemd/system/clash-meta@.service
%{_libdir}/systemd/system/clash-meta.service

%changelog
