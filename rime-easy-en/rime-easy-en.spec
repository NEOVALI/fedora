
%global build_timestamp %(date +"%Y%m%d")
%global forgeurl        https://github.com/BlindingDark/rime-easy-en
%global branch          master

%forgemeta

Name:           rime-easy-en
Version:        git
Release:        1%{?dist}
Summary:        RIME Easy English
License:        LGPLv3
Url:            %{forgeurl}
Source:         %{forgesource}
BuildArch:      noarch
Recommends:     librime

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
RIME Easy English.

%prep
%forgesetup

%build

%install
install -Dm644 easy_en.yaml -t %{buildroot}%{_datadir}/rime-data/
install -Dm644 easy_en.dict.yaml -t %{buildroot}%{_datadir}/rime-data/
install -Dm644 easy_en.schema.yaml -t %{buildroot}%{_datadir}/rime-data/
install -Dm644 lua/* -t %{buildroot}%{_datadir}/rime-data/lua

%post
%postun

%files
%license LICENSE
%doc README.md
%{_datadir}/rime-data/*.yaml
%{_datadir}/rime-data/lua/*

%changelog
