%global debug_package %{nil}

Name:           clash-premium-bin
Version:        2022.11.25
Release:        2%{?dist}
Summary:        Close-sourced pre-built Clash binary with TUN support
License:        GPLv3
URL:            https://github.com/Dreamacro/clash/releases/tag/premium
Source0:        https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-amd64-%{version}.gz
Source1:        https://github.com/NEOVALI/fedora/raw/main/clash-premium-bin/clash@.service
Source2:        https://github.com/NEOVALI/fedora/raw/main/clash-premium-bin/clash.service
BuildArch:      x86_64
Conflicts:      clash
BuildRequires:  bash
BuildRequires:  gzip

%description
Close-sourced pre-built Clash binary with TUN support


%prep
mkdir -p %{_builddir}/%{name}-%{version}
cd %{_builddir}/%{name}-%{version}
cp %{S:0} ./
gzip -d ./*


%build
# Nothing to build


%install
cd %{_builddir}/%{name}-%{version}
install -Dm755 clash-linux-amd64-%{version} %{buildroot}/%{_bindir}/clash
install -Dm644 %{S:1} %{buildroot}/usr/lib/systemd/system/clash@.service
install -Dm644 %{S:2} %{buildroot}/usr/lib/systemd/user/clash.service

%post
setcap "cap_net_admin=ep" %{_bindir}/clash

%files
%{_bindir}/clash
/usr/lib/systemd/system/clash@.service
/usr/lib/systemd/user/clash.service

%changelog
