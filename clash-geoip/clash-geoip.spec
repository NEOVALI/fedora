Name:           clash-geoip
Version:        20221212
Release:        1%{?dist}
Summary:        A GeoLite2 data created by MaxMind
Url:            https://github.com/Dreamacro/maxmind-geoip
Source0:        %{url}/releases/download/20221212/Country.mmdb
BuildArch:      noarch

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages


%description
A GeoLite2 data created by MaxMind

%prep
%build

%install
install -Dm0644 %{S:0} %{buildroot}/%{_sysconfdir}/clash/Country.mmdb

%post
%postun

%files
%{_sysconfdir}/clash/Country.mmdb