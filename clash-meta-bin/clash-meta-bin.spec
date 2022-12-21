%global debug_package %{nil}

Name:           clash-meta-bin
Version:        1.13.2
Release:        2%{?dist}
Summary:        Another Clash Kernel.
License:        GPLv3
URL:            https://github.com/MetaCubeX/Clash.Meta
Source0:        %{url}/releases/download/v%{version}/Clash.Meta-linux-amd64-v%{version}.gz
Source1:        https://github.com/NEOVALI/fedora/raw/main/clash-meta-bin/clash-meta@.service
Source2:        https://github.com/NEOVALI/fedora/raw/main/clash-meta-bin/clash-meta.service
Source3:        https://github.com/NEOVALI/fedora/raw/main/clash-meta-bin/config.yaml
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
install -Dm755 Clash.Meta-linux-amd64-v%{version} %{buildroot}/%{_bindir}/clash-meta
install -Dm644 %{S:1} %{buildroot}/%{_unitdir}/clash-meta@.service
install -Dm644 %{S:2} %{buildroot}/%{_userunitdir}/clash-meta.service
install -Dm644 %{S:3} %{buildroot}/etc/clash-meta/config.yaml


%post
%systemd_user_post clash-meta.service
%systemd_post clash-meta@.service

%preun
%systemd_user_preun clash-meta.service
# disable --now seems don't work here.
if [ $1 -eq 0 ] && [ -x /usr/bin/systemctl ] ; then
        # Package removal, not upgrade
        /usr/bin/systemctl --no-reload stop clash-meta@*.service || :
        /usr/bin/systemctl --no-reload disable clash-meta@.service || :
fi

%postun
%systemd_user_postun_with_restart clash-meta.service
%systemd_postun_with_restart clash-meta@*.service


%files
%{_bindir}/clash-meta
/%{_unitdir}/clash-meta@.service
/%{_userunitdir}/clash-meta.service
/etc/clash-meta/config.yaml

%changelog
