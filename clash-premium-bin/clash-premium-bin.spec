%global debug_package %{nil}

Name:           clash-premium-bin
Version:        2022.11.25
Release:        2%{?dist}
Summary:        Close-sourced pre-built Clash binary with TUN support
License:        GPLv3
URL:            https://github.com/Dreamacro/clash/releases/tag/premium
Source0:        https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-amd64-%{version}.gz
Source1:        https://github.com/valig5/fedora/raw/main/clash-premium-bin/clash@.service
Source2:        https://github.com/valig5/fedora/raw/main/clash-premium-bin/clash.service
BuildArch:      x86_64

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
install -Dm644 %{S:1} %{buildroot}/%{_unitdir}/clash@.service
install -Dm644 %{S:2} %{buildroot}/%{_userunitdir}/clash.service


%post
%systemd_user_post clash.service
%systemd_post clash@.service

%preun
%systemd_user_preun clash.service
# disable --now seems don't work here.
if [ $1 -eq 0 ] && [ -x /usr/bin/systemctl ] ; then
        # Package removal, not upgrade
        /usr/bin/systemctl --no-reload stop clash@*.service || :
        /usr/bin/systemctl --no-reload disable clash@.service || :
fi

%postun
%systemd_user_postun_with_restart clash.service
%systemd_postun_with_restart clash@*.service


%files
%{_bindir}/clash
%{_unitdir}/clash@.service
%{_userunitdir}/clash.service

%changelog
