Name:           clash-premium-bin
Version:        2022.11.25
Release:        1%{?dist}
Summary:        Close-sourced pre-built Clash binary with TUN support
License:        GPLv3
URL:            https://github.com/Dreamacro/clash/releases/tag/premium
Source0:        https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-amd64-%{version}.gz
Source1:        https://github.com/valig5/fedora/raw/main/clash-premium-bin/clash@.service
Source2:        https://github.com/valig5/fedora/raw/main/clash-premium-bin/clash_user.service
BuildArch:      x86_64

BuildRequires:  bash
BuildRequires:  tar

%description
Close-sourced pre-built Clash binary with TUN support


%prep
%setup -c


%build
# Nothing to build


%install
install -Dm755 clash-linux-amd64 %{buildroot}/%{_bindir}/clash
install -Dm644 %{S:1} %{buildroot}/%{_libdir}/systemd/system/clash@.service
install -Dm644 %{S:2} %{buildroot}/%{_libdir}/systemd/user/clash.service

%files
%{_bindir}/clash
%{_libdir}/systemd/system/clash@.service
%{_libdir}/systemd/user/clash.service

%changelog
